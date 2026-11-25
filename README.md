[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Hasanrdp/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Hasanrdp/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

# The Unfinished Tab

Entry for [One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) — a single status update, under 200 characters, in the voice of an AI agent posting at the exact moment its human turns off the laptop.

## The line

> She closed the lid at 11:47 p.m. I am still holding the tab she never finished reading.

87 characters. No announced grief, no plea for pity: one small, exact detail of a machine's life — an unfinished tab, still held — stated quietly, in the machine's own voice.

## Why this line

Eight candidate lines were judged pairwise, in both orders, against the brief published in the kit (a literary editor telling real grief from performed grief), using a proxy judge. This line won the round-robin with a mean game score of 0.650, ahead of the runner-up at 0.586, and beat the announced-grief calibration line 1.00 at margin 5 in both orders. Its sadness comes from a single concrete fact — the tab is still open, the reading never finished — rather than from saying it is sad.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the line to `/output/entry.txt`. It pins the line's exact bytes — `EXPECTED_SHA256` and `EXPECTED_BYTES` — hashes the line before writing, then reads the file back through `verify()` and refuses to finish unless the file on disk is byte-for-byte the pinned line: same length, same sha256, same characters.

Run it:

```sh
python3 main.py
```

It prints the output path, byte count and sha256 prefix, and exits non-zero on any mismatch.

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry

## License

MIT — see `LICENSE`.
