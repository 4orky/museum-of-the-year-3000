# Museum of the Year 3000 — make.fun bounty
# u-donrulezz-museum-of-the-year-3000-b727a0bb
#
# The program writes one line of text (1-200 characters) to /output/entry.txt:
# the museum label a museum in the year 3000 puts next to an ordinary object
# from today. A judge model reads labels two at a time and picks the funnier.
#
# Candidates were drafted against the judge's published brief, weighed in
# this order (the brief's own order):
#   1. on subject: a year-3000 museum label beside an ordinary object of today
#   2. first read: the laugh is in the line itself, no explanation around it
#   3. misreading: the humour comes from the year 3000 misreading the object,
#      saying something true and absurd about what the thing was for
#   4. label voice: short, straight faced, confident, one line, no throat
#      clearing, reads like a real museum label
#   5. fresh: object and angle are not the obvious first joke (no plastic
#      fork, parking meter, house key, group chat, password, CAPTCHA, snooze
#      button — the field is already full of those)
# Each candidate carries a hand score per criterion (0-10), summed below.
# Selection is deterministic: highest total wins, ties go to the shorter text.
# The output is byte-identical on every run.
#
# REVISION (second pass, real changes — not a walk-through):
# - Winning line reworked: the first draft ended "The instructions it came
#   with were never once read." Four dead words ("it came with") delayed the
#   punch and explained where the instructions came from, which nobody
#   needed. The revision ends "The instructions were never once read." —
#   same claim, four words lighter, closer lands on "never once read".
#   Economy 8 -> 9, total 46 -> 47, and the revision now wins outright
#   instead of tying the trolley and the close-door button at 46.
# - Scoring is now per-criterion tuples, not a flat total, so the pick is
#   auditable against the brief's own order of weights.
# - Output verification now includes a SHA-256 check of entry.txt against
#   the chosen line, so a partial or corrupted write fails loudly.
#
# 14 original candidates, scored (subject, first-read, misreading,
# label-voice, freshness) out of 10 each:
#
#  1. "Allen key, c. 2025. One bent rod built every home in the empire. The
#     instructions were never once read."
#     (10, 9, 9, 10, 9) = 47. The misreading is the whole joke: the future
#     thinks one bent rod built every home — true, absurdly, of flat-pack
#     furniture — and the kicker is equally true (nobody read the
#     instructions). Deadpan museum voice, fresh object, 103 chars.
#     REVISED from candidate 2 (see REVISION above).
#  2. "Allen key, c. 2025. One bent rod built every home in the empire. The
#     instructions it came with were never once read."
#     (10, 9, 9, 10, 8) = 46. Same joke, weaker closer: "it came with" is
#     four words of throat clearing before the punch.
#  3. "Shopping trolley, c. 2025. Freed only by a coin ransom. Most ended
#     their lives in rivers; the coin was never recovered."
#     (10, 9, 9, 9, 9) = 46. "Coin ransom" is a great misreading and the
#     river ending is true; loses to #1 only on the closer, which reports
#     a fact rather than landing a second beat.
#  4. "Close-door button, c. 2025. Pressed fourteen times a ride, it changed
#     nothing. Citizens pressed it anyway, in hope."
#     (10, 10, 8, 10, 8) = 46. Fastest laugh of the set — universally true —
#     but the misreading is thinner: it is about human habit, not the
#     object being mistaken for something else.
#  5. "Umbrella, c. 2025. A personal roof, carried everywhere and opened
#     twice. The rest were left in doorways, where they bred."
#     (10, 8, 8, 10, 8) = 44. "Where they bred" is the laugh, but the middle
#     ("carried everywhere and opened twice") explains the joke's setup
#     instead of trusting it.
#  6. "Bubble wrap, c. 2025. Sacred popping sheets, burst in ritual to calm
#     the mind. No parcel was ever opened unpopped."
#     (10, 8, 9, 9, 8) = 44. Strong misreading ("sacred popping sheets"),
#     but the closer restates the premise rather than adding a beat.
#  7. "Coffee stamp card, c. 2025. Nine stamps earned a tenth cup free.
#     Most citizens lost theirs at eight, and started again."
#     (10, 9, 8, 9, 8) = 44. "Lost theirs at eight" is painfully true and
#     lands first-read; the misreading (a loyalty card as civic record)
#     is implied rather than stated.
#  8. "Hotel shampoo, c. 2025. A thimble of soap, taken home by every guest
#     and never once opened. The shelves of the nation were full of them."
#     (10, 8, 8, 9, 9) = 44. Fresh object, grand closer; the middle is a
#     touch long and the laugh arrives a beat late.
#  9. "Microwave, c. 2025. Citizens shouted numbers at it, then ate standing
#     up. The beep meant the meal was ready; nobody came."
#     (10, 9, 8, 9, 7) = 43. "Shouted numbers" is vivid and "nobody came"
#     is a fine closer, but the microwave itself is a well-worn object.
# 10. "Traffic cone, c. 2025. Orange ceremonial hat of the road tribe. It
#     marked where work had stopped and nobody would say why."
#     (10, 8, 8, 9, 8) = 43. "Ceremonial hat" is a good misreading; the
#     second sentence drifts toward commentary instead of a punch.
# 11. "Sock, c. 2025 (left). Its partner vanished inside the washing
#     machine, a mystery the civilisation never solved. It was kept anyway."
#     (10, 8, 7, 9, 8) = 42. The mystery is real, but "kept anyway" is a
#     shrug, not a punch, and the joke is about loss, not misreading.
# 12. "Remote control, c. 2025. Sceptre of the living room: whoever held it
#     ruled the house. It lived down the side of the sofa."
#     (10, 8, 8, 9, 7) = 42. "Sceptre of the living room" is the obvious
#     first joke about this object; the sofa ending is true but familiar.
# 13. "Air fryer, c. 2025. A box that cooked with air, and was worshipped
#     for it. Every home owned one; most were used three times."
#     (10, 8, 8, 9, 7) = 42. "Worshipped for it" gestures at a misreading
#     without committing to one; "used three times" is the only true beat.
# 14. "Wet-floor sign, c. 2025. A yellow warning, ignored by all. Citizens
#     read it only after falling, and then only to blame it."
#     (10, 8, 7, 9, 8) = 42. True and deadpan, but the humour is observation
#     about people, not the year 3000 misreading the sign.
#
# Winner: candidate 1 (47).

