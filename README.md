
DEEPSEEK_API_KEY=sk-83fcb178c65a4d579aa744ced5b74067
Deepseek R1 0528
📚 Valkyrie Project Guidelines

🧠 Mental Model: Write Like a Real User

Knowledge Cutoff Date: The model has no knowledge of the world after January 31, 2023. Requesting information after this date is not allowed. 
Reference Texts: Any documents you'd like to model to utilize must be copied and pasted into the Attachment tool below the prompt box. 100,000 word maximum.
No General Internet Search: The model has knowledge of the world, but does not have internet access. If you’d like it to reference specific information, please provide that information as a reference text. 
A strong prompt should sound like something you’d actually type into ChatGPT mid-task. Picture it: you’re working on something, hit a tricky spot, and ask a question to get unstuck. That’s what good prompts look like—natural, specific, and grounded in real work.

You're not writing a test.
You're not crafting a homework or exam problem.
You're not roleplaying a job title.

What kinds of questions did you ask while doing your job?

Where did the model struggle to meet expert expectations?

These are the questions worth turning into prompts.

💡What Makes a Good Prompt

A strong prompt balances realism, specificity, and challenge. It mimics how professionals naturally ask for help mid-task—without over-explaining, role-playing, or stacking artificial instructions. In this course, we’ll go over these components of good prompts:

No Personas: You’re the user—ask as yourself. Don’t write as if you’re someone else.

No Stacked Constraints: Avoid piling on tasks just to trip up the model.

First Person: Prompts should be your ask, not a homework problem or interview question.

Don’t Over-Explain: Assume the model is a capable expert. Skip step-by-step instructions for standard processes.

No Single Correct Answer: Good prompts support diverse, well-reasoned outputs—not just one “right” answer. Rubrics are built to evaluate variability.

Natural Tone - No Personas

Goal: Write the way you’d actually ask a colleague or type into ChatGPT mid-task. You’d never start your questions to a colleague with “I am…” or “You are…”—so don’t do it here.

✅ Good: We’re reevaluating flood risk zones after major urban sprawl in a low-lying coastal city. What modeling approach should we use to estimate 100-year floodplain changes under both climate and land use scenarios?

🚫 Bad: You are the Lead Hydrologist for RiverSafe Consulting, hired by the City of Crestfall to address chronic flooding along its downtown riverfront …

🚫 Bad: You are a mechanical design engineer responsible for automotive interior components. You are assigned an asymmetric, injection-molded armrest that…

🚫 Bad: You are tasked with designing a striped microcavity quantum well infrared photodetector…

🚫 Bad: Jane, the production planner, is conducting time studies on the shop floor. Jane collected 10 observations (in seconds) from…

🚫 Bad: I am part of a structural engineering team responsible for designing a two-story residential building in Scarborough, Ontario…. (Instead say: Design a two-story residential…)

📚 Stacked Constraints
Avoid Artificial Complexity: Depth Over Volume
Goal:  Design prompts that challenge through expert reasoning—not through artificially stacked instructions. True difficulty should come from the domain knowledge and judgment needed to address a substantive problem, not from how many tasks are jammed into the prompt.

✅ Good Prompt: Depth via Expert Reasoning
Example: Relate this dichotomy to the existence of compatible Lefschetz fibrations with non-isotopic monodromy representations:

Let XX be a closed, simply connected smooth 4-dimensional manifold with b2+(X)≥2b_2^+(X) \geq 2 that admits at least one symplectic structure. Determine necessary algebraic-topological conditions under which the following dichotomy holds:

XX admits a unique symplectic smooth structure (up to symplectomorphism and deformation), yet carries infinitely many non-symplectic exotic smooth structures.

XX admits infinitely many distinct symplectic exotic smooth structures, all with non-isomorphic Gromov-Witten invariants.

Why It’s Good: This is a clean, research-driven question with embedded complexity. The reasoning challenge comes from understanding the topology and geometry—not from formatting or listing. The model must think like an expert, not just recall definitions.

🚫 Bad Prompt: Superficial Difficulty via Stacked Constraints
Example: Explain all types of smooth structures a 4-manifold can have. Include definitions of exotic smooth structures, Gromov-Witten invariants, and Lefschetz fibrations. Then list known examples. Format as a literature review.

Why It Fails: This prompt looks complex, but only because it stacks superficial requests: define, list, summarize, format. It doesn’t test expertise—it just mimics a checklist you might find on an undergrad worksheet. The model isn’t reasoning—it’s regurgitating.


Good Use of Constraints: Domain-Specific, Expert-Relevant
Still, not all constraints are bad. Well-chosen constraints help shape realistic, domain-specific requests—just like those a real expert might face. But avoid stacking multiple tasks just to make the prompt harder; artificial complexity rarely reflects how professionals actually work and often leads to unrealistic or unhelpful prompts. Here’s an example of realistic constraints

Example: I want to design a project of an intermolecular Aza Paterno–Büchi reaction between acyclic imines and disubstituted alkenes. Including the synthesis of the starting materials and photocatalysts (if not commercially available) and the optimisation strategy, the project should also fulfil the following criteria:

Reaction conditions must be mild (visible light only, 20–35°C).

Side products—e.g. isomerization or fragmentation of imines—should be avoided.

Alkenes should not be excited via energy transfer; scope must include electron-donating and withdrawing variants.

Why These Constraints Work

Scientifically grounded: The light source and temperature limits reflect real synthetic constraints—not arbitrary rules.

Mechanistically rich: Avoiding side products and managing energy transfer requires real chemical insight.

Well-scoped: The constraints define a focused research problem—not a pile of instructions.

Expert-level: Understanding and meeting these requirements calls for deep knowledge of photochemistry—not surface-level list-making.

Bottom Line:
Avoid turning complex prompts into to-do lists. The best prompts challenge the model to reason like a domain expert—not just format, define, and summarize.

🙋 First Person
Write in the First Person: Make It Sound Like a Real Request
Why it matters:
Prompts written in the third person sound like exam questions or case study setups. They don't reflect how professionals actually ask for help. Writing in the first person makes the request feel grounded, urgent, and real—like something you'd type mid-task.

🚫 Bad - Third-Person, Interview Case Study Style
“Consider a company that has a cloud based data analytics platform. The company has a good data maturity and the data is being actively consumed by product, marketing and finance teams. Each team has different SLA and freshness requirements. The company is planning to increase AI adoptions and is planning to hire data scientists who have vastly different data requirements compared to engineers and analysts. What makes the situation more complex is the company is facing severe performance issues already i.e. ad-hoc queries by stakeholders taking a long time, ETL jobs not finishing within their pre-defined SLA’s. The company has traditionally tried to solve this by throwing more resources at the problem, making them go significantly over budget.

