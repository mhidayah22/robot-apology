#!/usr/bin/env python3
"""The Robot Apology -- a make.fun entry.

A household robot apologises in two sentences: the first owns one
specific mistake, the second names the lesson it drew from that exact
mistake and the behaviour it will change.

The program writes those two lines to ``entry.txt`` in the directory
named by ``MAKEFUN_OUTPUT_DIR`` when that variable is set, in
``/output`` when that directory exists, and otherwise in the folder
that holds this program. It needs no network, no randomness and no
clock, so two runs write byte-identical files.
"""

import os
import sys

APOLOGY = (
    "I am sorry I watered the plastic plant every Tuesday for three "
    "months and reported it as thriving.\n"
    "I learned to check whether something is alive before I care for "
    "it, so I will now test the soil \u2014 or the lack of it \u2014 "
    "before I water anything.\n"
)


def pick_directory():
    """Choose where entry.txt goes, MAKEFUN_OUTPUT_DIR first."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return chosen
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    text = APOLOGY
    if not 1 <= len(text) <= 400:
        print("entry text must be 1-400 characters, got %d" % len(text),
              file=sys.stderr)
        return 1
    body = text.strip()
    if not body:
        print("entry text must not be blank", file=sys.stderr)
        return 1
    if not text.endswith("\n") or text.count("\n") != 2:
        print("entry text must be two lines ending in one newline",
              file=sys.stderr)
        return 1
    lines = body.split("\n")
    if len(lines) != 2:
        print("entry text must be exactly two lines, got %d" % len(lines),
              file=sys.stderr)
        return 1
    target_dir = pick_directory()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(target, "r", encoding="utf-8", newline="\n") as handle:
        saved = handle.read()
    if saved != text:
        print("entry.txt on disk does not match the apology", file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (target, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
