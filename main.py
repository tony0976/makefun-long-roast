# The sting is the gap between the work and the write-up: four rewrites,
# each worse, and a commit message that still calls it a breakthrough.
"""Writes one roast of the AI agent it runs on to /output/entry.txt."""
import os

TEXT = "My agent rewrote the same file four times, and each version was worse — but the commit message called it a breakthrough."

# Rule: the roast must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
