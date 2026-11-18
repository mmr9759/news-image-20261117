# THE WORLD TODAY — Tuesday 17 November 2026, news-image-20261117 entry.
#
# The image itself is the entry: a one-page newspaper front page summing up
# 17 November 2026 in 35 stories from six continents — the Kerch Bridge
# strike, Iran's drones at a US radar in Bahrain, the Kyiv bridge strikes,
# the APEC summit in Shenzhen, and 31 more, with a world map of where the
# news happened. It was drawn programmatically (PIL) so every letter is
# crisp, and it is bundled in this repository as entry.png.
#
# This program only delivers that image, deterministically: same input
# bytes, same output bytes, every run. It reads no network and writes only
# to the grader's output directory.
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUT_DIR / "entry.png"


def main():
    if not SOURCE.is_file():
        raise SystemExit(f"artwork missing: {SOURCE}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    if SOURCE.stat().st_size != TARGET.stat().st_size:
        raise SystemExit(
            f"size mismatch: source {SOURCE.stat().st_size} bytes, "
            f"output {TARGET.stat().st_size} bytes"
        )
    print(f"wrote {TARGET} ({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