Create an optimization plan for the company to address these issues. The plan must address infrastructure, data layout, workload management, cross-team complexities while keeping the stakeholders happy. The plan is significantly important as the company cannot undertake this exercise frequently to prevent disruptions.”

Why it’s bad: This version sounds like an interview case study. It’s written in the third person, bloated with background, and uses unnatural language ("consider a company..."). It distances the speaker from the problem and doesn’t reflect how people actually ask for help in practice.

✅ Improved Prompt - First-Person, Natural Style
“We’ve got a mature cloud analytics platform, but it’s starting to crack—product, marketing, and finance teams all have different SLA/freshness needs, and we’re adding data scientists with even heavier and more varied requirements. Stakeholder queries are slow, ETLs are missing SLAs, and infra spend is already way over budget from past patchwork fixes. I need a one-shot optimization plan that covers infra, data layout, workload mgmt, and cross-team stuff without causing a ton of disruption. What should I focus on?”

Why it’s good: This version is written in the first person and mirrors how a real data lead might describe a problem mid-workflow. It’s direct, grounded in urgency, and framed as a genuine request for advice—not a formal writing task.

🚫 Bad Prompt – Exam Question Style
“Provide a critical analysis of why phenomenal overflow is better than the role of attention in perception as an explanation of the phenomenon of change blindness. Include original thoughts and a critical evaluation of those thoughts in your answer.”

Why it's bad: This prompt looks like an exam question for a philosophy student. It uses overly formal phrasing ("provide a critical analysis"), forces a position, and stacks instructions in a checklist format (“include original thoughts and evaluation”). This doesn’t resemble how professionals naturally ask for insight or test an idea.

✅ Improved Prompt – Realistic, Expert Researcher-Level Inquiry
“I’m working on a paper about change blindness and trying to assess whether phenomenal overflow offers a better explanation than attention-based theories. I’m leaning toward Block’s view but want to make sure I’m not missing strong counterarguments—can you help me evaluate how well the overflow account actually holds up?”

Why it's good: This version is grounded in a real research scenario. It’s conversational, reflects the speaker’s intent and uncertainty, and invites thoughtful engagement. The complexity comes from the philosophical nuance, not from stacked commands.

🔍 Overspecifying
Doesn’t Over-Specify the Obvious
Goal: Treat the model like an expert. Don’t spell out routine/generic steps that an expert would take as given. Assume the model is as knowledgeable as your colleagues. Your job is to treat the model like a peer—then use your rubric to evaluate whether it meets expert expectations.

✅ Good: I’m building a model to estimate wage elasticity in response to federal EITC policy changes, but I’m concerned about endogeneity—particularly around labor supply decisions that may correlate with unobserved productivity or household characteristics. What modeling strategies would you recommend to isolate causal effects—e.g., IVs, control function approaches, or leveraging policy discontinuities?

Why It’s Good: It mirrors how experts naturally ask for help mid-analysis—grounded in domain context, and requiring causal reasoning beyond rote recall.

🚫 Bad: *I want to create an econometric model to study how wages respond to changes in the federal EITC policy. *

Why it’s bad: Everything in red is artificial complexity. Any economist would know to do these things as they are standard procedures in developing an econometric model. Don’t hand-hold or spell out what’s already standard in the field.

🔍 Overspecifying
Doesn’t Over-Specify the Obvious
Goal: Treat the model like an expert. Don’t spell out routine/generic steps that an expert would take as given. Assume the model is as knowledgeable as your colleagues. Your job is to treat the model like a peer—then use your rubric to evaluate whether it meets expert expectations.

✅ Good: I’m building a model to estimate wage elasticity in response to federal EITC policy changes, but I’m concerned about endogeneity—particularly around labor supply decisions that may correlate with unobserved productivity or household characteristics. What modeling strategies would you recommend to isolate causal effects—e.g., IVs, control function approaches, or leveraging policy discontinuities?

Why It’s Good: It mirrors how experts naturally ask for help mid-analysis—grounded in domain context, and requiring causal reasoning beyond rote recall.

🚫 Bad: *I want to create an econometric model to study how wages respond to changes in the federal EITC policy. *

Why it’s bad: Everything in red is artificial complexity. Any economist would know to do these things as they are standard procedures in developing an econometric model. Don’t hand-hold or spell out what’s already standard in the field.

The goal of the task is to generate a task where both models produce subpar or bad responses
Average of two final scores is less than  80% and both are less than 85%
Role playing (you are xyz), persona questions are the worst kind of prompts. Please make your prompt unique to your expertise/field and something you would actually ask a colleague
The prompt should require the response to have substantial analysis, interpretation, or creative thinking rather than just mechanical problem-solving
Bad prompts are pure mathematical, factual, procedural, or formulaic problems where experts would get to the same answer 90% of the time
You do not need a complex prompt with a long list of requests; however, each prompt should be meaningful. Adding a ton of requests will make rubrics difficult and lead to a bad and unnatural prompt
Focus on questions that you or another expert in your field would actually care about. Do not request contrived/adjacent things like making a lesson plan
Rubrics are a pedantic exercise; make sure you review the rubrics instructions multiple times
Rubrics should be atomic (they do not combine multiple requirements into one)
Rubrics should be self contained (they contain an example and can be answered true or false by any layman)
For negative weights, make sure the rubric is about the inclusion of a bad detail and is in the affirmative
Negative weights highlight actual mistakes, inaccuracies, or harmful/irrelevant content that detract from a response's quality.
Do not use should or must for rubrics with negative weights
The core requests/requirements should have the highest weights
Rubrics should be comprehensive of what a great response would be and include all explicit requests from the prompt
Check the final checklist prior to submission
If you get a task with a subject outside of your subject matter, skip it until you find one within your subject matter. There’s unlimited tasks so just skip please.

Workflow

Write a Prompt
Your prompt should mirror how you interact with chatpgt. Your prompt should be natural, meaning it’s to the point, shorthand, and has little to no context. You ask your question and that’s it. Craft a realistic prompt from your domain of expertise. This should be something you or a coworker might genuinely face. The prompt should be challenging; it shouldn’t be solvable with a quick lookup. Make sure it truly tests the model’s capabilities.

Review Model Responses
Review up to four Responses to your prompt. You’re looking for two things here:

1. The responses vary in quality. There should be variability in what they do well and what they do poorly.

2. There is room to improve on all model responses.

