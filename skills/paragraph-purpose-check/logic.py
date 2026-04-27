# logic.py — Paragraph Purpose Check skill entry point

def run(input: dict) -> dict:
    """
    :param input: dict with keys:
        - thesis (str): student's central argument
        - paragraphs (list[str]): list of draft paragraphs
    :return: dict with purpose-check questions per paragraph
    """
    thesis = input.get("thesis", "")
    paragraphs = input.get("paragraphs", [])

    questions = []
    for i, para in enumerate(paragraphs):
        questions.append({
            "paragraph": i + 1,
            "preview": para[:80] + "..." if len(para) > 80 else para,
            "prompts": [
                "What is this paragraph's job in your argument?",
                "How does this paragraph move the reader toward your conclusion?",
                "If I removed this paragraph, what would the reader lose?",
            ]
        })

    return {
        "thesis": thesis,
        "paragraph_count": len(paragraphs),
        "purpose_checks": questions,
        "closing_prompt": "Which paragraph needs the most work, and what would you change first?",
    }
