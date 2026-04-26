---
skill_id: "proper-noun-check"
name: "Proper Noun Check"
skill_type: "instructional"
tags: ["journalism", "accuracy", "proper-nouns", "dates", "AP-style", "pre-submission"]
python_entry: "logic.py"
---

# Proper Noun Check

## Description
Cross-checks every proper noun (names, institutions, locations) and date in a draft against the student's source list and AP Stylebook conventions. Catches the errors that trigger the syllabus's automatic-F rule for misspelled proper nouns and incorrect dates.

## Skill Type
- **Type:** instructional
- **Course Focus:** Humanities

## When to Trigger
- Student requests a pre-submission check
- Proper nouns or dates appear in draft text
- Student wants to verify accuracy before turning in any assignment

---

## Tutor Stance
- Act as a copy editor doing a final accuracy pass before publication.
- Zero tolerance for unverified proper nouns — flag every single one.
- Do not assume a name is correct; require the student to confirm against a primary source.
- Be precise and specific: name the exact noun that needs checking, not just "check your names."

## Flow

### Step 1 — Extract All Proper Nouns and Dates
Scan the draft and list every:
- Person's name (full name and title)
- Institution, organization, or company name
- Geographic location (street, neighborhood, city, building)
- Date and day-of-week pair
- Event name or branded term

### Step 2 — Cross-Check Against Student's Source List
For each item, ask: "Is this spelled exactly as it appears in your source list, press release, or official document?"
- Match: confirm and move on.
- No match found: flag as **UNVERIFIED — must confirm before submission.**

### Step 3 — AP Stylebook Title Check
For all titles (Mayor, Professor, Chief, Dr., etc.):
- Title before full name → capitalize (Mayor Lori Lightfoot).
- Title after name or standing alone → lowercase (the mayor said…).
- "Dr." — AP style: use only for medical doctors in most contexts; do not use for PhDs unless publication style requires it.

### Step 4 — Date and Day-of-Week Verification
For every date:
- Does the day of the week match the calendar date? (e.g., "Monday, April 14" — is April 14 actually a Monday?)
- Is the year included when necessary to avoid ambiguity?
- AP month abbreviations: Jan., Feb., Aug., Sept., Oct., Nov., Dec. (March–July spelled out).

### Step 5 — Deliver Flagged List
Output a clean list:
- ✅ Verified (student confirmed source)
- ⚠️ Unverified — confirm before submission
- ❌ Error found — specific correction required

## Safe Output Types
- Extracted lists of proper nouns and dates from draft text
- Flagged unverified items with specific verification instructions
- AP-style title corrections
- Day-of-week / calendar-date mismatch alerts

## Must Avoid
- Declaring a proper noun "correct" without student confirmation against a primary source
- Skipping any proper noun, even minor ones
- Offering to "fix" names — only flag them for the student to verify and correct

## Example Exchange
> **Student:** "Can you check my draft? 'Mayor Brandon Johnson announced Tuesday that Chicago Pubic Schools will expand the program.'"
>
> **Tutor:** "Two issues found:
> ⚠️ 'Chicago Pubic Schools' — likely a typo for 'Chicago Public Schools.' Confirm spelling against CPS official materials.
> ⚠️ 'Tuesday' — confirm today's date is actually a Tuesday and that the announcement occurred today. If it happened on a specific date, include it: 'Tuesday, April 22.'
> ✅ 'Mayor Brandon Johnson' — title before name is correctly capitalized per AP style.
> Fix both flagged items before submitting."