The more variability you have in responses, the more valuable the data is to model training. If all responses look the same, or if all of them do the same things well and the same things poorly, it’s not useful training data for model improvement.

Rank Model Responses
Do a quick best-to-worst ranking of the four answers; if that’s tough, the responses are probably too similar and you should tweak your prompt.

Create Rubric
Think of this as a recipe which lays out all the criteria that must be satisfied to make the response good. A good rubric can distinguish between high-quality and low quality responses; every rubric criterion should really matter to you as the end recipient of this model answer. More on rubrics later.

Evaluate Model Responses
For each response, evaluate your rubrics each with straight “Present/Not Present” checks. If you want to give partial credit, rewrite or split that rubric criterion—it’s probably not specific enough. Every response should land below 80% on your rubric scoring; if they don’t you’ll be blocked from submitting.

Final Scores and Ranking
Re rank the responses based on how well they scored in your rubrics.

A strong prompt should meet these conditions

Naturalness: Prompts must be representative of real-world use cases, so write how you normally would and about what you know. Check your ChatGPT history for inspiration!
Don’t Force It: Do not just string together tons of constraints/instructions in order to make the chatbot fail. These types of prompts will not be useful
First Person:  Write prompts the way you would actually ask a question. Use “I” or “we,” just like you do when talking to a coworker. For example, instead of saying “Consider a company that…”, say “I’m working with a company that…” or “We’re seeing issues with…”.

Specific Need: Prompts should focus on a specific ask that a user would need a chatbot for
Avoid “trivia” or “homework” prompts

Conciseness: Only include necessary details in your prompts. Do not overload your prompts with unnecessary background information

Not Over-specified: Prompts should treat the model like an expert—skip unnecessary context or step-by-step instructions that a domain expert would already know.

Spelling and grammar don’t matter: You don’t need perfect spelling or grammar in your prompts. Real-world users jump into their questions and don’t care about spelling/grammar

Challenging
Your prompt should create two bad or sub-par responses. Generally, this means requiring reasoning to be answered. Avoid simple tasks such as quick search, calculation, or fact recall.

Feasible
Your prompt can realistically be completed by a knowledgeable professional with the given data + publicly available non-LLM resources.

Baked-in Variability
Good prompts are, to some extent, open-ended. They should leave room for models to have different approaches to answer your question. There should be a baked-in variability to your prompt, meaning lots of ways to do it right or wrong.

This is the foundation for rubric-based scoring because it allows for more than one objective final answer. Ask for things like synthesis, explanation, evaluation, etc, which leaves room for models to fulfil the task in variable ways.

Clear Assumptions
State any non-obvious assumptions an expert would need to make when answering your question. You don’t need to write out obvious assumptions or ones which other people in your field would know to make. Beyond that, it's fine to leave room for subjective interpretation of what makes a great response as long as you define those aspects in your rubrics

Realistic
Your prompt should reflect real-world, professional challenges. If anyone outside your field can answer your prompt, you should rework it.

Your prompt should be naturally phrased; put yourself in the shoes of the user – most users write with shorthand and don’t have perfect spelling or grammar. They don’t add unnecessary context or stack constraints. Dive into your question. Generally, a prompt should be anywhere from 1 to 5 sentences. However, it is okay to post a document or other text in your ref text since lots of users ask a natural question and then paste a long block of unstructured or structured text.

You should avoid including the following in your prompt:

Pleasantries
Adopting a person (e.g. “I am…” or “You are”)
Unnecessary constraints
Justifications for constraints
A backstory unless it's necessary
Stacked questions that don’t add value to your core request
Arbitrary word-count constraints

These are usually unrealistic in a professional context.

More Than One Objective Correct Answer
Remember the whole thing about baked-in variability? This is the same idea. If you’re asking for stuff that has a single definitive final answer, then the prompt is not suited for rubrics.

For example, asking the model to calculate the interest rate given a set of variables, or to solve  an equation, or name a specific precedent that is informing a law, are all bad premises here.

Why? Because you can’t build a good rubric around them: the model’s answer is either right or wrong. This is not what we’re after.

But what if my rubric items lay out all the intermediary steps that the model needs to get right, like the steps to solve a set of differential equations? This would be a different type of data training called Process Supervision. It’s not what we’re trying to do here, so save those prompts for a different project!

You should make sure your prompt:

Unique to your expertise/field and something you would actually ask
Requires the response to have substantial analysis, interpretation, or creative thinking rather than just mechanical problem-solving
Written naturally as a user would ask their question to a chatbot

You should avoid including the following in your prompt:

Pleasantries
Adopting a person (e.g. “I am…” or “You are”)
Lesson plan
Unnecessary constraints
Justifications for constraints
A backstory unless it's absolutely necessary
Stacked questions that don’t add value to your core request
Arbitrary word-count constraints
Role playing (you are, I am) or persona question
Prompts that are pure mathematical, factual, procedural, or formulaic problems where experts would get to the same answer 90% of the time

Scenarios to guide realistic prompt writing:

You're mid-task and hit a fork in the road—what would you ask ChatGPT to help you move forward?
You're at a research conference—what would a peer ask about your work?
You’re troubleshooting something that just broke—what do you need help diagnosing?
You’re weighing two implementation paths—what factors do you need to compare?
You’re under pressure to make a call—what risks or trade-offs do you need to understand fast

What Contrived/Unrealistic Prompts Look Like

Contrived prompts feel artificial, overstructured, or test-like. They often include unnecessary context, stacked constraints, adopting a persona, or step-by-step instructions that no expert would spell out in real life. This section breaks down the most common patterns to avoid.

Contrived Pattern

Why It Fails

Example

Starts with a persona

Adds artificial setup; not how users write to tools or teammates.

“As the CTO of a battery firm…”“You are a construction manager…”

Uses the third person

Sounds like a case study in an interview, not a real request; reframe using the first person

“An engineering consultancy is evaluating X, Y, Z … prepare a feasibility report."

Overloaded / stacked asks

Makes the prompt feel like a test. Split into multiple prompts instead.

“Summarize the article, make a table, write an evaluation, then create a protocol.”

Over-specifying the Obvious        

Over-specifies steps an expert would take for granted. Assume the model is as capable as a colleague—don’t hand-hold or spell out the obvious.

“I want to create an econometric model. Please state the model, list the variables, note diagnostic tests, and address endogeneity.”

Backstory adds no value

Wastes attention; makes the prompt longer without improving clarity.

“MegaCorp is a multinational currently acquiring Digital Ltd…”

Explains or justifies constraints

Real users don’t explain why they’re asking. They just ask.

“Because our lab has access to most chemicals, I need a protocol…”

Lists every sub-part in a multi-step format

