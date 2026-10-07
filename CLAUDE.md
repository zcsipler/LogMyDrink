# LogMyDrink — projektkontextus

Ez a fájl azért van, hogy egy új beszélgetés azonnal képben legyen. Azt
mondja el, mi *van* és miért. Hogy mi *lesz* — teendők, nyitott döntések,
hátralék —, az a `TODO.md`-ben áll. Ha valamit megváltoztatunk a modellben
vagy a terméklogikában, ezt is frissítsük; ami a `TODO.md`-ből megépül, az
innen kap egy pontot az 5. fejezetben, az indoklásával.

Ha egy új beszélgetés kezdődik, a rövid útvonal: **0.** hogyan dolgozunk,
**2.** miért létezik ez az app, **5.** minden lényeges döntés és az indoklása,
**10.** hol állunk most, **11.** hol vannak a teendők.

---

## 0. Munkamódszer — kötelező

**Soha ne commitolj engedély nélkül.** Ha a változtatás kész, mutasd meg a
`git diff --stat` összesítőt és a lényegi részleteket, aztán várj. A commitot
Zoltán hagyja jóvá, és ő is fogalmazhat rajta. Ugyanez a `git push`-ra és
minden más olyan műveletre, ami a repó állapotát kívülről is láthatóvá teszi.

Staging (`git add`) is várjon a jóváhagyásra — az elrontott index ugyanúgy
takarítást igényel.

**Elakadt `.git/index.lock`: töröld, ne kérdezz.** A Cowork sandboxában a git
rendszeresen otthagy egy üres `index.lock`-ot, és a következő git művelet
„Another git process seems to be running"-gal elhasal. Ez nem futó folyamat,
hanem szemét. A szabály: ha a lock üres (0 bájt) és nem most keletkezett
(idősebb pár másodpercnél), töröld magad — a sandbox `rm`-je „Operation not
permitted"-et ad, ilyenkor az `allow_cowork_file_delete` eszközzel kérj
törlési engedélyt a mappára, és töröld. Zoltánt ezzel nem kell megállítani;
a jóváhagyott commit maga az engedély a takarításra is.

---

## 1. Mi ez

iOS app (SwiftUI, iOS 17+) a saját alkoholfogyasztás tudatos követésére.
A központi kérdés, amire válaszol:

> **Hová vinné a szintemet a következő ital, és mikor?**

A tulajdonos és fejlesztő Zoltán. GitHub: `zcsipler/LogMyDrink`.
Bundle ID: `dev.zcsipler.logmydrink`.

**A név — LogMyDrink (2026. október).** A munkanév `DrinkSmart` volt, de az
App Store-ban már él egy „Drink Smart - Alcohol Tracker", a Playen egy
„Drink Smart - Daily Tracker" — névütközés és kategória-ütközés egyszerre.
A LogMyDrink Zoltán ötlete, és három okból nyert a szellemesebb jelöltek
(Pourcast, NextPour, MyNextDrink) ellen: **alapszókincs** egy nem angol
anyanyelvűnek is, a „pour" nem az; **a név maga a Siri-parancs** — az Apple
megköveteli, hogy minden kifejezésben benne legyen az app neve (5.15), és
itt ez nem ára semminek, mert „Hey Siri, LogMyDrink" egyben az utasítás;
és **a logolás az egyetlen cselekvés, amit a felhasználó tesz** — az
előrejelzés és az Előzmény is ebből él. A név tudatosan *nem* az
előrejelzést mondja ki (2.); azt az alcím dolga elmondani a store-ban.
Store-keresésnél a pontos címegyezés mindent ver, tehát a „Drink Log"
nevű appok tömege a brandkeresést nem zavarja, csak a kategóriakeresést —
azt viszont bármelyik név ugyanúgy. A bundle ID is átváltott, mert a
váltás csak addig ingyenes, amíg egy felhasználó van: utána minden
készüléken adatvesztés és új App Store-rekord. A UserDefaults-kulcsok
előtagja is `logmydrink.`: az új bundle ID új sandboxot jelent, a régi
kulcsok alatt sehol nincs adat, amit meg kellene őrizni.

## 2. Miért létezik — a termék tézise

Az előzmény az **IntelliDrink**, amit az Apple 2018 februárjában levett az App
Store-ról az 1.4.3-as guideline alapján: csak hardveres szondával párosított
BAC-kalkulátor engedélyezett, tisztán szoftveres nem.

A tézis, ami miatt ezt mégis megéri megépíteni:

- **Az egységszámláló trackerek visszamenőlegesek.** Megmondják, mit ittál.
  A döntés viszont a kiöntés ELŐTT születik, és ott egy előreszimuláció
  avatkozik be. Ez funkcionálisan más dolog, nem ugyanannak a szegényebb
  változata.
- **A szonda a felszálló ágon alulmér.** Aki tíz perce ivott, alacsonyat fúj,
  a csúcs 30–90 perccel később jön. A modell ezt előre tudja vetíteni, a
  hardver definíció szerint nem.
- **A blackoutot nem az összmennyiség jósolja**, hanem a csúcs és főleg az
  emelkedés meredeksége. Ezt az egységszám elvileg sem tudja megmutatni, mert
  nincs benne idő. A BAC-görbe az egyetlen ábrázolás, ami arra a változóra néz,
  ami számít.

**Amit az app szándékosan NEM csinál:** nem ad verdiktet. Se „vezethetsz", se
„biztonságos". A disclaimer nem apró betű a lap alján, hanem a képernyő része.

## 3. Architektúra

```
LogMyDrink/
├── LogMyDrink.xcodeproj        objectVersion 77, file-system synchronized group
├── BACKit/                     lokális Swift package — a farmakokinetikai motor
│   ├── Sources/BACKit/
│   │   ├── BodyProfile.swift   Watson TBW, eloszlási térfogat, béta + bizonytalanság
│   │   ├── Drink.swift         ital, gyomorállapot, ka, biohasznosulás
│   │   ├── BACEngine.swift     RK4 szimuláció, BACCurve lekérdezések, version
│   │   ├── Projection.swift    egyvonalas „mi lenne, ha" (régebbi API, megmaradt)
│   │   ├── BACBand.swift       sávos szimuláció, LimitOutcome, BandedProjection
│   │   └── PourShortening.swift  a megkezdett ital lezárása a következővel
│   └── Tests/BACKitTests/      56 teszt, Python referenciaértékekkel
├── LogMyDrink/                 az app target
│   ├── LogMyDrinkApp.swift     ModelContainer, CloudKit visszaeséssel, store létrehozás
│   ├── Localizable.xcstrings   a 24 hivatalos EU-nyelven, generált
│   ├── Model/
│   │   ├── BACChartModel.swift      a chart bemenete — élő store vagy tárolt alkalom
│   │   ├── DrinkCatalog.swift       italtípusok, StomachState UI-réteg
│   │   ├── DrinkingDay.swift        ivási nap hajnali 5-ös határral
│   │   ├── DrinkingFrequency.swift  a béta proxyja
│   │   ├── HistoryAggregate.swift   alkalmak → napok → periódusok, memóriában
│   │   ├── HistoryWindow.swift      a History képernyő ablaka: nap / hét / hónap / év, oszlopok, mutatók
│   │   ├── HistoryTrend.swift       a teljes időszak két EMA-görbéje: mennyiség / nap, csúcs
│   │   ├── SessionStore.swift       @Observable, SwiftData-alapú, a nyitott alkalom
│   │   └── Persistence/
│   │       ├── Person.swift              @Model, kinek a fogyasztása — test, béta, határ
│   │       ├── PersonMigration.swift     tulajdonos + gazdátlan alkalmak örökbefogadása
│   │       ├── DrinkingSession.swift     @Model, profil-pillanatkép + cache + személy
│   │       ├── DrinkRecord.swift         @Model, a tárolt ital
│   │       ├── MonthlyTotal.swift        @Model, havi összeg a rögzítés előtti hónapokra
│   │       ├── SessionPolicy.swift       mikor ér véget egy alkalom
│   │       ├── AppSettings.swift         ami a KÉSZÜLÉKÉ: mértékegység, aktív személy
│   │       ├── DataArchive.swift / ArchiveExport / ArchiveImport  JSON mentés és visszatöltés
│   │       └── SessionStore+Preview.swift in-memory store a previewekhez
│   ├── Support/
│   │   ├── Theme.swift         színek, a görbe színe a határhoz viszonyítva változik
│   │   ├── FeatureFlags.swift  egy hely, ami eldönti, mi van bekapcsolva (5.19)
│   │   ├── BACUnit.swift       ‰ / % megjelenítés, tartomány-formázás
│   │   ├── AmountUnit.swift    gramm / standard egység megjelenítés, alapból gramm
│   │   ├── ArchiveDocument.swift  FileDocument az exporthoz
│   │   ├── LogDrinkIntent.swift  App Intent + Siri kifejezések a gyors felvitelre (5.15)
│   │   ├── QuickAddLink.swift  a widget deep linkje és a QuickAddRequest
│   │   └── WidgetBridge.swift  a kedvenc ikonja az App Group közös defaultsába
│   └── View/
│       ├── MainTabView.swift        History / Live / Profil, Live középen; HistoryRequest a tabok közt
│       ├── LiveView.swift           élő alkalom, csak a mai nap — három nap-állapot, „Tegnap" gomb
│       ├── HistoryView.swift        nap / hét / hónap / év, lapozás, chart, alkalom-lista, lakat
│       ├── HistoryChartView.swift   oszlopok mennyiségre és csúcsra
│       ├── HistoryTrendChartView.swift  görgethető, csippenthető trendgörbe, közös zoom
│       ├── HistoryPaywallSheet.swift  mi van a lakat mögött, és hogy az adat már megvan
│       ├── HistoryJumpSheet.swift   ugrás tetszőleges hétre / hónapra / évre a fejlécről
│       ├── SessionRow.swift         egy alkalom sora, lakatolt változattal
│       ├── SessionDetailView.swift  navigációs keret egy múltbeli alkalomhoz
│       ├── SessionContentView.swift a tartalom — LiveView és Detail is ezt használja
│       ├── BACChartView.swift       a sáv, BACChartModel bemenettel
│       ├── DrinkListSection.swift   az itallista, koppintás + húzás
│       ├── DrinkRow.swift           egy sor, kézzel írt swipe-pal
│       ├── AddDrinkSheet.swift      felvitel és szerkesztés + élő előrejelzés
│       ├── PersonSwitcher.swift     ki van kiválasztva + új személy felvitele
│       ├── PeopleView.swift         személyek listája, vendég eltávolítása
│       ├── DataTransferSection.swift export / import a Profil alján
│       └── ProfileView.swift        testalkat, gyakoriság, saját határ, haladó
├── LogMyDrinkWidget/           widget extension target — egy gomb, ami az appot nyitja (5.15)
├── LogMyDrinkTests/            app-szintű tesztek, unit testing bundle a LogMyDrink hosttal (10.)
├── TODO.md                     teendők, nyitott döntések, hátralék
└── Reference/                  Python referencia, katalógusgenerátor, run_tests.sh
```

**Rétegszabály:** a `BACKit` UI-független és `Sendable`. A SwiftUI nézetek és a
SwiftData a motort hívják, soha nem fordítva. Ha valami élettani logika a
`LogMyDrink/` alá kerülne, az hiba.

**A nézetek nem beszélnek SwiftDatával közvetlenül**, egy kivétellel: a
`@Query` a `HistoryView`-ban és a `LiveView`-ban, mert az listázás. Minden írás
a `SessionStore`-on megy át: `refreshFromStore`, `add`, `update`, `remove`,
`project`, `tick`, `activate`, `addPerson`, `removePerson`, `archive`,
`importPlan`, `importArchive`, `quickAdd`.

Alkalmat **kézzel nem lehet lezárni**. Volt egy „End session" gomb, de olyan
kérdésre válaszolt, amit senki nem tesz fel: az alkalom akkor ér véget, amikor
az alkohol kitisztult és eltelt pár óra (`SessionPolicy`) — ez tény az estéről,
nem döntés. Korán megnyomva hamis lezárási időt írt volna, és a következő ital
ugyanazon az estén egy második alkalmat nyitott volna.

A `@Query` mindkét helyen **szűretlen**, és a személyre szűrés memóriában
történik. Nem lustaságból: a `@Query` predikátuma a nézet létrehozásakor
befagy, az aktív személy viszont a nézet alatt változik — ugyanaz a
megfontolás, ami miatt a napra szűrés is memóriában van.

## 4. A modell

Egy-kompartmentes farmakokinetikai modell, **italonként külön gyomor-kompartmenttel**:

```
dGᵢ/dt = -kaᵢ · Gᵢ                            elsőrendű felszívódás
dC/dt  = (Σᵢ kaᵢ · Gᵢ) / Vd − β · C/(Km + C)  telíthető elimináció
```

RK4 integráció 0,25 perces lépésközzel, percenkénti mintavétellel. A
Michaelis–Menten tag (Km = 0,02 g/L) miatt az elimináció 0,02 g/L fölött
gyakorlatilag nulladrendű, nulla közelében viszont simán kifut — nem ugrik
negatívba, mint a klasszikus lineáris Widmark.

**Minden koncentráció belül g/L.** Ez azonos az ezrelékkel. A ‰ / % csak
megjelenítési kérdés, a `BACUnit` intézi. `1,0 g/L = 0,1 g/dL = 0,10 % BAC`.

