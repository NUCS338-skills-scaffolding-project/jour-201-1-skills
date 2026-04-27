# logic.py — Ask for Example skill entry point

ABSTRACT_SIGNALS = [
    "society", "people", "everyone", "always", "never", "in general",
    "nowadays", "today", "the world", "humans", "we as a society",
]

def is_abstract(text: str) -> bool:
    """Check if text contains signals of abstract thinking."""
    return any(signal in text.lower() for signal in ABSTRACT_SIGNALS)

def run(input: dict) -> dict:
    """
    :param input: dict with keys:
        - student_claim (str): the abstract claim or statement the student made
    :return: dict with abstraction detection and example prompts
    """
    claim = input.get("student_claim", "")
    abstract = is_abstract(claim)

    return {
        "claim": claim,
        "is_abstract": abstract,
        "prompt": "Give me a specific example of that." if abstract else "Good — now connect that example back to your claim.",
        "follow_up": "That's still general. Give me a specific case — a real person, place, or moment.",
    }