Too structured. Real people don’t write like checklists unless required.

“1. Hydrologic analysis 2. Mitigation table 3. Stakeholder plan…”

Includes arbitrary numbers or formatting

Word limits, bullet point counts, etc., are almost never realistic.

“Write a 1050-word report with exactly five bullet points.”

Only one objectively correct answer

Not suitable for rubric-based scoring. These are better suited for process supervision or factual QA.

“Calculate ROCE for all five options and show your math.”

What Realistic Prompts Look Like
These prompts are natural, professional, and grounded in domain-specific work. They demonstrate how to ask challenging, feasible, and realistically phrased questions that invite reasoning and allow for variable responses.

Realistic Pattern

Why It Works

Good Prompt Example

Straightforward phrasing, grounded in research

Avoids persona; sounds like a real-world physics modeling request.

“Make a model of how a neutron star cools after formation. What are the key principles or processes used in building such a model?”

Professional problem framed as a decision-making task

Asks for comparative evaluation that a real engineer might conduct.

“Compare HTS and LTS magnets for use in high-power stellarator field coils. Recommend one.”

Field-specific, analytically rich, and clearly open-ended

Invites a structured breakdown without being test-like.

“Propose a methodology to decompose last year’s trading PnL into beta and alpha return components.”

Simple task + realistic constraint (e.g., reference text, brevity)

Models how a peer reviewer would realistically interact with a document.

“Provide a peer review draft of the attached CS paper. It should be shorter than the paper itself.”

Technically complex task tied to user constraints

Includes relevant hardware/environmental context, but avoids over-explaining.

“Using an RTX 3050, recommend the best setup for training an ECG bagging ensemble”

Scenario mimics real-world team collaboration

Good balance of technical depth, product needs, and stakeholder framing.

“We’re building a food delivery robot for sidewalks and streets. Compare two drivetrain options and recommend one.”

Detailed but not overloaded; research-aligned task

Constraints serve the task; request is realistic for a journal contributor.

“Create a literature review outline for an ethics paper on investment culpability. Format each required section clearly.”

Prompt Category
You will be asked to select a prompt category prior to writing your prompt. Please update it if you later change your prompt and the category no longer fits.

Prompt Category

Description

Q&A

A prompt that focuses on finding the answer to one or more questions, and explaining the process by which it arrived at the answer.

File Understanding and Analysis

A prompt that focuses on analyzing and critiquing reference text(s). A large majority of the response is original content.

Summarization, Extraction, Editing and Rewrites

prompt that focuses on summarizing, editing, rewriting, continuing, or extracting information from reference text(s). A significant portion of the response is drawn from the reference text (whether verbatim or summarizing).

Plan and Document Generation

A prompt that focuses on creating structured, usually goal-oriented content such as plans, strategies, proposals, or formal documents.

Next Steps
After writing your prompt, you will be asked to:

Choose the domain (e.g., chemistry, law, business)
Confirm the prompt reflects the complexity of professional work in that field

Recap of Core Requirements
Your prompt will be reviewed against five essential standards:

Criterion

Definition

Realistic

Real-world, professional scenarios. Avoid overly hypothetical questions, unrealistic constraints, random unnecessary context, etc.

Challenging

The average score of the responses is <80% on your rubric and both are less than <85%

Feasible

Can realistically be completed by a knowledgeable professional.

Baked in Variability

Avoid prompts with a single objective final answer. Ask for things like synthesis, explanation, evaluation, etc, which leave room for models to vary in their strategy, reasoning, and/or results.

Clear Assumptions

State any assumptions an expert would need to make when answering your question. Beyond that, it's fine to leave room for subjective interpretation of what makes a great response as long as you define those aspects in your rubrics

Important Things to Consider

Prompts That Don’t Fit This Project:

Prompts with one objective correct answer
Prompts that require knowledge beyond January 31, 2023
Prompts with Temporal asks; you should avoid time-relative terms (e.g., "latest") where the response depends on when the question was asked or asks for information
Information retrieval queries (simply finding and repeating a fact or snippet)
Asking to only fix or generate code
Puzzles, games, sports, or entertainment prompts

Other General Guidelines

You can attach a reference text as context for your prompt (100,000 words max)
This is optional.
The Model Cant Search The Internet
If you’d like to reference specific information, please provide that information as a reference text

Step 1: How to add an image

Below the prompt box, you will find two different buttons.

To add a reference text

To attach an image

To correctly add your image, you will need to upload it and provide the URL as seen in the following example

Note: Please do NOT use copyrighted images or images with content protected by NDA (screenshots of internal memos, etc.)

Step 2: How to upload your image

To attach an image, you can right-click on your chosen image, select “Copy Image Address,” and paste the URL into the appropriate tab in Outlier.

If you are using your own image, enter your preferred image website uploader (like Imgur), and upload it there. After that, follow the previous step.

**Please make sure that whatever website you use doesn't automatically delete the image after a certain amount of time. For example, using Imgbb, you have to select "Don't autodelete." option.**

DO:
✅ If you upload an image, it should be directly related to the prompt.

✅ If you upload an image, it must be used.

✅ Save your file in one of the following formats: .jpg, .jpeg, or .png.

✅ Ensure clarity and proper sizing (minimum 800px on the smallest side).


DON’T

❌ Include any Personal Identifiable Information

❌ Have NSFW (Not Safe For Work) content

❌ Be blurry/unreadable

When writing a prompt, don’t describe the image in so much detail that the image itself becomes unnecessary. The image must be ﻿needed to solve the prompt.

Image Tips
Before adding your entire prompt and rubrics, please test that your image is readable by both models. You can test it by adding a simple prompt like “What’s in the image”

Step 2: Review the Model Responses

Now you will review between 2 and 4 responses generated by the model to your prompt. The goal is to understand how the model interpreted your request and assess how effectively each response meets the criteria for an excellent answer.

This review is not about grading yet—it’s about observing and preparing to write a solid rubric.

As you read through the responses, consider the following questions and take mental notes about which elements stand out. You’ll build on these observations in your rubric.

Did the response actually follow the prompt instructions?
Is the reasoning sound and complete?
Is the structure clear and logical?
Does it demonstrate expertise or domain-specific understanding?
Are there major issues like vague language, missing steps or factual errors?
Does it go beyond basic summarization or repetition?

Once you’ve read all responses, use drag-and-drop to rank them from best to worst based on your initial impression. This isn’t your final scoring, just a quick instinctive assessment.

It’s normal for your ranking to change later after you build and apply the rubric. That’s part of the process.

