# logic.py — Depth of Interviewing skill entry point

QUESTION_TYPES = {
    "closed": "Can be answered with yes/no — needs to open up.",
    "leading": "Suggests the answer — needs to neutralize.",
    "too_broad": "Too general — needs a specific moment or experience.",
    "open_ended": "Strong — requires the source to tell a story.",
}

def classify_question(question: str) -> str:
    """Heuristic classification of interview question type."""
    q = question.strip().lower()
    if q.startswith(("do ", "did ", "is ", "are ", "was ", "were ", "have ", "has ")):
        return "closed"
    if "don't you think" in q or "isn't it" in q or "wouldn't you say" in q:
        return "leading"
    if len(q.split()) < 6:
        return "too_broad"
    return "open_ended"

def run(input: dict) -> dict:
    """
    :param input: dict with keys:
        - questions (list[str]): student's planned interview questions
    :return: dict with question classifications and improvement prompts
    """
    questions = input.get("questions", [])

    results = []
    for q in questions:
        qtype = classify_question(q)
        results.append({
            "question": q,
            "type": qtype,
            "feedback": QUESTION_TYPES[qtype],
            "needs_revision": qtype != "open_ended",
        })

    return {
        "total": len(questions),
        "needs_revision": sum(1 for r in results if r["needs_revision"]),
        "analysis": results,
    }
