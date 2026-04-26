# logic.py — Lead and Structure skill entry point

MAX_LEAD_WORDS = 35

def count_words(text: str) -> int:
    return len(text.split())

def extract_lead(draft: str) -> str:
    """Returns the first paragraph of the draft as the lead."""
    paragraphs = [p.strip() for p in draft.strip().split('\n') if p.strip()]
    return paragraphs[0] if paragraphs else ""

def run(input: dict) -> dict:
    """
    Main entry point for the Lead and Structure skill.
    :param input: dict with keys:
        - draft (str): full story draft
    :return: dict with lead analysis, word count, and structure checklist
    """
    draft = input.get("draft", "")
    lead = extract_lead(draft)
    lead_word_count = count_words(lead)

    return {
        "lead": lead,
        "lead_word_count": lead_word_count,
        "lead_over_limit": lead_word_count > MAX_LEAD_WORDS,
        "checklist": {
            "5W1H": ["Who", "What", "When", "Where", "Why/How"],
            "nut_graph": "Must appear by paragraph 3-4",
            "inverted_pyramid": "Most newsworthy facts first",
            "attribution": "Every non-obvious claim requires a named source",
        },
        "instructions": (
            "Evaluate lead against 5W1H and 35-word limit. Check nut graph placement. "
            "Review inverted pyramid hierarchy. Flag all attribution gaps. "
            "Never rewrite the student's story — coach and prompt only."
        ),
    }