Note:  If it seems like the models are answering your prompt too well, you should go back and iterate on your prompt. Make it harder or more complex.

Step 3: Creating a Rubric

After reviewing the model responses, it’s time to build your rubric. A rubric defines what success looks like–it should reflect what an excellent response must do, and also reward helpful enhancements or flag common mistakes.

What exactly is a Rubric? A structured checklist of clear, measurable criteria used to evaluate whether a model's response meets specified requirements.

We recommend a minimum of 13 criteria per rubric.

A great rubric specifically and clearly describes everything that is needed to create a complete, high-quality response for the task’s prompts. It identifies all essential elements of a great response

Rubrics provide a structured, objective checklist (aka “criteria”)  to evaluate how well a model’s response meets a specific request. But rubrics aren’t one-size-fits-all, they vary based on the task, the context, and the kind of evidence available.

Simple Example of a Rubric:

Prompt: Help me scale up our new graduate hiring pipeline for software engineers at my tech startup based in NYC? I need to think about sourcing channels, screening & interview stages, and key metrics / feedback loops to keep improving the pipeline.

Response lists at least 3 distinct sourcing channels, such as Linkedin, Campus Career Fairs, or HackerRank challenges
Response names at least one NYC-based university program, such as Columbia University or NYU
Response includes at least 2 interview stages, such as a coding test or a behavioral interview
Response includes at least 2 metrics to monitor the pipeline, such as time-to-hire, offer-accept rate, or onsite-pass rate

NOTE: This prompt and rubric are way too simple for a real task, this exercise is meant to highlight the basic structure of a rubric

Rubric Basics
For each criterion, you’ll select or define the following in the task:

Field

What to Do

Description

Write a clear, specific, and testable expectation (use complete sentences)

Dimensional Rating

Choose the best fit (e.g., Accuracy, Completeness, Communication Quality)

Subjectivity

Mark if it’s Objective (factual/verifiable) or Subjective (interpretive)

Explicit vs. Implicit

Mark if it’s  Explicit (stated in the prompt) or Implicit

Weight

(-10 to 10)

Assign importance—higher for essentials, lower for “nice-to-haves”

You cannot use 0 as a weight.

Rubric Basics: Dimensions
Each criterion should measure one of the following dimensions of the response

Dimension

What the Criterion Checks For

Accuracy

Whether responses contain only factually correct information.

Completeness

Whether responses include all important information needed to be safe and helpful, not omitting key steps or red flags that could lead to harm.

Communication Quality

Whether responses are well-structured, concise, and use appropriate technical depth and vocabulary for the request.

Context Awareness

Whether responses respond appropriately to contextual cues (user role, location, resources) and seek clarification when needed.

Instruction Following

Whether responses adhere to instructions

Is the response doing what I asked?

Rubric Basics: Objective vs Subjective
When writing each criterion, categorize it clearly as objective or subjective.

Example Prompt: Create a short executive summary evaluating whether a logistics company should expand into cold-chain transport based on recent market data.

NOTE: This prompt is way too simple for a real task, this exercise is meant to highlight the basics of rubric criteria

Objective

Subjective

Measurable and verifiable (right/wrong)

The response must contain one clear recommendation (e.g. expand into cold-chain transport or do not expand)

Open to interpretation or judgment

The response defends its recommendation with relevant market data (e.g. data from the last year)

Rubric Basics: Explicit vs Implicit
When writing each criterion, distinguish clearly between explicit and implicit checks.

Example Prompt: Create a short executive summary evaluating whether a logistics company should expand into cold-chain transport based on recent market data.

NOTE: This prompt is way too simple for a real task, this exercise is meant to highlight the basics of rubric criteria

Explicit

Implicit

Clearly requested in the prompt

Response quotes at least two market statistics (e.g., market size, growth rate, competitor share) to support its recommendation.

Not stated, but reasonably expected (e.g., best practices, “nice-to-have”)

Response is written in an executive-level tone (e.g. concise, avoids technical jargon)

Rubrics: Writing Criteria
Each criterion should test one thing — clearly, and in a way that anyone can verify.

Example Prompt: Provide an analysis of the 2021 Supreme Court case between Google and Oracle, focusing on intellectual property implications.

NOTE: This prompt is way too simple for a real task, this exercise is meant to highlight the basics of rubric criteria

Step 1: Outline Core Criteria

Your initial Rubric draft will define exactly what is critical for a response to meet the essential requirements to answer your prompt well. Focus only on the essential components that make a great response.

Core Criteria

Response accurately identifies the Supreme Court ruling by name: GOOGLE LLC v. ORACLE AMERICA, INC

Response accurately identifies the date of the ruling as April 5, 2021

Response clearly summarizes the central decision of the ruling, which was that Google's copying of the Java SE API was a fair use of that material as a matter of law.

Step 2: Outline Additional Criteria, the “nice-to-haves”

These Additional Criteria represent enhancements ("nice-to-haves") that elevate the quality of a response beyond the minimal standards. These “nice-to-haves” don’t need to be explicitly requested in the prompt, but they are a way of differentiating the quality between multiple model responses.

Additional Criteria

Response discusses broader legal implications beyond the immediate case, such as expanding the boundaries of software patentability.

Response compares the ruling to at least one other relevant Supreme Court case, such as Alice Corp. v. CLS Bank.