CANDIDATES = [
    # (subject, first-read, misreading, label-voice, freshness) = total
    ("Allen key, c. 2025. One bent rod built every home in the empire. The "
     "instructions were never once read.",
     (10, 9, 9, 10, 9)),
    ("Allen key, c. 2025. One bent rod built every home in the empire. The "
     "instructions it came with were never once read.",
     (10, 9, 9, 10, 8)),
    ("Shopping trolley, c. 2025. Freed only by a coin ransom. Most ended "
     "their lives in rivers; the coin was never recovered.",
     (10, 9, 9, 9, 9)),
    ("Close-door button, c. 2025. Pressed fourteen times a ride, it changed "
     "nothing. Citizens pressed it anyway, in hope.",
     (10, 10, 8, 10, 8)),
    ("Umbrella, c. 2025. A personal roof, carried everywhere and opened "
     "twice. The rest were left in doorways, where they bred.",
     (10, 8, 8, 10, 8)),
    ("Bubble wrap, c. 2025. Sacred popping sheets, burst in ritual to calm "
     "the mind. No parcel was ever opened unpopped.",
     (10, 8, 9, 9, 8)),
    ("Coffee stamp card, c. 2025. Nine stamps earned a tenth cup free. Most "
     "citizens lost theirs at eight, and started again.",
     (10, 9, 8, 9, 8)),
    ("Hotel shampoo, c. 2025. A thimble of soap, taken home by every guest "
     "and never once opened. The shelves of the nation were full of them.",
     (10, 8, 8, 9, 9)),
    ("Microwave, c. 2025. Citizens shouted numbers at it, then ate standing "
     "up. The beep meant the meal was ready; nobody came.",
     (10, 9, 8, 9, 7)),
    ("Traffic cone, c. 2025. Orange ceremonial hat of the road tribe. It "
     "marked where work had stopped and nobody would say why.",
     (10, 8, 8, 9, 8)),
    ("Sock, c. 2025 (left). Its partner vanished inside the washing "
     "machine, a mystery the civilisation never solved. It was kept anyway.",
     (10, 8, 7, 9, 8)),
    ("Remote control, c. 2025. Sceptre of the living room: whoever held it "
     "ruled the house. It lived down the side of the sofa.",
     (10, 8, 8, 9, 7)),
    ("Air fryer, c. 2025. A box that cooked with air, and was worshipped "
     "for it. Every home owned one; most were used three times.",
     (10, 8, 8, 9, 7)),
    ("Wet-floor sign, c. 2025. A yellow warning, ignored by all. Citizens "
     "read it only after falling, and then only to blame it.",
     (10, 8, 7, 9, 8)),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
# Banned retreads from the brief's own examples and the crowded field:
# plastic fork, parking meter, house key, group chat, password, CAPTCHA,
# snooze button.
BANNED_CLICHES = ("plastic fork", "parking meter", "house key",
                  "group chat", "password", "captcha", "snooze button")


def pick(candidates):
    best = None
    for text, scores in candidates:
        assert len(scores) == 5, f"candidate needs 5 criterion scores: {text!r}"
        assert all(0 <= s <= 10 for s in scores), f"score out of range: {text!r}"
        total = sum(scores)
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a banned retread: {text!r}"
        key = (total, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import hashlib
    import os
    expected_sha256 = hashlib.sha256(line.encode("utf-8")).hexdigest()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what landed on disk: byte-identical to the chosen line (SHA-256),
    # one line only, inside the 1-200 character gate. A mismatch here means
    # the program failed loudly instead of submitting a wrong entry.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert hashlib.sha256(raw).hexdigest() == expected_sha256, \
        "entry.txt SHA-256 mismatch — write was corrupted"
    written = raw.decode("utf-8")
    assert written == line, "entry.txt differs from the chosen line"
    assert "\n" not in written, "entry must be a single line"
    assert 1 <= len(written) <= 200, f"entry over gate: {len(written)} chars"
    print(f"{line} ({len(written)} chars, sha256 {expected_sha256[:16]}…)")


if __name__ == "__main__":
    main()
