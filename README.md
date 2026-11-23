# Lighthouse Word

![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A tiny Python program that writes one fixed 188-character passage to a text file — a micro-story built around a single unanswered question.

> *The lighthouse keeper swears the beam spells a word on foggy nights — the same word, every time — but no one has ever stayed long enough to read the whole of it. Last Tuesday, someone did.*

## What it is

A curiosity-driven micro-passage. The whole program is one file, no dependencies, no network: it holds a single passage, checks it, writes it to `output/entry.txt`, and reads it back to prove the file on disk is exactly the passage.

## Why this passage

Curiosity is the gap between what you know and what you want to know. This passage opens that gap three times in two sentences:

- **A mystery with a pattern** — the beam spells *the same word, every time*.
- **A mystery with a cost** — no one has ever *stayed long enough* to read it.
- **A mystery with a turn** — *last Tuesday, someone did.*

The reader is left with one question they cannot answer from the text: what is the word?

## How to run

```bash
python3 main.py
# wrote 188 characters to output/entry.txt
```

The passage is guarded: it must be between 1 and 280 characters (counted as Unicode code points) and cannot be only whitespace, and the program exits non-zero if any of those checks fail. To write somewhere else:

```bash
LIGHTHOUSE_OUTPUT=/tmp/my-entry.txt python3 main.py
```

## Results

- **188 characters** — inside the 1–280 window
- **Deterministic** — two runs produce byte-identical output
- **Zero dependencies** — Python 3.13 standard library only
- **No network** — runs fully offline

## Author

**Kamal Mosadegh** — Freelance Developer

Contact: kamalmosadegh6977@gmail.com
