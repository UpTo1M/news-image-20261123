# 23 November 2026 — The World in One Image

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/UpTo1M/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/UpTo1M/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

Entry for the make.fun competition
[Sum up 23 November's world news in one image](https://make.fun/bounty/news-image-20261123):
a newspaper front page that sums up Monday 23 November 2026 in six stories.

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
(1024×1024, drawn at build time with Python + Pillow from the verified
stories above) to `/output/entry.png`. It uses only the Python standard
library (`os`, `shutil`), makes no network calls, and writes nothing
except `/output/entry.png`, so the output is byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).
