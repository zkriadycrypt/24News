# 24News: one-image summary of 18 November 2026 world news.
# Deterministic by design — writes the bundled image bytes, every run.
"""24News entry for make.fun news-image-20261118.

Writes the bundled front-page image to /output/entry.png. The image is
stored in the repo as base64 text (assets/entry.png.b64); if a binary
assets/entry.png is also present it is copied directly instead.
Deterministic: no network, no randomness, no timestamps — the output bytes
are the same every run.
"""

import base64
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
SRC_B64 = os.path.join(HERE, "assets", "entry.png.b64")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    if os.path.exists(SRC):
        # Bundled image present: exact copy.
        shutil.copyfile(SRC, OUT)
    else:
        # Bundled image stored as base64 text (binary files cannot be
        # pushed through the text-only snapshot tool): decode it.
        with open(SRC_B64, "r", encoding="ascii") as f:
            data = base64.b64decode(f.read())
        with open(OUT, "wb") as f:
            f.write(data)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
