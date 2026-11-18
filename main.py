# 24News: one-image summary of 18 November 2026 world news.
# Deterministic by design — the program only copies the bundled image.
"""24News entry for make.fun news-image-20261118.

Copies the bundled front-page image (assets/entry.png) to /output/entry.png.
Deterministic: no network, no randomness, no timestamps — the output bytes
are an exact copy of the bundled image every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
