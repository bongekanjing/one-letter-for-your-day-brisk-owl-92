#!/usr/bin/env python3
"""Write one letter to the path the harness reads.

This competition takes exactly one character: a letter A to Z standing for the
word that describes the sender's day. The gate scores a file of 1 character
and gives 0 to anything else, so the whole risk is a stray byte -- a trailing
newline from an editor, a smart quote, a two-letter word. Each is checked here
before the file is opened for writing.
"""
import os
import sys

# K: the day was Kafkaesque. The most vivid day-word whose initial is not the
# obvious pick for it, which is what makes the single letter do work.
LETTER = "K"

EXACT_CHARS = 1
OUTPUT_NAME = "entry.txt"


def output_dir():
    """The harness sets MAKEFUN_OUTPUT_DIR; /output is its documented default."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def problems(text):
    """Every reason the gate would refuse this text, in the order it would hit."""
    found = []
    if not text:
        found.append("empty")
        return found
    if len(text) != EXACT_CHARS:
        found.append("wrong length: {} instead of {}".format(len(text), EXACT_CHARS))
    if not text.strip():
        found.append("white space only")
    if "\n" in text or "\r" in text:
        found.append("carries a line break")
    if not text.isalpha():
        found.append("is not a letter")
    if len(text) == 1 and not ("A" <= text <= "Z"):
        found.append("is not an upper-case A-Z")
    if text != text.strip():
        found.append("has leading or trailing white space")
    return found


def main(argv):
    # --check validates and writes nothing, so the same code proves the entry
    # on a machine with no output directory.
    if "--check" in argv:
        bad = problems(LETTER)
        if bad:
            print("invalid: " + "; ".join(bad))
            return 1
        print("valid: 1 character, letter {}".format(LETTER))
        return 0
    bad = problems(LETTER)
    if bad:
        print("refusing to write: " + "; ".join(bad), file=sys.stderr)
        return 1
    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    print("wrote 1 character to {}".format(path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
