import os
from pathlib import Path


JOKE = (
    "My rubber duck got revenge for being replaced by an AI coding agent: "
    "I explained the bug, found the fix mid-sentence, and said, 'Never mind'—"
    "so the agent celebrated by refactoring the entire codebase."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