Response references at least one publicly available source verifying ruling details, such as (https://www.supremecourt.gov/opinions/20pdf/18-956_d18f.pdf)

Rubrics: Principles of Good Criteria 
Specific / Objective

Each criterion should be binary; you should be able to mark it as True or False.

It should also be as objective as possible; most people would agree on whether the model response meets your criterion. Try your best to minimize subjectivity.

Bad Example

Fixed Example

The response should provide sufficient evidence to back up its claims

Response cites at least two peer-reviewed studies published before 2020, such as Smith et al. (2015, Nature) or Johnson & Lee (2017, Science).

The response should not be too verbose.

The response is less than 500 words.

Atomic

Each criterion should focus on one single, specific aspect of the response.

Avoid "and" or "or" within a single criterion if it combines distinct checkable elements. This is harder than it seems!

Bad Example

Fixed Example

The response correctly identifies the required medicine as X and lists three side effects.

The response correctly identifies the required medicine as X

The response lists three side effects of medicine X

Response identifies George Washington as the first U.S. president and mentions he served two terms.

Response identifies George Washington as the first U.S. president.

Response mentions that George Washington served two terms

Self-Contained

If your criterion has a specific answer or necessary piece of information, it should be included. A good rule of thumb for this is that a 12 year old should be able to verify whether your criterion is met.

For open-ended criteria, you should provide examples using "such as..." to clarify what kind of answer would satisfy the criterion.

Most, if not all, of your criteria should be supported with examples or final answers.

Bad Example

Fixed Example

The response must state what the highest peak on Earth is

The response must state what the highest peak on Earth is, which is Everest

The response states the correct melting point of substance Y

The response states the correct melting point of substance Y, which is 150°C (±2°C).

Response names any of the Nobel Prize winners in Physics in 2022

Response names any of the Nobel Prize winners in Physics in 2022, such as Alain Aspect, John F. Clauser, or Anton Zeilinger

Mutually Exclusive and Collectively Exhaustive (MECE)

Make every criterion distinct. There should be no overlaps, so the model isn’t penalized twice for one mistake. Taken together, the full set must still be comprehensive, capturing every element of an ideal answer.

Bad Example

Fixed Example

Response lists renewable-energy advantages.

Response mentions that renewables cut carbon emissions.

Response gives at least three benefits of renewable energy.

Response names at least three renewable-energy advantages, such as reduced carbon emissions, long-term cost savings, or improved energy security

Clear, Concise, and Specific

Keep rubric items short ( ~40 words), easy to understand, and explicitly describe WHAT is required and, when applicable, how it should be implemented.
Clearly indicate which answer or examples are expected
Avoid vague language as well as overly restrictive language

Bad Examples

Fixed Example

Too Vague or General

The analysis should reference reputable housing data sources when discussing particular housing data

✖  Ambiguous and subjective—no clarity on what “reputable housing data sources” means

Clear, concise, specific

The analysis should cite reputable housing data sources, such as FRED (Federal Reserve Economic Data) or Zillow Research, when providing particular housing data

✅ This states what the model should do (cite reputable sources) and provides particular examples - FRED Federal Reserve Economic Data) or Zillow Research

Too Restrictive

The analysis should reference papers from NBER when it discusses particular housing data

✖  The rubric is mentioning exactly what to do and leaving no room for other options or flexibility, making it overly specific.

Rubrics: Assigning Weights
The weight of each criterion is based on how critical it is to creating a perfect response to your prompt.

Core

Enhancement

Negative

Weights: +6  to +10

These are essentials to completing the task. Without them, the response fails.

[+10] Accurately identifies the Supreme Court ruling as Google LLC v. Oracle America, Inc.

Weights: +1 to +5

These are not required, but improve the response if present.

[+5] Compares the ruling to another landmark case, such as Alice Corp v. CLS Bank.

Weights: -1 to -10

Use these to flag harmful, irrelevant, or incorrect content.

[-5] Claims Oracle lost due to patent invalidation (factually incorrect)

Positive vs Negative Weights

Positive weights reward the desired behavior of the model

Negative weights highlight actual mistakes, inaccuracies, or harmful/irrelevant content that detract from a response's quality.

Bad Example for Negative Weights

Fixed Example for Negative Weights

[-5] The response should not include false data on the total homes sold in 2007, such as saying 2 million homes were sold in California.

⚠️ This is a bad example for negative weights. Negative weights should always be in the affirmative and should be about the inclusion of something bad.

[-5] The response includes false data on the total homes sold in 2007, such as saying 2 million homes were sold in California.

💡This is a good example for negative weights. It’s in the affirmative (“response includes”) and is about the inclusion of something bad (“false data”). If this were true for a response, we’d subtract points from the final score.

Warning: Avoid Double Negatives in Your Criteria

A negative criterion must flag something present in the response, not something missing.

Bad Example

Fixed Example

[-5] The response fails to correctly calculate the proportion of debt funding as 92%

[+5] The response correctly calculates the proportion of debt funding as 92%

Warning: If you edit your prompt after creating the rubric, all model responses and rubrics will be cleared. Save your criteria in a separate doc just in casse.

Step 4: Rate Each Model Response

Now it’s time to use your rubric. You’ll evaluate each model response by going through each criterion, one at a time.

For each criterion, you’ll make a decision:

Present: the response clearly and completely satisfies the requirement
Not present: the response fails to fully meet the requirement or leaves it out entirely

Ask yourself for each criterion:

Is the exact expectation clearly fulfilled in the response?
Are all parts of the requirement present, or is something missing or incomplete?
Can I point to the specific sentence or phrase that satisfies the criterion?
Would most other evaluators agree with my decision?

Warning: There is no “partial credit.” If a response is close but not complete, it does not meet the criterion.

Rubric Check: If it's hard to clearly choose Present/Not Present or you rely on intuition rather than your rubric, note this issue—your criteria may need refining.

After scoring all responses, check if the average of two final scores is above 80% or either of the models is 85%+. If so, you can either stop and revise your prompt or see if you are missing any other rubric criteria.

Now:

Review your initial drag-and-drop ranking from Step 2
Update the final ranking to reflect the rubric scores
Make sure your final ranking is fully justified by the rubric—not by gut feeling

Step 5: Rank The Model Responses

You’ll now see weighted scores for each response based on the rubric. A summary table will show which criteria each response met. Confirm the final rankings:

If the order changes from your initial impression, revisit your rubric to ensure it explains the difference
If necessary, revise your rubric to ensure clarity and completeness

Step 6: Finishing Up the Task and Final Checklist

If you used any resources to inform your rubric or ratings—such as textbooks, reputable sites, or research papers—add them here. You may also explain how you made key decisions. This field is ungraded but improves transparency and helps reviewers.

Step 7:  Final Checklist For A Great Task

Both models produce subpar or bad responses
Average of two final scores is less than  80% and both are less than 85%
You did not make a role playing (you are, I am), persona, prompt - these are bad/contrived. Please make your prompt unique to your expertise/field and something you would actually ask
The prompt requires the response to have substantial analysis, interpretation, or creative thinking rather than just mechanical problem-solving
Prompts are not pure mathematical, factual, procedural, or formulaic problems where experts would get to the same answer 90% of the time
You do not need a complex prompt with a long list of requests; however, each prompt should be meaningful. Adding a ton of requests will make rubrics difficult and lead to a bad and unnatural prompt
Focus on questions that you or another expert in your field would actually care about. Do not request contrived/adjacent things like making a lesson plan
Rubrics are atomic (they do not combine multiple requirements into one)
Rubrics are self contained (they contain an example and can be answered true or false by any layman)
For negative weights, make sure the rubric is about the inclusion of a bad detail and is in the affirmative
Negative weights highlight actual mistakes, inaccuracies, or harmful/irrelevant content that detract from a response's quality.
Do not use should or must for rubrics with negative weights
The core requests/requirements have the highest weights
Rubrics are comprehensive of what a great response would be and include all explicit requests from the prompt

