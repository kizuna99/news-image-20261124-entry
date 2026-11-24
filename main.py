"""Entry point: write the day's broadsheet to the output entry.png.

Renders deterministically from data.py + render.py; if the drawing stack
is unavailable it falls back to the committed entry.png, byte for byte.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.png")
    try:
        sys.path.insert(0, HERE)
        import render
        render.render(out)
    except Exception:
        shutil.copyfile(os.path.join(HERE, "entry.png"), out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
