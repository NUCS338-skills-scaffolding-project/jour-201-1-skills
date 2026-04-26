# demo.py — Example usage of the breaking-news-coach skill
import sys
sys.path.append("../skills/breaking-news-coach")
from logic import run

print("=== Breaking News Coach Demo ===")

# Demo 1: Plenty of time
result = run({"minutes_remaining": 20, "draft": "A fire broke out on campus today."})
print(f"\n[{result['minutes_remaining']} min remaining]")
print(f"Guidance tier: {result['guidance_tier']}")
print(f"5W1H Checklist: {result['checklist']}")

# Demo 2: Mid-range time pressure
result2 = run({"minutes_remaining": 8})
print(f"\n[{result2['minutes_remaining']} min remaining]")
print(f"Guidance tier: {result2['guidance_tier']}")

# Demo 3: Deadline crunch
result3 = run({"minutes_remaining": 3})
print(f"\n[{result3['minutes_remaining']} min remaining]")
print(f"Guidance tier: {result3['guidance_tier']}")
print(f"Unverified label required: {result3['unverified_label_required']}")