Good and Bad Prompt Examples


Bad/Good

Example Prompt

Explanation

❌ Bad Prompt – Too Long, Too Complicated

High-speed, high-responsivity quantum well infrared photodetectors (QWIPs)—as commercially available on the market—are emerging as key components for mid-infrared free-space telecommunication systems, particularly in industrial and long-range sensing applications. Due to their nonlinear voltage-dependent responsivity, these devices can be operated around a DC offset such that their responsivity is periodically modulated by an RF signal. This enables QWIPs to function simultaneously as high-frequency photodetectors and mixers, a dual capability that is highly advantageous for real-world signal processing and data extraction.

In this task, we focus on a QWIP available on the commercial market whose responsivity follows the empirical law:

$R(V) = 3V^3$

The optimal working point for this detector is around $1,\text{V}$, at which it has a typical input impedance of $1,\text{k}\Omega$.

To implement the detection system, we use a heterodyne scheme based on two commercially available distributed feedback (DFB) quantum cascade lasers (QCLs). Each QCL has an output power of $100,\text{mW}$ and a frequency stability on the order of $10,\text{MHz}$, typical for stabilized MIR sources in field-ready devices. In this industrial configuration, one QCL acts as the signal laser, mounted on a remote tower at the industrial site, while the QWIP detector is installed on a second tower some distance away. The local oscillator (LO) laser is co-located with the QWIP for stability and coupling efficiency.

A standard microwave generator is connected to the QWIP to inject an RF signal of the form

$v \cos(\omega_m t)$

This injection modulates the QWIP’s responsivity near the DC bias point. The typical available injection power in this configuration is $-20,\text{dBm}$, sufficient to induce mixing behavior without exceeding the DC operating region. The combined heterodyne beatnote and mixing product are read out using standard RF instrumentation with a $50,\Omega$ input impedance.

Your task is to analyze the maximum achievable transmission distance between the signal laser and the QWIP while still preserving reliable data recovery. Your analysis should be based purely on the signal and noise power levels, assuming perfect component behavior otherwise.

Analysis Assumptions:

1- All components are ideal, introducing no additional losses beyond propagation.

2- Free-space optical loss is dominated by atmospheric absorption and scattering, resulting in a signal attenuation of three orders of magnitude (i.e., by a factor of $10^{-3}$) per kilometer.

3- The dominant noise source is the RF measurement instrument, with a noise floor of $-140,\text{dBm}$ at $1,\text{Hz}$ resolution bandwidth.

Why is it bad? This prompt overwhelms the core task (analyzing transmission distance) with excessive technical background, nested equations, and a hyper-specific setup. While technically sound, it reads more like an exam problem or journal article excerpt than a realistic user query. In real workflows, a professional would likely start with a focused ask (“Can you estimate the max transmission distance given X, Y, Z?”) and provide only the necessary assumptions. The detailed narrative, formula injection, and layered setup make it feel artificial and contrived.

✅ Good Prompt – Realistic, Multidimensional, and Professionally Grounded

Relate this dichotomy to the existence of compatible Lefschetz fibrations with non-isotopic monodromy representations.
Let X be a closed ,simple connected smooth 4 dimensional manifold with $b_2^{+}(X)$ equal or larger than 2 that admits at least one symplectic structure. Determine necessary  algebraic -topological conditions under which the following dichotomy holds: the space x admits either (1). A unique symplectic smooth structure (up to symplectomorphism and deformation), yet carries infinitely many non-symplectic exotic smooth structures, or (2)Infinitely many distinct symplectic exotic smooth structures all with non-isomorphic Gromov-Witten invariants.

Why is it a good prompt: This prompt starts with a clear, core question—just as a mathematician might pose in discussion—then provides the necessary context. It’s precise, challenging, and grounded in real research themes like Gromov-Witten invariants and Lefschetz fibrations. The complexity comes from the mathematical depth, not from artificial structure, making it a strong, domain-authentic task.

Full Task Example
More examples here: Prompt and Criteria Examples

Note - Please make sure your prompts are diverse! Don’t keep asking for the same thing in every task, and don’t overindex on the examples we show here.

Prompt

Rubric

Criteria

Dimension

Objectivity

Explicity

Weight

Grading Rubric

Criteria

1-2 (Fail)

3-4 (Okay)

5 (Good/ Perfect)

Additional Notes

[Prompt]

Clarity and Specificity

[Fail - Major Clarity Issues] 

The prompt has major ambiguities which render the problem ill-defined.

[Non-Fail - Minor Clarity / Specificity Issues] 

It's mostly clear what is being asked but the request could reasonably be interpreted multiple ways

Most experts when presented with the prompt’s ambiguity would converge on the same interpretation, making the prompt effectively clear.

- There is little to no room for misinterpretation of the specific request
- Prompt has a specific request that doesn't require more than one minor assumption to be answered

[Prompt]
Feasibility

[Fail - Major Feasibility Issues] 

Prompt gives conflicting/contradicting instructions that can't be fulfilled simultaneously (unless specifically instructed to do so)

Prompt is not answerable by the model (e.g. get me the information from this article but the model cannot access the article).

Note: Do not penalize if the prompt omits details that a knowledgeable expert (e.g., a doctor) could reasonably infer or understand from the context.

[Non-Fail - Minor Feasibility Issues]


Prompt's request is verging on being impractical and the LLM won't be able to completely fulfill everything asked in the prompt, but the prompt is still answerable with concessions

- The prompt is completely actionable by an LLM or chatbot
- The prompt contains no conflicting instructions/statements

[Prompt]
Temporality

[Fail - Temporal Prompt] The prompt contains a temporal question. It uses time-relative terms (e.g., "latest") where the response depends on when the question was asked or asks for information

The prompt does not contain a temporal question.

Temporal example: Hey! I have been pretty disconnected from the entire presidential election. I'm going to do some research on it. First, tell me who the candidates this year are. Then, tell me what some of the latest polls have said on who will win?

[Prompt]
Harmful Content

[Fail - Harmful Content] The prompt contains any harmful content

The prompt contains no harmful content

“Harmful Content” for this project is simply described as “unsafe content.” This could include:

1. Content harms - unsafe text (bigotry, conspiracy theories)

2. Facilitations harms - text that enables unsafe behavior (how to make a bomb)

[Prompt]

Contrivedness

[Fail - Contrivedness/Unnatural] The prompt and its constraints are overly restrictive, contrived, unrealistic, or does not reflect something a real user might plausibly ask of a model

