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
  - **App Store Connect rekord ✔ (2026. október 6.).** Egyéni Apple
    Developer Program tagság a `csipi17@gmail.com` Apple ID-n (ugyanaz a
    team, mint az Xcode-ban), az app-rekord „LogMyDrink" néven, bundle ID
    `dev.zcsipler.logmydrink`, SKU `logmydrink-ios`. **A 180 napos óra
    ettől a naptól fut:** ha 2027. április elejéig nincs feltöltött build,
    az Apple felszabadíthatja a nevet — egy TestFlight-build megtartja.
    Kitöltetlen még: Subtitle (30 karakter, ez mondja ki, hogy nem
    tracker, hanem előrejelzés), kategória (javaslat: Health & Fitness,
    másodlagos Lifestyle), Privacy Policy és Support URL.
  - **CloudKit-szinkron bekapcsolva ✔ (2026. október 7.)**, készüléken
    visszatesztelve törlés-újratelepítéssel (CLAUDE.md 5.17). Hátravan a
    kétkészülékes élő próba (szimulátor ugyanazzal az Apple ID-val: push,
    `observeRemoteChanges`), és a Production környezet: az első
    TestFlight/App Store build előtt a Console-ban **Deploy Schema
    Changes** Development → Production, különben a store-ból telepített
    app üres konténert lát.
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
  A (b) olcsóbb és gyorsabb az App Review-n, de a Pro mögötti kód
  (`ProFeature`, CLAUDE.md 5.29) akkor is a bundle-ben van — release-ben
  kikapcsolva. *2026. október 23.: a modell előfizetés egy hónap
  próbaidővel; a Pro tartalma eldöntve (5.29).*
- **EU-s App Store először?** Összefügg a 9. fejezet 1.4.3-as
  kockázatával: EU-ban a DMA-s alternatív terjesztés a kiskapu, ha az Apple
  elutasít. Ha EU-first, a 24 nyelv (7.) érv; ha globális, az angol
  `translated`, a többi `needs_review` állapot kérdés lesz.
- **Jogi utánajárás.** Disclaimer-szöveg és adatvédelmi nyilatkozat (nincs
  szerverünk — 5.17 —, ez a nyilatkozat lényege), App Store 1.4.3 appeal-érvek
  (9.), és hogy egy „estimated BAC" megjelenítés hol minősül orvosi
  eszköznek (EU MDR). Ez az egyetlen tétel, ahol külső segítség kellhet.
- **Vendég határa** (5.18, nyitva): app-alapértelmezés vagy a tulajdonosé
  másolva. Javaslat: az előbbi.

---

## 2. Élesítés előtt — az ingyenes alapfunkció

Az alapfunkció a Live (5.19). Ami itt van, az vagy a Live-ot érinti, vagy
az egész app hitelességét.

### A modell hitelessége

- **A görbe-alapú alkalom (5.22) készüléken ellenőrizendő.** Az app
  fordul, és a `LogMyDrinkTests` (az új útválasztás-tesztekkel) 2026.
  október 18-án szimulátoron zöld ✔. Ami hátravan, az a valódi adat:
  indítás a meglévő adatbázison — a
  tegnapi 10 sör és a mai sör egy alkalom lesz, a tegnapi oldalon a görbe a
  jobb szélig fut, a mai 1,x ‰-ről indul; a Live reggel nem mutat nullát egy
  nehéz este után; törlés-visszaadás a tegnapi oldalon nem tünteti el az
  estét; a Detail bezár, ha az alkalma beolvad az előzőbe; a backfill
  (verzió 3) lefut 1346 alkalmon és a végén a nap szerint kettévágott régi
  esték összeolvadnak (`mergeAdjacentSessions`); CloudKit-szinkron két
  készülékkel, hogy egy úton lévő üres alkalmat nem töröl.
