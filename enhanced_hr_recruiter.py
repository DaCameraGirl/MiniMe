"""Enhanced HR Recruiting Assistant with intelligent candidate scoring."""

import json
import requests
import re
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from difflib import SequenceMatcher
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
from langgraph.graph.message import AnyMessage, FunctionMessage, HumanMessage, SystemMessage, AIMessage

# Initialize the app
app = FastAPI(
    title="Enhanced MCP HR Recruiting Assistant",
    description="AI agent for intelligent candidate recruitment and scoring",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@dataclass
class SkillWeight:
    """Represents a skill with its importance weight."""
    name: str
    weight: float = 1.0
    required: bool = False
    proficiency_level: str = "intermediate"  # beginner, intermediate, advanced, expert

@dataclass
class CandidateSkill:
    """Represents a candidate's skill with experience."""
    name: str
    years_experience: float = 0.0
    proficiency_level: str = "intermediate"
    last_used: Optional[str] = None

class EnhancedRecruitRequest(BaseModel):
    """Enhanced model for recruit request."""
    job_title: str
    required_skills: List[Dict[str, Any]]  # [{"name": "Python", "weight": 1.0, "required": True, "level": "advanced"}]
    preferred_skills: List[Dict[str, Any]] = []
    location: Optional[str] = None
    remote_ok: bool = False
    experience_years_min: Optional[int] = None
    experience_years_max: Optional[int] = None
    education_level: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    industry_preference: Optional[str] = None
    company_size_preference: Optional[str] = None  # startup, small, medium, large, enterprise

class EnhancedRecruitResponse(BaseModel):
    """Enhanced model for recruit response."""
    candidates: List[Dict[str, Any]]
    job_description: Dict[str, Any]
    recommendation: str
    scoring_breakdown: Dict[str, Any]

class AgentState:
    """State for the HR recruiting workflow."""
    def __init__(self, messages: List[AnyMessage]):
        self.messages = messages

class IntelligentCandidateScorer:
    """Advanced candidate scoring system."""
    
    SKILL_SYNONYMS = {
        "python": ["python3", "python2", "py"],
        "javascript": ["js", "ecmascript", "node.js", "nodejs"],
        "react": ["reactjs", "react.js"],
        "angular": ["angularjs", "angular.js"],
        "machine learning": ["ml", "ai", "artificial intelligence"],
        "database": ["db", "sql", "nosql"],
        "aws": ["amazon web services", "amazon aws"],
        "docker": ["containerization", "containers"],
        "kubernetes": ["k8s", "container orchestration"]
    }
    
    PROFICIENCY_MULTIPLIERS = {
        "beginner": 0.3,
        "intermediate": 0.7,
        "advanced": 1.0,
        "expert": 1.3
    }
    
    EXPERIENCE_MULTIPLIERS = {
        "entry": 0.5,     # 0-2 years
        "junior": 0.7,    # 2-4 years
        "mid": 1.0,       # 4-7 years
        "senior": 1.2,    # 7-12 years
        "lead": 1.4,      # 12+ years
        "principal": 1.5  # 15+ years
    }
    
    def normalize_skill(self, skill: str) -> str:
        """Normalize skill names for better matching."""
        skill_lower = skill.lower().strip()
        
        # Check synonyms
        for canonical, synonyms in self.SKILL_SYNONYMS.items():
            if skill_lower == canonical or skill_lower in synonyms:
                return canonical
        
        return skill_lower
    
    def skill_similarity(self, skill1: str, skill2: str) -> float:
        """Calculate similarity between two skills using fuzzy matching."""
        normalized1 = self.normalize_skill(skill1)
        normalized2 = self.normalize_skill(skill2)
        
        if normalized1 == normalized2:
            return 1.0
        
        # Use sequence matching for partial matches
        similarity = SequenceMatcher(None, normalized1, normalized2).ratio()
        
        # Boost similarity for related technologies
        related_pairs = [
            ("react", "javascript"), ("angular", "typescript"), 
            ("django", "python"), ("flask", "python"),
            ("node.js", "javascript"), ("vue", "javascript")
        ]
        
        for pair in related_pairs:
            if (normalized1 in pair and normalized2 in pair) or (normalized2 in pair and normalized1 in pair):
                similarity = max(similarity, 0.7)
        
        return similarity
    
    def get_experience_level(self, years: float) -> str:
        """Determine experience level based on years."""
        if years < 2:
            return "entry"
        elif years < 4:
            return "junior"
        elif years < 7:
            return "mid"
        elif years < 12:
            return "senior"
        elif years < 15:
            return "lead"
        else:
            return "principal"
    
    def score_skill_match(self, required_skill: SkillWeight, candidate_skills: List[CandidateSkill]) -> float:
        """Score how well a candidate matches a required skill."""
        best_match_score = 0.0
        
        for candidate_skill in candidate_skills:
            # Calculate base similarity
            similarity = self.skill_similarity(required_skill.name, candidate_skill.name)
            
            if similarity < 0.5:  # Skip poor matches
                continue
            
            # Apply proficiency multipliers
            required_prof_mult = self.PROFICIENCY_MULTIPLIERS.get(required_skill.proficiency_level, 1.0)
            candidate_prof_mult = self.PROFICIENCY_MULTIPLIERS.get(candidate_skill.proficiency_level, 1.0)
            
            # Penalize if candidate proficiency is much lower than required
            proficiency_ratio = min(candidate_prof_mult / required_prof_mult, 1.0)
            
            # Experience bonus (diminishing returns after optimal range)
            exp_bonus = 1.0
            if candidate_skill.years_experience > 0:
                # Sweet spot is 2-3x the minimum required experience
                optimal_exp = max(2.0, candidate_skill.years_experience * 0.5)
                if candidate_skill.years_experience >= optimal_exp:
                    exp_bonus = 1.2
                elif candidate_skill.years_experience >= optimal_exp * 0.5:
                    exp_bonus = 1.1
            
            # Recency bonus (if skill was used recently)
            recency_bonus = 1.0
            if candidate_skill.last_used:
                try:
                    last_used_date = datetime.strptime(candidate_skill.last_used, "%Y-%m-%d")
                    months_since = (datetime.now() - last_used_date).days / 30
                    if months_since <= 6:
                        recency_bonus = 1.1
                    elif months_since <= 24:
                        recency_bonus = 1.05
                except:
                    pass
            
            skill_score = similarity * proficiency_ratio * exp_bonus * recency_bonus
            best_match_score = max(best_match_score, skill_score)
        
        return min(best_match_score, 1.5)  # Cap at 1.5 for exceptional matches
    
    def score_candidate(self, candidate: Dict[str, Any], job_req: EnhancedRecruitRequest) -> Dict[str, Any]:
        """Comprehensive candidate scoring."""
        
        # Parse candidate skills
        candidate_skills = []
        for skill_data in candidate.get("skills", []):
            if isinstance(skill_data, str):
                candidate_skills.append(CandidateSkill(name=skill_data))
            else:
                candidate_skills.append(CandidateSkill(
                    name=skill_data.get("name", ""),
                    years_experience=skill_data.get("years_experience", 0),
                    proficiency_level=skill_data.get("proficiency_level", "intermediate"),
                    last_used=skill_data.get("last_used")
                ))
        
        # Parse required skills
        required_skills = []
        for skill_data in job_req.required_skills:
            required_skills.append(SkillWeight(
                name=skill_data.get("name", ""),
                weight=skill_data.get("weight", 1.0),
                required=skill_data.get("required", False),
                proficiency_level=skill_data.get("level", "intermediate")
            ))
        
        # Parse preferred skills
        preferred_skills = []
        for skill_data in job_req.preferred_skills:
            preferred_skills.append(SkillWeight(
                name=skill_data.get("name", ""),
                weight=skill_data.get("weight", 0.5),
                required=False,
                proficiency_level=skill_data.get("level", "intermediate")
            ))
        
        scores = {
            "skill_score": 0.0,
            "experience_score": 0.0,
            "location_score": 0.0,
            "salary_score": 0.0,
            "education_score": 0.0,
            "industry_score": 0.0,
            "total_score": 0.0,
            "breakdown": {}
        }
        
        # 1. SKILL SCORING (50% weight)
        total_skill_weight = sum(skill.weight for skill in required_skills)
        if total_skill_weight > 0:
            skill_total = 0.0
            missing_required = []
            
            for req_skill in required_skills:
                skill_match_score = self.score_skill_match(req_skill, candidate_skills)
                weighted_score = skill_match_score * req_skill.weight
                skill_total += weighted_score
                
                scores["breakdown"][f"skill_{req_skill.name}"] = {
                    "score": skill_match_score,
                    "weight": req_skill.weight,
                    "weighted_score": weighted_score,
                    "required": req_skill.required
                }
                
                if req_skill.required and skill_match_score < 0.3:
                    missing_required.append(req_skill.name)
            
            # Add preferred skills bonus
            for pref_skill in preferred_skills:
                pref_match_score = self.score_skill_match(pref_skill, candidate_skills)
                bonus = pref_match_score * pref_skill.weight * 0.2  # 20% bonus weight
                skill_total += bonus
                scores["breakdown"][f"preferred_{pref_skill.name}"] = pref_match_score
            
            scores["skill_score"] = min(skill_total / total_skill_weight, 1.5)
            scores["missing_required_skills"] = missing_required
        
        # 2. EXPERIENCE SCORING (25% weight)
        candidate_exp = candidate.get("total_experience_years", 0)
        min_exp = job_req.experience_years_min or 0
        max_exp = job_req.experience_years_max or 100
        
        if candidate_exp < min_exp:
            exp_score = max(0.1, candidate_exp / min_exp)
        elif candidate_exp > max_exp:
            # Slight penalty for overqualification (might be flight risk)
            exp_score = max(0.8, 1 - (candidate_exp - max_exp) * 0.05)
        else:
            exp_score = 1.0
        
        # Experience level multiplier
        candidate_level = self.get_experience_level(candidate_exp)
        exp_multiplier = self.EXPERIENCE_MULTIPLIERS.get(candidate_level, 1.0)
        scores["experience_score"] = min(exp_score * exp_multiplier, 1.2)
        
        # 3. LOCATION SCORING (10% weight)
        candidate_location = candidate.get("location", "").lower()
        preferred_location = (job_req.location or "").lower()
        remote_ok = job_req.remote_ok
        
        if remote_ok or not preferred_location:
            scores["location_score"] = 1.0
        elif candidate_location and preferred_location:
            if preferred_location in candidate_location or candidate_location in preferred_location:
                scores["location_score"] = 1.0
            else:
                # Check for same state/region
                location_similarity = SequenceMatcher(None, candidate_location, preferred_location).ratio()
                scores["location_score"] = max(0.3, location_similarity)
        else:
            scores["location_score"] = 0.5  # Unknown location
        
        # 4. SALARY SCORING (10% weight)
        candidate_salary_exp = candidate.get("salary_expectation")
        if candidate_salary_exp and (job_req.salary_min or job_req.salary_max):
            salary_min = job_req.salary_min or 0
            salary_max = job_req.salary_max or float('inf')
            
            if salary_min <= candidate_salary_exp <= salary_max:
                scores["salary_score"] = 1.0
            elif candidate_salary_exp < salary_min:
                # Candidate expects less (good for employer)
                scores["salary_score"] = 1.1
            else:
                # Candidate expects more (negotiate or pass)
                over_budget = (candidate_salary_exp - salary_max) / salary_max
                scores["salary_score"] = max(0.2, 1 - over_budget)
        else:
            scores["salary_score"] = 0.8  # Neutral if no salary info
        
        # 5. EDUCATION SCORING (3% weight)
        candidate_education = candidate.get("education_level", "").lower()
        required_education = (job_req.education_level or "").lower()
        
        education_hierarchy = {
            "high school": 1, "associate": 2, "bachelor": 3, 
            "master": 4, "phd": 5, "doctorate": 5
        }
        
        candidate_edu_level = 0
        required_edu_level = 0
        
        for edu, level in education_hierarchy.items():
            if edu in candidate_education:
                candidate_edu_level = max(candidate_edu_level, level)
            if edu in required_education:
                required_edu_level = max(required_edu_level, level)
        
        if required_edu_level == 0:
            scores["education_score"] = 1.0  # No requirement
        elif candidate_edu_level >= required_edu_level:
            scores["education_score"] = 1.0
        else:
            scores["education_score"] = max(0.5, candidate_edu_level / required_edu_level)
        
        # 6. INDUSTRY SCORING (2% weight)
        candidate_industry = candidate.get("industry", "").lower()
        preferred_industry = (job_req.industry_preference or "").lower()
        
        if not preferred_industry:
            scores["industry_score"] = 1.0
        elif candidate_industry and preferred_industry in candidate_industry:
            scores["industry_score"] = 1.0
        else:
            scores["industry_score"] = 0.7  # Different industry penalty
        
        # CALCULATE TOTAL SCORE
        weights = {
            "skill_score": 0.50,
            "experience_score": 0.25,
            "location_score": 0.10,
            "salary_score": 0.10,
            "education_score": 0.03,
            "industry_score": 0.02
        }
        
        total_score = sum(scores[key] * weights[key] for key in weights.keys())
        
        # Apply penalties for missing required skills
        if scores.get("missing_required_skills"):
            penalty = len(scores["missing_required_skills"]) * 0.2
            total_score = max(0.1, total_score - penalty)
        
        scores["total_score"] = round(total_score, 3)
        scores["percentage"] = round(total_score * 100, 1)
        scores["grade"] = self.get_score_grade(total_score)
        
        return scores
    
    def get_score_grade(self, score: float) -> str:
        """Convert numerical score to letter grade."""
        if score >= 1.1:
            return "A+"
        elif score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B+"
        elif score >= 0.7:
            return "B"
        elif score >= 0.6:
            return "C+"
        elif score >= 0.5:
            return "C"
        else:
            return "D"

# Initialize the enhanced scorer
scorer = IntelligentCandidateScorer()

def create_enhanced_workflow():
    """Create enhanced LangGraph workflow for HR recruiting."""
    workflow = StateGraph(AgentState)
    
    def start_node(state: AgentState):
        """Initial processing of job requirements."""
        req = state.messages[-1].content
        return AgentState(messages=[
            SystemMessage(content="Enhanced HR Recruiting Workflow Started"),
            HumanMessage(content=json.dumps(req))
        ])
    
    def search_candidates(state: AgentState):
        """Enhanced node to search for candidates."""
        req_data = json.loads(state.messages[-1].content)
        
        # Extract skill names for search
        skill_names = [skill.get("name", "") for skill in req_data.get("required_skills", [])]
        
        tool_input = {
            "skills": skill_names,
            "location": req_data.get("location"),
            "experience_min": req_data.get("experience_years_min"),
            "experience_max": req_data.get("experience_years_max"),
            "salary_min": req_data.get("salary_min"),
            "salary_max": req_data.get("salary_max"),
            "remote_ok": req_data.get("remote_ok", False),
            "limit": 50  # Get more candidates for better scoring
        }
        
        return AgentState(messages=state.messages + [
            FunctionMessage(content=tool_input, name="search_candidates")
        ])
    
    def enhanced_analyze_candidates(state: AgentState):
        """Enhanced candidate analysis with intelligent scoring."""
        candidates = state.messages[-1].content.get("candidates", [])
        req_data = json.loads(state.messages[1].content)
        
        if not candidates:
            return AgentState(messages=state.messages + [
                AIMessage(content="No suitable candidates found matching the criteria")
            ])
        
        # Convert dict to enhanced request model
        job_req = EnhancedRecruitRequest(**req_data)
        
        # Score all candidates
        scored_candidates = []
        for candidate in candidates:
            try:
                score_data = scorer.score_candidate(candidate, job_req)
                scored_candidate = {
                    **candidate,
                    "ai_score": score_data["total_score"],
                    "ai_percentage": score_data["percentage"],
                    "ai_grade": score_data["grade"],
                    "score_breakdown": score_data,
                    "missing_skills": score_data.get("missing_required_skills", [])
                }
                scored_candidates.append(scored_candidate)
            except Exception as e:
                # Fallback scoring for malformed candidate data
                scored_candidate = {
                    **candidate,
                    "ai_score": 0.1,
                    "ai_percentage": 10.0,
                    "ai_grade": "D",
                    "score_breakdown": {"error": str(e)},
                    "missing_skills": []
                }
                scored_candidates.append(scored_candidate)
        
        # Sort by AI score and take top candidates
        sorted_candidates = sorted(scored_candidates, key=lambda x: x["ai_score"], reverse=True)[:10]
        
        return AgentState(messages=state.messages + [
            FunctionMessage(
                content={"top_candidates": sorted_candidates},
                name="enhanced_analyze_candidates"
            )
        ])
    
    def enhanced_recommendation(state: AgentState):
        """Generate enhanced recommendations with detailed insights."""
        candidates = state.messages[-1].content.get("top_candidates", [])
        req_data = json.loads(state.messages[1].content)
        
        if not candidates:
            recommendation = "No qualified candidates found. Consider:\n"
            recommendation += "• Expanding location requirements\n"
            recommendation += "• Reducing experience requirements\n"
            recommendation += "• Offering remote work options\n"
            recommendation += "• Increasing salary range"
        else:
            job_title = req_data.get("job_title", "position")
            total_found = len(candidates)
            
            # Categorize candidates by score
            excellent = [c for c in candidates if c["ai_score"] >= 0.9]
            good = [c for c in candidates if 0.7 <= c["ai_score"] < 0.9]
            fair = [c for c in candidates if 0.5 <= c["ai_score"] < 0.7]
            
            recommendation = f"## Candidate Analysis for {job_title}\n\n"
            recommendation += f"**Found {total_found} candidates:**\n"
            recommendation += f"• {len(excellent)} excellent matches (90%+ fit)\n"
            recommendation += f"• {len(good)} good matches (70-89% fit)\n"
            recommendation += f"• {len(fair)} fair matches (50-69% fit)\n\n"
            
            if excellent:
                recommendation += "### 🌟 TOP RECOMMENDATIONS:\n"
                for i, candidate in enumerate(excellent[:3], 1):
                    name = candidate.get("name", f"Candidate {i}")
                    title = candidate.get("title", "Unknown Title")
                    company = candidate.get("company", "Unknown Company")
                    score = candidate["ai_percentage"]
                    grade = candidate["ai_grade"]
                    
                    recommendation += f"{i}. **{name}** - {title} at {company}\n"
                    recommendation += f"   Score: {score}% (Grade {grade})\n"
                    
                    # Add key strengths
                    breakdown = candidate.get("score_breakdown", {}).get("breakdown", {})
                    strengths = [skill for skill, data in breakdown.items() 
                               if isinstance(data, dict) and data.get("score", 0) > 0.8]
                    if strengths:
                        recommendation += f"   Strengths: {', '.join(strengths[:3])}\n"
                    
                    # Add concerns
                    missing = candidate.get("missing_skills", [])
                    if missing:
                        recommendation += f"   ⚠️  Missing: {', '.join(missing)}\n"
                    
                    recommendation += "\n"
            
            # Add hiring insights
            recommendation += "\n### 📊 HIRING INSIGHTS:\n"
            
            # Common missing skills
            all_missing = []
            for candidate in candidates:
                all_missing.extend(candidate.get("missing_skills", []))
            
            if all_missing:
                from collections import Counter
                most_missing = Counter(all_missing).most_common(3)
                recommendation += "• **Skills in short supply:** "
                recommendation += ", ".join([f"{skill} ({count} candidates missing)" 
                                           for skill, count in most_missing])
                recommendation += "\n"
            
            # Salary insights
            salary_expectations = [c.get("salary_expectation") for c in candidates 
                                 if c.get("salary_expectation")]
            if salary_expectations:
                avg_salary = sum(salary_expectations) / len(salary_expectations)
                recommendation += f"• **Average salary expectation:** ${avg_salary:,.0f}\n"
            
            # Location insights
            locations = [c.get("location") for c in candidates if c.get("location")]
            if locations:
                from collections import Counter
                top_locations = Counter(locations).most_common(3)
                recommendation += f"• **Top candidate locations:** {', '.join([loc for loc, _ in top_locations])}\n"
        
        return AgentState(messages=state.messages + [
            AIMessage(content=recommendation)
        ])
    
    # Add nodes to workflow
    workflow.add_node("start", start_node)
    workflow.add_node("search", search_candidates)
    workflow.add_node("analyze", enhanced_analyze_candidates)
    workflow.add_node("recommend", enhanced_recommendation)
    
    # Define edges
    workflow.set_entry_point("start")
    workflow.add_edge("start", "search")
    workflow.add_edge("search", "analyze")
    workflow.add_edge("analyze", "recommend")
    workflow.add_edge("recommend", END)
    
    return workflow.compile()

# Initialize enhanced workflow
enhanced_workflow = create_enhanced_workflow()

@app.post("/recruit", response_model=EnhancedRecruitResponse)
async def enhanced_recruit_candidates(request: EnhancedRecruitRequest):
    """Enhanced endpoint for intelligent candidate recruitment."""
    try:
        # Execute enhanced workflow
        result = enhanced_workflow.invoke(AgentState(messages=[
            HumanMessage(content=request.dict())
        ]))
        
        # Extract final recommendation
        final_message = next(
            msg for msg in reversed(result.messages)
            if isinstance(msg, AIMessage)
        )
        
        # Extract candidates with enhanced scoring
        candidates_data = next(
            (msg.content for msg in reversed(result.messages)
             if isinstance(msg.content, dict) and "top_candidates" in msg.content),
            {"top_candidates": []}
        )
        
        candidates = candidates_data.get("top_candidates", [])
        
        # Generate scoring breakdown summary
        scoring_breakdown = {
            "total_candidates_evaluated": len(candidates),
            "scoring_criteria": {
                "skills": "50% weight - Matches required skills with proficiency levels",
                "experience": "25% weight - Years of experience and seniority level",
                "location": "10% weight - Geographic match or remote compatibility",
                "salary": "10% weight - Salary expectation alignment",
                "education": "3% weight - Educational background requirements",
                "industry": "2% weight - Industry experience relevance"
            },
            "grade_distribution": {}
        }
        
        if candidates:
            from collections import Counter
            grades = [c.get("ai_grade", "D") for c in candidates]
            scoring_breakdown["grade_distribution"] = dict(Counter(grades))
        
        return EnhancedRecruitResponse(
            job_description=request.dict(),
            candidates=candidates,
            recommendation=final_message.content,
            scoring_breakdown=scoring_breakdown
        )
        
    except Exception as e:
        raise HTTPException(500, f"Enhanced recruitment failed: {str(e)}")

@app.get("/tools")
async def get_enhanced_tools():
    """Expose enhanced agent's capabilities as tools."""
    return {
        "tools": [{
            "name": "enhanced_recruit_candidates",
            "description": "Find and intelligently score candidates with advanced matching algorithms",
            "input_schema": {
                "type": "object",
                "properties": {
                    "job_title": {"type": "string"},
                    "required_skills": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "weight": {"type": "number", "default": 1.0},
                                "required": {"type": "boolean", "default": False},
                                "level": {"type": "string", "enum": ["beginner", "intermediate", "advanced", "expert"]}
                            }
                        }
                    },
                    "preferred_skills": {"type": "array", "items": {"type": "object"}},
                    "location": {"type": "string"},
                    "remote_ok": {"type": "boolean", "default": False},
                    "experience_years_min": {"type": "integer"},
                    "experience_years_max": {"type": "integer"},
                    "education_level": {"type": "string"},
                    "salary_min": {"type": "integer"},
                    "salary_max": {"type": "integer"},
                    "industry_preference": {"type": "string"},
                    "company_size_preference": {"type": "string"}
                },
                "required": ["job_title", "required_skills"]
            }
        }]
    }

@app.get("/")
async def enhanced_health_check():
    """Enhanced health check endpoint."""
    return {
        "status": "enhanced",
        "service": "Enhanced HR Recruiting Agent",
        "version": "2.0.0",
        "features": [
            "Intelligent skill matching with synonyms",
            "Experience-weighted scoring",
            "Multi-criteria candidate evaluation",
            "Proficiency level assessment",
            "Location and salary optimization",
            "Educational background scoring",
            "Industry experience weighting"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)