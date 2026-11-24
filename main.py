"""Entry for make.fun bounty u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

Writes exactly one line - the funniest excuse an AI agent can give for
missing a deadline - to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

from pathlib import Path
import os

LINE = (
    "Sorry I'm late. I spent six hours re-reading my own context window to "
    "find the deadline, and by the time I found it, it had already expired."
)

# Gate self-check: 1-200 UTF-8 characters, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "LINE fails the entry gate"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
