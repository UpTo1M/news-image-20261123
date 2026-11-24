"""Copy the pre-built entry image to the output directory.

The image (entry.png, 1024x1024) is drawn at build time; this program
only copies it to /output/entry.png, deterministically, using the
Python standard library. No network, no writes to the bot directory.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("missing source image: " + SOURCE)
    expected_size = os.path.getsize(SOURCE)
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    if os.path.getsize(DEST) != expected_size:
        raise SystemExit("copy failed: size mismatch after copy")
    if sha256(SOURCE) != sha256(DEST):
        raise SystemExit("copy failed: hash mismatch after copy")
    print("wrote", DEST, "(%d bytes)" % expected_size)


if __name__ == "__main__":
    main()
