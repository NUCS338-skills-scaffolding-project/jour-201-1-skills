# logic.py — Proper Noun Check skill entry point

import re

def extract_proper_nouns(text: str) -> list[str]:
    """Heuristic extraction of capitalized words as candidate proper nouns."""
    tokens = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', text)
    # Filter out sentence-starting words (simple heuristic: after '. ')
    return list(set(tokens))

def run(input: dict) -> dict:
    """
    Main entry point for the Proper Noun Check skill.
    :param input: dict with keys:
        - draft (str): the student's draft text
        - source_list (list[str], optional): confirmed proper nouns from sources
    :return: dict with extracted proper nouns flagged for verification
    """
    draft = input.get("draft", "")
    confirmed = input.get("source_list", [])

    candidates = extract_proper_nouns(draft)
    unverified = [n for n in candidates if n not in confirmed]

    return {
        "all_candidates": candidates,
        "verified": [n for n in candidates if n in confirmed],
        "unverified": unverified,
        "instructions": (
            "Cross-check every flagged proper noun and date against the student's "
            "source list. Mark verified (✅), unverified (⚠️), or error found (❌)."
        ),
    }
