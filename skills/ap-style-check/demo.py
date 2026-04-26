# demo.py — Example usage of the ap-style-check skill
import sys
sys.path.append("../skills/ap-style-check")
from logic import run

print("=== AP Style Check Demo ===")

# Demo 1: Draft review mode
draft = (
    "The 5 students attended the event on Sept. 3rd. "
    "Governor Pritzker, 58 years-old, spoke at 2 PM."
)
result = run({"draft": draft, "mode": "review"})
print(f"\nMode: {result['mode']}")
print(f"Draft word count: {result['draft_length']} words")
print(f"\nAP Rules loaded ({len(result['ap_rules'])} categories):")
for category, rule in result["ap_rules"].items():
    print(f"  [{category}] {rule}")
print(f"\nInstructions: {result['instructions']}")

# Demo 2: Quiz prep mode
result2 = run({"mode": "quiz"})
print(f"\n--- Demo 2: Quiz Prep Mode ---")
print(f"Mode: {result2['mode']}")
print(f"Instructions: {result2['instructions']}")
