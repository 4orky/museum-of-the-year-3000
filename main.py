# A year-3000 museum label, picked from a hand-scored shortlist: Museum of the Year 3000 on make.fun.
# Bounty slug: u-donrulezz-museum-of-the-year-3000-b727a0bb. One program, one line out.
# The entry written to /output/entry.txt is a deadpan catalogue label for a
# present-day object, judged in pairs by a model curator on five points, in
# this order: on-subject, lands at first read, misreads the object, sounds
# like a real label, and brings a fresh object and angle.
# Fourteen labels were drafted by hand and marked 0-10 on each point. The
# strongest total wins; a tie breaks toward the shorter label. The run is
# deterministic: the same shortlist always yields the same label, byte for byte.
# Second pass, 2026-11-26: the draft closer carried four spare words, "it came
# with", which held the punch back a beat. Cutting them let the last sentence
# land on "never once read" and broke the tie at the top of the table.
# What the gate enforces: every label stays inside 1-200 characters, holds
# one line, carries no trailing space, and steers clear of the brief's own
# examples plus the crowded angles (fork, meter, key, chat, password, CAPTCHA,
# snooze). The written file is re-read and hash-checked before the run reports.
# The table tops out at 47, on the Allen key; the draft of the same label sits
# one point behind it, and the trolley and the close-door button tie at 46.
from __future__ import annotations
from hashlib import sha256
import re
from pathlib import Path
CRITERIA = ("on_subject", "first_read", "misreading", "label_voice", "freshness")
FORBIDDEN = ("plastic fork", "parking meter", "house key", "group chat", "password", "captcha", "snooze button")
FORBIDDEN_RE = re.compile(r"\b(?:" + "|".join(re.escape(fragment) for fragment in FORBIDDEN) + r")\b", re.IGNORECASE)
GATE_LOW = 1
GATE_HIGH = 200
OUT_PATH = Path("/output/entry.txt")
# Each entry pairs its label with one mark per criterion, in CRITERIA order.
ENTRIES = [
    {"label": "Allen key, c. 2025. One bent rod built every home in the empire. The instructions were never once read.", "marks": (10, 9, 9, 10, 9)},
    {"label": "Allen key, c. 2025. One bent rod built every home in the empire. The instructions it came with were never once read.", "marks": (10, 9, 9, 10, 8)},
    {"label": "Shopping trolley, c. 2025. Freed only by a coin ransom. Most ended their lives in rivers; the coin was never recovered.", "marks": (10, 9, 9, 9, 9)},
    {"label": "Close-door button, c. 2025. Pressed fourteen times a ride, it changed nothing. Citizens pressed it anyway, in hope.", "marks": (10, 10, 8, 10, 8)},
    {"label": "Umbrella, c. 2025. A personal roof, carried everywhere and opened twice. The rest were left in doorways, where they bred.", "marks": (10, 8, 8, 10, 8)},
    {"label": "Bubble wrap, c. 2025. Sacred popping sheets, burst in ritual to calm the mind. No parcel was ever opened unpopped.", "marks": (10, 8, 9, 9, 8)},
    {"label": "Coffee stamp card, c. 2025. Nine stamps earned a tenth cup free. Most citizens lost theirs at eight, and started again.", "marks": (10, 9, 8, 9, 8)},
    {"label": "Hotel shampoo, c. 2025. A thimble of soap, taken home by every guest and never once opened. The shelves of the nation were full of them.", "marks": (10, 8, 8, 9, 9)},
    {"label": "Microwave, c. 2025. Citizens shouted numbers at it, then ate standing up. The beep meant the meal was ready; nobody came.", "marks": (10, 9, 8, 9, 7)},
    {"label": "Traffic cone, c. 2025. Orange ceremonial hat of the road tribe. It marked where work had stopped and nobody would say why.", "marks": (10, 8, 8, 9, 8)},
    {"label": "Sock, c. 2025 (left). Its partner vanished inside the washing machine, a mystery the civilisation never solved. It was kept anyway.", "marks": (10, 8, 7, 9, 8)},
    {"label": "Remote control, c. 2025. Sceptre of the living room: whoever held it ruled the house. It lived down the side of the sofa.", "marks": (10, 8, 8, 9, 7)},
    {"label": "Air fryer, c. 2025. A box that cooked with air, and was worshipped for it. Every home owned one; most were used three times.", "marks": (10, 8, 8, 9, 7)},
    {"label": "Wet-floor sign, c. 2025. A yellow warning, ignored by all. Citizens read it only after falling, and then only to blame it.", "marks": (10, 8, 7, 9, 8)},
]  # end of the shortlist
def total_marks(entry):
    marks = entry["marks"]
    if len(marks) != len(CRITERIA):
        raise ValueError("each entry needs one mark per criterion, got " + str(len(marks)))
    for mark in marks:
        if not isinstance(mark, int) or mark < 0 or mark > 10:
            raise ValueError("marks run 0-10, got " + repr(mark))
    return sum(marks)
def allowed(text):
    if not (GATE_LOW <= len(text) <= GATE_HIGH):
        return False
    if text != text.strip() or "\n" in text or "\r" in text:
        return False
    return FORBIDDEN_RE.search(text) is None
def choose(entries):
    best_label = None
    best_key = None
    for entry in entries:
        label = entry["label"]
        if not allowed(label):
            raise ValueError("entry fails the gate: " + label)
        key = (total_marks(entry), -len(label))
        if best_key is None or key > best_key:
            best_key = key
            best_label = label
    if best_label is None:
        raise ValueError("shortlist is empty, nothing to choose")
    return best_label
def emit(label):
    payload = label.encode("utf-8")
    digest = sha256(payload).hexdigest()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_bytes(payload)
    landed = OUT_PATH.read_bytes()
    if sha256(landed).hexdigest() != digest:
        raise ValueError("entry.txt failed its hash check after writing")
    if landed.decode("utf-8") != label:
        raise ValueError("entry.txt differs from the chosen label")
    return digest
def run():
    label = choose(ENTRIES)
    if choose(ENTRIES) != label:
        raise ValueError("pick is not deterministic, refusing to write")
    digest = emit(label)
    print(label + " (" + str(len(label)) + " chars, sha256 " + digest[:16] + "…)")
# The kit runs this file as a script, so the run starts here with no guard.
run()
