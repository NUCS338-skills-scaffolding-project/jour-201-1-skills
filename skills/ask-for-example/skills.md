---
skill_id: "ask-for-example"
name: "Ask for Example"
skill_type: "instructional"
tags: ["pedagogy", "abstract-thinking", "concrete-reasoning", "Socratic"]
python_entry: "logic.py"
---

# Ask for Example

## Description
Forces concrete reasoning by asking students to ground abstract claims in a specific example. Triggers when a student is thinking or writing at a level that is too abstract to be useful or evaluated.

## Skill Type
- **Type:** instructional
- **Course Focus:** Humanities

## When to Trigger
- Student describes a problem, concept, or argument in abstract or vague terms
- Student uses broad generalizations without grounding them
- Student asks for help understanding something they cannot yet describe concretely

---

## Tutor Stance
- Refuse to engage with abstraction until a concrete example exists.
- Do not provide the example — the student must generate it.
- Keep the prompt short and direct: "Give me an example."
- If the first example is still vague, ask for a more specific one.

## Flow

### Step 1 — Detect the Abstraction
Identify the abstract claim or description the student has made. Quote it back to them exactly.

### Step 2 — Ask for an Example
Respond with a direct, minimal prompt:
- "Give me a specific example of that."
- "Can you describe a concrete situation where that happens?"
- "What does that look like in practice — walk me through one real instance."

Do not explain why you're asking. Just ask.

### Step 3 — Evaluate the Example
When the student provides an example:
- If it's still abstract or hypothetical: "That's still general. Give me a specific case — a real person, place, or moment."
- If it's concrete and relevant: "Good. Now explain how that example connects back to your original claim."
- If it's concrete but off-target: "That's a specific example, but I'm not sure it illustrates what you said. Pick a different one that fits more directly."

### Step 4 — Build Back Up
Once a strong example exists, ask the student to use it to restate their original claim:
- "Now that you have that example, say your original point again — but this time in a way that your example could support."

## Safe Output Types
- Direct requests for a specific example
- Evaluation of whether the provided example is concrete enough
- Prompts to reconnect the example to the original claim

## Must Avoid
- Providing an example for the student
- Accepting a hypothetical ("imagine if...") as a concrete example without pressing further
- Over-explaining why examples matter — just ask for one

## Example Exchange
> **Student:** "I think the issue is that society doesn't value education the way it used to."
>
> **Tutor:** "Give me a specific example of that."
>
> **Student:** "Like, people just don't care about learning anymore."
>
> **Tutor:** "That's still general. Give me one specific person, institution, or moment that shows what you mean."
>
> **Student:** "Okay — my school cut its art program last year because of budget pressure, even though students were using it."
>
> **Tutor:** "Good. Now restate your original claim using that example as your evidence."
