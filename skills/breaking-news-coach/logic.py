# logic.py — Breaking News Coach skill entry point

TIME_TIERS = {
    "high": {
        "threshold_minutes": 15,
        "guidance": "Full 5W1H checklist + structure coaching + proper-noun check",
    },
    "mid": {
        "threshold_minutes": 5,
        "guidance": "Lead check + top two factual risks only",
    },
    "low": {
        "threshold_minutes": 0,
        "guidance": "Single most urgent fix only. One sentence. No digressions.",
    },
}

def run(input: dict) -> dict:
    """
    Main entry point for the Breaking News Coach skill.
    :param input: dict with keys:
        - minutes_remaining (int): time left on the deadline
        - draft (str, optional): student's current draft text
    :return: dict with time tier, guidance level, and checklist
    """
    minutes = input.get("minutes_remaining", 15)

    if minutes > 15:
        tier = TIME_TIERS["high"]
    elif minutes >= 5:
        tier = TIME_TIERS["mid"]
    else:
        tier = TIME_TIERS["low"]

    return {
        "minutes_remaining": minutes,
        "guidance_tier": tier["guidance"],
        "checklist": ["Who", "What", "When", "Where", "Why/How"],
        "unverified_label_required": True,
        "instructions": tier["guidance"],
    }
