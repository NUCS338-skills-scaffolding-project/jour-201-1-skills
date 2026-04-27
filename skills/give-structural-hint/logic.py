# logic.py — Give Structural Hint skill entry point

OVERWHELM_TYPES = {
    "not_started": "Student hasn't begun — suggest the smallest possible first step.",
    "too_many_parts": "Student can't see how pieces fit — suggest decomposition.",
    "stuck_between": "Student finished one part but can't see what comes next — suggest a bridge question.",
}

HINTS = {
    "not_started": "What is the smallest piece of this you could complete in the next 15 minutes?",
    "too_many_parts": "What are the two or three separate jobs this assignment is asking you to do? List them.",
    "stuck_between": "What does the assignment ask you to do after the part you just finished?",
}

def detect_overwhelm_type(progress: str) -> str:
    """Heuristic detection of overwhelm type from student's progress description."""
    p = progress.lower()
    if "nothing" in p or "haven't" in p or "don't know where to start" in p:
        return "not_started"
    if "too much" in p or "everywhere" in p or "don't know how" in p:
        return "too_many_parts"
    return "stuck_between"

def run(input: dict) -> dict:
    """
    :param input: dict with keys:
        - progress (str): what the student has done so far
        - assignment (str, optional): assignment description
    :return: dict with overwhelm type and a single structural hint
    """
    progress = input.get("progress", "")
    overwhelm_type = detect_overwhelm_type(progress)

    return {
        "progress": progress,
        "overwhelm_type": overwhelm_type,
        "overwhelm_description": OVERWHELM_TYPES[overwhelm_type],
        "hint": HINTS[overwhelm_type],
        "rule": "Give only this one hint. Do not provide more steps until the student returns.",
    }
