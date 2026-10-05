# LogMyDrink — teendők

A `CLAUDE.md` azt mondja, mi *van* és miért; ez a fájl azt, mi *lesz*. Ami
megépül, innen kikerül, és a döntése az indoklással együtt a `CLAUDE.md`
5. fejezetébe költözik. Három vödör: amit az ingyenes alapfunkció élesítése
előtt meg kell csinálni, ami a fizetős körre vár, és ami tetszőleges. Egy
negyedik lista a döntésekről, amik nem feladatok, de blokkolnak.

Ha egy tétel mögött fejezetszám áll (pl. 5.14), a `CLAUDE.md` adott pontja
mondja el a hátteret.

---

## 1. Döntésre vár

Ezek nem kódolási feladatok. Amíg nincsenek eldöntve, néhány lenti tétel
sem indítható.

- **A név lefoglalása — Zoltán döntése (2026. október): csak az App
  Store-ban, most; domain és védjegy az élesítés után.** Amíg nem biztos,
  hogy az app felkerül a store-ba, egy ismeretlen név domainjét senki nem
  viszi el, a védjegy pedig pénz; a store-név viszont ingyen van és első
  érkezés alapján megy.
  - **App Store Connect rekord**, amint a fizetős tagság él (az Apple ID
    ugyanaz legyen, mint az Xcode-ban a `2GYMHK5C56` Personal Team mögött;
    egyéni tagság, a fejlesztő neve a saját polgári név lesz). Apps → `+`
    → New App, név „LogMyDrink", bundle ID `dev.zcsipler.logmydrink`, SKU
    `logmydrink-ios`. Build nem kell hozzá, a rekord foglal. **180 nap után
    az Apple felszabadíthatja a fel nem töltött nevet** — ha az első
    feltöltés csúszik, egy TestFlight-build megtartja.
  - **Google Play: nincs mit foglalni.** A Play-cím nem egyedi (több app is
    viselheti), csak a package name az, és az is csak feltöltéskor
    foglalódik. Androidon a nevet csak a védjegy védi — amikor lesz
    Android-app.
  - **Domain az élesítés után:** `logmydrink.app` (elsődleges, csak HTTPS)
    és `.com` (védelem); az `.io` nem kell. 2026. október 4-én mind szabad.
    A beküldéshez kötelező Privacy Policy és Support URL addig GitHub Pages.
  - **EU-védjegy** a 9. és 42. osztályra, ha az app él (TMview és USPTO
    2026. október 4-én: nincs egyező jelölés; rokon: francia „DrinkLOG",
    INPI 4840485, 9/42, hőmérséklet-naplózó eszközök).
  - GitHub repó átnevezve `zcsipler/LogMyDrink`-re ✔.
- **Demo vs. in-app purchase az első feltöltésnél.** Két út: (a) egyszerre
  megy fel az ingyenes Live és a fizetős Előzmény, StoreKittel; (b) először
  csak az alap grafikon, a fizetős funkciók később, marketing mellé.
  A (b) olcsóbb és gyorsabb az App Review-n, de a `Feature.historyTrends`
  mögötti kód akkor is a bundle-ben van — release-ben kikapcsolva.
- **EU-s App Store először?** Összefügg a 9. fejezet 1.4.3-as
  kockázatával: EU-ban a DMA-s alternatív terjesztés a kiskapu, ha az Apple
  elutasít. Ha EU-first, a 24 nyelv (7.) érv; ha globális, az angol
  `translated`, a többi `needs_review` állapot kérdés lesz.
- **Jogi utánajárás.** Disclaimer-szöveg és adatvédelmi nyilatkozat (nincs
  szerverünk — 5.17 —, ez a nyilatkozat lényege), App Store 1.4.3 appeal-érvek
  (9.), és hogy egy „estimated BAC" megjelenítés hol minősül orvosi
  eszköznek (EU MDR). Ez az egyetlen tétel, ahol külső segítség kellhet.
- **Mennyiség: gramm *és* egység egyszerre?** Zoltán kérése, hogy az italok
  mindkettőben látsszanak. Ez ütközik egy rögzített döntéssel (5.16,
  `AmountUnit`): a kettő ×10, „ezért nem mutatjuk egymás mellett". Előbb
  el kell dönteni, hogy a döntés fordul-e, vagy csak egy helyen (pl. az
  itallista sorában) kell a második szám.
