# demo.py — Example usage of the lead-and-structure skill
import sys
sys.path.append("../skills/lead-and-structure")
from logic import run

print("=== Lead and Structure Demo ===")

# Demo 1: Weak, over-limit lead
weak_draft = (
    "Northwestern University has been dealing with a lot of issues lately "
    "when it comes to their budget situation, and on Thursday administrators "
    "made a big announcement about what they plan to do going forward.\n\n"
    "The university announced it will cut 200 staff positions by June."
)
result = run({"draft": weak_draft})
print(f"\nLead: '{result['lead'][:80]}...'")
print(f"Word count: {result['lead_word_count']} words (limit: 35)")
print(f"Over limit: {result['lead_over_limit']}")
print(f"\n5W1H Checklist: {result['checklist']['5W1H']}")
print(f"Nut graph rule: {result['checklist']['nut_graph']}")
print(f"Structure rule: {result['checklist']['inverted_pyramid']}")
print(f"Attribution rule: {result['checklist']['attribution']}")
print(f"\nInstructions: {result['instructions']}")

# Demo 2: Strong lead
strong_draft = (
    "Northwestern University will cut 200 staff positions by June, "
    "Provost Kathleen Hagerty announced Thursday, citing a $50 million budget shortfall."
)
result2 = run({"draft": strong_draft})
print(f"\n--- Demo 2: Strong Lead ---")
print(f"Lead: '{result2['lead']}'")
print(f"Word count: {result2['lead_word_count']} words | Over limit: {result2['lead_over_limit']}")
