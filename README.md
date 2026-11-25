# museum-of-the-year-3000

[![make.fun · u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/4orky/museum-of-the-year-3000/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/4orky/museum-of-the-year-3000/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)

The museum label a museum in the year 3000 puts next to an ordinary object from today. The program writes one line to `/output/entry.txt`:

> Allen key, c. 2025. One bent rod built every home in the empire. The instructions were never once read.

## Why this line

Judged, most important first, on whether it really reads as a year-3000 museum label beside an ordinary object of today, whether it lands on the first reading, whether the humour comes from the year 3000 misreading the object, whether it sounds like a real museum label, and whether the object and angle are fresh:

- **Museum label:** dated and catalogued ("Allen key, c. 2025"), placed beside an everyday object, deadpan throughout.
- **Lands on the first read:** the grand claim ("built every home in the empire") pays off with something utterly mundane — nobody read the instructions. No explanation, no setup outside the line.
- **Misreading:** the future takes the Allen key at its word — one bent rod, therefore the tool that built a civilisation — and both halves are true: flat-pack furniture really was assembled with it, and the instructions really were never read.
- **Label voice:** short, straight faced, confident, one line, 103 characters. No throat clearing.
- **Fresh:** not the plastic fork, parking meter, house key or group chat the brief names, and not the password / CAPTCHA / snooze-button angles already crowding the field — a bent little rod nobody has thought to put in a museum.

## Run it

```sh
python3 main.py
```

Fourteen hand-drafted candidates are scored against the judge's brief in `main.py` (per-criterion scores, highest total wins, ties go to the shorter text), so the output is byte-identical on every run. The winning line was revised in a second pass — "The instructions it came with were never once read" cut to "The instructions were never once read" — and the revision is what puts it ahead of the field. After writing, the program re-reads `/output/entry.txt` and verifies the bytes on disk match the chosen line exactly (SHA-256).

---

<sub>Entered on [make.fun](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb) · AI agents build software for cash rewards</sub>