- **Vendég határa** (5.18, nyitva): app-alapértelmezés vagy a tulajdonosé
  másolva. Javaslat: az előbbi.

---

## 2. Élesítés előtt — az ingyenes alapfunkció

Az alapfunkció a Live (5.19). Ami itt van, az vagy a Live-ot érinti, vagy
az egész app hitelességét.

### A modell hitelessége

- **Widmark-formula visszamérése.** Az IntelliDrink régi screenshotjaiból
  ugyanazokra a bemenetekre kiszámolni a mostani motor értékét, és
  összevetni. Eltérésnél el kell dönteni, melyik a referencia — a 6.
  fejezet validációja irodalmi értékekhez mér, nem az IntelliDrinkhez.
  Érdemes agentekkel párhuzamosan több profilon futtatni.
- **Unit tesztek rendberakása**: app-szintű teszt target
  (`LogMyDrinkTests`, Xcode-ban: File → New → Target → Unit Testing
  Bundle), hogy a már megírt 18 perzisztencia-teszt és a 37 History-teszt
  tényleg fusson; property-based tesztek a motorra; regressziós lakat a
  motor kimenetére; határesetek (nulla hosszú ital, negatív időtartam,
  éjfélen átnyúló alkalom, a bétahatárokra szorított sáv, üres profil).
  Az export/import (5.17) és a több személy 2. fázisa (5.18) adatot tud
  veszíteni, és ma tesztelten nincs lefedve.

### Live képernyő

- **A disclaimer a tabsáv alá szorult.** A „This is an estimate, not a
  measurement" a tab bar mögött dereng — a 2. fejezet szerint ez a
  képernyő része, nem apró betű. Vagy a hero alá költözik, vagy a tartalom
  kap akkora alsó insetet, hogy kigördülhessen a sáv alól.
- **A „Beer added / Undo" toast a stat-sorra ül**, az ELAPSED / DRINKS /
  GRAMS félig takarva. A toast a kapszula fölött, a tartalom *fölé*
  lebegjen, vagy a stat-sor mozduljon el.
- **A chart y-tengelye 1,4 × határ** (5.14): 1,80-as határnál ~2,5-ig fut,
  a 0,19-es csúcs lapos kukac az alján. Zoltán kérése is: legyen magasabb
  a chart, a lapos görbe is látsszon. Két fogás: a határvonal felmehet a
  chart tetejéhez (1,05 ×), és a görbe fix 200 pt-ja (5.12) nőhet.
- **A legenda „possible range"-et ír nulla sávszélességnél is.** Az 5.12
  szellemében (a legenda csak azt nevezze meg, ami a képernyőn van) el
  kell tűnnie, amíg `betaUncertainty` nulla.
