#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Explain the smartphone to someone from the year 1800 in a single sentence
of at most 200 characters. Every image in the sentence belongs to the
traveler's own world:

- library       -- where all written knowledge is kept;
- post office   -- where a message can be sent to anyone, anywhere;
- market square -- where the whole town gathers to trade and talk;
- speaking mirror -- the only honest name an 1800 eye could give a small
  glowing glass in the pocket that answers when spoken to.

Fold the three institutions into that one mirror, then measure its speed
in units the traveler can feel: an answer arrives before tea cools.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

SENTENCE = (
    "Imagine every library, post office and market square on Earth folded "
    "into one speaking mirror in your pocket, where any soul may ask any "
    "question and be answered before tea cools."
)


def write_sentence(path=OUTPUT_PATH, sentence=SENTENCE):
    """Write the sentence to *path* exactly, with no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(sentence)


def main():
    write_sentence()


if __name__ == "__main__":
    main()