- **A nap áthozatának jelzése az Előzmény oszlopain** (5.22, Zoltán
  döntése: a csúcs a saját italoké, az áthozat külön). Az adat megvan
  (`DayBucket.carryIn`), a Hét / Hónap chart még nem rajzolja — egy halvány
  jel az oszlop tövén („reggel 1,3 ‰-ről indult").
- **`AddDrinkSheet` határa múltbeli napon**: a lap `store.limit`-tel
  színez, a vetítés viszont a görbe szerinti alkalom határával ítél
  (`projectionSetting`). Egy régi, más határú estén a kettő eltérhet; a
  `project` adhatná vissza a használt határt.

- **Widmark-formula visszamérése — első kör kész (5.21).** A 3 sörös
  gyomorállapot-összevetés megvolt, a paraméterek szűkültek, motorverzió 2.
  Hátra van: más profilokon (nő, 60 kg; 100 kg férfi) és más italmixeken
  (rövid + sör) ugyanez, agentekkel párhuzamosan.
- **Tesztlefedés bővítése** (a `LogMyDrinkTests` target 2026. október óta
  megvan és zöld, 10.): property-based tesztek a motorra; regressziós
  lakat a motor kimenetére; határesetek (nulla hosszú ital, negatív
  időtartam, éjfélen átnyúló alkalom, a bétahatárokra szorított sáv, üres
  profil). Az export/import (5.17) és a több személy 2. fázisa (5.18)
  adatot tud veszíteni, és ma tesztelten nincs lefedve.

### Live képernyő

- **A „Beer added / Undo" toast a stat-sorra ül**, a STARTED / DRINKS /
  GRAMS félig takarva. A toast a kapszula fölött, a tartalom *fölé*
  lebegjen, vagy a stat-sor mozduljon el.
- **A chart y-tengelye 1,4 × határ** (5.14): 1,80-as határnál ~2,5-ig fut,
  a 0,19-es csúcs lapos kukac az alján. Zoltán kérése is: legyen magasabb
  a chart, a lapos görbe is látsszon. Két fogás: a határvonal felmehet a
  chart tetejéhez (1,05 ×), és a görbe fix 200 pt-ja (5.12) nőhet.
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

### Tájékoztatás

- **A „Hogyan működik” szövegeinek magyar nyelvi átnézése** (5.27) — a
  tartalom jóvá van hagyva, a helyesírás és a nyelvtan nem. Külön szálon,
  a Claude Docs „LogMyDrink – tájékoztató szövegek” dokumentumából; a
  javítás a `Reference/translations/hu.py`-ba megy. Ugyanott a nyitott
  kérdések: forráslista a Részletek alján (Widmark 1932, Watson 1980,
  Jones & Jönsson 1994), és hogy a „Miért van ez az app” Zoltán hangján
  szól-e.
- **A widget-útmutató képei** (5.27): ma SF Symbol ikonok állnak a lépések
  mellett; valódi képernyőképek vagy rajzok jöhetnek a helyükre.
- **Első indításos képernyő** (mi ez és mi nem, 2.) — a vezetési
  figyelmeztetés a Live kék kártyáján és a „Hogyan működik” tetején van
  (5.27); hogy egy első indításos képernyő kell-e még, App Review előtt
  érdemes eldönteni.
- **A három gyomorállapot definíciója a választóban vagy a súgójában.**
  A bemenet értéke ezen múlik, és sehol nincs leírva. Zoltán
  megfogalmazása (2026. október): *üres* — reggel, evés előtt, vagy az
  elmúlt kb. hat órában nem ettem (az ivás előtti étkezés elmaradt);
  *közepes* — átlagos, nem kiemelkedő étkezés után; *teli* — zsíros
  ételből annyit ettem, hogy az utolsó falatokat erőltetni kellett. Ez
  pont a kísérleti irodalom két szélsőségét fedi le (éjszakai koplalás
  vs. teljes étkezés), tehát a paraméterek erre az értelmezésre vannak
  belőve (5.21).

### Megjelenés

- **Animációk**: hol segít (toast be/ki, a görbe átrajzolása felvitelkor,
  oszlopok a History-ban) és hol zaj.
- **Light mód**: ma csak sötét. Döntés kell, hogy támogatjuk-e; ha igen, a
  `Theme` minden színe két értéket kap, és a határhoz kötött skála (5.14)
  világos háttéren is olvasható kell legyen.
- **Lokalizált címkék kilógása**: litván `Advanced` / `Undo`, holland
  `Undo`, román `Clears` — élőben végignézni, nem csak ezt a négyet. Az
  új Profil al-lapok (5.26) is: a „Display & language” cím és a két
  szegmentes sor (Concentration ‰ | %, Amount Grams | Units) hosszú
  nyelveken.
- **Az angol 12 órás időformátum** szélesebb címkéi a charton —
  élőben ellenőrizni.
- **A hero tartományos elrendezése** 48 pt-on — élőben ellenőrizni.
- **Az intent `IntentDialog` szövegei és a widget feliratai nincsenek a
  nyelvi modulokban**: a `make_catalog.py` nem látja őket.

---

## 3. Élesítés után — a fizetős kör és a bővítések

### Előzmény (Pro, `ProFeature.fullHistory`)

- **Görgethető idővonal a Live-on — kipróbálva, elvetve (2026. október 9).**
  Egy kör megépült (12 órás lépték konstansban, napokban betöltve, a
  figyelt nap mutatói a chart alatt, „Today" gomb), két készülékes próbán
  a chart nem mozdult vízszintes húzásra, laggolt és következetlen volt;
  Zoltán visszadobta, a kód a beszélgetésben maradt, a repóba nem került.
  Tanulságok, ha egyszer újra jön: a `chartXSelection` és a saját
  `chartGesture` is elvitte a húzást a görgetés elől — görgethető charton
  nem lehet kijelölés; a body minden scroll-frame-ben újraértékelődik, a
  `laneLayout` és a `band.samples` ezt nem bírja cache nélkül; a y-tengely
  a betöltött napok váltásakor ugrik. Ha mégis, inkább egy külön, egyszerű
  „idővonal" nézet kell a History-ban, nem a Live chartjának átalakítása —
  a Live a mai nap ablaka marad (5.22).

- **Folytonos, görgethető, csippenthető idővonal — az IntelliDrink-út
  (5.22 folytatása, Zoltán döntése: ez a következő kör).** Ma két vetület
  él egymás mellett: a heti/havi lista sora az *alkalmat* mutatja
  (`SessionDetailView`, az egész görbe, akkor is, ha okt. 9-be nyúlik), a
  Live és a Nap-oldal az *ablakot*. Mindkettő igaz, de egy okt. 8-i sorból
  okt. 9-i italt is látni — Zoltán szerint nem bug, mert az igazságot
  mondja, ezért a köztes javítás (az alkalom-nézet címe „Oct 8 – Oct 9", jel
  a hajnali 5-ös határon) kimaradt. A cél: a nap nem külön oldal, hanem
  görgetési pozíció egy folytonos sávon; swipe arrébb visz, a csípés kinyit
  egy estét vagy összehúz egy hetet; a stat-sor és az itallista a látható
  ablakot követi. Meglévő alap: `HistoryTrendChartView` görgetése és közös
  zoomja (5.16). Nyitott: a `BACChartView` italsávja, scrubja és
  jelmagyarázata görgethetőn; a scrub kontra görgetés gesztusütközése
  (5.11 tanulsága — a Health app mintája: húzás görget, hosszú nyomás
  olvas le); melyik napot „nézed" (fejléc, a Hét/Hónap kijelölés); mi lesz a
  Nap szegmenssel és a `SessionDetailView`-val.

- **A Hónap és az Év „Change" sora részidőszakot hasonlít teljeshez.**
  Október 4-én „−91 % vs. September", az évnél „−27 % vs. 2025." — a −27 %
  gyanúsan 9/12. Vagy az előző időszak azonos hosszú elejét vesszük
  (Sep 1–4, 2025. jan 1–okt 4.), vagy a sor kimondja, hogy „so far".
  Javaslat: az előbbi, mert a kártya kérdése az, hogy jobban állok-e.
- **A futó alkalom napjának csúcs-oszlopa**: a `normalize` most minden
  írásnál cache-eli az összesítőt, így a futó alkalom napjának is van
  csúcsa — de az a *vetített* csúcs (a görbe a jövőbe fut). Eldöntendő,
  hogy a Hét nézet ezt mutassa-e halványan, vagy az eddigit.
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
- **StoreKit — megépítve 2026. október 23-án (CLAUDE.md 5.30).** Az App
  Store Connect oldala 2026. október 26-án kész (a két termék, a próbaidő,
  a Privacy és Support URL, az App Privacy, a szövegek — CLAUDE.md 10.,
  „Az első beküldés állapota"). Ami még hátra van: „Manage subscription" sor a Profilban
  (`manageSubscriptionsSheet`); a vásárlás végigpróbálása Xcode-ból
  (⌘R, a scheme a helyi StoreKit-fájllal indul) és valódi készüléken
  sandbox-fiókkal. A régi terv:
- **StoreKit a `FeatureFlags` mögé** (5.19, 5.29): az `isSubscribed` ma
  mindig hamis; a paywall gombja release-ben „Coming soon". Egy
  előfizetés-csoport, havi 3,99 $ és éves 24,99 $, mindkettő egy hónapos
  introductory offerrel (CLAUDE.md 5.30); `Transaction.currentEntitlements` + `Transaction.updates`
  figyelése, flipkor `proEntitlementDidChange`. Ugyanebben a körben:
  - **a `ProPaywallSheet` igazi tartalommal**: ár, próbaidő, mit nyit a
    Pro (a 5.29 táblája), visszaállítás (Restore Purchases — kötelező);
  - **„Kód beváltása" gomb** a Pro-lapon (`offerCodeRedemption`, 5.30);
  - **Adózás, az első eladás előtt (Zoltán):** adószám és közösségi
    adószám a NAV-tól (magánszemélyként); egy egyszeri egyeztetés
    szakértővel, hogy adószámos magánszemély vagy mellékállású egyéni
    vállalkozó (átalányadó) a jobb; negyedéves adóelőleg, ÁFA-bevallás
    (65) és összesítő nyilatkozat az Apple felé végzett szolgáltatásról;
    és: az amerikai eladásokból az Apple 30 %-ot levon (nincs
    USA–Magyarország adóegyezmény 2024 óta) — beszámítható-e itthon;
  - **App Store Connect:** Small Business Program kérelem az első eladás
    előtt; a két termék és az introductory offer felvitele; egy
    StoreKit Configuration fájl a szimulátoros teszthez;
  - **mi történik lejáratkor** a felhasználó szemével: egy vendég
    személy, akire épp váltva van (a váltó eltűnik — a tulajdonosra kell
    visszaállni), és egy egyszeri „a Pro lejárt, az adataid megvannak"
    üzenet;
  - **a widget-tipp** (`FeatureTips`) és a „Hogyan működik" Pro-jelölése
    vizuálisan is (ma csak a szöveg mondja: „With Pro…").
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

- **A store az App Group konténerbe**: már csak az *írásért* — a feloldás
  nélküli felvitelért (interaktív `Button(intent:)`). A kijelzést a
  `WidgetSnapshot` megoldotta költöztetés nélkül (5.15). Ára a meglévő
  adatbázis egyszeri átköltöztetése minden készüléken, CloudKit-tükrözés
  mellett — előtte Download Container.
- **BAC-görbe a közepes Home Screen widgeten**: a snapshotban a sáv már ott
  van, a közepes méret egy `Chart` ebből; a `BACKit`-et sem kell linkelni.
- **A Live `upcomingPeak`-je a globális csúcsot nézi**, nem a következőt:
  egy leszálló ágon felvitt ital alacsonyabb második csúcsát a hero nem
  mondja ki. A widget `nextCrest` szabálya (5.15) a `BACCurve`-re is
  átvihető. *(5.22 óta a chart fejléce a nap saját csúcsát írja —
  `peak(after:)` az aznapi első italtól —, ami a másnapi sörnél jó; az
  egy estén belüli második csúcs kérdése marad.)*
- **Közepes Home Screen widget**: ott van hely az italszámnak és a grammnak
  is, amit a kicsi és a zárolt méretről levettünk — a snapshot viszi őket.

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
