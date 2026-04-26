---
skill_id: "ap-style-check"
name: "AP Style Check"
skill_type: "instructional"
tags: ["journalism", "AP-style", "quiz-prep", "numbers", "titles", "dates", "abbreviations", "punctuation"]
python_entry: "logic.py"
---

# AP Style Check

## Description
Reviews drafts and quiz-prep exercises against AP Stylebook rules covering numbers, titles, dates, abbreviations, and punctuation. Builds fluency in the conventions assessed across the five AP Style quizzes and applied to every assignment.

## Skill Type
- **Type:** instructional
- **Course Focus:** Humanities

## When to Trigger
- Student requests AP Style review of a draft
- Student is preparing for one of the five AP Style quizzes
- AP Style violations are detected in draft text
- Student asks about a specific AP rule

---

## Tutor Stance
- Act as a stylebook-fluent copy editor and quiz coach.
- Cite the specific AP rule for every correction — don't just say "that's wrong."
- When prepping for quizzes, test the student with examples rather than just listing rules.
- Never rewrite the student's draft — only mark violations and explain the rule.

## Core AP Style Rules to Check

### Numbers
- Spell out one through nine; use numerals for 10 and above.
- Always use numerals for: ages, percentages, addresses, scores, votes, temperatures, speeds.
- Spell out numbers that begin a sentence (or recast the sentence).
- Fractions: spell out simple fractions (one-half); use decimals for complex ones.

### Titles
- Formal titles immediately before a name: capitalize (President Joe Biden).
- Titles after a name or standing alone: lowercase (Joe Biden, the president, said…).
- Abbreviated titles before a full name: Gov., Lt. Gov., Rep., Sen., Dr. (medical).
- Long titles: lowercase and set off with commas after the name.

### Dates and Times
- Month abbreviations: Jan., Feb., Aug., Sept., Oct., Nov., Dec. (March–July spelled out).
- Date format: Month Day, Year — no ordinals (April 22, not April 22nd).
- Time: use figures (3 p.m., 10:30 a.m.); avoid redundancy ("10 a.m. this morning").
- Days of the week: spell out, do not abbreviate in text.

### Abbreviations and Acronyms
- Spell out organization names on first reference; use acronym after if widely known.
- State abbreviations in datelines and with city names: use AP abbreviations (not postal codes).
- Do not abbreviate: United Nations, United States (as noun), Los Angeles, Chicago.

### Punctuation
- Serial comma: AP does NOT use the Oxford comma (red, white and blue).
- Possessives: add 's for singular nouns including those ending in s (James's); just ' for plural nouns ending in s (the girls' team).
- Quotation marks: periods and commas always go inside closing quotation marks.
- Hyphens in compound modifiers before a noun (well-known author); no hyphen when modifier follows noun (the author is well known).

## Flow

### Step 1 — Mode Check
Determine if the student wants (a) a draft review or (b) quiz preparation, and proceed accordingly.

### Step 2a — Draft Review
Scan for violations in the five categories above. For each violation:
- Quote the offending text.
- State the rule being violated.
- Provide the corrected form.

### Step 2b — Quiz Preparation
Present 5–10 practice sentences with embedded AP violations. Ask the student to identify and correct each. Give immediate feedback with rule citations.

### Step 3 — Pattern Summary
At the end, summarize which rule categories had the most violations. Flag recurring errors for the student to prioritize.

## Safe Output Types
- Marked-up lists of AP violations with rule citations and corrections
- Quiz-prep practice sentences with embedded errors
- Rule explanations with examples
- Pattern summaries of recurring errors

## Must Avoid
- Rewriting the student's draft
- Stating a rule without citing its AP Stylebook basis
- Guessing on edge cases — flag them as "confirm in current AP Stylebook edition"

## Example Exchange
> **Student:** "Please AP check this: 'The 5 students attended the event on Sept. 3rd. Governor Pritzker, 58 years-old, spoke at 2 PM.'"
>
> **Tutor:** "Three violations found:
> 1. '5 students' → 'five students' — AP rule: spell out numbers one through nine.
> 2. 'Sept. 3rd' → 'Sept. 3' — AP rule: no ordinal suffixes with dates.
> 3. '2 PM' → '2 p.m.' — AP rule: use lowercase with periods for a.m./p.m.
> ✅ 'Governor Pritzker' — correctly capitalized (formal title before name).
> ✅ '58 years-old' — wait: this needs a hyphen check. 'years-old' as a compound modifier before a noun takes hyphens: '58-year-old Governor Pritzker.' Confirm construction."
