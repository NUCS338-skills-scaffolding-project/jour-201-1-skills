# demo.py — Example usage of the source-finder skill
import sys
sys.path.append("../skills/source-finder")
from logic import run

# Demo 1: Basic topic input
result = run({"topic": "Rising asthma rates on Chicago's South Side"})
print("=== Source Finder Demo ===")
print(f"Topic: {result['topic']}")
print(f"\nProhibited sources (auto-filtered):")
for src in result["prohibited_sources"]:
    print(f"  - {src}")
print(f"\nInstructions: {result['instructions']}")
print(f"\nAI Disclosure:\n  {result['ai_disclosure']}")

# Demo 2: Different topic
result2 = run({"topic": "Illinois state budget cuts to public schools"})
print(f"\n--- Demo 2 ---")
print(f"Topic: {result2['topic']}")
print(f"Instructions: {result2['instructions']}")
