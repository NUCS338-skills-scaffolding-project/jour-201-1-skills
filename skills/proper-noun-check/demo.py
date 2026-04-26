# demo.py — Example usage of the proper-noun-check skill
import sys
sys.path.append("../skills/proper-noun-check")
from logic import run

print("=== Proper Noun Check Demo ===")

# Demo 1: Draft with some confirmed and unconfirmed proper nouns
draft = (
    "Mayor Brandon Johnson announced Tuesday that Chicago Public Schools "
    "will expand its after-school program. Fire Chief Maria Alvarez confirmed "
    "two people were taken to Evanston Hospital."
)
source_list = ["Brandon Johnson", "Chicago Public Schools", "Maria Alvarez"]

result = run({"draft": draft, "source_list": source_list})
print(f"\nDraft excerpt: '{draft[:80]}...'")
print(f"\nAll candidates found: {result['all_candidates']}")
print(f"✅ Verified: {result['verified']}")
print(f"⚠️  Unverified (must confirm before submission): {result['unverified']}")
print(f"\nInstructions: {result['instructions']}")

# Demo 2: Draft with no source list provided
result2 = run({"draft": "Governor Pritzker signed the bill at Springfield."})
print(f"\n--- Demo 2 (no source list) ---")
print(f"Unverified: {result2['unverified']}")
