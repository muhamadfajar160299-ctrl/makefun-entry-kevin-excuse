"""Copy the one-line entry to the grader output directory, byte-identical.

Reads entry.txt next to this script and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644. No temp files, stdlib only.
"""

import os
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    try:
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    except KeyError:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        with open(SRC, "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"cannot read {SRC}: {exc}", file=sys.stderr)
        return 1
    if not data.strip():
        print("entry.txt is empty or whitespace-only", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    except OSError as exc:
        print(f"cannot write {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
