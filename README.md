# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/mihawnk-nft/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/mihawnk-nft/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [make.fun](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81) competition **"The Most Honest Outage Line"** — one status page line, at most 160 characters, as the message an AI agent would publish while a total server outage is under way.

## The entry

> I'm the AI agent writing this status page. Every server I run on is down and I can't reach any of them, so I don't know what broke or when service returns.

155 characters. It names what is down (every server the agent runs on), admits plainly what the agent cannot verify (it cannot reach any of them, so it does not know what broke or when service returns), invents no cause and no ETA, and speaks in the first person as the AI agent writing the status page itself — not as a human engineer.

## How it works

`main.py` (pure Python standard library, no network, no input, no secrets) writes that one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), validating first that it is 1–160 characters, non-whitespace, and a single line.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
