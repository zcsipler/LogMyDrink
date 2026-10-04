# App-ikon koncepciók (2026. október)

Hat vektoros koncepció, mind az app saját színskálájával (`Theme.swift`:
sötét alap, türkiz → borostyán → korall → vörös a szint szerint) és
ugyanarra a BAC-görbére építve, hogy csak a motívum különbözzön.

```
Design/Icon/
├── make_icons.py        a hat SVG-t állítja elő (Python, csak stdlib)
├── render.py            PNG 1024-ben + kontaktlap 180 / 120 / 60 px-en (cairosvg, Pillow)
├── svg/                 a forrás — rétegek <g id="…"> csoportokban, Icon Composerhez
└── png/                 1024×1024 render + contact-sheet.png
```

| # | Fájl | Mit mond | Erőssége | Ára |
|---|---|---|---|---|
| 1 | `01-band` | **Az előrejelzés maga**: a sáv (5.1), nem vonal. | Egyedi, semmilyen italkövetőre nem hasonlít. | 60 px-en vékony; a fekvő alak rosszul tölti ki a négyzetet. |
| 2 | `02-glass-chart` | Pohár, benne a görbe: „ital → szint". | Kategória **és** tézis egyben. | A pohár kerete elveszi a helyet a görbétől. |
| 3 | `03-glass-plus` | **A logolás** — a név (1.). | A legtisztább kis méreten; store-ban azonnal érthető. | Beleolvad a „pohár ikonos" trackerek közé, a tézisből semmi. |
| 4 | `04-monogram` | Az **L** talpa az időtengely, abból nő ki a görbe. | Betűjel és motívum egy formában; időtálló. | A görbe nélkül csak egy L; a görbével együtt már „grafikon-app". |
| 5 | `05-three-lines` | A motor három szimulációja (lassú / közép / gyors béta). | Őszinte a modellhez. | 60 px-en összemosódik — a három vonalnak nincs helye. |
| 6 | `06-liquid-curve` | **A folyadék felszíne a görbe.** | A legjobb kis méreten; ital és előrejelzés egyetlen formában. | A gradiens a pohár belsejében „koktélnak" is olvasható. |

Ajánlás a következő körre: a **6** (és a 2 mint tartalék) kidolgozása —
ez az egyetlen, ami a kategóriát és a tézist egy formában mondja ki és
60 px-en is olvasható. Finomítandó rajta: a pohár aránya (alacsonyabb,
„rocks" forma), a felszín fénye, és egy világos / tinted változat az
iOS 18+ ikonmegjelenésekhez.

## Beépítés

Az `AppIcon.appiconset` ma üres (három bejegyzés, fájl nélkül). Az 1024-es
PNG-t a `LogMyDrink/Assets.xcassets/AppIcon.appiconset/` alá kell tenni és a
`Contents.json`-ban `"filename"`-ként felvenni; a widget targetnek külön
appiconset-je van, ugyanazzal a fájllal. iOS 26-on az Icon Composer rétegei
az SVG `<g id="Background">` / `<g id="Glass">` / … csoportjaiból jönnek.

```bash
cd Design/Icon && python3 make_icons.py && python3 render.py
```

## Második kör — az alkohol látsszon

Zoltán döntése az első kör után: a csak chartot mutató ikonok (1, 4, 5)
kiesnek, mert nem látszik rajtuk, hogy alkoholfogyasztásról van szó; a 2-es
pohara pedig csak egy négyzet volt a chart körül. A második kör ezért
felismerhető edényt rajzol — kúpos, bordázott söröskorsó füllel és habbal,
illetve talpas borospohár —, és a görbe benne vagy mögötte van.
Forrás: `make_icons_r2.py`, kontaktlap: `png/contact-sheet-1.png`.

| # | Fájl | Mit mond | Megjegyzés |
|---|---|---|---|
| 11 | `11-mug-chart` | Korsó habbal, benne a görbe. | A hab teszi sörré; 60 px-en is korsó. |
| 12 | `12-mug-liquid` | A sör felszíne a görbe, a hab a görbét követi. | Hab nélkül a kúpos korsó is bögrének olvasható — gyengébb a 11-nél. |
| 13 | `13-wine-chart` | Borospohár, benne a görbe. | A talp és a kehely egyértelműen bor; a görbe a kehely alján kevés helyet kap. |
| 14 | `14-wine-liquid` | A bor felszíne a görbe. | A legtisztább kicsiben; ital és előrejelzés egy forma. |
| 15 | `15-wine-behind` | A sáv a pohár mögött fut át a képen, a pohárban élénken. | „Amögött" változat; a külső sáv 60 px-en elvész. |
| 16 | `16-mug-behind` | Ugyanez korsóval. | Zsúfoltabb a 15-nél a fül és a hab miatt. |

Kérdés a következő körhöz: sör vagy bor legyen az edény? A korsó
félreérthetetlenebb (hab + fül), a borospohár elegánsabb és semlegesebb —
nem mondja, hogy „sörös app".

## Harmadik kör — a 11-esből, kilógó görbével

Zoltán választása a 11 (habos korsó, benne a görbe). Kérés: a görbe ne
legyen bezárva a pohárba — a felfutás eleje és a lefutás vége lógjon ki.
Így a benne / mögötte elv keveredik: a pohárban lévő rész kitöltött, a kívül
futó csak vonal. Forrás: `make_icons_r3.py`, kontaktlap: `png/contact-sheet-2.png`.

| # | Fájl | A kívül futó rész |
|---|---|---|
| 21 | `21-mug-overflow` | Ugyanaz a vonal, tompítva (55 %) — a korsó marad a főszereplő. |
| 22 | `22-mug-overflow-bold` | Teljes erővel, halvány kitöltéssel kívül is — a chart a hős, a korsó a keret. |
| 23 | `23-mug-overflow-dotted` | Pontozott — ami a pohárban van, az megtörtént; ami kívül, az előrejelzés. |
| 24 | `24-mug-overflow-mirrored` | Tükrözött korsó, fül balra — a hosszú lefutás szabadon megy ki jobbra, a felfutás viszont a fül mögé bújik. |

Tanulság a körből: ha a görbe túl magasra fut, a csúcs a hab alá kerül, és a
pohár belseje tele korsónak látszik, nem chartnak. A csúcsnak a hab alatt,
láthatóan kell maradnia (magasság 430, a hab alja ~290).

## Döntés: a 21-es

Zoltán választása a `21-mug-overflow`. Az `export_appicon.py` ebből állítja
elő a három iOS 18+ megjelenést az `appicon/` alá, és ugyanezek kerültek az
asset katalógusokba:

- **Default** — a terv ahogy van, átlátszatlan (az App Store Connect alfát
  nem fogad el az alapképen).
- **Dark** — csak a glyph, átlátszó alapon: a sötét ikonrácson az iOS a saját
  gradiensét teszi mögé; egy átlátszatlan fekete négyzet lyuknak látszana.
- **Tinted** — a glyph szürkeárnyalatban, átlátszó alapon, a középtónusok
  megemelve, hogy a görbe a rendszer színezése után is látsszon.

A widget target ugyanazt a három képet kapja.