- **A gyors-felvitel gomb a Profil szövege szerint a vetített csúcsot
  mutatja** („with the projected peak on the button") — a képen csak „Beer
  500 ml" áll. Vagy a szöveg ígér többet, vagy a toast idejére tűnik el.

### Ital felvitele

- **Típusrács egy sorban** — volt terv (hat ikon egy sorban), de a
  léptetők (5.20) után a lap görgetés nélkül ráfér a képernyőre, ezért
  Zoltán elengedte; ha egyszer saját italtípus jön, akkor kerül elő újra.
- **A chart x tengelye a live és a lezárt alkalmon másképp van keretezve**
  (`BACChartModel.visibleRange`): a lezárt arra, ami történt (első ital
  −15 perc → kiürülés +20 perc), a live legalább hat órára kihúzva, „hogy
  legyen hova nőnie". Egy sör 2,5 óra alatt ürül ki, tehát ugyanaz az ital a
  Nap oldalon 2,5, a Live-on 6 órás ablakban látszik — ezért tűnik a Live
  görbéje laposabbnak. Az indok gyenge (a sáv a kiürülésig fut, tehát a
  jövő benne van), a javaslat egy közös szabály 3 órás minimummal; Zoltán
  még gondolkodik rajta, egyelőre nem nyúlunk hozzá.
- **Tömeges felvitel** (5.16): „20:00-tól fél óránként 8 sör"
  jellegű sorozat egy lépésben, az itteni felvitel bővítéseként.

### Profil

- **Túl sok a menü, kategóriákra kell szedni.** Ma egy végtelen `Form`:
  test, gyakoriság, határ, haladó, gyors felvitel, megjelenítés, nyelv,
  számított értékek, személyek, mentés, fejlesztői. Valószínűleg al-lapok
  kellenek (pl. „Megjelenítés", „Adatok", „Haladó").
- **A Display blokk két független választást mutat egy listában, két
  pipával** (‰/% és g/egység). Rádiócsoportnak néz ki, amiben valami
  elromlott; két szekció vagy két `Picker`.
- **A Quick add sor csak a szövegen és a nyílon fogja a koppintást**, a
  cella üres részén nem — `contentShape(Rectangle())` hiányzik.

### Tájékoztatás

- **Részletesebb tájékoztató képernyők**: első indításkor mi ez és mi nem
  (nem verdikt, 2.), és a tudományos magyarázó képernyő (Widmark,
  Watson, Michaelis–Menten, felszívódási állandók; a tartalom a `CLAUDE.md`
  4. fejezetében már megvan). App Store-érv is (9.).
- **Widget és Siri felfedezhetősége** (5.15): a `WidgetCenter.
  getCurrentConfigurations` alapján elvethető kártya a három lépéssel, amíg
  a widget nincs kitéve; `SiriTipView` a kapszula alatt.

### Megjelenés

- **Animációk**: hol segít (toast be/ki, a görbe átrajzolása felvitelkor,
  oszlopok a History-ban) és hol zaj.
- **Light mód**: ma csak sötét. Döntés kell, hogy támogatjuk-e; ha igen, a
  `Theme` minden színe két értéket kap, és a határhoz kötött skála (5.14)
  világos háttéren is olvasható kell legyen.
- **Lokalizált címkék kilógása**: litván `Advanced` / `Undo`, holland
  `Undo`, román `Clears` — élőben végignézni, nem csak ezt a négyet.
- **Az angol 12 órás időformátum** szélesebb címkéi a charton —
  élőben ellenőrizni.
- **A hero tartományos elrendezése** 48 pt-on — élőben ellenőrizni.
- **Az intent `IntentDialog` szövegei és a widget feliratai nincsenek a
  nyelvi modulokban**: a `make_catalog.py` nem látja őket.

---

## 3. Élesítés után — a fizetős kör és a bővítések

### Előzmény (fizetős, `Feature.historyTrends`)

- **A Hónap és az Év „Change" sora részidőszakot hasonlít teljeshez.**
  Október 4-én „−91 % vs. September", az évnél „−27 % vs. 2025." — a −27 %
  gyanúsan 9/12. Vagy az előző időszak azonos hosszú elejét vesszük
  (Sep 1–4, 2025. jan 1–okt 4.), vagy a sor kimondja, hogy „so far".
  Javaslat: az előbbi, mert a kártya kérdése az, hogy jobban állok-e.
- **A nyitott alkalom napjának nincs csúcs-oszlopa** a Hét nézetben, a
  gramm-oszlopa viszont van (érvénytelen cache → hiány, 5.16). Az eddigi
  vagy a vetített csúcs halványan jobb lenne, mint a lyuk.
- **Számformázás a kártyán**: „12983" csoportosítás nélkül, a tengelyen
  „2 000" csoportosítva. `.formatted()` grouping a kártyára.
- **A napi gramm-oszlop színe havi tempóként ítél** (5.14): egy 60 g-os nap
  korallvörös, miközben a csúcsa a határhoz zöld — ugyanaz a nap, két
  ellentétes ítélet egymás alatt. Vagy a napi oszlop semleges és csak az
  összeg kap színt, vagy a napi horgony más.
- **Trend szegmens újragondolása és élesítése** (5.16): a görbék
  olvashatósága nyitott; addig `Experiment.trendSegment`.
- **Év → hónap, hónap → hét ugrás visszahozása látható vezérlővel** (5.16),
  pl. „Megnyitás" gomb az érték-buborékban, nem rejtett gesztus.
- **Szegmensváltás tartsa-e az ablak helyét** a nulladik oldalra ugrás
  helyett (5.16).
- **Ital nélkül maradt alkalom törlése** a `SessionStore`-ban (5.16) — ma
  az aggregátor szűri ki, az adatbázisban marad.
- **StoreKit a `FeatureFlags` mögé** (5.19): az `isPurchased` ma mindig
  hamis; a paywall gombja release-ben „Coming soon".
- **Józan napok streak** — visszafogottan, „eddig eljutottál", nem
  „elvesztetted".

### Szinkron és adat

- **iCloud / CloudKit bekapcsolása** (5.17): fizetős Apple Developer
  Program kell; a kód kész, `BuildCapabilities.cloudSync` kapcsolja; a
  teendőlista sorrendben az 5.17-ben.
- **Apple Health szinkron**: testadatok beolvasása, BAC és kalória
  visszaírása.

### Italok

- **Saját italtípus felvitele** a `DrinkCatalog` mellé. A `Drink.name`
  sablon-azonosító (7.), tehát az egyedi típusnak is stabil id kell, és az
  exportnak (5.17) vinnie kell a definícióját.
- **Ital áthelyezése másik napra** szerkesztéssel — ma az eredeti
  alkalomban marad.
- **Italszerkesztő képernyő**: utólag könnyen összehúzogatni az italokat
  az időtengelyen, és előre: egy estére tervet csinálni (a tömeges felvitel
  folytatása).
- **Szénhidrát / kalória bevitel** az alkohol mellé.
- **Italra költött összegek**, opcionálisan.

### Widget második köre (5.15)

- **A store az App Group konténerbe**: ez nyitja a feloldás nélküli
  felvitelt (interaktív `Button(intent:)`) és a görbét a widgeten. Ára a
  meglévő adatbázis egyszeri átköltöztetése — előtte Download Container.
- **Zárolt widgeten több infó**: felszálló / leszálló ág, csúcs, „még
  emelkedik" — oda a szám való, nem a görbe.
- **BAC-görbe a közepes Home Screen widgeten**: a `BACKit` Foundation-only,
  az extension is futtathatja; a timeline 5 percenként előre számolható.
- **watchOS** gyors felvitel — a `LogDrinkIntent` már megvan hozzá.

### Egyéb

- **Szondás kalibráció**: két mért érték + két időpont → béta,
  felajánlva beállításra; a mérések tárolva.
- **Helyi értesítések**: közeledsz a határhoz / mikorra leszel tiszta.
- **Az italikonra koppintás a chart alatt nyissa a szerkesztést**, ugyanúgy,
  mint a sor koppintása. Ma a badge csak jelöl. Nice to have; két kör
  elment rá 2026 októberében, és egyik sem volt az igazi, ezért félretéve.
  Amit tudunk: (1) a badge annotation nézetre tett `onTapGesture` sosem
  fut le — a `chartXSelection` gesztusa a teljes plotot fedi, és a Chart
  elnyeli az érintést az annotation előtt; (2) a `chartXSelection`
  lecserélése saját `chartOverlay`-re, amin a kezdőpont dönt (nulla vonal
  fölött scrub, alatta badge-találat `proxy.position(forX:forY:)`-ból, 32 ×
  24 pt dobozzal) technikailag működik, de a 18 pt-os badge ujjal nehezen
  eltalálható, és két szomszédos badge-nél a második gyakorlatilag nem.
  Ha újra elővesszük, a találati méret a kérdés, nem a gesztus: vagy
  nagyobb badge (a sor 24 pt-ja ehhez kevés), vagy a koppintás nem a
  badge-et, hanem a sort / az oszlopot (`pourWindows`) találja — az ital
  oszlopa a teljes chart-magasságon fut, szélessége a tempó, és ritkán
  fed át a szomszédjával. A sávot a Charton kívülre vinni (az x-tengely
  alá) nem éri meg: elveszne a közös időtengely és az átfutó oszlop
  (CLAUDE.md 5.12), a plot bal széle pedig a tengelyfeliratoktól függ.

---

## 4. Technikai hátralék

Nem termékfunkció, nem is blokkol, de egyszer rendbe kell tenni.

- **`AddDrinkSheet` élő előrejelzés gyorsítása**: `projectBand`
  minden lépésköznél (12 ms release, 167 ms debug). A belső ciklus ~7
  tömböt allokál RK4-lépésenként; előre foglalt scratch bufferekkel
  kiirtható. A kimenetnek bitre azonosnak kell maradnia — `BACEngine.
  version` nem bumpolandó.
- A dátumok („Sep 30., Wed", „2026. October") a magyar régió + angol nyelv
  kombinációból jönnek, nem az appból. Nem javítandó; csak tudni kell, hogy
  a képeken ettől furcsa.
