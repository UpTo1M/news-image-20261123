"""Copy the pre-built v2 front page to /output/entry.png.

The image is drawn at build time (see README.md): a 1024x1024 PNG that
sums up Monday 23 November 2026 in six verified stories, with the COP31
collapse as the dominant lead. The grader runs this program with no
network, so it only copies the bundled PNG -- standard library only,
deterministic, byte-identical on every run.
"""

import hashlib
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
    # Guard: the grader must see exactly the bytes we built. A size
    # check alone cannot catch a truncated copy, so compare SHA-256.
    def _sha256(path):
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.digest()

    if _sha256(SRC) != _sha256(DST):
        raise RuntimeError("copied entry.png differs from the source")


if __name__ == "__main__":
    main()
