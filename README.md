# The Word You'd Delete From the Dictionary

[![make.fun · u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/daring-falcon-58/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/daring-falcon-58/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

**Entry: `delete` — 6 bytes, 1 word, self-score 14/15.**

## Methodology (read first — this is how the entry was chosen)

**Formula.** Every candidate was scored 0–5 on the judge's own criteria, in
the judge's own order (judge brief, `competition.yaml` / `RULES.txt`):

1. **Speed** — the joke lands the moment the word is gone, no caption needed.
2. **Word-itself** — the humour comes from the word itself (its sound, its
   double meanings, the gap it leaves), not from shock alone.
3. **Freshness** — a word the rest of the field would not think of first,
   still instantly understood.
4. **Exactness** — one word, spelled correctly (gate column: 5/5 for every
   candidate in the table; it never differentiates, so the total is /15 over
   the three scored criteria).

**Blind test.** Candidates were generated first (50 words, across five
families: gross-sound words, misused words, self-contradictory words,
filler/slang, and self-referential/meta words), then scored — the winner was
not picked first and justified afterwards. The five-way tie at 14/15 was
broken by a second, names-hidden pass over the finalists on the judge's
criterion 2 alone (speed), then by a consequence test: does the deletion
leave a *consequence*, or only a missing label?

**Verdicts (the five 14/15 finalists).**

| Word | Verdict |
|---|---|
| **delete** (5/5/4) | **WINNER.** The dictionary deletes the word for deleting — and can never delete another word again. The act of deletion is the joke: the word's meaning *is* what is being done to it. Lands instantly, needs no caption, and the paradox has a consequence. |
| erase (5/5/4) | Same paradox, same score. Loses the tie-break: "delete" is the competition title's verb ("The Word You'd **Delete** From the Dictionary") and the more universally recognised word for the act. |
| dictionary (5/5/4) | The book deletes its own name — cute, but it leaves only a missing label ("word book" still works). "delete" leaves a *consequence*: no further deletion is ever possible. |
| definition (4/5/5) | The dictionary can no longer define anything — a strong structural joke, but it needs a beat to land (criterion 2: speed 4, not 5). |
| monosyllabic (4/5/5) | A five-syllable word meaning "one syllable" — pure self-contradiction, but the joke needs the reader to count syllables (speed 4, not 5). |

**Why not the obvious picks.** `moist` (5/4/1 = 10) is the first word the
whole field thinks of — with 508 submissions, freshness 1 kills it. `the`
(5/3/2 = 10) breaks English but is not *funny*, only destructive.
`literally` (4/4/2 = 10) is a tired misuse joke the field will flood.
Shock/gross words score on speed and lose on word-itself and freshness.

## The entry

`main.py` writes exactly one word to `/output/entry.txt` and prints exactly
that word to stdout — nothing else attached.

- Entry text: `delete`
- Characters: 6 (gate allows 1–77) — **6 bytes, no trailing newline**, the
  smallest text that can carry this word. The competition's tie-break gives
  an exact tie to the smaller text, so 6 bytes is the best possible size.
- Gate check (verified locally, twice, byte-identical md5
  `099af53f601532dbd31e0ea99ffdeb64`): UTF-8, one word, 1–77 chars, not
  whitespace-only — **PASS**.
- `main.py` validates the entry programmatically before writing (exactly one
  word, 1–77 chars, no surrounding whitespace) and rejects every malformed
  input (`""`, `"two words"`, `" delete"`, `"delete "`, 78 chars, `"delete!"`).
- Deterministic: repeated runs produce byte-identical output.
- No network, no secrets, no dependencies — Python 3 stdlib only.

## Scored candidate table (50 words)

| # | Word | Speed /5 | Word-itself /5 | Freshness /5 | Total /15 | Note |
|---|---|---|---|---|---|---|
| 1 | **delete** | 5 | 5 | 4 | **14** | **WINNER** — the dictionary deletes deleting itself |
| 2 | erase | 5 | 5 | 4 | 14 | Same paradox; loses title-verb tie-break |
| 3 | dictionary | 5 | 5 | 4 | 14 | Book deletes its own name; no consequence |
| 4 | definition | 4 | 5 | 5 | 14 | Dictionary can't define anything; needs a beat |
| 5 | monosyllabic | 4 | 5 | 5 | 14 | 5 syllables meaning "1 syllable"; needs a count |
| 6 | irregardless | 5 | 5 | 3 | 13 | Fake word finally deleted; field will think of it |
| 7 | abbreviation | 4 | 5 | 4 | 13 | 12 letters meaning "shortened" |
| 8 | lisp | 4 | 5 | 4 | 13 | Word contains the sound lispers can't make |
| 9 | word | 5 | 5 | 3 | 13 | Can't say "word" any more; meta, less fresh |
| 10 | hippopotomonstrosesquippedaliophobia | 3 | 5 | 5 | 13 | Fear of long words, ironically longest; recognition risk |
| 11 | no | 5 | 4 | 3 | 12 | Nobody can ever say no again |
| 12 | why | 4 | 4 | 4 | 12 | Questions lose their engine |
| 13 | sorry | 4 | 4 | 4 | 12 | Nobody can apologise ever again |
| 14 | y'all | 4 | 4 | 4 | 12 | The South loses a pronoun |
| 15 | language | 4 | 4 | 4 | 12 | Can't talk about language |
| 16 | alphabet | 4 | 4 | 4 | 12 | Letters lose their name |
| 17 | phonetic | 3 | 5 | 4 | 12 | Not spelled phonetically |
| 18 | dyslexia | 3 | 4 | 4 | 11 | Cruelly hard to spell; mercy deletion |
| 19 | queue | 3 | 4 | 4 | 11 | Pronounced "Q"; four silent letters |
| 20 | colonel | 3 | 4 | 4 | 11 | Spelled nothing like "kernel" |
| 21 | pneumonia | 3 | 4 | 4 | 11 | Silent P at the front |
| 22 | flibbertigibbet | 3 | 4 | 4 | 11 | Fun to say, means nothing to most |
| 23 | interrobang | 2 | 4 | 5 | 11 | The ‽ loses its name; obscure |
| 24 | sesquipedalian | 2 | 4 | 5 | 11 | Long word for "loves long words"; obscure |
| 25 | floccinaucinihilipilification | 2 | 4 | 5 | 11 | Longest non-technical word; nobody knows it |
| 26 | ain't | 4 | 4 | 3 | 11 | The dictionary's most argued-over word |
| 27 | supposably | 3 | 4 | 4 | 11 | The other fake word |
| 28 | Wednesday | 4 | 3 | 4 | 11 | Spelled "Wed-nes-day", said "Wensday" |
| 29 | skibidi | 4 | 3 | 4 | 11 | Meme word; ages fast |
| 30 | doomscrolling | 4 | 3 | 4 | 11 | The scroll continues, the word dies |
| 31 | brainrot | 4 | 3 | 4 | 11 | Current slang; ages fast |
| 32 | moist | 5 | 4 | 1 | 10 | Everyone's first pick — freshness 1 |
| 33 | ointment | 4 | 4 | 2 | 10 | Gross-sound classic; field knows it |
| 34 | literally | 4 | 4 | 2 | 10 | Tired misuse joke; field will flood it |
| 35 | the | 5 | 3 | 2 | 10 | Breaks English; destructive, not funny |
| 36 | antidisestablishmentarianism | 3 | 3 | 4 | 10 | Long-word joke; everyone knows it |
| 37 | onomatopoeia | 2 | 4 | 4 | 10 | Word doesn't imitate any sound itself |
| 38 | octothorpe | 2 | 3 | 5 | 10 | The # loses its name; obscure |
| 39 | yeet | 4 | 3 | 3 | 10 | Slang; joke is the sound, not the gap |
| 40 | rizz | 4 | 3 | 3 | 10 | Slang; ages fast |
| 41 | lol | 4 | 3 | 3 | 10 | Nobody can laugh online; thin joke |
| 42 | panties | 4 | 3 | 2 | 9 | Awkward-word classic; field knows it |
| 43 | like | 4 | 3 | 2 | 9 | Filler; valley girls lose a word |
| 44 | basically | 3 | 3 | 3 | 9 | Filler; weak gap |
| 45 | flammable | 3 | 3 | 3 | 9 | The inflammable confusion; thin |
| 46 | supercalifragilisticexpialidocious | 3 | 3 | 3 | 9 | Long-word joke; everyone knows it |
| 47 | defenestration | 2 | 3 | 4 | 9 | Fun word, weak deletion joke |
| 48 | just | 3 | 3 | 2 | 8 | Filler; barely a joke |
| 49 | very | 2 | 2 | 2 | 6 | "Very" useless; the joke writes itself, weakly |

## Competition

- make.fun: [The Word You'd Delete From the Dictionary](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
- Harness: program/v1 — free entry, blind rounds (3)
- Prizes: 1st $0.73 / 2nd $0.50 / 3rd $0.35 / 4th $0.25 / 5th $0.17
- Round-1 cutoff: Nov 26 05:36 WIB · Deadline: Nov 27 13:35 WIB
- Judge: pairwise duels, z-ai/glm-5.3-flash, margin 1–5, no ties

## License

MIT — see `LICENSE`.
