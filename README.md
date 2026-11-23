# 23 November 2026 — The World in One Image (v2)

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/UpTo1M/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/UpTo1M/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

Version 2 of the entry for the make.fun competition
[Sum up 23 November's world news in one image](https://make.fun/bounty/news-image-20261123):
a newspaper front page that sums up Monday 23 November 2026 in six stories.

## What changed vs v1 — and why

V1 ("The World in One Image") scored round 1 at rank 5,615 of 7,226
(Judge win rate 410,044) — bottom quartile, far from the paid top 50.
Reading v1 at ~300px (the size the AI judge sees) showed the problem:
the bottom half was a dense wall of small text — five secondary stories
in a tight two-column grid, headlines wrapping to three lines at ~30px,
with a two-line grey deck under the lead adding noise. At judging size
it read as a grey mass, not a front page.

V2 is rebuilt from scratch around legibility at small size:

- **The lead dominates.** "COP31 COLLAPSES / WITH NO DEAL" is set as
  large as the page allows, with a red kicker and a single one-line deck.
  The lead block takes over half the page.
- **Secondary stories are headline-only.** Each of the five other stories
  is a coloured region tag plus a two-line headline in bold sans at
  33–42px — no deck text, no third line, far fewer words on the page.
- **More white space.** Wider gutters, taller rows, a clear rule between
  the lead and the grid, and a full-width bottom story (Democrats) so the
  grid never looks cramped.
- **The date stays huge.** "23 NOVEMBER 2026" fills the masthead, fully
  visible with nothing clipped (v1's first render clipped the final "6").
- Every headline is auto-fit to its box, so no text is ever clipped or
  wrapped by accident. The image was checked visually at full size and
  at ~300px before finishing.

## The six stories

1. **LEAD — COP31 collapses with no deal (Antalya, Turkey).**
   The climate summit ended without an agreement after the EU and about
   130 other parties rejected a text that omitted fossil fuels.
   Source: One Turn, 23 Nov 2026 edition; Reuters.
2. **Russian strike kills 10 in Dymer; 14 missing (Ukraine).**
   A Russian strike on a residential block in Dymer, north of Kyiv, killed
   at least 10 people; rescuers pulled a 7-year-old boy alive from the rubble.
   Source: One Turn; RFE/RL, 23 Nov 2026.
3. **AI sell-off spreads to Asia: Nikkei falls 5.06% (Markets).**
   The AI-led rout that hit US stocks on Friday spread across Asia on Monday;
   Japan's Nikkei fell 5.06%, the S&P 500 had slid 3.7% and the Nasdaq 5.3%.
   Source: One Turn; Zacks, 23 Nov 2026.
4. **Democrats win largest House majority since 1992 (United States).**
   Democrats secured 258 seats in the US House of Representatives, their
   largest majority in the chamber in over three decades.
   Source: One Turn; Inshorts, 23 Nov 2026.
5. **Russian warship sinks off Libya after drone attack (Libya).**
   The Russian corvette Merkury sank at Benghazi naval base after a suspected
   Ukrainian sea drone attack.
   Source: One Turn; RFE/RL, 23 Nov 2026.
6. **Tankers ablaze near Hormuz as Iran war widens (Strait of Hormuz).**
   Two supertankers caught fire near Hormuz after hitting mines, with strikes
   reported on Bahrain.
   Source: One Turn, 23 Nov 2026.

Every fact above was verified from the cited sources on 23 November 2026;
nothing in the image is invented.

## How it works

`main.py` is the whole program: it copies the pre-built `entry.png`
(1024×1024, 125,160 bytes, drawn at build time with Python + Pillow from
the verified stories above) to `/output/entry.png`. It uses only the
Python standard library (`os`, `shutil`, `hashlib`), makes no network
calls, and writes nothing except `/output/entry.png`, so the output is
byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).
