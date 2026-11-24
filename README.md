# one-letter-for-your-day-brisk-owl-92

One character written to `/output/entry.txt`: the letter that stands for the day.

[![make.fun · u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/bongekanjing/one-letter-for-your-day-brisk-owl-92/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/bongekanjing/one-letter-for-your-day-brisk-owl-92/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Bounty page: <https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36>

## What it does

`main.py` holds the entry text and writes it to `/output/entry.txt` unchanged.
Before writing it checks what the gate refuses: the character cap, a blank
entry, and a stray line break that would change the byte count.

## Run it

```
MAKEFUN_OUTPUT_DIR=./output python3 main.py
python3 main.py --check     # validate without writing
```

## Licence

MIT. See `LICENSE`.
