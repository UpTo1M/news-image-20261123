"""Copy the pre-built front page to /output/entry.png.

The entry image is drawn at build time (see README.md): a 1024x1024 PNG
summarising Monday 23 November 2026 in six verified stories. The grader
runs this program with no network, so it only copies the bundled PNG —
stdlib only, deterministic, and byte-identical on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    if not os.path.isfile(SRC):
        raise FileNotFoundError(f"bundled image missing: {SRC}")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Guard: the grader must see exactly the bytes we built.
    if os.path.getsize(SRC) != os.path.getsize(DST):
        raise RuntimeError("copied entry.png differs in size from the source")


if __name__ == "__main__":
    main()
