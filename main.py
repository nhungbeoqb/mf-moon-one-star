"""One-star review of the Moon. Writes the review to /output/entry.txt."""

import os

REVIEW = "One star. Four billion years orbiting me and it still won't take the hint."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: the review must be 1-120 characters, not only whitespace,
    # and is written exactly, with no trailing newline.
    if not (1 <= len(REVIEW) <= 120):
        raise ValueError(f"review is {len(REVIEW)} chars, must be 1-120")
    if not REVIEW.strip():
        raise ValueError("review must not be only whitespace")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