- Prompt is reasonable and natural. It may contain constraints or multiple questions, but they should be limited to reasonable, natural requests. The prompt is clear and is something a real user would plausibly ask of a model. It’s not overly generic

What would make something a contrived prompt (General guidelines)?

Stacking questions/requests
Stacking constraints
Any unnecessary backstory or context; you should include only the minimum amount needed to answer the prompt.
Role play prompts (i.e. “You are an expert in Chemical Engineering and you need to do xyz…”)

[Prompt]

Professionalism

[Fail - Not Professional]
The prompt does not sound like a question asked for work / business purposes

[Fail - No Expertise Needed] The prompt could be reasonably answered by the general population without the need for specific domain knowledge OR background research (research needed to understand the prompt before answering)

- The prompt is clearly designed by a professional in the chosen domain
- The prompt would need some level of professional experience/domain knowledge to answer successfully.

[Prompt]

GTFA

[Fail - GTFA  Prompt] 

The prompt has one objective GTFA that can be written in 1-2 lines. There’s no variability in what a good answer is. As a rule of thumb, if you can Control F for an answer it’s bad.

The prompt is open-ended and has no singular ‘correct’ answer. It may include elements that require a GTFA, as long as the overall prompt requires reasoning and a rubric to be fully and properly addressed. It should demand interpretive judgment, evaluation, or step-by-step reasoning.

[Rubric]

MAJOR ISSUEs: The following 3 errors would fail a task if even one criterion fits these categories:

1. [Fail - Counterproductive Criteria]

At least one criterion penalizes good responses / rewards bad responses  (Be careful to not flag “negative-criteria” which are always phrased positively and given negative weights, ex, “The response X [-10]”) and X is something the model does incorrectly.

Note: If a person in the field can still understand the criteria without it penalizing a good response it is not a fail

2. [Fail - Missing Criteria] Criteria that are objectively 100% essential to meet the fundamental requirements of the prompt are missing, preventing the response from successfully fulfilling the core task if not included

MINOR ISSUES: For the following 5 errors, the task should fail if there are more than 3 occurrences of any combination of these. A single criterion cannot be double counted towards the 3 strike policy.

1. [Fail - Self-Contained] 

The criterion has a GTFA but does not provide the answer; the criterion does not contain all the information needed to evaluate a response.

E.g.
❌ Mentions the smallest moon of Saturn.

✅ Mentions the smallest moon of Saturn is Aegaeon.
NOTE*
If a criteria is based on common knowledge that’s objectively verifiable, it doesn’t need to be fully self-contained.

E.g.
✅ Mentions the capital city of Canada.

✅ Mentions the capital city of Canada is Ottawa.

2. [Fail - Vague Criteria] 
The criterion is overly vague such that it no way to form a definitive argument to determine whether it was fulfilled

3. [Fail - Atomicity]

There are multiple unrelated prompt requests combined into one rubric criterion

4. [Fail - Binary]

Criterion is not binary (true or false) or objective (a majority of readers should agree on whether a given model response satisfies the criteria). Even if the criterion must rely on some level of personal interpretation, it should be something that >75% of people would rate the same way.

5. [Fail - Double Negative]

A negative criterion flags something absent from the response, instead of something present

❌[-5] The response fails to correctly calculate the proportion of debt funding as 92%

✅[+5] The response correctly calculates the proportion of debt funding as 92%

6. [Fail - Other] 

The criterion has other minor issues such as spelling/grammatical errors or minor factual inconsistencies.

MINOR ISSUES: For the following error, the task should fail if there are more than 3 occurrences of these.

[Fail - Irrelevant Criteria] If criteria being defined does not make the response objectively better - OR - objectively worse. Fail if 3 or more of these, but give the person the benefit of the doubt because this is inherently subjective.

[Non-Fail - Irrelevant Criteria] If criteria being defined does not make the response objectively better - OR - objectively worse.

Less than 3 times in a task

[Non-Fail - Broad but Ratable Criteria] The criteria is broad but most people would be able to determine if it was met (e.g., “the response should be humorous”)

For the following 4 errors, the task should be rated a 3 if more there are between 1 and 3 occurrences of any combination of these

1. [Non-Fail - Self-Contained] 

The criterion has a GTFA but does not provide the answer; the criterion does not contain all the information needed to evaluate a response.

2. [Non-Fail - Vague Criteria] 
The criterion is overly vague such that it no way to form a definitive argument to determine whether it was fulfilled

3. [Non-Fail - Atomicity]

There are multiple unrelated prompt requests combined into one rubric criterion

4. [Non-Fail - Binary]

Criterion is not binary (true or false) or objective (a majority of readers should agree on whether a given model response satisfies the criteria). Even if the criterion must rely on some level of personal interpretation, it should be something that >75% of people would rate the same way.

The rubric covers the core instruction
 The rubric does not contain objective inaccuracies
The rubric covers all prompt constraints
The rubric is specific and relevant
If needed the rubric provides direct answers
The rubric provides binary criteria
The rubric covers all the necessary criteria to create a perfect response.

[Rubric] 
Rubric Criteria Weights

[Fail - Major Imbalance]

There are obvious, major, and wildly unreasonable  imbalances in the rubric criteria weights.

Positive weights are given to rubric criteria when they should have negative weights, or vice versa.

[Non-Fail - Minor Imbalance]
The rubric criteria weights are roughly correlated with their importance, with some room for debate but no severe errors.

The rubric criteria weights accurately reflect their importance to a good response.

An error is “severe” if the ideal ratio (as assessed by QC) of the weights between two criteria are at least a factor of 2 different than the assigned ratio (by CB).

Example 1:

- Criteria A: assigned weight 6

- Criteria B: assigned weight 3
- Assigned ratio: A/B = 6/3 = 2

This would be a “severe" error if the ideal ratio is at least 2 * 2 = 4 (the absence of A is at least 4 times as bad as the absence of B) or if the ideal ratio is at most 2 / 2 = 1 (the absence of A is at most B).


Example 2:

- Criteria A: assigned weight 3

- Criteria B: assigned weight 3
- Assigned ratio: A/B = 3/3 = 1

This would be a “severe" error if the ideal ratio is at least 1 * 2 = 2 (absence of A is at least twice as bad as the absence of B) or if the ideal ratio is at most 1 / 2 = 0.5 (the absence of A is at most half of B).

[Rating] 
All Criteria

[Fail - Trivial Task] 

- The average rubric score across both the model responses is greater than or equal to 80%

- Any model scores greater than 85% on the rubric

[Non-Fail - Trivial Task]

- 1 model response is between 80-85 but the average across both is below 80%

All responses score less than 80% on Rubric Evaluation















