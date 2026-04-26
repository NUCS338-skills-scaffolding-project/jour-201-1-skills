# logic.py — Source Finder skill entry point

PROHIBITED_SOURCES = [
    "Medill students",
    "Northwestern University faculty (without documented instructor approval)",
    "CAPS (Counseling and Psychological Services)",
    "NUHS (Northwestern University Health Services)",
    "Evanston Chamber of Commerce",
]

AI_DISCLOSURE = (
    "AI-assisted source suggestions generated with Claude. "
    "Student is responsible for verifying all contact information "
    "and confirming source eligibility before outreach."
)

def run(input: dict) -> dict:
    """
    Main entry point for the Source Finder skill.
    :param input: dict with keys:
        - topic (str): the story topic
        - source_list (list[str], optional): sources already found
    :return: dict with suggested source types, institutions, and disclosure
    """
    topic = input.get("topic", "")
    return {
        "topic": topic,
        "prohibited_sources": PROHIBITED_SOURCES,
        "ai_disclosure": AI_DISCLOSURE,
        "instructions": (
            "Suggest 4-6 expert types with Chicago/Illinois institutions for the given topic. "
            "Filter out all prohibited sources. Format output as Appendix B source list. "
            "Always append the AI disclosure statement."
        ),
    }
