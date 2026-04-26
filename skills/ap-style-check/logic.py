# logic.py — AP Style Check skill entry point

AP_RULES = {
    "numbers": "Spell out one through nine; use numerals for 10 and above.",
    "titles": "Capitalize formal titles immediately before a name; lowercase after.",
    "dates": "Abbreviate Jan. Feb. Aug. Sept. Oct. Nov. Dec.; no ordinals (April 3, not April 3rd).",
    "time": "Use figures with a.m./p.m. lowercase (3 p.m., 10:30 a.m.).",
    "serial_comma": "AP does NOT use the Oxford/serial comma.",
    "abbreviations": "Spell out organization names on first reference; acronym after.",
    "possessives": "Singular nouns including those ending in s take 's (James's). Plural nouns ending in s take just '.",
    "quotation_marks": "Periods and commas always go inside closing quotation marks.",
    "hyphens": "Hyphenate compound modifiers before a noun; no hyphen when modifier follows noun.",
}

def run(input: dict) -> dict:
    """
    Main entry point for the AP Style Check skill.
    :param input: dict with keys:
        - draft (str): text to review
        - mode (str): 'review' for draft check or 'quiz' for practice exercises
    :return: dict with mode, applicable rules, and instructions
    """
    draft = input.get("draft", "")
    mode = input.get("mode", "review")

    return {
        "mode": mode,
        "draft_length": len(draft.split()),
        "ap_rules": AP_RULES,
        "instructions": (
            "For 'review': scan draft for violations in all rule categories, cite the rule, "
            "and provide the corrected form. For 'quiz': generate 5-10 practice sentences "
            "with embedded errors for the student to identify and correct."
        ),
    }