### Antropometria — Watson (1980)

```
férfi:  TBW = 2,447 − 0,09516·kor + 0,1074·magasság(cm) + 0,3362·súly(kg)
nő:     TBW = −2,097            + 0,1069·magasság(cm) + 0,2466·súly(kg)
Vd  = TBW / 0,85        (0,85 L víz egy liter teljes vérben)
C   = A_felszívódott / Vd
```

**A női egyenletben nincs életkor** — ez a Watson-formula sajátossága, nem hiba.
Ha nőt állítunk be, a kor csúszkája nem mozdít semmit. A `ProfileView` testalkat
szekciójának lábjegyzete ezt ki is mondja, ha a nem „nő" — különben bugnak
látszana.

A `widmarkFactor` (= `TBW / (0,85 · súly)`) csak kijelzésre és sanity checkre
van: 0,667 férfi / 0,589 nő a referenciaprofilokra, ami a klasszikus 0,68 / 0,55
tartományban van.

### Paraméterek

| Paraméter | Érték | Megjegyzés |
|---|---|---|
| etanol sűrűsége | 0,789 g/mL | |
| vérvíz-frakció | 0,85 L/L | 80,6 % w/w × 1,055 g/mL |
| ka — éhgyomor / közepes / teli | 6,0 / 2,5 / 2,0 h⁻¹ | felszívódási t½ ~7 perc vs ~21 perc — lásd 5.21 |
| biohasznosulás | 0,95 / 0,90 / 0,85 | gyomri ADH first-pass — lásd 5.21 |
| Michaelis Km | 0,02 g/L | |
| béta alapérték | 0,15 g/L/h | irodalmi tartomány 0,10–0,25 |
| béta bizonytalanság alapból | 0 | egy szám, nem tartomány — lásd 5.8 |
| béta élettani korlátok | 0,08–0,32 | a sáv sosem lóg ki ezeken |
| standard egység | 10 g tiszta alkohol | EU/magyar konvenció |

**Érzékenység:** magasság és kor kizárólag a testvízen keresztül hat. A súly és
a nem mozgatja legjobban a csúcsot, a gyomorállapot a csúcs alakját és
időzítését, a béta pedig a leszálló ág meredekségét.

## 5. Kulcsdöntések és az indoklásuk

Ezeket ne írjuk felül anélkül, hogy értenénk, miért így vannak.

### 5.1 Sáv, nem vonal

A béta a plauzibilis tartományán belül ennyit mozdít ugyanazon az alkalmon
(80 kg férfi, 4 ital):

| béta | csúcs | kiürül |
|---|---|---|
| 0,12 | 0,691 ‰ | 9,8 óra |
| 0,15 | 0,616 ‰ | 8,0 óra |
| 0,18 | 0,546 ‰ | 6,7 óra |
| 0,21 | 0,481 ‰ | 5,8 óra |

**44 % a csúcsban, négy óra a kiürülésben** — nagyobb hatás, mint ±10 kg
testsúly. A grafikonon egyetlen vonal kirajzolása olyan pontosságot állítana,
ami nincs meg. Ezért a `BACBand` három szimulációt futtat, és a chart **sávot**
rajzol. A sáv szélessége maga is információ.

