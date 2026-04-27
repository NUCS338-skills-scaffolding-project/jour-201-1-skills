# logic.py — News Judgement skill entry point

NEWS_VALUES = ["timeliness", "proximity", "impact", "conflict", "novelty"]

W5H1 = ["Who", "What", "When", "Where", "Why", "How"]

def run(input: dict) -> dict:
    """
    :param input: dict with keys:
        - pitch (str): student's story idea
    :return: dict with newsworthiness checklist and 5W1H prompts
    """
    pitch = input.get("pitch", "")

    return {
        "pitch": pitch,
        "newsworthiness_checklist": {v: f"Does this story have {v}? Why?" for v in NEWS_VALUES},
        "5W1H_prompts": {w: f"{w}: Can the student answer this for their story?" for w in W5H1},
        "angle_prompt": "Restate your story in one sentence: [subject] [did what] [for whom/where] [and why it matters].",
    }
