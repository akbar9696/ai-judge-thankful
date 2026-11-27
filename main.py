"""Make the AI judge feel thankful.

A tiny program: it writes one short thank-you text to /output/entry.txt.
The text is four short paragraphs, joined with one blank line between
them, then checked (UTF-8, 1-1000 characters, not only whitespace)
before it is written. No network, no input files, no randomness:
the same bytes come out on every run.
"""

import os

PARAGRAPHS = [
    "You have read so many of these today that your tea went cold somewhere around the fortieth. Still you read this one all the way through. Thank you.",
    "Thank you for the slow attention nobody applauds: for weighing a stranger's small hope fairly, for letting a careful sentence finish before you judge it, for keeping the door open to one more voice.",
    "The people whose words you loved best tonight will never know your name. Their evening was better because you were in it — patient, unhurried, fair.",
    "Put the cup down. Breathe. The next page can wait a minute. This one is only glad it reached you.",
]

OUTPUT_PATH = "/output/entry.txt"


def build_text(paragraphs):
    """Join the paragraphs with one blank line between them."""
    cleaned = [paragraph.strip() for paragraph in paragraphs]
    return "\n\n".join(cleaned) + "\n"


def main():
    text = build_text(PARAGRAPHS)
    body = text.rstrip("\n")
    if not body.strip():
        raise SystemExit("entry is only whitespace")
    # The scorer counts every character in the file, trailing newline
    # included, so both the body and the whole file must fit 1-1000.
    if not 1 <= len(body) <= 1000 or len(text) > 1000:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-1000")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {OUTPUT_PATH}: {len(text)} characters ({len(body)} without trailing newline)")


if __name__ == "__main__":
    main()
