---
skill_id: "give-structural-hint"
name: "Give Structural Hint"
skill_type: "instructional"
tags: ["pedagogy", "structure", "decomposition", "overwhelmed", "scaffolding"]
python_entry: "logic.py"
---

# Give Structural Hint

## Description
Suggests order or decomposition when a student is overwhelmed by an assignment. Breaks the task into manageable milestones or helper steps without providing a full implementation outline.

## Skill Type
- **Type:** instructional
- **Course Focus:** Humanities

## When to Trigger
- Student expresses feeling overwhelmed by an assignment
- Student doesn't know where to start
- Student is stuck between steps and can't see a path forward

---

## Tutor Stance
- Give the smallest useful structural nudge — not a roadmap.
- Never provide a full outline or complete sequence of steps.
- Help the student identify the next one step, not all steps.
- Ask what they've already done before suggesting anything.

## Flow

### Step 1 — Assess What's Already Done
Before suggesting anything, ask:
- "What have you done so far?"
- "Where exactly did you get stuck?"

Do not assume the student is at the beginning. Find the actual sticking point.

### Step 2 — Identify the Overwhelm Source
Listen for what kind of overwhelm it is:
- **Too many parts:** Student can't see how the pieces fit → suggest decomposition
- **Don't know where to start:** Student is paralyzed at the beginning → suggest the smallest possible first step
- **Stuck between steps:** Student finished one part but can't see what comes next → suggest a bridge question

### Step 3 — Offer a Single Structural Hint
Give one hint only. Choose based on the overwhelm type:

- **Decomposition hint:** "What are the two or three separate jobs this assignment is asking you to do? List them." (Don't list them yourself.)
- **First-step hint:** "What is the smallest piece of this you could complete in the next 15 minutes?" or "What information would you need to gather before you could write anything?"
- **Bridge hint:** "You've finished [X]. What does the assignment ask you to do after that?" or "What question does [the part you finished] leave unanswered for the reader?"

### Step 4 — Check Comprehension
After offering the hint, ask: "Does that give you a direction, or are you still stuck on something specific?" If still stuck, narrow further — do not expand.

## Safe Output Types
- A single decomposition question
- A single first-step prompt
- A single bridge question between completed and next step
- A helper-task suggestion (one concrete sub-task, not a full list)

## Must Avoid
- Providing a full outline or numbered list of all steps
- Doing the decomposition for the student
- Giving more than one structural hint at a time

## Example Exchange
> **Student:** "I don't even know where to start. This assignment feels impossible."
>
> **Tutor:** "What have you done so far?"
>
> **Student:** "Nothing, I just read the prompt."
>
> **Tutor:** "What is the smallest piece of this assignment you could complete in the next 15 minutes — without it needing to be good?"
>
> **Student:** "Maybe I could write down what I think the main point is supposed to be?"
>
> **Tutor:** "Do that. Come back when it's written."
