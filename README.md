# THE WORLD TODAY — Tuesday, 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/mmr9759/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/mmr9759/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A make.fun entry for **news-image-20261117**: sum up 17 November's world
news in one image. See the live bounty on [make.fun](https://make.fun/bounty/news-image-20261117).

The entry is a one-page newspaper front page, drawn programmatically so
every letter stays crisp: **35 stories from six continents** — the Kerch
Bridge strike, Iran's drones at a US radar in Bahrain, the Kyiv bridge
strikes, the APEC summit in Shenzhen, the Rwanda return hub, the tanker
hit near the Strait of Hormuz, the Pentagon's ninth failed audit, and 28
more in brief — plus a world map marking where the news happened. All
stories were verified against reports published on Tuesday 17 November
2026 (Reuters, AP, BBC, Al Jazeera, AFP).

## How it works

`main.py` (Python 3.13, no dependencies, no network) copies the bundled
`entry.png` to the grader's output directory (`$MAKEFUN_OUTPUT_DIR`, or
`/output` by default) as `entry.png`. Same input bytes, same output bytes,
every run.

## Files

- `main.py` — the entry program
- `entry.png` — the front page, 1024×1024 PNG
- `LICENSE` — MIT

## Verify locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png  # must match
```

## License

MIT — see `LICENSE`.
