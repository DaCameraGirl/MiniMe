import React, { useState } from 'react';
import PromptGenerator from './components/PromptGenerator';
import RubricBuilder from './components/RubricBuilder';
import ResponseGrader from './components/ResponseGrader';
import ResultsExport from './components/ResultsExport';

const STEPS = ['Create Prompt', 'Design Rubric', 'Evaluate Responses', 'Download Report'];

export default function App() {
  const [step, setStep] = useState(0);
  const [prompt, setPrompt] = useState(null);
  const [rubric, setRubric] = useState([]);
  const [grades, setGrades] = useState(null);

  const next = () => setStep(s => Math.min(s + 1, 3));
  const back = () => setStep(s => Math.max(s - 1, 0));

  return (
    <div style={{
      minHeight: '100vh',
      background: '#0a0e17',
      color: '#e6edf3',
      fontFamily: "'Segoe UI', sans-serif",
      padding: '0 20px 40px'
    }}>
      {/* Header */}
      <div style={{
        textAlign: 'center',
        padding: '30px 0 20px',
        borderBottom: '1px solid rgba(255,255,255,0.1)',
        marginBottom: 30
      }}>
      <h1 style={{ fontSize: 28, fontWeight: 700, margin: 0, letterSpacing: 2 }}>
  🚀 AI Evaluator Pro
</h1>
<p style={{ color: '#8b949e', fontSize: 13, marginTop: 6 }}>
  Advanced AI Response Assessment System
</p>
      </div>

      {/* Step Indicator */}
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        gap: 8,
        marginBottom: 30,
        flexWrap: 'wrap'
      }}>
        {STEPS.map((label, i) => (
          <div key={i} onClick={() => setStep(i)} style={{
            padding: '8px 18px',
            borderRadius: 6,
            fontSize: 12,
            fontWeight: 600,
            cursor: 'pointer',
            background: step === i ? '#ffb800' : '#161b22',
            color: step === i ? '#07090e' : '#8b949e',
            border: `1px solid ${step === i ? '#ffb800' : 'rgba(255,255,255,0.1)'}`,
            transition: 'all 0.2s'
          }}>
            {i + 1}. {label}
          </div>
        ))}
      </div>

      {/* Content */}
      <div style={{ maxWidth: 800, margin: '0 auto' }}>
        {step === 0 && (
          <PromptGenerator
            onGenerate={(p) => { setPrompt(p); next(); }}
          />
        )}
        {step === 1 && (
          <RubricBuilder
            prompt={prompt}
            rubric={rubric}
            setRubric={setRubric}
            onNext={next}
            onBack={back}
          />
        )}
        {step === 2 && (
          <ResponseGrader
            prompt={prompt}
            rubric={rubric}
            onGrade={(g) => { setGrades(g); next(); }}
            onBack={back}
          />
        )}
        {step === 3 && (
          <ResultsExport
            prompt={prompt}
            rubric={rubric}
            grades={grades}
            onBack={back}
            onRestart={() => { setStep(0); setPrompt(null); setRubric([]); setGrades(null); }}
          />
        )}
      </div>

{/* Footer */}
<div style={{
  textAlign: 'center',
  marginTop: 40,
  paddingTop: 20,
  borderTop: '1px solid rgba(255,255,255,0.1)',
  color: '#8b949e',
  fontSize: 12
}}>
  Built with React • MiniMe v1.0
</div>

    </div>
  );
}
