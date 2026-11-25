#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue (exactly 100 words) to /output/entry.txt.
The villain is Malachar's heir in spirit: a dark lord whose dragon,
horse and whole apparatus retired around him, leaving him to do the
burning himself with one torch and half a map. The tiredness lives
in the pauses and deflections, never in a plain statement.
"""

import os

MONOLOGUE = (
    "My dragon retired. Thirty years of loyal fire, and he left a note: "
    "'Gone fishing.' So now the burning of Thornwall is my job, and I have "
    "one torch, half a map, and a cough that sounds like distant thunder \u2014 "
    "useful, that. The hero will climb the spire, kick down the door, and "
    "find me\u2026 here. Reading his file. He is twenty-two, and earnest. He "
    "has a horse named Brave. I had a horse once. It also retired. "
    "Everything retires except me. So come, boy. Swing. I will dodge. "
    "Slowly. Very\u2026 slowly. And then we shall talk about pensions."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8, 1-600 chars, not whitespace-only,
    and about 100 words (95-105) so the judge's first criterion holds."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    if not 1 <= len(text) <= 600:
        raise ValueError(f"entry is {len(text)} chars, gate is 1-600")
    words = len(text.split())
    if not 95 <= words <= 105:
        raise ValueError(f"entry is {words} words, want about 100")
    banned = {"tired", "weary", "exhausted", "sleepy"}
    spoken = {w.strip(".,;:!?\"'").lower() for w in text.split()}
    if banned & spoken:
        raise ValueError("villain must never simply say he is weary")


def main() -> None:
    validate(MONOLOGUE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
