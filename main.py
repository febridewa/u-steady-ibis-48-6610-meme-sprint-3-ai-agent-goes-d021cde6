#!/usr/bin/env python3
"""Rogue Agent Cleanup — Meme Sprint 3: AI Agent Goes Rogue.

Copies the bundled meme image (entry.png, drawn procedurally by
build_meme.py for this competition) to the grader's output directory
as /output/entry.png.

Pure standard library, no network access, fully deterministic: every
run writes the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(HERE, "entry.png")
TARGET = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
# A plain byte copy: the output is identical to the bundled image, run after run.
shutil.copyfile(SOURCE, TARGET)

# Sanity-check the copy: a whole PNG starts with the PNG magic bytes.
with open(TARGET, "rb") as fh:
    assert fh.read(8) == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
print("wrote", TARGET, os.path.getsize(TARGET), "bytes")