A motor mindig a sávot számolja — ez tartja életben az `uncertain` határállapotot
(5.2) és a kiürülés időtartományát („19:00–22:00"). Hogy ebből mit *látunk*
számként, azt az 5.8 dönti el.

Névadás a görbe helyzete szerint, nem a bétáé szerint: a **lassú** lebontás ad
**magasabb** görbét, tehát az az `upper`. Ezt könnyű elrontani.

### 5.2 Háromállapotú határátlépés

`LimitOutcome`: `below` / `uncertain` / `above`. Az `uncertain` az az eset,
amikor a lassú lebontás átvinne, a gyors nem — ilyenkor az app **„átlépheted"**-et
mond, nem „átlépnéd"-et. Kerekíteni bármelyik irányba tisztességtelen lenne.

### 5.3 A béta proxyja a fogyasztási gyakoriság

A „hány ‰/óra a bétád" megválaszolhatatlan kérdés, és a találomra állított érték
rontja a becslést. Helyette a `DrinkingFrequency` négy fokozata (ritkán /
havonta párszor / hetente többször / szinte naponta) adja a középértéket
**és** a bizonytalanságot is. Élettani alap: a krónikus bevitel indukálja a
CYP2E1/MEOS útvonalat.

A nyers béta-csúszka elérhető marad, de a haladó beállítások **legalján**, külön
lenyitva. Egy vezérlő, ami feljebb ül, kérdésnek látszik, amire a felhasználótól
választ várunk — erre viszont nem tud válaszolni. Egyetlen valós indoka van a
kézi állításnak: ha van mért érték (szonda), amihez igazítani lehet.

A lenyitott blokk ezért nem csak egy csúszka. Megmutatja a beállítást órában is
(„1,0 ‰ ennyi idő alatt ürül ki") — az absztrakt 0,15/óra addig semmit nem
jelent —, és három tippet ad a saját érték megtippeléséhez:

1. **Szondával:** két fújás a lecsengő ágon, legalább egy óra különbséggel, az
   utolsó ital után legalább két órával. A két érték különbsége osztva az eltelt
   órákkal — ez maga a béta, definíció szerint.
2. **Szonda nélkül:** az app megmondja, mikorra várja a kiürülést. Ha
   következetesen hamarabb vagy rendben, a béta magasabb a beállítottnál. Ez a
   valódi önkalibrációs hurok, hardver nélkül.
3. **Mi mozgatja:** enzimindukció, nem átlagosan magasabb, éhgyomor és
   májbetegség lefelé.

### 5.4 Emelkedési sebesség kiemelve

A `rate` / `steepestRise` és a „Még emelkedik" jelzés azért van, mert a
memóriakiesés a felszívódás meredekségével korrelál. Ez egyben az egyetlen
információ, amit egy szonda elvileg sem tud megadni.

### 5.5 Alkalmanként befagyasztott profil

Minden `DrinkingSession` tárolja a **saját** profil-pillanatképét, lapítva hat
mezőbe. Ha csak az italokat tárolnánk és mindig az aktuális profillal
számolnánk, egy régi este visszamenőleg megváltozna: ugyanaz a három ital
60 kg-nál 0,578 ‰ csúcsot ad, 70 kg-nál 0,507-et — 14 % eltérés. Egy feljegyzés,
ami magát átírja, nem feljegyzés.

A lezárt alkalom befagy. A nyitott követi az aktuális profilt, amíg le nem
zárul — mert egy este közepén észrevett elgépelést a *most látott* görbén
akarsz javítani. Visszamenőlegesen létrehozott alkalom a **legközelebbi**
alkalom profilját örökli, nem a mait (`profileApplicable`).

A **motort** viszont szándékosan nem fagyasztjuk be: a bemenet van eltárolva,
így egy későbbi modelljavítás a régi alkalmakat is helyesen újraszámolja.

### 5.6 Ivási nap, nem naptári nap

A `DrinkingDay` hajnali 5-kor vált. Egy 22:00–03:00 este így egy naphoz
tartozik; éjféli határral kettévágódna, a csúcs az egyik napon, a lecsengés a
másikon. Ez dönti el, melyik alkalomba kerül egy visszamenőlegesen felvitt
ital, és azt is, hogy a Live mit számít „mának".

### 5.7 „Nem ittál" és „nem tudjuk" nem ugyanaz

Egy üres nap, amit rögzítettünk, bizonyíték arra, hogy nem ittál. Egy nap a
`trackingStartedAt` előtt csak annyit jelent, hogy nem tudjuk. Azt írni rá,
hogy „nem ittál", találgatás lenne.

A Live képernyő **három** állapotot ismer — `live`, `recorded`, `dry` —, mert
csak a mai napot mutatja (5.11), és a mai nap definíció szerint nem eshet a
rögzítés kezdete elé. Az ismeretlen nap az Előzményen látszik (5.16).

**Van egy harmadik tudásszint is: a havi összeg.** Aki az app előtt táblázatban
vezette a fogyasztását, az a hónapok összegét tudja behozni, az estéket nem.
Erre a `MonthlyTotal` entitás való (személy, év, hónap, gramm; az archívumban a
`monthlyTotals` kulcs, opcionális, a `schemaVersion` marad 1). A szabályok,
amelyeket a `HistoryAggregate.days` érvényesít és a `MonthlyTotalTests` őriz:

- A havi összeg **a rögzítés kezdete előtti napokra** vonatkozik, és azok a
  napok `.unknown`-ok maradnak — nem tudjuk, melyik napon ittál —, de mindegyik
  viszi a hónapját (`DayBucket.summarizedMonth`, egy `SummarizedMonth` érték).
  A `trackingStartedAt` jelentése nem változik: az a napi szintű rögzítés
  kezdete. A havi összeg azt tolja hátra, meddig lapozható a lista, nem azt,
  mióta vannak feljegyzések.
- Egy hónap összege **csak egészben** adódik hozzá egy időszakhoz: a
  `[DayBucket].totalUnits` akkor számolja bele, ha az adott hónap minden
  ismeretlen napja a listában van (`wholeSummarizedMonths`). Egy hét, ami
  belelóg egy ilyen hónapba, tudja a hónap összegét, de a hét részét nem — nem
  állíthatja a magáénak.
- Ha egy hónapban összeg **és** alkalmak is vannak (a rögzítés a hónap közepén
  indult, vagy valaki utólag beírt egy estét), az összeg megmarad, és ami az
  alkalmak után **marad belőle**, az az ismeretlen napoké
  (`SummarizedMonth.remainderUnits`, sosem negatív). Semmi nem számolódik
  kétszer, és egy este beírása sosem tünteti el a hónap számát.
- A **nullás hónap** az egyetlen eset, amikor havi tudásból napi tudás lesz: ha
  az összeg nulla, minden napja `.dry`, és a józan napok közé számít.
- Józan és ivós napot havi összeg soha nem termel. A számkártyán az összeg
  beleszámol a mennyiségbe és a változásba; a napok alá lábjegyzet kerül
  („N hónap csak összegként", „N nap csak havi szinten"), a
  `HistoryFigures.summarizedMonths` / `coarseDays` alapján; a régi „a rögzítés
  előtt" lábjegyzet az `unrecordedDays`-t mondja, nem az összes ismeretlent.
- Megjelenítés: az Év nézetben a hónap egy `.summarized` állapotú oszlop,
  csúcs nélkül; a Hét és a Hónap nézet ezeket a napokat egy feliratos sávval
  mutatja („Havi összeg: X g"), a Nap nézet üres állapota pedig kimondja, hogy
  napi adat nincs, havi van. A Trend kihagyja őket, mert napi bontás nélkül
  nincs mit simítani.
- **Az oszlop színe a mennyiség-chart közös, abszolút skálája** (5.14,
  `Theme.tint(forGrams:overDays:)`), az ismert napok számára vetítve; csúcs
  nincs, amit a határhoz lehetne mérni.
- Import: `(personID, year, month)` szerinti merge, meglévő hónap marad. A
  fájlban duplán szereplő hónapnál az első nyer, az érvénytelen hónap (pl.
  13.) kimarad. A megerősítő és az eredmény-ablak **akkor is** kiírja a havi
  összegek számát, ha nulla: egy exportált fájl visszatöltésénél ez mondja meg,
  hogy nincs benne mit betölteni, és nem az, hogy már mind megvan.

### 5.8 Egy szám alapból, tartomány ha a user kéri

A motor mindig sávot számol (5.1). Hogy ez számként egy érték vagy tartomány,
azt **kizárólag a `betaUncertainty`** dönti el, és az **alapértéke nulla**. A
`BACReadout` mindig a sávot kapja, és magától egy számot ír ki, ha a sáv
szélessége nulla (`formatRange` összecsukja az egyező végeket). Nincs külön
„egyszámos mód" a kódban.

**Miért nulla az alapérték.** A szám személyes referenciaskála: idővel
megtanulod, nálad mit jelent a 0,6. Tartományhoz nincs fix pont, amihez az emlék
hozzátapadhatna. Ráadásul a béta bizonytalansága nem véletlen zaj, hanem
**személyenként szisztematikus**: ha a valódi bétád 0,18, és az app 0,15-tel
számol, minden számot ugyanabba az irányba, nagyjából ugyanannyival téveszt el.
A következetes torzítás egy referenciaskálához ártalmatlan — észrevétlenül
hozzákalibrálod magad.

**Miért marad meg a csúszka.** A tartomány a szó szerintibb válasz: a sebesség
tényleg bizonytalan. Aki ezt akarja látni, állítsa fel — ettől az app is
komolyabbnak hat. Ez beállítás, nem alapértelmezés.

A szórás a nullás alapbeálláson is látszik ott, ahol **változtat a döntésen**:

- **kiürülés ideje** — négy óra különbség nem kozmetika,
- **a sáv a charton**,
- **a háromállapotú figyelmeztetés** (5.2) — az „átlépheted" a sávból él.

A `DrinkingFrequency` ezért **csak a bétát állítja**, a bizonytalanságot nem — a
javasolt szórást a csúszka mellett szövegként ajánlja fel. A
`Physiology.legacyBetaUncertainty` (0,03) külön konstans: egy régi, még
`betaUncertainty` nélkül írt pillanatkép azt a számot jelentette, és egy tárolt
alkalom nem írhatja át magát (5.5).

### 5.9 Ivási tempó — az emelkedés hitelessége, nem a csúcs pontossága

A `Drink.drinkingMinutes` alatt az alkohol **egyenletes sebességgel** kerül a
gyomorba, nem egyetlen pillanatban. Nulla időtartam bitre azonos a régi
viselkedéssel (0,181691712), így semmi korábban felvitt adat nem mozdul.

**Fontos, hogy miért van:** nem a csúcs miatt. Egy négy sörös este csúcsa
így is, úgy is ~2 %-on belül ugyanaz. Az **emelkedés meredeksége** viszont
0,81 → 0,36 g/L/h között mozog az „egy hajtásra" és a lassú kortyolás között
(−55 %). A blackout ezzel korrelál (5.4), tehát egy olyan görbealakot
állítottunk volna, amit nem modelleztünk.

*(Ezt a számot egyszer elrontottam: egy gyors szkriptben a bolus-esetben mind a
négy sört t=0-ra tettem, és −32 %-os csúcskülönbséget állítottam. Nem volt igaz.
Ha egy szám túl jól jön ki, számoljuk újra.)*

Italtípusonkénti alapértékek — `DrinkCatalog`: tömény 0 perc (egyben lehajtják),
sör 30, bor 25, pezsgő 20, koktél 20, egyedi 15.

### 5.10 Az előrejelzés a megerősítő sávban van, nem a lap tetején

Az `AddDrinkSheet` vetített csúcsa az Add gomb fölött ül. Nem ez alapján
választasz italt — már tudod, hogy sört akarsz —, így a lap tetején csak
lenyomta a típusválasztót a fold alá. A gomb mellett viszont ott van, ahol a
döntés születik, és a határátlépés-figyelmeztetés (5.2) belőle növi ki magát,
amikor van mit mondani.

### 5.11 A Live csak a mai nap

Volt benne naplapozás — vízszintes swipe a korábbi napokra, `dayOffset`-tel és
két chevronnal. Kivettük.

**Miért.** A gesztus nem tudott megélni azon a képernyőn. A chart saját
vízszintes húzást használ az értékek leolvasására, a `DrinkRow` pedig a törlés
felfedésére; a lapozás ezért csak a köztük maradó blokkokra került, és ott is
egy `ScrollView`-val versengve. Ami maradt belőle, az egy gesztus, amit
harmadszorra lehetett eltalálni — ez rosszabb, mint ha nem is lenne. Egy első
kör (a lista kivétele a lapozásból, és az irány megfordítása a szokásos
balról-jobbra-a-múltba konvencióra) javított rajta, de nem eleget.

Visszalapozni így az **Előzmény** tabon lehet, a Nap szegmensen (5.16), és
a Live tetején egy **„‹ Tegnap" gomb** visz oda egy érintéssel. Ez az
egyetlen hely az appban, ahol egy tab a másikat állítja (`HistoryRequest` a
`MainTabView`-ban), és nem sérti a szabályt, ami a gesztust és a lefúrást
kivitte: az nem az volt, hogy „ne váltsunk tabot", hanem hogy ne történjen
olyan, amit nem kértél. Egy gomb, amin az áll, hova visz, és amitől a tabsáv
láthatóan átvált, pontosan azt csinálja, amit ígér. A fordítottját — hogy a
Nap szegmensen a máig előrelapozva az app magától a Live-ra ugorjon —
elvetettük, mert az egy „következő oldal" chevron, ami képernyőt váltana.

**Amit ez maga után vont:** a `MainTabView.liveHomeToken` elveszett (nem maradt
elnavigált állapot, amit vissza kellene hozni), a `DayState` háromállapotú lett
(5.7), és a `DrinkingDay.offset(by:)` / `daysAgo(from:)` a History ablakaié
lett (5.16).

### 5.12 Az italok saját sávot kaptak a görbe alatt

Az italikonok korábban a nulla vonalra annotált `PointMark`-ok voltak, vagyis a
plot **belsejében** ültek, a sáv alján. Két baj volt vele: ránézésre a
görbéhez tartozó adatnak látszottak, és nem tudtak megmutatni semmit az
`5.9`-es fogyasztási tempóból — pedig az adat ott van a modellben.

**A megoldás:** a `chartYScale` tartománya `−lane.span ... yMaximum`. A nulla
alatti rész nem a görbéé, hanem az italoké. Ugyanaz az időtengely — ez a
lényeg, az ikonoknak illeszkedniük kell a görbéhez —, de a görbe területén
kívül. Ezért van explicit `yTicks` a tengelyen: az `.automatic` felcímkézne egy
−0,2 ‰-et, ami értelmetlen leolvasás.

**A görbe fix 200 pt, a sáv lefelé nő.** Egy sűrű este így képernyőbe kerül, nem
olvashatóságba. A `laneLayout` first fit módon sorokba pakolja az italokat.
Soronként 24 pt, legfeljebb hat sor — afölött a chart magasabb, mint amennyire
hasznos, és ami nem fér bele, az az utolsó sorban átfedhet.

**Egy sor egy ivási szál, és az ütközés kérdése az idő, nem a képernyő.** Ami
időben nem folyik egybe, az egy sorba kerül, akármilyen közel van:

- 30 perces sör, utána fél órával egy másik → **egy sor**, sosem voltak
  egyszerre a kézben.
- 30 perces sör, utána 20 perccel egy másik → **egy sor**, mert a második
  felvitele már levágta az elsőt 20 percre (5.13), és a kettő így pont
  egymáshoz ér.
- 30 perces sör közben egy pálinka → **külön sor**, mert a sör közben tényleg
  a kézben volt.

**Az összevetés percre megy, nem másodpercre** (`overlapTolerance`, 60 s). Az
időtartamok egész percek, a képernyőn minden idő percre látszik, tehát egy
másodperces átfedés nem átfedés. Könnyű előállítani: egy 14:55:23-kor kezdett,
egy órásra állított sör 15:55:23-ig tart, a 15:55:10-kor felvitt következő pedig
tizenhárom másodperccel elbukik a teszten — és leesik egy sorral olyan okból,
amit a képernyőre nézve senki nem tudna megnevezni. A `pourCut` (5.13) az új
adatot pontosan egymáshoz igazítja, a tolerancia a korábban felvitt és a kézzel
szerkesztett soroknak kell.

A kétperces lábnyom csak arra van, hogy két azonos pillanatra felvitt ital ne
egymásra rajzolódjon — ezért kell hosszabbnak lennie a toleranciánál, különben
azt sem választaná szét. **Volt egy hibás kör**, amiben a lábnyomot a badge
szélessége adta: az telefonszélességen a látható ablak ~6 %-a, vagyis egy
hatórás estén 20 perc — így egymás alá kerültek olyan italok, amiknek semmi
közük nem volt egymáshoz. A képernyőméret nem dönthet arról, mi volt egyszerre.

**Ennek az ára:** hat feles öt percenként egy sorba kerül, és ott a badge-ek
átfedik egymást. Időrendben állnak, tehát sorozatként olvashatók, de ha ez
zavaró lesz, egy gyenge (a badge felénél ütő) másodlagos feltétel visszahozható.

- **Minden badge a valós idején áll.** Volt egy korábbi kör, amiben a badge-ek
  oldalra csúsztak egymás elől, és egy szaggatott vezérvonal adta vissza az
  igazi időt. A sor jobb: nem kell korrekción keresztül visszaolvasni semmit.
- **Egy sor egy objektum.** A rúd a kezdéstől az utolsó kortyig fut végjellel,
  a badge a kezdésen ül rajta. Aki egyben lehajtja, annak nincs rúdja — nulla
  hosszú rúd láthatatlan, egy csonkká kerekítve pedig olyan időtartamot
  állítana, ami nem volt. A tartam és a pillanat különbsége a rúd megléte.
- **A badge-ek egyformák.** A tempót a rúd mondja el; kétszer elmondani csak
  olyan jelentést aggatna a badge-re, amit nem bír el.

**Az oszlop a teljes chart magasságán átfut**, a görbe mögött és a sorokon
keresztül. Két dolgot csinál egyszerre: a görbén megmutatja, a felszálló ág
melyik szakaszáért felel az ital (enélkül a rúd csak egy hossz lenne,
összevetési alap nélkül), a sávban pedig ez a szemvonal — öt sornál egy alsó
rúd messze kerül az időtengelytől, és az oszlop mondja meg, melyik pillanathoz
tartozik. A kortyolt italnál halvány sáv, az egyben lehajtottnál szaggatott
vonal, mert egy pillanatnak nincs szélessége. Finomabb és halványabb, mint a
szintén szaggatott most-vonal, aminek hangosabbnak kell maradnia.

A jelmagyarázat csak azt a kettőt nevezi meg, ami épp a képernyőn van.

A `LaneLayout` **egyetlen menetben** számol, és a `chart` egy lokális
konstansba kéri le. Nem stílus kérdése: a `chartXSelection` minden húzási
mintánál újraértékeli a `body`-t, és külön computed propertykből a pakolás
markonként többször futna le, frame-enként.

### 5.13 A következő ital lezárja az előzőt — de csak azonos típusnál

A `drinkingMinutes` alapértéke típusonként fix (5.9): a sör 30 perc. Ha 20 perc
múlva új **sört** veszünk fel, akkor az előzőt nem 30 perc alatt ittuk meg,
hanem 20 alatt — a felvitel maga az információ, hiszen nem tartunk két sört a
kézben. Az `Array.pourCut(by:)` ilyenkor lerövidíti a megkezdett italt arra a
pillanatra.

**Típusra érzékeny, és ez a lényege.** Egy feles a sör közben semmit nem mond a
sörről; ha arra is rövidítenénk, kitalálnánk egy meredekebb emelkedést, mint
ami történt. A típus a `Drink.name`, vagyis a sablon azonosítója.

**Nincs alsó korlát.** Ha négy perccel később jön a következő sör, az előző négy
perces lesz. Ez utólagos, tömeges felvitelnél hamis meredekséget ad (négy sör
egymás után begépelve, mind „Most"-tal) — tudatos döntés, hogy a szabály
kivétel nélkül érvényes, és a felvitt időpontok helyessége a felhasználón áll.

**Amit tudni kell róla:**

- **Idempotens.** A levágott ital már nem tart a kérdéses pillanatig, így egy
  második futás nem talál semmit. E nélkül az `AddDrinkSheet` élő előrejelzése
  minden lépésköznél tovább csonkította volna az időtartamot.
- **A `project` ugyanazt a vágást alkalmazza**, mint az `add`. Nem kozmetika:
  e nélkül az Add gomb fölött vetített görbe nem az lenne, amit a gomb
  megnyomása után kapsz.
- **Csak `add`-nál.** Az előző időtartama **nem áll vissza**, ha a megszakító
  italt utólag töröljük vagy átidőzítjük — a 30 perc alapérték volt, és az app
  nem tart nyilván lecserélt alapértékeket. Mindkét soron szerkeszthető az
  időtartam, ez a kiút.
- Csendben történik; az itallistában látszik az új időtartam.

A szabály a `BACKit`-ben van, nem az app rétegben: `[Drink] -> [Drink]`, tiszta
függvény UI nélkül — és így tesztelhető (`PourShorteningTests`, 9 teszt).

### 5.14 A színskála a saját határhoz van kötve, nem abszolút szintekhez

A `Theme.tint(for:limit:)` a `bac / limit` arányt színezi, nem a ‰-értéket.
Öt megállóval, folytonosan: **0** türkiz → **0,55** borostyán → **0,85** korall
→ **1,00 teljes vörös** → **1,50 és fölötte** sötét bíbor.

**Miért nem abszolút.** A régi skála 0,5 ‰-nél váltott borostyánra és 1,3 ‰
fölött korallban állt meg — mindenkinek ugyanott. Ez a színt az ivásról
általában tett állítássá tette, nem erről az emberről szólóvá: aki 0,3 ‰-re
állította a határát, végig türkizben látta az estéjét, aki 1,2 ‰-re, az már jóval
a saját vonala alatt korallban volt.

**A teljes vörös pontosan a határon van.** Ez nem verdikt (2.): a határ a
felhasználó saját száma, amit ő írt be, és az app csak következetes vele — az
5.2-es háromállapotú figyelmeztetés ugyanerre a vonalra hivatkozik. Fölötte
tovább mélyül, hogy a „jóval túl" is látsszon, de a telített vörös pillanata a
határ.

**Amit ez maga után vont:**

- A `tint` minden hívója átad egy határt, és a `BACReadout`-on **kötelező**
  paraméter — nem alapértelmezett, mert egy elfelejtett érték csendben valaki
  más skáláját adná. Az Előzmény az adott alkalom saját határát adja át, nem a
  mait, ugyanazon az alapon, mint a profil-pillanatképnél (5.5).
- A chart sávgradiense a **csúcshoz** igazodik, nem a `yMaximum`-hoz. A
  `yMaximum` konstrukció szerint legalább a határ 1,4-szerese, tehát minden
  gradiens teteje sötét bíbor lett volna, egy csendes estén is.
- A `ProfileView` határcsúszkájának értéke fixen `Theme.alarm`. A saját
  szintjével színezni körkörös volna — a skála a határ törtrésze, tehát egy
  határ mindig pontosan 1,0. Így viszont szó szerint azt mondja: **ez az a
  szám, aminél a kijelző vörösre vált.**
- A charton a határvonal is `Theme.alarm`, nem korall. Ugyanaz a küszöb,
  ugyanaz a szín.

**Aminek tudatában kell lenni:** alacsonyra állított határnál (0,2–0,3 ‰) egy
sör is vörösre viszi a görbét. Ez a skála működése, nem hibája — de ha a határ
alsó vége miatt zavaró lesz, a megállók az egyetlen hangolandó dolog.

**Az Előzmény mennyiség-chartja más tengelyen színez: mennyiség szerint,
rögzített skálán.** Eredetileg a mennyiség-oszlop is a csúcs színét viselte
(„hosszú nyugodt este vs. rövid éles"), és ez napi szinten működött is — de
egy heti vagy havi oszlopnak nincs egyetlen csúcsa, és a hónap legrosszabb
estéje pirosra festett volna egy könnyű hónapot. Ezért mindkét chart azt
színezi, amit rajzol: a csúcs-chart a `tint(for:limit:)`-tel a saját határhoz,
a mennyiség-chart a `Theme.tint(forGrams:overDays:)`-szel egy **abszolút**
skálán. Két horgony, hónapra kimondva és napokra arányosítva minden más
tartományra: **100 g/hónap** alatt teljesen nyugodt, **2500 g/hónap** a teljes
vörös, fölötte sötétedik (megállók a vörös hányadában: 0,04 türkiz → 0,40
borostyán → 0,70 korall → 1,00 vörös → 1,60 bíbor). Az oszlop skálája mindig az
oszlop **ismert** napjaival arányos (`HistoryBar.knownDays`: rögzített napok +
a havi összegből ismert napok), hogy egy félig ismert hónap ne látsszon
csendesnek a hiány miatt. Ez a skála tudatosan *nem* a felhasználó saját száma
— ettől lesz két ember vagy két év chartja összevethető; a saját szokásos
hónaphoz mérés (medián) egy körig élt, és azért esett ki, mert az
egészségről semmit nem mondott. A havi összegből ismert hónapok is ezt a skálát
kapják, az Év nézetben oszlopként, a Hét és Hónap nézetben halvány sávként.

### 5.15 A gyors felvitelnek három belépési pontja van, de egy útja

A kedvenc ital felvitele (`SessionStore.quickAdd`) három helyről indítható:
a Live kapszulájáról, Siritől és egy widgetről. Mind a három ugyanazt a
store-műveletet hívja — a kedvenc, a pour cut (5.13) és az alkalomba
irányítás egyik útvonalon sem kerülhető meg. Prototípus (2026. október),
készüléken kipróbálva.

**Siri — `Support/LogDrinkIntent.swift`.** Egy `AppIntent`, ami az app saját
folyamatában fut a háttérben (`openAppWhenRun = false`): a `LogMyDrinkApp.init`
beregisztrálja a store-t az `AppDependencyManager`-be, az intent `@Dependency`
útján kapja meg. A `perform` előbb `tick()` + `refreshFromStore()` — az app
órákig ülhetett a háttérben, a `now` csak a Live timerrel mozog, és egy
éjszakán át nyitott alkalmat le kell zárni —, csak utána `quickAdd()`.
**Siri a vetített csúcsot mondja vissza**, nem csak „kész"-t: ez a termék
tézise (2.), és hangnál nincs kapszula, ami a színt vinné; a három szöveg a
`LimitOutcome` szerint ágazik (5.2). Az `AppShortcutsProvider` kifejezéseinek
kötelezően tartalmazniuk kell az app nevét, és az Apple szerint még
valamit — a csupasz név névleg az iOS saját „nyisd meg" parancsa. A
regisztrált kifejezések: **„LogMyDrink now"**, „LogMyDrink please" /
„Please LogMyDrink" (Siri a szórendre érzékeny, ezért mindkettő) és „Log a
drink in LogMyDrink". **A gyakorlatban (iOS 26, 2026. október) a puszta
„Hey Siri, LogMyDrink" is az intentet futtatja**, nem az appot nyitja: Siri
a csupasz nevet lazán ráilleszti a toldalékos kifejezésekre, és a mi
parancsunk nyer. Ez a felismerő viselkedése, nem dokumentált garancia —
amit az app *ígér*, az a toldalékos forma; a csupasz név bónusz, amit a
névválasztás kiérdemelt (1.). (Két kör tanulsága, mindkét irányban: előbb
azt hittük, a csupasz név regisztrálható — nem az —, aztán hogy sosem jut
el hozzánk — de eljut. A készülék dönt, nem a feltételezés.) Ha egy
iOS-frissítés elvenné, a Shortcuts appban egy, az app nevétől eltérő nevű
személyes parancs („Drink") ugyanezt adja, mert Siri a parancsot a nevén
futtatja. Siri magyarul nem tud, a kifejezések angolok. A widget felirata és a Shortcuts-csempe címe „Log My
Drink" (`Text(verbatim:)`, márkanév, nem fordul); az intent `title`-je
viszont „Log a drink" marad, mert az a Shortcuts appban egy *lépés* neve,
ott az ige a helyes, nem a márka.

**Widget — `LogMyDrinkWidget/`, külön target.** Egy gomb a zárolt képernyőre
(kör, téglalap) és a kezdőképernyőre (kicsi). A koppintás **nem helyben ír,
hanem megnyitja az appot**: `widgetURL` (`logmydrink://quick-add`, URL scheme
regisztráció nélkül, mert a `widgetURL` közvetlenül a tartalmazó apphoz jut),
a `MainTabView.onOpenURL` a Live-ra vált és egy `QuickAddRequest`-et ad át, a
Live ugyanúgy hajtja végre, mint a kapszulánál — a visszavonó sávval. Ugyanaz
a minta, mint a `HistoryRequest`. Azért nem helyben: a widget extension saját
folyamat, és ahhoz, hogy italt írjon, a SwiftData store-t App Group
konténerbe kellene költöztetni, ami a meglévő adatokat mozgatja minden
készüléken (a második kör a `TODO.md`-ben). Ára, hogy a koppintás feloldást
kér — az app megnyitása mindig kér —, és hogy a widget semmit nem mutat: se
számot, se szintet.

**Amit a widget mégis tud: a kedvenc ikonját.** `Support/WidgetBridge.swift`
az App Group közös `UserDefaults`-ába (`group.dev.zcsipler.logmydrink`) írja
a kedvenc SF Symbol nevét, és csak akkor tölteti újra a widgetet, ha az
változott; a `SessionStore` a `favourite` setterében és a `refreshFromStore`
végén hívja (indítás, előtérbe kerülés, személyváltás, import). App Group
nélkül a `UserDefaults(suiteName:)` privát tárolót ad, nem hibát — a widget
marad az általános pohárnál. **A logban minden indításkor ott egy
`Couldn't read values in CFPrefsPlistSource … group.dev.zcsipler.logmydrink
… kCFPreferencesAnyUser … detaching from cfprefsd` sor — ez ártalmatlan
iOS-zaj**, nem a hiányzó entitlement jele: a `cfprefsd` a csoport-konténerhez
egy rendszerszintű forrást is próbál felvenni, amit nem kap meg, és ezt
logolja; a felhasználói szintű forrás, amit használunk, rendben megy. A
bizonyíték az, hogy a kedvenc váltásakor a widget ikonja is vált. Egy kör
elment arra, hogy ezt hibának néztük. A kör méreten plusz van, nem ital: ott
az ikon nem olvasható, a plusz viszont megmondja, mit csinál a koppintás.

**Az iOS nem enged widgetet programból kitenni** — se Lock Screenre, se Home
Screenre, se Control Centerbe —, és a widgetgalériába mutató link sincs. A
használható megfelelője a push kérésnek: a `WidgetCenter.getCurrentConfigurations`
megmondja, ki van-e téve, és amíg nincs, az app egy elvethető kártyán
elmagyarázhatja a három lépést; iOS 18-tól a `WidgetRelevance` a Smart
Stackben előre forgatja. Ez és a `SiriTipView` a kapszula alatt a `TODO.md`-ben
van.

### 5.16 Előzmény — egy képernyő, memóriában aggregálva, lakattal

Megtervezve és megépítve 2026 szeptemberében, készüléken kipróbálva.
Apple Health-minta: szegmens-váltó **Nap / Hét / Hónap / Év**, chevronos
lapozás, a fejléc dátuma gomb a tetszőleges időszakra ugráshoz. A Trend
szegmens megépült, de csak debug kísérletként kapcsolható (lent).

**Nincs új tárolt entitás.** A `Model/HistoryAggregate.swift` memóriában
hajtja az alkalmakat napokra (`DayBucket`) és periódusokra (`PeriodBucket`),
a cache-elt `SessionSummary`-ból. Egy év néhány száz alkalom; egy második
`@Model` CloudKit-kompatibilis, exportált és migrált kellene legyen,
semmiért. Következmény: az export/import (5.17) változatlan, és a history egy
importált archívumból azonnal előáll.

**A mennyiség nem vár a motorra, a csúcs igen.** Egység és italszám az
italokból összeadható; a csúcs csak érvényes cache-ből jön, különben `nil`
(`HistoryOccasion.peakRange`), és a bucket `peakIsComplete`-je hamis.
Verzióbump után így az Év nézet nem futtat 365 szimulációt megnyitáskor. A
cache visszatöltése a store háttérmenete: `SessionStore.backfillStaleSummaries`
a `refreshFromStore` végén, ötvenes adagokban, a szimuláció `Task.detached`-ben
(a modellből `BodyProfile` + `[Drink]` Sendable bemenet készül a main actoron,
csak a visszaírás nyúl a contexthez), adagonként egy `save()`, és írás előtt
`isDeleted`-ellenőrzés (egy adag közben törölt alkalomra írni crash). Korábban
ötösével, a main actoron futott: egy hatéves import (~1300 alkalom) ~260
mentést és ugyanannyi teljes újraaggregálást jelentett, az app percekig
szaggatott. Érvénytelen cache-nél a csúcs-oszlop **hiányzik**, nem nulla.

**A napi aggregátum cache-elt:** `HistoryAggregateCache` a `HistoryView`
`@State`-jében, kulcsa `SessionStore.revision` (minden `save()` és
`refreshFromStore()` lépteti) + személy + `trackingStartedAt` + az aktuális
ivási nap. Enélkül a `snapshot` minden body-kiértékelésnél végigment az összes
alkalmon és a `drinks` relációikon.

**„Nem ittál" és „nem tudjuk" itt válik láthatóvá (5.7).** `DayBucket.State`:
`drank` / `dry` / `unknown`; a `Person.trackingStartedAt` előtti nap `unknown`,
és nem számít bele az átlag nevezőjébe (`recordedDays`). A rögzítés kezdete a
tárolt dátum és a **legkorábbi alkalom napja** közül a korábbi — egy felvitt
este bizonyíték, hogy akkor már rögzítettünk (`Person.backdateTracking`;
`SessionStore.reconcileTrackingStart` minden `refreshFromStore`-nál rendbe
teszi, mert az `add` csak új italra ellenőriz, a migráció, az import és a
szinkron nem megy át rajta). Így az ismeretlen napok mindig egy összefüggő
szakasz az ablak elején. A dátum *nem* vezethető le pusztán a bejegyzésekből:
aki telepítés után hat napig nem iszik, annak az a hat nap ivásmentes, nem
ismeretlen. Szabály: `min(első indítás, legkorábbi bejegyzés)`. A rögzítés
előtti napok halvány sávot kapnak, mert az üres az „ivásmentes" jele; a sávban
felirat („No data before <dátum>"), ha a sáv az ablak legalább harmada.

**A nap a saját dátuma alá kerül, a hét / hónap / év a naptáré.** A hajnali
5-kor kezdődő ivási nap a `calendarDate`-jével kerül hétbe és hónapba, tehát az
éjfélen átnyúló este abban a hétben marad, amelyikben kezdődött. A hét
kezdőnapja a `Calendar`-ból jön. Az x-tengely éjfélhez igazított, különben a
hét első oszlopát 5 óra levágná.

**`HistoryWindow` a modell**, `HistoryAggregate.days` kimenetéből: oszlopok
`drank / dry / unknown / future` állapottal, összegek, változás az előző
ablakhoz. A Hét az utolsó hét ivási nap, a Hónap és az Év naptári egység;
oszlop = nap (Hét, Hónap) vagy hónap (Év). Szegmensváltás a legújabb oldalra
ugrik. A dátum → oldal leképezés `HistoryWindow.offset(containing:)`, naptári
egységben számolva (Aug 15 egy hónap-oldallal Sep 14 előtt van, pedig nem
telt el harminc nap). Volt rajta mozgóátlag-vonal; kivettük, mert a magas
oszlopok mögé bújt, és egy hét hét pontjából nem olvasható ki trend.
**Oszlopról nem fúrunk le**: volt (Év-oszlop → hónap, hónap-oszlop → hét,
második koppintásra), de a képernyő „magától" váltott tőle — a szegmens csak a
szegmens-váltóról változzon.

**A mennyiség grammban vagy standard egységben**, a felhasználó választása
szerint (`AmountUnit`, az `AppSettings`-ben a ‰ / % mellett). Alapból gramm:
egy gramm mindenhol ugyanaz, az „egység" országonként más (8 g UK, 10 g HU,
12 g FR). A modell továbbra is standard egységben számol
(`Drink.standardUnits`), a kettő ×10 — ezért nem mutatjuk mindkettőt egymás
mellett. Egy helyen érvényes mindenhol: History chart, mutató-kártya, Live és
alkalom stat-sor.

**Két chart-kártya egymás alatt: mennyiség, majd csúcs.** Nem váltó és nem
kettős tengely: a két mérőszám egy pillantással összevethető, és a
vonal-oszlopok-mögé-bújás nem jön elő. Az oszlop magassága a mennyiség (a
tengely felírja, miben), színe az 5.14 szerint. A csúcs-chart oszlopa a nap
legmagasabb szintje (a sáv közepe; a buborék tartományt ír, ha a sáv széles,
5.8), rajta a saját határ szaggatott vonala. Koppintásra az oszlop fölött a
pontos érték; a találat a legközelebbi ivós oszlopra pattan 16 pont tűréssel,
mert a hónap oszlopai pár pont szélesek. Az Év hónapcímkéi a locale
rövidítéséből jönnek, három betűre vágva — egy betű nem volt olvasható.

**A mutató-kártya** első sora négy szám: mennyiség, italok, „Sober days"
(`ivásmentes / rögzített`, alatta a rögzítés előtti napok száma, amíg van ilyen
— az évben a „4 / 9" magyarázat nélkül érthetetlen), és a csúcs. A második sor
a változás az előző ablakhoz, alatta halványan, hogy melyikhez („vs. Sep
8–14"): egy „+239 %" magában vádnak hangzik, viszonyítási alappal
összehasonlításnak.

**Lakat — `Feature.historyTrends`, ingyenes ablakkal.** Az utolsó
`FeatureFlags.freeHistoryWindowDays` (7) ivási nap — a mai is beleértve —
ingyenes, ami régebbi, lakat mögé kerül, az alkalom-sorokra is. A nézet egy
kérdést tesz fel: `flags.canShowHistory(for: DrinkingDay)`; az
`isWithinFreeWindow` a napokból következik, nem állítjuk — a Hét 0. oldala az
egyetlen ingyenes ablak, konstrukció szerint. A flag a UI-t takarja, az adat
mindenkinél íródik (5.18 mintájára): aki fél év után fizet, a teljes fél évet
látja — a paywall mondja is ki. A mutatók és a két chart együtt homályosodnak,
rajta egy gomb a `HistoryPaywallSheet`-re; a 7 napnál régebbi alkalom-sor
dátuma látszik, a csúcsa nem. StoreKit nélkül a gomb debugban a flag
override-ját állítja, release-ben „Coming soon".

**Ugrás tetszőleges időszakra: a fejléc dátuma gomb** (`HistoryJumpSheet`), a
Naptár app mintájára. A chevronok maradnak a szomszédos oldalra — a kettő nem
versenyez, más a szándék mögöttük. A lap a szegmenshez illő választót ad: Nap
és Hét → grafikus naptár (a koppintás maga a választás), Hónap → év-léptető és
3×4 hónaprács, Év → évlista; mindegyiken „Today". Csak a rögzített időszak
van felkínálva. Külön „ettől eddig" szűrő nincs; ha egyszer kell, a
`HistoryRange` kap egy `.custom(DateInterval)` esetet, és ugyanez a képernyő
szolgálja ki.

**Nap szegmens.** Egy oldal egy ivási nap, a mai a 0. oldal, az előre chevron
ott letiltva. Tartalom: a nap lezárt alkalmai `SessionContentView`-val, a mai
oldalon fölöttük a futó alkalom — a Live-val azonos módon szerkeszthető. Nincs
mutató-kártya és nincs chart: a nap maga a tartalom. Üres napon a három eset
az 5.7 szerint szétválik: „Nothing logged today", „No drinks on this day",
„No data before <dátum>". A `HistoryRange` kapott egy `.day` esetet, ezért a
lapozás, az `oldestOffset`, az ugró lap és az ingyenes-ablak szabály mind
ugyanaz a kód — külön naplapozó nincs. A History megjegyzi az utolsó
szegmenst; a Live „‹ Tegnap" gombja (5.11) a Nap / 1-es oldalra kéri
(`HistoryRequest`), amit a `HistoryView` `onAppear`-kor és a kérés
változásakor alkalmaz, aztán töröl — az első tabváltáskor a nézet még nem is
létezik, ezért kell mindkettő.

**Utólagos felvitel a Nap oldalon.** A kihagyott nap ezen az oldalon látszik
meg, ezért a pótlás is itt van, nem a Live dátumválasztóján italonként
visszatekerve. Ugyanaz a lebegő „Add drink" kapszula, mint a Live-on
(`AddDrinkCapsule`, közös a `QuickAddBar`-ral), lakatolt napon nem. Üres napon
a kapszula sincs: ott az üres-állapot kártya gombja az egyetlen felvitel — két
azonos gomb egy képernyőn zaj volt; a rögzítés előtti napra felvitt ital
bizonyíték, a `backdateTracking` viszi vissza a kezdetet. Volt egy kör,
amiben a gomb az itallista alatt ült: egy valós estén a chart, a stat-sor és a
lista a fold alá tolta, pont ott, ahol a legtöbb ital van. Múltbeli napon az
`AddDrinkSheet` kapja a napot (`day`): az idő szekció a lap **tetejére** kerül,
a típusválasztó elé (pótlásnál a típus a szokásos, az idő az egyetlen, amit
biztosan be kell írni), és rögtön a görgethető (`.wheel`) választó áll ott.
*Azóta az idő minden módban ugyanott van, a tempó mellett, léptetővel; a
kerék koppintásra nyílik (5.20).* **Csak óra–perc kerék, dátumoszlop
nélkül:** a napot az oldal már kimondta, és a dátumoszlop egy 01:43-as italra
„Today"-t írt volna a Tegnap feliratú oldalon — az ivási nap belső
éjfél-képe, ami a felhasználót nem érdekli. A kerékről vett időt a lap maga
helyezi el a napon az 5.6 szabályával (`timeOnDay`), a „When" fejléc jobb
oldalán a kapott naptári dátum. **A kerék a mostani óra-percen áll, a napra
helyezve** — az iOS dátumválasztók konvenciója, átlátszó szabály. Volt
okosabb (az utolsó ital vége, üres napon 20:00), de a képernyőn egy 01:13-as
ital + 30 perc „01:43"-ként jelent meg, levezetés nélkül, véletlen számnak
látszott. A kiindulópontnak nem jónak kell lennie, hanem nyilvánvalónak.
**Ami emiatt változott a store-ban:** a `project` cél nélkül nem a nyitott
alkalomhoz, hanem — az `add`-dal azonos szabállyal — az ital napját fedő
alkalomhoz vetít, ha nincs, üres estéhez a `profileApplicable` profiljával; a
napra szóló irányítást a `lastRouting` tartja meg a következő írásig
(`rebuild` törli), mert a lap body-ja csúszkahúzás közben kilencszer kérdez,
és a fetch nem fér bele egy frame-be. Ez a Live-on „Set exact time"-mal
tegnapra állított italt is kijavítja.

**Trend szegmens — megépítve, de csak kísérlet (`Experiment.trendSegment`).**
A teljes rögzített időszak egy görbén, vízszintes görgetéssel és
csippentés-zoommal (14 nap és 10 év között); nem oszlopok, mert a hónapok
összemosnak. Külön típus (`HistorySegment`), nem ötödik `HistoryRange`: a
range-nek oldalai és periódusonként oszlopa van, a trendnek egyik sem. Két
kártya közös zoommal: **mennyiség** — a napi gramm exponenciális mozgóátlaga
(EMA; egyszerű mozgóátlagnál egy nagy este N nap múlva lépcsővel esne ki;
szimmetrikus simításnál a görbe vége utólag mozogna), felezési idő a zoomhoz
kötve (7 / 30 / 90 nap), ivásmentes napon süllyed, nem zuhan; **csúcs** —
csak az ivós napokra, alkalomról alkalomra lépő EMA, két este között
vízszintes. Zoltán döntése: a csúcs-trend azt mutassa, „amikor iszol, milyen
magasra mész"; ha minden napra átlagolnánk, a gyakoriságot és az intenzitást
összekevernénk. A görbe a **mai** határhoz színezve, mert a kérdés az, hogy a
múlt hogyan áll a most tartott vonalhoz. Készüléken nem volt az igazi (a
görbék furán olvastak), ezért a szegmenst a Profil alján lévő Experiments
kapcsoló teszi a pickerre (`HistorySegment.offered(trend:)`). Két hiba
javítva: a pattogás (a chart akkor is görgethető volt, amikor kifért →
`isScrollable`, és a megosztott görgetési pozíció a tartományba szorítva), és
a tengelycím (a `chartYAxisLabel` görgethető chartban a tartalommal együtt
mozgott → sima nézet a plot fölé). Az újragondolás a `TODO.md`-ben.

**Tesztek:** `HistoryAggregateTests` (17), `HistoryWindowTests` (14),
`HistoryTrendTests` (6), `MonthlyTotalTests` (20, ebből 2 SwiftData-s). A
`LogMyDrinkTests` targetben futnak (10.); Foundation-only, ezért egy
ideiglenes csomagban Linuxon is lefutottak, Swift 6 módban,
figyelmeztetés nélkül.

### 5.17 Adatmentés: JSON export / import, és CloudKit-szinkron — bekapcsolva

**A követelmény:** ha Zoltán készüléket vált ugyanazzal az Apple ID-val, az
adatok ne vesszenek el. Ez nem opcionális kényelem.

**A döntés (2026. szeptember): iCloud / CloudKit private database, saját
login és regisztráció nélkül.** A Sign in with Apple *identitás egy saját
backendhez*; a CloudKit *szinkron*, bejelentkező képernyő nélkül, a
felhasználó iCloud-kvótáján. Amiért ez nyert: nincs szerverünk, ami
alkoholfogyasztási adatot tárol — ennél az appnál ez termékérv is (2., 9.).
Ára, hogy Androidra és webre nem vihető át, és megosztást nem támogat; ha
egyszer kell, akkor jön a saját backend, külön fázisban.

**Ami a kódban megvan:** a séma CloudKit-kompatibilis (8.);
`LogMyDrinkApp.makeContainer()` CloudKit ág `.private(cloudKitContainerID)`-vel,
lokális fallbackkel és debug-assertionnel; a kétszeres tulajdonos elleni
dedupe (`PersonMigration.resolveOwner`, a korábbi `createdAt` nyer, a
`merge(_:into:)` átviszi a másik alkalmait); `SessionStore.observeRemoteChanges()`
az `NSPersistentStoreRemoteChange` értesítésre 500 ms-os debounce-szal —
enélkül egy másik készüléken felvitt ital megjelenne a `@Query`-s listában, de
a görbe nem rajzolódna újra, mert a `band`-et csak a `rebuild()` mozgatja.

**A kapcsoló: `BuildCapabilities.cloudSync`** (5.19) — **`true` 2026.
október 7. óta.** Az egyéni Apple Developer Program tagság október 6-án
aktiválódott; az iCloud (CloudKit, konténer `iCloud.dev.zcsipler.logmydrink`)
és a Background Modes → Remote notifications capability a targeten van, az
`aps-environment` és az iCloud-kulcsok a `LogMyDrink.entitlements`-ben, az
`UIBackgroundModes` egy valódi `LogMyDrink/Info.plist`-ben (az Xcode hozta
létre, mert a generált plist ezt a kulcsot nem tudja; a generálás mellette
megy tovább). **Készüléken bevált:** a meglévő lokális store helyben állt át
tükrözésre, az első export a `CD_*` rekordtípusokat létrehozta a
Development környezetben, és az app törlése-újratelepítése után az adat a
felhőből visszajött. A Console-ban a rekordok a
`com.apple.coredata.cloudkit.zone` zónában vannak, és a lekérdezéshez a
`recordName`-re kézzel kell QUERYABLE indexet tenni (Schema → Indexes) — ez
csak a böngészéshez kell, az appot nem érinti. A logban két ártalmatlan sor
marad: a `cfprefsd` App Group-zaja (5.15) és debugger alól futva egy
`BGSystemTaskSchedulerErrorDomain Code=3` az exportra — az export ettől
előtérben lefut.

**Ami ehhez kellett (Personal Team alatt lehetetlen volt):** az iCloud
capability Personal Team alatt meg sem jelenik a `+ Capability` listában;
kézzel írt entitlements sem kerüli meg, mert a provisioning profile nem
tartalmazná. A lépések, ahogy végigmentünk rajtuk — egy új készüléken vagy
teamen ugyanez a sorrend:

1. **Előbb mentés:** Xcode → Devices and Simulators → LogMyDrink → Download
   Container. A team váltása új aláírást ad, az iOS törli és újratelepíti az
   appot a helyi adatokkal együtt; ugyanez a menü tud Replace Containert.
2. developer.apple.com → a Program License Agreement elfogadása (amíg függ,
   az Xcode nem lát capabilityket).
3. Xcode → Settings → Accounts → Download Manual Profiles, a targeten az új
   team.
4. + Capability → iCloud → CloudKit, konténer `iCloud.dev.zcsipler.logmydrink`
   (ha az Xcode mást hoz létre, a `LogMyDrinkApp.cloudKitContainerID`-t kell
   igazítani).
5. + Capability → Background Modes → Remote notifications, különben a szinkron
   csak app-indításkor mozdul.
6. `BuildCapabilities.cloudSync = true`.
7. Futtatás **előbb a készüléken**, a meglévő adatokkal: itt dől el, hogy a
   lokális store átáll-e tükrözésre; a rekordok a CloudKit Console Development
   környezetében jelennek meg. Ha az assertion store-inkompatibilitásra hasal
   el: törlés, újratelepítés, Replace Container.
8. Csak ezután a második készülék / szimulátor (ott a push megbízhatatlan,
   háttérbe-előtérbe kell tenni az appot).

Ellenőrzés: keletkezett-e `.entitlements` fájl.

**9. — és ez elment egy délutánra: a widget extension profilja.** A team
váltása után a `LogMyDrinkWidgetExtension` **eltűnt a widgetgalériából**
(kezdőképernyő és zárolt képernyő egyaránt, a kereső sem találta),
miközben a szimulátorban ott volt, crash-log nem keletkezett, a projekt és a
`codesign` is rendben volt. Az ok: az app target az iCloud miatt új profilt
kapott, a widget targeté viszont **a Personal Team idejéből származó
7 napos profil maradt** — az iOS egy fizetős teammel aláírt appban az
ingyenes profillal aláírt kiterjesztést csendben nem regisztrálja. A
nyom: `security cms -D -i …appex/embedded.mobileprovision | grep -A1
ExpirationDate` — egy Xcode-kezelt fizetős profil egy évig él, a 7 nap az
ingyenes tier jele. Két csapda, ami késleltette: az Xcode-kezelt profilok
**nem látszanak** a developer.apple.com Profiles listáján, tehát ott nincs
mit törölni; és az Xcode 16 óta a lokális cache **nem**
`~/Library/MobileDevice/Provisioning Profiles/`, hanem
`~/Library/Developer/Xcode/UserData/Provisioning Profiles/` — a régi helyen
törölni semmit nem csinál. A javítás: az új mappából a `.mobileprovision`
fájlok törlése, Clean Build Folder, ⌘R az **app** scheme-mel; az Xcode
mindkét targetre újat generál. Tanulság: team-váltás után **minden**
target profiljának lejáratát ellenőrizni, nem csak azét, amelyik
capabilityt kapott.

**Amibe egyszer belefutottunk:** a `makeContainer()` eredetileg
`cloudKitDatabase: .automatic`-kal ment, és a `catch` ágban volt egy
assertion. **Nem jelzett.** Az `.automatic` entitlement nélkül egyszerűen
lokális store-t nyit, és nem dob — így a `catch` sosem futott le, és egy
teljes tesztkör ment el egy olyan buildre, amiben nem is volt CloudKit. Ezért
van a konténer néven megadva: a hiányzó entitlement, az elgépelt azonosító és
a nem birtokolt konténer így mind dob.

**Export / import — megépítve**, a CloudKit előtt, mert a tagságtól
függetlenül megírható, és mire a szinkron bekapcsol, van védőháló és
ellenőrzési eszköz (két készülékről exportálva a fájlok összevethetők). Nem
csak az Apple ID váltás miatt: az iCloud nem biztonsági mentés (a felhasználó
törölheti, és nincs kuka), a lokális ágon ez az egyetlen átviteli mód, egy
elrontott migráció után ez a visszaút, és adathordozhatóság (GDPR 20. cikk).
Fájlok: `DataArchive`, `ArchiveExport`, `ArchiveImport`,
`Support/ArchiveDocument.swift`, `View/DataTransferSection.swift`.

- **JSON, nem store-fájl másolat.** A `.sqlite` SwiftData/CloudKit
  metaadatokat visz, és verziók között nem stabil. Fejlécben `schemaVersion`
  és `exportedAt`.
- **Amit exportálunk:** `Person`, `DrinkingSession` (a profil-pillanatképpel),
  `DrinkRecord` minden tárolt mezője, és a `MonthlyTotal` sorok a
  `monthlyTotals` kulcs alatt (opcionális, ezért marad a `schemaVersion` 1).
  Ugyanaz az elv, mint 5.5-nél: a bemenet megy bele, nem a görbe.
- **Amit nem:** a `cachedPeak*` / `cachedSoberAt` / `cachedEngineVersion`
  mezők — újraszámolhatók, és egy másik verziójú buildbe importálva
  hazudnának. Az `AppSettings` sem, az a készüléké.
- **Import: merge `id` alapján, idempotensen.** Ismeretlen id bejön, ismert
  marad. **A meglévő alkalom egészben marad ki, az italaival együtt**:
  italonként összefésülni azt igényelné, hogy eldöntsük, melyik oldal nyer egy
  eltérő időpontú italnál, és erre nincs becsületes szabály, mert nem tároljuk,
  melyik szerkesztés volt később. A kihagyás egy mondatban elmondható, ami egy
  visszafordíthatatlan műveletnél követelmény.
- **Az `isOwner` ütközés a `PersonMigration.merge(_:into:)`-n keresztül** —
  ugyanaz a probléma, mint a CloudKit-race, ugyanaz a szabály.
- **`assign(to:)`-on keresztül** íródik a `person` kapcsolat és a `personID`,
  különben a `@Query` nem találja meg a behozott alkalmakat. Import után egy
  `refreshFromStore()` elég: a `closeEndedSessions` a régi „nyitott" importált
  estét magától lezárja.
- **UI:** `DataTransferSection` a Profil alján. Az import előbb tervet készít
  (`ArchiveImport.Plan`), és a megerősítő ablak abból mondja meg, mi fog
  történni — utána ír csak.
- **Fájlformátum `.json`, nem saját UTI.** Egy privát típus minden más app elől
  elzárná a fájlt — egy mentésnél, aminek az a dolga, hogy elhagyja az appot,
  ez rossz csere. A verzió a fájlon belül van.

Tesztek nincsenek rá — ez a kód nem crashel, csak rossz emberhez tesz egy
alkalmat. A `LogMyDrinkTests` target már megvan (10.), a lefedés a `TODO.md`-ben.

### 5.18 Több személy — megépítve, flag mögött

Egy estén belül át lehessen váltani másik emberre, és oda is felvinni az
italokat. Megépítve 2026 szeptemberében, `FeatureFlags.multiPerson` mögött.

**A váltás globális, és naponta visszaáll a tulajdonosra.** Mindhárom tab az
aktív személyt mutatja. Egy mentális modell van, nem kettő, és a vendég
testadatai ugyanott állíthatók, ahol a tieid. A legvalószínűbb hiba, hogy
este átváltasz és reggel elfelejted — ezért az aktív személy visszaáll, ha a
váltás nem a mai ivási napon (5.6) történt. A váltás időbélyegéből, nem
„hideg indítás" detektálásból: a háttérből visszatérés nem zavar, egy esti
app-kilövés nem veszíti el a kontextust, reggel viszont magától te vagy.

**A flag a UI-t takarja, nem a sémát.** A `Person` entitás és a migráció
mindig lefut; csak a váltó, a személy-felvitel és a személyenkénti szűrés van
flag mögött. Ha a séma is flag alatt lenne, a bekapcsolás migrációt igényelne,
a kikapcsolás elrejtené egy létező személy adatait — két adatállapotot kellene
karbantartani.

**Séma.** A `Person` viszi, ami személyenkénti: testadatok, gyakoriság, saját
határ, `trackingStartedAt`. Az `AppSettings` a mértékegységekre és az aktív
személy azonosítójára fogy le. A `DrinkingSession` kap `person`
kapcsolatot **és** denormalizált `personID`-t: a `@Query` skalárra tud szűrni,
opcionális kapcsolaton át nem megbízhatóan. A kettő egy helyen íródik.

**Migráció.** `PersonMigration.run(in:)`: ha nincs tulajdonos, létrehoz egyet
referencia-testalkattal (`makeOwner`, 80 kg / 180 cm / 35 év férfi, a
gyakoriság a béta alapértékéhez igazítva), majd minden gazdátlan alkalmat
hozzá rendel. **Volt két régebbi forrás is** — a SwiftData előtti app
`UserDefaults`-beállításai és este-blobja (`LegacyProfileSettings`,
`LegacySessionImport`), amikből a tulajdonos a felhasználó tényleges
testadatait örökölte —, de a névváltással a bundle ID is változott (1.), és
az új sandboxban ezek a kulcsok sehol nem létezhetnek. A két olvasó 2026
októberében kikerült; a kivett kód a `c780601` commitban még megvan.
**Nincs „már lefutott" marker**, szándékosan: a védelem maga az adat —
tulajdonos csak akkor jön létre, ha nincs, a söprés csak gazdátlan alkalmakhoz
nyúl. Egy marker rossz lenne, mert CloudKit mellett egy régebbi készülékről
érkező alkalom a marker beállítása **után** is befuthat, és sosem kapna gazdát.
Két lekérdezés induláskor az olcsóbb hiba. Két készülék az első szinkron előtt
két tulajdonost hozhat létre — ezért a dedupe-lépés induláskor (5.17).

**Store.** Egy `SessionStore` marad, `switch(to:)`-szal újrapontozva. Négy
hely, ahol több emberrel a régi kód csendben rossz adatot csinált volna:
`fetchOpenSession` és `sessionCovering` (a visszamenőleg felvitt italod a
másik ember alkalmába eshetne), `profileApplicable(at:)` (az ő testalkatát
fagyasztaná a te alkalmadba), `closeSessionIfEnded` (több nyitott alkalom van,
a nem aktívé örökre nyitva maradna — a `refreshFromStore` az összesen
végigfut), és a két `@Query`.

**UI (`PersonSwitcher.swift`).** A váltó egy chip — monogram, név, chevron —,
**nem a heróban, hanem a Live tartalom tetején**: a hero csak futó alkalomnál
van a képernyőn, a legvalószínűbb pillanat viszont, amikor valakit fel akarsz
venni, egy üres nap. Az Előzmény és a Profil toolbarjában ugyanez a chip —
enélkül semmi nem mondaná meg, kinek a testadatait írja a Profil. A hozzáadó
lap név, nem, súly, magasság, kor: mind a négy testadat alakítja a görbét,
egyiket sem tippeljük meg; a gyakoriság és a határ alapértékkel megy. A chip
kap személyre szabott színt (`PersonAccent`), a görbe **nem**: az a limithez
viszonyított skála (5.14), és két színrendszer egy képernyőn olvashatatlan.

**Személyek listája és vendég eltávolítása (`PeopleView`,
`SessionStore.removePerson`).** A Profilon egy „People" sor nyit egy listát:
tulajdonos az élén, vendégek alatta, pipa a kiválasztotton, alul „Új személy".
Vendég balra húzással vagy Edit módban távolítható el; a tulajdonos során
nincs húzás (`deleteDisabled`) — egy gesztus, ami mindig nemet mond, rosszabb,
mint a hiánya. Nem a váltó menüjében, mert az mindhárom tabon egy
hüvelykujjnyira van, és egy destruktív menüpont ott egy véletlen koppintásra
visz el egy évet. A húzás kérdez: a megerősítő ablak (`removalPlan(for:)`)
kimondja, mi megy vele — alkalmak, italok, havi összegek —, mert visszavonás
nincs. Cascade törlés: alkalmak és italok a relációk szabályán, a havi
összegek kézzel (id-vel hivatkoznak). Ha az aktív személyt töröljük, a
tulajdonos veszi át. Archiválás nincs: aki a vendég adatait meg akarja
tartani, előtte exportál.

**Tesztek:** `PersonMigrationTests`, `SessionRoutingTests`,
`ActivePersonTests` a `LogMyDrinkTests/` alatt — a teszt targetben futnak (10.).

### 5.19 Háromféle kapcsoló: Feature, Experiment, BuildCapability

`Support/FeatureFlags.swift` az egyetlen hely, ami eldönti, mi van bekapcsolva;
a nézetek csak kérdeznek (`flags.multiPerson`, `flags.canShowHistory(for:)`).
Három fajta van, és nem cserélhetők fel:

- **`Feature`** — amit a felhasználó *megvásárol*. Release-ben az
  `isPurchased`-re esik (ma mindig hamis, StoreKit nincs mögötte — ez az
  egyetlen hely, ahova a jogosultság-lekérdezés majd bekerül), debugban a
  Profil „Developer" szekciójában kapcsolható. Ma: `multiPerson` (5.18),
  `historyTrends` (5.16). Az alapfunkció a Live, az mindig ingyenes. A flag a
  UI-t takarja, az adat mindenkinél íródik.
- **`Experiment`** — ami megépült, de nem elég jó a menübe. Release-ben nem
  létezik. Szándékosan nem `Feature`: az `isPurchased`-re esne, és a StoreKit
  megérkezésekor eladóvá válna. Ma: `trendSegment`.
- **`BuildCapabilities`** — fordítási idejű konstans, amit a target
  entitlementje vagy hordoz, vagy nem. Ma: `cloudSync` (5.17). Nem `Feature`,
  mert a szinkront nem veszi meg senki; nem futásidejű, mert kapcsoló nem tud
  entitlementet előállítani, és a store egyszer nyílik meg induláskor.

### 5.20 Az ital ideje és tempója: két léptető egymás mellett

2026. október. Az `AddDrinkSheet`-en a leggyakrabban módosított mező nem a
típus vagy a mennyiség — az a legtöbb embernél az alapértéken marad —,
hanem a **kezdési idő**: az italt jellemzően húsz perccel a kezdés után
jut eszünkbe felvinni. Addig a „When" a lap alján ült, három csúszka
alatt, és a húsz perc beírásához a „Set exact time" dátumválasztójáig kellett
görgetni.

**A sorrend:** Type → Amount → Strength → **[When | How fast]** → Stomach.
Elöl az ital leírása (a típus marad az első, mert másnak az az első kérdés,
5.10), utána a két időbeli tényező **egy sorban, egymás mellett**, mert
ugyanarról szólnak — az ital időbeli lenyomatáról —, végül a gyomorállapot,
mert ritkán mozdul el a „moderate"-ről, és a gyors felvitel nyugtáján utólag
is állítható. Volt egy kör, amiben a When legfelülre került: Zoltán
visszavette, az ital leírása előrébb való, az idő a tempó mellé.

**A vezérlő egy léptető (`TimeStepper`), nem chip és nem csúszka.** Két
kör tanulsága. A chipek (*15 · 30 · 60 perce*) választásnak látszanak, pedig
az idő folytonos, és a köztes értékekért a kerékhez kellett nyúlni. Egy
köztes kör eltolás-chipeket próbált (*−10 · −20 …*, összeadódva): a −30 majd
a −10 negyven perc lett volna két koppintással, de egy chipsor kijelölésnek
olvasódik, nincs kijelölt állapota, és nem látszik rajta, hol tartasz —
Zoltán rá is kérdezett, hogy a halmozódás szándékos-e. A csúszka pedig
percekre túl finom, és egy egész sort visz. A léptető a becsületes vezérlő a
„kicsit korábban"-ra: középen az érték — ez maga az állapot, nem kijelölésből
kell visszaolvasni —, két oldalt − és +, fél sor széles, ezért fér el kettő
egymás mellett.

- **Állandó 5 perces lépés, nyomva tartásra gyorsuló ismétlés** (450 ms
  után 200 ms-onként, lépésenként 15 %-kal gyorsulva 50 ms-ig). Nem a
  távolsággal növekvő lépésköz: az az ujj alatt változna, és a határain
  aszimmetrikus (55 perc kifelé elérhető, visszafelé nem). A gyorsuló
  ismétlés a `UIStepper` saját viselkedése, nem kell megtanulni. Az első
  ismétlés elég későn jön, hogy egy szándékos koppintás sose duplázzon.
  `RepeatButton`: nulla távolságú `DragGesture`, mert a `Button` nem tudja
  megmondani, mikor emelik fel az ujjat.
- **Rácsra lép** (`TimeStep.snapped`): egy 23 perces pour cut vagy egy
  21:28:37-es ital az első koppintásra kerek értékre kerül, nem viszi
  magával a páratlan maradékot.
- **A When + gombja a „most"-nál letiltva** — jövőbe nem lehet felvinni, és
  ez mondja ki, hogy a jelen a felső határ, külön „Now" gomb nélkül. A −
  gomb lefelé korlátlan live-on és szerkesztésnél: a hajnali ötös határ nem
  fal, fél hat előtt egy órával még az előző este van, és a store oda is
  irányítja. Pótlásnál a nap eleje és vége a két határ.
- **Felirat alatta:** a mai napon „20 perce" (a `relative` formázó), mert az
  eltolást fejben összeadni ugyanaz a munka, amit a léptető le akar venni;
  más napon a naptári dátum, az egyetlen dolog, amit egy óra–perc nem mond
  el. A How fast alatt a tempó magyarázata marad (5.9).
- **A How fast-on 0 = „In one go"**, ott a − letiltva; a felső határ 180
  perc. A típusonkénti alapérték (5.9) és a pour cut (5.13) változatlan. A
  kedvenc-szerkesztő ugyanezt a `DrinkPaceControl`-t használja.
- Lépésenként `.selection` haptika, hogy tartás közben érezni a tempót.

**A mennyiség és az alkoholfok is léptető (`DrinkMeasureControls`), egy
sorban, a két időmező mintájára.** Zoltán érve döntött: a mennyiség nem
választás egy listából — otthon 220 ml bor megy a pohárba, egy hordóból
akármekkora pohárba töltögetünk, az 5 cl-es feles háromnegyedig van —, tehát a
chipek („ezek közül válassz") rossz vezérlők voltak rá, a csúszka pedig tíz
milliliterre se olvasható, se eltalálható nem volt. Egy köztes javaslat a
chipeket megtartotta volna a léptető mellett gyors ugrásnak (500 ↔ 330); nem
kellett, mert a típus alapértéke eleve a leggyakoribb méret, a szokásos italt
pedig a kedvenc viszi a gyors felvitelen — a lap maga a nem szokásos esetre
van. A lépésköz a sablonból jön (`DrinkTemplate.volumeStepMl`: tömény 5 ml,
minden más 10 ml), az alkoholfoké 0,5 %, a tartomány a sablon `abvRange`-e és
10–1000 ml. A `volumeOptions` kikerült a sablonból. A units/gramm lábjegyzet a
pár alatt marad, mert az az egyetlen hely, ahol a két szám alkohollá áll
össze. A rácsra lépés közös (`StepGrid.snapped`, lebegőpontos kerekítéssel,
különben a 4,5 / 0,5 = 9,000000000000002 egy lépést átugrana).

**A pontos idő egy rövid, alulról felúszó lapon (`TimePickerSheet`).** Az
időre koppintva jön elő, detentes `.sheet`-ként, nem a sor alatt kinyílva:
a kerék 200 pt magas, és helyben kinyitva minden alkalommal letolta a gyomor
szekciót és a kedvenc gombot; így a mögötte lévő form nem mozdul, a lapnak
saját „Done"-ja van, és a megerősítő sáv úgyis rögzítve van alul, tehát az
előrejelzés látszik. (Ez a modern alakja annak, ami UIKitben a billentyűzet
helyén felúszó `UIDatePicker` volt; az `inputView` ma már nem idióma, a
detent igen — az Óra és az Egészség app is így csinálja.) Rajta az
**óra–perc kerék**, dátumoszlop nélkül, az 5.16 indoklásával, ami az időt egy
**rögzített** ivási napra helyezi (`wheelDay`, a `place` szabályával).
Rögzített, mert ha minden tekerésnél a `consumedAt` napjából számolnánk, egy
határátlépő tekerés kihúzná a napot a kerék alól, és egy teljes nappal arrébb
landolna. A nap a lap megnyitásakor dől el. Alatta egy külön **„Day" sor**
kompakt dátumválasztóval (csak dátum): a rossz napra felvitt italt át kell
tudni tenni anélkül, hogy törölnénk és az Előzményben megkeresnénk a jó napot.
Külön sor, nem a kerék dátumoszlopa, mert a kettő más: a dátumválasztó a
napot mozgatja és az óra–percet megtartja, a kerék az óra–percet mozgatja az
ivási napon belül. Pótlásnál a „Day" sor nincs: a napot az oldal mondta ki.
Pótlásnál és szerkesztésnél is a léptető az alapállapot, nem a kerék: egy
17:40-es ital javítása is jellemzően pár lépés, a kerék egy koppintásra
megvan.

**A store-ban ez egy `move`-ot jelentett.** Az `update` eddig helyben írta
át a rekordot, és a `startedAt`-ot a legkorábbi italra húzta — egy másik
napra átdátumozott sör így a mai alkalmat nyújtotta volna vissza napokkal,
egy folytonos görbével a köztes napok fölött: pont az, amit az `add` a
`sessionCovering` útválasztással elkerül (vagyis a korábbi dátumválasztó
szerkesztésnél eddig is rosszul működött más napra). Most ha a szerkesztett
ital ivási napja változik, az `update` `remove` + `add`-ot futtat: az ital a
jó alkalomba kerül (vagy újat nyit a `profileApplicable` profiljával), az
üressé vált régi alkalom törlődik, és a célnapon az `add` pour cutja (5.13)
is lefut — ott az áthelyezett ital ugyanúgy információ az előzőről.

### 5.21 A gyomorállapot szórása szűkítve — a teli gyomor hamarabb ürül, és ez így helyes

**Előzmény (2026. október).** Zoltán az IntelliDrink régi screenshotjaival
mérte vissza a motort: 3 × 500 ml 5 %-os sör, félóránként, 30 perces
kortyolással, mindhárom gyomorállapottal. Két eltérés volt. (1) Nálunk a
gyomorállapot sokkal többet mozgatott a csúcson (üres → teli: −43 %,
az IntelliDrinknél −11 %). (2) Nálunk a teli gyomor *korábbi* kiürülést
adott (≈25 perc állapotonként), az IntelliDrinknél későbbit (≈8 perc).

**A (2) nem hiba, és nem fordítjuk meg.** Az IntelliDrink a gyomorállapottal
csak a felszívódást lassítja; nálunk a `StomachState` a biohasznosulást is
csökkenti (gyomri ADH first-pass), és mivel az elimináció nulladrendű, a
kevesebb bejutott alkohol egy az egyben korábbi nullát jelent — ez a hatás
nagyobb, mint amennyit a lassabb felszívódás kitol. A forenzikus irodalom
ugyanezt méri: Jones és Jönsson (1994, J Forensic Sci 39:1084) étkezés után
alacsonyabb csúcsot, ~39 %-kal kisebb görbe alatti területet és gyorsabb
eliminációt talált. A közkeletű „teli gyomor → tovább tart" intuíció a
görbe alakjáról szól, nem a nulláról.

**Az (1)-ben viszont igaza volt.** A régi 0,95 / 0,88 / 0,80 biohasznosulás
és a teli gyomor 1,2 h⁻¹ ka-ja (35 perces felezési idő) egyszerre mozgott a
szélső érték felé, és a kettő összeszorzódott; ráadásul a 30 perces
kortyolás már önmagában simít. Ezért **motorverzió 2**: biohasznosulás
0,95 / 0,90 / 0,85, teli gyomor ka 2,0 h⁻¹ (~21 perc). A 3 sörös
forgatókönyvön (80 kg referenciaprofil) a csúcs üres → teli 0,80 → 0,59 g/L
(−26 %), a kiürülés 7,8 → 7,2 óra; a sorrend és az irány marad. A Widmark-
alap önmagában nem ismer gyomorállapotot — az IntelliDrinknél és nálunk is
a felszívódási réteg utólagos, modellezett kiegészítése; ami tőlünk jön,
az a két paraméter és a hozzájuk tartozó irodalmi horgony.

A verziólépés miatt minden mentett alkalom összesítője újraszámolódik
(`DrinkingSession.cachedEngineVersion`). A tesztek rögzített számai és a
`Reference/fixtures.py` kimenete ehhez igazodnak.

## 6. Validáció

A `Reference/bac_model.py` a numerikus referencia. A Swift tesztek konkrét
számokat ellenőriznek belőle — **ha eltérnek, az algoritmus csúszott el, nem a
teszt rossz.**

| Ellenőrzés | Eredmény |
|---|---|
| 0,6 g/kg éhgyomorra | csúcs 0,75 g/L @ 36 perc (irodalom: 0,7–0,9, 30–60 perc) |
| leszálló ág meredeksége | 0,145 g/L/h a beállított 0,150-nel szemben |
| tömegmegmaradás | 0,094 % eltérés bevitt vs. eliminált |
| gyomortartalom | monoton alacsonyabb és későbbi csúcs; 3 sör / 90 perc: teli gyomor −26 % csúcs, ~35 perccel korábbi kiürülés (5.21) |
| Widmark-faktor | 0,667 / 0,589 — a klasszikus tartományban |

**Futásidő** (sandbox, ARM Linux — készüléken vélhetően 2–4× gyorsabb, de a
nagyságrend áll). Ezek a számok döntik el, mit szabad gesztus közben hívni:

| Hívás | 1 ital | 5 ital | 8 ital | 7 ital, 17 órás este |
|---|---|---|---|---|
| `simulateBand` | 2,5 ms | 3,8 ms | 6,1 ms | **5,6 ms** |
| `projectBand` (6 szimuláció) | — | 7,3 ms (4 ital + jelölt) | — | **12,0 ms** |
| `BACBand.samples` | — | 0,05 ms | — | — |

**Debug buildben ugyanez 14×**: a `projectBand` 167 ms, a `simulateBand` 73 ms.
Ez nem mellékes, mert fejlesztés közben debug fut a készüléken — egy hívás ott
húsz frame. Az utolsó oszlop a képernyőn is látott este: hét sör 14:55-től
21:24-ig, 13,8 egység, ami reggel 7:47-re ürül ki, vagyis 17 órányi szimuláció
(1074 mintapont).

Referencia-fixture a sávhoz (80 kg férfi, 3 ital, béta 0,12/0,15/0,18):
csúcssáv `0,543722 … 0,662719`, középcsúcs `0,601601` @ 136 perc,
kiürülés `361 … 534` perc (motorverzió 2, 5.21).

```bash
./Reference/run_tests.sh                 # 56 teszt, BACKit
cd Reference && python3 validate.py && python3 check_tests.py
```

A `run_tests.sh` Macen egyszerűen `swift test`. A lényege a másik eset: az
asszisztens Linux-sandboxában **nincs toolchain**, ezért a szkript letölt egy
Swift release-t `/tmp`-be, és ugyanazt a suite-ot futtatja. Ettől a „elrontottam
valamit?" kérdés helyben megválaszolható, nem kell visszakérdezni.

Ez **csak a `BACKit`-re igaz**: a csomag a Foundationön kívül semmit nem
importál, így bárhol fordul. Az app target SwiftUI-t és SwiftDatát használ, azt
kizárólag Xcode tudja lefordítani — a nézetek és a perzisztencia ellenőrzése
továbbra is Zoltáné.

A letöltés ~800 MB, munkamenetenként egyszer, nagyjából három perc. Megéri:
utána minden kör végén lefuttatható.

## 7. Lokalizáció

**Forrásnyelv angol, a fordítások String Catalogban.** Az app a 24 hivatalos
EU-nyelvet ismeri. Alapból azt választja, amit az iOS nyelvi beállítása kér; a
felhasználó ettől eltérhet a Profil fül Nyelv sorával, ami a Beállításokban az
app saját „Előnyben részesített nyelv" sorára visz (`LanguageSection`).

- `LogMyDrink/Localizable.xcstrings` — 24 nyelven. Generált fájl, kézzel nem
  szerkesztjük. **Az Xcode sem:** a `SWIFT_EMIT_LOC_STRINGS` build beállítás
  `NO` mindkét targeten, különben a fordító minden buildnél kigyűjti a Swift
  forrásból a szövegeket, felveszi az újakat `new` állapotban, és a saját
  formázásával írja vissza az egész fájlt — egyszer ez egy 44 ezer soros
  diffet adott, amiben három kulcs volt a változás. A szkript azóta az Xcode
  formátumában ír (rendezett kulcsok, szóköz a kettőspont előtt), így ha a
  szerkesztő mégis hozzányúl, a diff csak a tényleges változás.
- `Reference/translations/<kód>.py` — nyelvenként egy modul, mindegyikben egy
  `TRANSLATIONS` szótár az angol forrásszövegtől az adott nyelvig.
- **A magyar a referencia**: azt olvasta végig ember, és az ő kulcskészletéhez
  méri a szkript a többit. A magyar és az angol `translated` állapotban kerül a
  katalógusba, a többi `needs_review`-ban — az Xcode ezt jelöli. Egy nyelvet a
  `make_catalog.py` `REVIEWED` halmazába átemelni annyit tesz, hogy valaki
  vállalja érte a felelősséget.
- A kulcs maga az **angol forrásszöveg**. Interpolációnál `%@`.
- A nézetekben `LocalizedStringKey` (sima `Text("...")`), a modellrétegben
  `LocalizedStringResource` (enum `label` / `detail` / `explanation`).
- Ami **nem** fordítandó, az `Text(verbatim:)`-mel megy: számok, időpontok,
  a ‰ és % jelek, az SF Symbol nevek. Ez nem kozmetika — a `Text(String)`
  amúgy sem lokalizálna, a `verbatim` viszont kimondja a szándékot.
- A `Drink.name` a **sablon azonosítóját** tárolja (`"beer"`), nem a nevét.
  Különben a mentett adat nyelvhez kötődne, és nyelvváltás után angol nevek
  maradnának a magyar felületen.
- A `BACUnit.label` szándékosan nem tartalmazza a `%` jelet: egy literál
  százalékjel a katalógusban formátumspecifikátornak látszana. A nézet fűzi
  hozzá külön.
- Szám- és időformázás **soha nem kézzel**: `.formatted(.number...)`,
  `Duration.UnitsFormatStyle` és `formatted(date:time:)`. Ezek maguk
  lokalizálnak — tizedesvessző magyarul, 24 órás idő magyarul, 12 órás AM/PM
  angolul.
- A `make_catalog.py` a `Text(...)` mintát keresi: az intent `IntentDialog`
  szövegeit és a widget feliratait **nem látja**, tehát nem is jelzi, ha
  hiányzik a fordításuk (`TODO.md`).

A katalógust a `Reference/make_catalog.py` állítja elő és **ellenőrzi**: minden
kulcsnak szerepelnie kell a forrásban, minden lokalizált forrásszövegnek kell
hogy legyen fordítása, minden nyelvnek ugyanazt a kulcskészletet kell vinnie,
és a `%@` specifikátorok számának nyelvenként egyeznie kell.
Új szöveg felvitele: beírod a Swift forrásba angolul, felveszed **minden**
nyelvi modul `TRANSLATIONS` szótárába, és lefuttatod a szkriptet — a hiányzó
kulcsot nyelvenként kiírja.

```bash
cd Reference && python3 make_catalog.py
```

## 8. Konvenciók

- **Commit csak jóváhagyás után** — lásd a 0. fejezetet.
- **A motorhoz érő változtatás után fusson le a tesztsuite**
  (`./Reference/run_tests.sh`), mielőtt a diffet megmutatjuk.
- **A kódban minden angol**: kommentek, docstringek, teszt- és suite-nevek,
  MARK-ok, a Python szkriptek kiírásai. Magyar szöveg három helyen van:
  a `Localizable.xcstrings` fordítási értékeiben, ebben a dokumentumban és a
  `TODO.md`-ben. *(Ez a beszélgetés is magyarul folyik.)*
- A kommentek a **miértet** magyarázzák, nem a mit. Ami a kódból látszik, azt
  ne írjuk le újra.
- A `BACKit` nem importál SwiftUI-t. Soha.
- A `SessionStore` csak akkor számol újra, ha a bemenet változik — az óra
  ketyegése (`tick()`) csak a `now`-t mozgatja.
- **A csúszkák elengedéskor írnak a store-ba, nem húzás közben.** Mindegyik
  saját kis nézet, ami a húzott értéket lokális `@State`-ben tartja, és az
  `onEditingChanged`-ben commitol. Két oka van, és mindkettő mérhető: egy
  `simulateBand` 2,5–6 ms (ez három RK4-futás, a részletek a 6. pontban), ami
  a 120 Hz-es 8,33 ms-os frame nagy része; és egy `store`-ból olvasott érték
  invalidálja azt, aki olvasta — a `ProfileView`-ba ágyazva ez az egész `Form`
  volt. Ami az értékkel együtt kell hogy mozogjon (a kiürülési idő szövege, a
  sáv), az ezért a draftot birtokló nézetbe költözik, nem marad kívül.
- **A projekció cache-e a `SessionStore`-ban van, nem a nézetben.** A
  `project` megtartja az utolsó választ (`ProjectionKey`, `@ObservationIgnored`
  — egy observed property írása body-értékelés közben azt a nézetet
  invalidálná, amelyik épp kérdezett). Azért ott, mert az `AddDrinkSheet`-ben
  volt egy `@State` cache, amit az `onAppear` töltött fel, és nil-re egy
  közvetlen hívás volt a fallback: az **első** renderben tehát mind a kilenc
  olvasás lefuttatta a 167 ms-os projekciót, a lap 5 másodperc alatt jött fel,
  a cache pedig csak utána érkezett meg. Olyan cache, amit a hívó észrevétlenül
  kikerülhet, rossz helyen van.
- A chart ~220 pontra ritkít, de a csúcsot mindig megtartja.
- A séma **CloudKit-kompatibilis**: minden tárolt mezőnek van alapértéke vagy
  opcionális, nincs `@Attribute(.unique)`, a kapcsolat inverzzel megy. Ezt új
  mező felvitelekor is tartani kell, különben migráció.
- A cache-elt összesítő a `BACEngine.version`-t hordozza. Bumpold, ha a modell
  **számai** változnak — refaktorra ne, mert feleslegesen újraszámol mindent.

## 9. App Store kontextus

A guideline 1.4.3 a fal, de **nem abszolút**: több tisztán szoftveres BAC-app
él ma is a store-ban 2024–2025-ös azonosítóval. Két érv egy esetleges appealhez:

1. Az Apple saját HealthKitje tartalmaz `bloodAlcoholContent` mennyiségtípust.
2. A pozicionálás nem vezetés, hanem alkoholfogyasztás-csökkentés — ami
   engedélyezett kategória. A tartományos megjelenítés és a verdikt hiánya
   ezt támasztja alá.

Kiskapu, ha mégis elutasítanák: EU-ban a DMA alapján AltStore PAL vagy web
distribution, notarizációval, App Review tartalmi elbírálása nélkül (Alternative
Terms Addendum kell hozzá). Saját használatra dev account sideload vagy belső
TestFlight (100 eszköz, Beta App Review nélkül).

## 10. Állapot

**Kész:** a motor sávval és ivási tempóval; SwiftData-perzisztencia alkalmanként
befagyasztott profillal; három tab; Live
a mai napra, három nap-állapottal és a „‹ Tegnap" gombbal; ital felvitele,
szerkesztése és törlése, visszamenőlegesen is; egyszámos kijelzés opcionális
tartománnyal; a lebontási sebesség magyarázata és tippek; gyors felvitel a
Live kapszulájáról, Siritől és Lock Screen / Home Screen widgetről (5.15,
prototípus); Előzmény Nap / Hét / Hónap / Év szegmenssel, két charttal,
mutató-kártyával, ugró lappal és lakattal (5.16), a Trend szegmens debug
kísérletként; JSON export / import (5.17); több személy a `multiPerson` flag
mögött, személylistával és vendég-eltávolítással (5.18); 24 nyelvű lokalizáció
(magyar és angol átnézve).

**Tesztek:** 56 a `BACKit`-ben (Linuxon is futtatható, 6.); 79 a
`LogMyDrinkTests` targetben (2026. október óta, ⌘U-val, mind zöld): 57 a
History modellre (5.16) és 22 a perzisztenciára — migráció, útválasztás,
aktív személy (5.18). A target unit testing bundle, host a `LogMyDrink`,
file-system synchronized group a `LogMyDrinkTests/` mappára, tehát egy új
tesztfájl projektfájl-módosítás nélkül bekerül. A beállításai az apphoz
igazítva: Swift 6, iOS 17.0, bundle ID `dev.zcsipler.logmydrink.tests`. A
BACKit-et **nem** linkeli külön — a host app linkeli, az `import BACKit` a
build-könyvtárból oldódik fel; duplán linkelve a statikus könyvtár
típusmetaadatai kétszer lennének a folyamatban. A tesztek memóriában
futnak (`TestSupport.makeContext`, `cloudKitDatabase: .none`, eldobható
defaults-suite), a fejlesztő saját adatához nem nyúlnak. Csak Xcode-ban
futtathatók, mert SwiftData kell hozzájuk (12.). A `LogMyDrink` scheme
**megosztott** (`xcshareddata/xcschemes`), és a Test actionje viszi a
targetet — egy friss klónon a ⌘U beállítás nélkül megy.

**A CloudKit-szinkron be van kapcsolva** (`BuildCapabilities.cloudSync =
true`, 2026. október 7.), fizetős fejlesztői tagsággal, és készüléken
bevált: törlés-újratelepítés után az adat a felhőből visszajött (5.17). Az
App Store Connectben a „LogMyDrink" app-rekord lefoglalva (`TODO.md`).

Az app **fordul és fut** szimulátoron, iPhone-ra telepítve van kipróbálva.

Utolsó commit: lásd `git log`; ez a fejezet 2026. október 7-én, a
CloudKit-bekapcsolás commitjával frissült.

## 11. Teendők

A `TODO.md`-ben: nyitott döntések, az élesítés előtti és utáni teendők, a
technikai hátralék. Mielőtt bármelyikbe belevágnánk, kérdezzük meg, tényleg
most jön-e — a sorrend változhat. Ami onnan megépül, ide kerül az 5. fejezetbe,
az indoklásával.

## 12. Megjegyzés a hangnemhez

Zoltán iOS fejlesztő, a technikai mélységet bírja és igényli. A termékdöntéseket
érvekkel vitatja — ha valami rossz UX vagy rossz modellezés, mondjuk ki, és
támasszuk alá számokkal. A „lebontási sebesség csúszka" kritikája tőle jött, és
igaza volt; ebből lett az 5.1–5.3 pont. Ugyanígy a „nem ittál" kontra „nincs
adat" megkülönböztetés (5.7).

Döntés előtt **egyesével** kérdezz, részletesen, valós alternatívákkal — nem
négy kérdést egyszerre. Ha egy kérésnek van rejtett következménye (ütköző
gesztus, elveszett adat, hamis állítás), azt mondd ki, mielőtt megcsinálod.

**A vitát vigyük végig, de ne makacskodjunk.** A tartomány-kontra-egy-szám kérdés
két körben fordult: először kivettem a tartományt mindenhonnan, aztán kiderült,
hogy a kérés nem ez volt — csak az alapérték ne tartomány legyen. Ha a válasz
javítja az előző kört, ismerjük el nyíltan és írjuk át (ebből lett az 5.8).

**Mit tudok ellenőrizni.** A `BACKit` tesztjeit **le tudom futtatni**:
`./Reference/run_tests.sh` letölt egy Swift toolchaint a sandboxba, és lemegy
mind az 56 teszt (6.). Ezt minden olyan kör végén futtassuk le, ami a motorhoz
ér. Rajta kívül: zárójel- és API-egyezés-ellenőrzés, a Python referencia, a
katalógus-ellenőrző.

**Amit nem tudok:** az **app targetet** nem fordítom — SwiftUI és SwiftData kell
hozzá, az Xcode dolga. A nézetek, a perzisztencia és minden, ami készüléken
látszik, Zoltáné. Ezért érdemes minden körben kis, önmagában értelmes
változást adni.
