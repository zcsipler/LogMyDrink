"""
Hungarian.

Hand-written and reviewed. This is the reference translation: its key set
defines what the catalog contains, and every other language file is checked
against it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Ezrelék",
    "Percent": "Százalék",

    # --- DrinkCatalog: drink types ---
    "Beer": "Sör",
    "Wine": "Bor",
    "Champagne": "Pezsgő",
    "Shot": "Feles",
    "Cocktail": "Koktél",
    "Custom": "Egyedi",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Éhgyomor",
    "Moderately full": "Közepesen telt",
    "Full stomach": "Teli has",
    "Empty": "Éhgyomor",
    "Moderate": "Közepes",
    "Full": "Teli",
    "Fast absorption, higher and earlier peak.": "Gyors felszívódás, magasabb és korábbi csúcs.",
    "Moderate absorption.": "Mérsékelt felszívódás.",
    "Slow absorption, lower and later peak.": "Lassú felszívódás, alacsonyabb és későbbi csúcs.",

    # --- DrinkingFrequency ---
    "Rarely": "Ritkán",
    "A few times a month": "Havonta párszor",
    "Several times a week": "Hetente többször",
    "Almost daily": "Szinte naponta",
    "A few occasions a year": "Évente néhány alkalom",
    "Social drinking": "Alkalmi, társasági fogyasztás",
    "Weekly routine": "Heti rendszeresség",
    "Daily or nearly daily": "Napi vagy majdnem napi",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Idő",
    "Level": "Szint",
    "Lower": "Alsó",
    "Upper": "Felső",
    "Lower estimate": "Alsó becslés",
    "Upper estimate": "Felső becslés",
    "Personal limit": "Saját határ",
    "Drink": "Ital",

    # --- BACChartView ---
    "Expected peak around %@": "Várható csúcs %@ körül",
    "Peaked around %@": "Csúcs volt %@ körül",
    "No active session": "Nincs aktív alkalom",
    "Still rising": "Még emelkedik",
    "YOUR LIMIT %@": "SAJÁT HATÁR %@",
    "possible range": "lehetséges tartomány",

    # --- Live screen: the day with nothing on it ---
    "Live": "Élő",
    "Nothing logged today": "Ma még nincs felvitt ital",
    "Add a drink when you have one.": "Vidd fel, amikor iszol valamit.",

    # --- Tabs and history ---
    "History": "Előzmény",
    "No past sessions yet": "Még nincs lezárt alkalom",
    "A session appears here once it has ended — when your level has cleared and a few hours have passed.":
        "Egy alkalom akkor kerül ide, ha lezárult — amikor a szinted kiürült, és eltelt néhány óra.",
    "%@ drinks": "%@ ital",
    "peak": "csúcs",
    "Started": "Kezdés",
    "Lasted": "Tartam",
    "Duration": "Időtartam",
    "Sober around": "Józan kb.",
    "Sober at": "Józan",
    "Remaining": "Még hátra",
    "next day": "másnap",
    "previous day": "előző nap",
    "%@ days later": "%@ nappal később",
    "%@ days earlier": "%@ nappal korábban",
    "Calculated with your profile at the time": "Az akkori profiloddal számolva",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Italok",
    "Units": "Egység",
    "Drinks this session": "Az alkalom italai",
    "Add drink": "Ital hozzáadása",

    # --- Editing an already logged drink ---
    "Edit drink": "Ital szerkesztése",
    "Save changes": "Mentés",
    "With this": "Ezzel",
    "Delete": "Törlés",
    "tap to edit · swipe to delete": "koppints a szerkesztéshez · húzd a törléshez",

    # --- Drinking pace ---
    "How fast": "Milyen tempóban",
    "In one go": "Egy hajtásra",
    "Counts as a single swallow — the steepest possible rise.":
        "Egyetlen kortynak számít — ez a lehető legmeredekebb emelkedés.",
    "A quick drink. The level climbs fast.":
        "Gyors ital. A szint meredeken emelkedik.",
    "A normal pace.": "Szokásos tempó.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Lassan kortyolva. Ugyanannyi alkohol, sokkal szelídebb emelkedés.",

    # --- AddDrinkSheet ---
    "Cancel": "Mégse",
    "Now": "Most",
    "Projected peak": "Vetített csúcs",
    "Peak at": "Csúcs ekkor",
    "Clears": "Kiürül",
    "This would cross your limit": "Átlépnéd a saját határod",
    "Around %@, for up to %@.": "%@ körül, legfeljebb %@ hosszan.",
    "This might cross your limit": "Átlépheted a saját határod",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "A lassabb lebontás esetén igen, a gyorsabbnál nem. Ez a becslés bizonytalansága.",
    "Type": "Típus",
    "Amount": "Mennyiség",
    "Strength": "Alkoholfok",
    "%@ units": "%@ egység",
    "%@ g alcohol": "%@ g alkohol",
    "Stomach": "Gyomor",
    "When": "Időpont",
    "Done": "Kész",
    "Add": "Hozzáadás",

    # --- ProfileSheet ---
    "Male": "Férfi",
    "Female": "Nő",
    "Sex": "Nem",
    "Weight": "Testsúly",
    "Height": "Magasság",
    "Age": "Életkor",
    "kg": "kg",
    "cm": "cm",
    "yrs": "év",
    "Body": "Testalkat",
    "Total body water comes from the Watson equations, which set the volume alcohol distributes into.":
        "A teljes testvíz a Watson-formulákból jön, ez adja meg az alkohol eloszlási terét.",
    "Total body water comes from the Watson equations, which set the volume alcohol distributes into. "
    "The female equation does not include age, so changing it will not affect the result.":
        "A teljes testvíz a Watson-formulákból jön, ez adja meg az alkohol eloszlási terét. "
        "A női egyenlet nem tartalmazza az életkort, ezért annak állítása nem változtat az eredményen.",
    "Drinking frequency": "Fogyasztás gyakorisága",
    "How often do you drink?": "Milyen gyakran iszol?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Ebből becsüljük a lebontási sebességet. A rendszeres fogyasztás indukálja a máj CYP2E1 útvonalát, ezért a gyakori fogyasztók gyorsabban bontják le az alkoholt. Ez a modell leggyengébb pontja, ezért a Megjelenítés és nyelv lapon megadhatod, mennyit mutasson meg az app ebből a bizonytalanságból.",
    "Your limit": "Saját határ",
    "Your own reference number, not a legal limit. The app tells you when a planned drink would take you "
    "past it, and for how long you would stay above.":
        "A te referenciaszámod, nem jogi limit. Az app jelzi, ha egy tervezett ital átvinne rajta — és azt "
        "is, mennyi ideig maradnál fölötte.",
    "Calculated values": "Számított értékek",
    "Total body water": "Teljes testvíz",
    "Distribution volume": "Eloszlási térfogat",
    "Widmark factor": "Widmark-faktor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far from that, "
    "it is worth checking the values above.":
        "A Widmark-faktor tipikusan 0,68 körül van férfiaknál és 0,55 körül nőknél. Ha a tiéd messze esik "
        "ettől, érdemes ellenőrizni a fenti adatokat.",
    "Elimination rate": "Lebontási sebesség",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling side of the curve.":
        "Milyen gyorsan üríti a májad a már felszívódott alkoholt — ez a görbe lecsengő szakaszának meredeksége.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the enzyme that breaks it down already runs at full capacity at almost any level. That is why rules of thumb like “one drink an hour” exist at all.":
        "Az alkohol nem százalékosan tűnik el, hanem óránként fix mennyiséggel, mert a lebontó enzim már nagyon alacsony szinten is teljes kapacitáson dolgozik. Innen van, hogy egyáltalán létezik olyan ökölszabály, mint az „óránként egy ital”.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Ezzel a beállítással %@ körülbelül %@ alatt ürül ki. Szinte mindenkinél %@ közé esik ez az "
        "érték óránként.",
    "How to find yours": "Hogyan derítheted ki a sajátodat?",
    "With a breathalyser": "Alkoholszondával",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your last drink, "
    "with nothing in between. Subtract the second reading from the first and divide by the hours between "
    "them.":
        "Fújj kétszer, legalább egy óra különbséggel, a lecsengő ágon — az utolsó ital után legalább két "
        "órával, és közben ne igyál. Vond ki a második mérést az elsőből, és oszd el a köztük eltelt órák "
        "számával.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Például %@, majd két órával később %@: ez %@ óránként.",
    "Without one": "Szonda nélkül",
    "The app tells you when it expects you to clear. If you are reliably back to normal well before that, "
    "your rate is higher than the setting — nudge it up a step and watch for a few sessions. If it takes "
    "longer than predicted, nudge it down.":
        "Az app megmondja, mikorra várja a kiürülést. Ha ennél jóval hamarabb vagy rendben, a lebontásod "
        "gyorsabb a beállítottnál — vidd feljebb egy lépéssel, és figyeld néhány alkalmon át. Ha tovább "
        "tart, vidd lejjebb.",
    "What moves it": "Mi befolyásolja",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It also runs "
    "slightly higher in women on average, and lower on an empty stomach or with liver trouble.":
        "A rendszeres fogyasztás növeli: a munkát végző májenzim a használattól indukálódik. Nőknél "
        "átlagosan valamivel magasabb, éhgyomorra és májbetegség esetén pedig alacsonyabb.",
    "Uncertainty": "Bizonytalanság",
    "At zero every figure is a single number — the app's best estimate. Above zero the same figures are "
    "shown as ranges, and the band on the chart widens to match.":
        "Nullán minden szám egyetlen érték — az app legjobb becslése. Nulla fölött ugyanezek "
        "tartományként jelennek meg, és a grafikon sávja is ennek megfelelően szélesedik.",
    "A single number is easier to learn against: over time you find out what your own 0.6 feels like. "
    "A range is the more literal answer, because the rate really is uncertain. Both are defensible — "
    "this is your call.":
        "Egyetlen számhoz könnyebb tanulni: idővel megtudod, nálad mit jelent a 0,6. A tartomány a szó "
        "szerintibb válasz, mert a lebontási sebesség tényleg bizonytalan. Mindkettő védhető — ez a te "
        "döntésed.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "A fogyasztási gyakoriságod alapján javasolt szórás ± %@ óránként.",
    "Rate": "Sebesség",
    "Range": "Sáv",
    "Advanced": "Haladó beállítások",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Több személy",
    "History trends": "Előzmény-trendek",
    "Week": "Hét",
    "Month": "Hónap",
    "Year": "Év",
    "Sober days": "Ivásmentes napok",
    "Change": "Változás",
    "before records": "a rögzítés előtt",
    "See further back": "Nézz vissza messzebbre",
    "Weeks, months and years side by side — and every evening older than seven days.": "Hetek, hónapok és évek egymás mellett – és minden hét napnál régebbi este.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Minden, amit eddig felvittél, már el van mentve. A feloldás csak megmutatja.",
    "Coming soon": "Hamarosan",
    "Today": "Ma",
    "Day": "Nap",
    "Yesterday": "Tegnap",
    "No drinks on this day": "Ezen a napon nem volt ital",
    "Trend": "Trend",
    "day": "nap",
    "Smoothing": "Simítás",
    "%@ sessions": "%@ alkalom",
    "No data before %@": "Nincs adat %@ előtt",
    "vs.": "az előzőhöz:",
    "Grams": "Gramm",
    "Grams of alcohol": "Gramm tiszta alkohol",
    "Standard units": "Standard egység",
    "Unit size": "Egység mérete",
    "Automatic": "Automatikus",
    "UK": "Egyesült Királyság",
    "Nordic countries": "Északi országok",
    "US standard drink": "Amerikai standard ital",
    "WHO, most of Europe": "WHO, Európa nagy része",
    "Period": "Időszak",
    "Switch person": "Személyváltás",
    "Add person": "Személy hozzáadása",
    "New person": "Új személy",
    "You": "Te",
    "Name": "Név",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Mind a négy módosítja a görbét, így egyiket sem lehet megtippelni valaki más helyett.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while they are "
    "the selected person.":
        "A saját határ és a finomabb beállítások később a Profil fülön módosíthatók, amíg ő a "
        "kiválasztott személy.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Gyorsfelvitel",
    "Choose a favourite drink": "Válassz kedvenc italt",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Válaszd ki, mit szoktál rendelni, és az Élő képernyőn egy gombnyomással felviheted.",
    "This is your quick-add drink": "Ez a gyorsfelvitel itala",
    "Set as my quick-add drink": "Legyen ez a gyorsfelvitel itala",
    "This is now your usual": "Ez lett a szokásos",
    "Remove favourite": "Kedvenc törlése",
    "Always add this one": "Mindig ezt vigye fel",
    "Logs it straight away, without opening anything.": "Azonnal felviszi, mindenféle felugró nélkül.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full your "
    "stomach is comes from the drink before it, and can be corrected straight after.":
        "Az Élő képernyőn egy koppintás felviszi, a gombon pedig ott a várható csúcs. A gyomor "
        "telítettségét az előző italtól veszi át, és utána azonnal javítható.",
    "Peak %@": "Csúcs %@",
    "%@ added": "%@ felvéve",
    "Save": "Mentés",
    "Undo": "Visszavonás",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Biztonsági mentés",
    "Export a backup": "Mentés exportálása",
    "Import a backup": "Mentés visszatöltése",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it never "
    "changes or removes anything already here.":
        "A mentés minden személyt, alkalmat és italt tartalmaz. A visszatöltés csak a hiányzókat adja "
        "hozzá — a már meglévő adatot nem módosítja és nem törli.",
    "Import this backup?": "Visszatöltöd ezt a mentést?",
    "Import": "Visszatöltés",
    "Everything in this backup is already here.": "A mentés minden eleme már megvan.",
    "Import finished": "A visszatöltés kész",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Nyelv",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Megnyitja az appot a Beállításokban, ahol az „Előnyben részesített nyelv” az app saját "
        "nyelvét állítja — a rendszeré marad, ami volt. Az iOS a váltáskor újraindítja az appot.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "A visszatöltés nem sikerült",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Ez a fájl nem a LogMyDrink mentése, vagy megsérült.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Ezt a mentést a LogMyDrink újabb verziója készítette. Frissítsd az appot, és próbáld újra.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Hozzáad %@ alkalmat, %@ italt és %@ havi összeget. A meglévő adatok nem változnak és nem vesznek el.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Hozzáadva: %@ alkalom, %@ ital és %@ havi összeg.',
    'months as totals': 'hónap csak összegként',
    'by month only': 'csak havi szinten',
    'monthly total': 'havi összeg',
    'No daily records for this day': 'Erről a napról nincs napi adat',
    'Monthly total: %@': 'Havi összeg: %@',
    'A dry month': 'Száraz hónap',

    # --- RemovePersonSection ---
    'Remove %@?': 'Eltávolítod: %@?',
    'Remove': 'Eltávolítás',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Töröl %@ alkalmat, %@ italt és %@ havi összeget. Ez nem vonható vissza.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Töröl %@ alkalmat és %@ italt. Ez nem vonható vissza.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Húzd balra a vendéget, hogy eltávolítsd mindennel együtt, amit alatta rögzítettünk. Téged nem lehet eltávolítani.',
    'People': 'Személyek',
    'Owner': 'Tulajdonos',
    'Everyone this app records. Switch, add, or remove someone.': 'Mindenki, akit ez az app rögzít. Válts, vegyél fel vagy távolíts el valakit.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Áthozat az előző estéről',
    # --- History, second card (5.24) ---
    'Calories': 'Kalória',
    'Sessions': 'Alkalmak',
    'Per session': 'Alkalmanként',
    'Under the influence': 'Befolyásoltan',
    '%@ of the time': '%@ az időből',
    'Days over limit': 'Határ fölötti napok',
    'Longest sober run': 'Leghosszabb józan sorozat',
    'Favourite drink': 'Kedvenc ital',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Megjelenítés és nyelv",
    "Data": "Adatok",
    "Concentration": "Koncentráció",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "A sebességet hagyd a gyakorisági kérdésre, hacsak nincs mért értéked, amihez igazítanád.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Becslés, nem mérés. Soha ne ez alapján döntsd el, hogy vezethetsz-e.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Becsült tartomány, nem mérés. Soha ne ez alapján döntsd el, hogy vezethetsz-e.',
    'How does the app calculate this?':
        'Hogyan számolja ki ezt az app?',
    'approximately %@ %@':
        'körülbelül %@ %@',
    'How it works':
        'Hogyan működik?',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Soha ne ez alapján döntsd el, hogy vezethetsz-e. Az app nem mér, hanem becsül, és a tényleges szinted jelentősen eltérhet a becsülttől.',
    'Why this app exists':
        'Miért készült ez az app',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'A LogMyDrink abban segít, hogy tudatosabban igyál, és kézben tartsd az ivást. A döntés a következő pohár előtt születik meg, ezért az app előre megmutatja, hová emelné a szintedet egy újabb ital, és mikor tetőzne.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'De nem csak a mai estéről szól. Minden felvitt ital bekerül az Előzménybe, így hónapok, évek távlatában is látod, mennyit, milyen gyakran és milyen magas szintig iszol. Ebből kirajzolódnak a szokásaid, és az is, merre tartanak: javul-e a helyzet, vagy romlik.',
    'How it calculates':
        'Hogyan számol',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'A becslés a Widmark-módszeren alapul, amellyel az 1930-as évek óta számítják a véralkoholszintet; az app ennek egy továbbfejlesztett változatával dolgozik.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'A testsúlyodból, a magasságodból, az életkorodból és a nemedből kiszámolja, mennyi víz van a szervezetedben, mert az alkohol ebben oszlik el. Minden italt külön követ nyomon: mennyi alkohol volt benne, milyen gyorsan ittad meg, és mennyit ettél előtte, mert ettől függ, milyen gyorsan szívódik fel.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Közben a májad óránként nagyjából állandó mennyiséget bont le; hogy nálad mennyit, azt az app abból becsüli, milyen gyakran iszol. Az eredmény egy percről percre számolt görbe: hol tartasz most, merre haladsz, és mikorra ürül ki teljesen az alkohol.',
    'Details':
        'Részletek',
    'Body water':
        'Testvíz',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'A Watson-képlet (1980), a testsúly, a magasság, az életkor és a nem alapján. A női képletben nem szerepel az életkor – ez a képlet sajátossága, nem hiba. Az eloszlási térfogat a testvíz 0,85-tel elosztva, ennyi a vér víztartalma.',
    'Absorption':
        'Felszívódás',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Minden italnak saját „gyomra” van. Éhgyomorra az alkohol fele kb. 7, teli gyomorra kb. 21 perc alatt szívódik fel. A kortyolgatott ital az ivás teljes ideje alatt egyenletesen jut a gyomorba.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Alacsonyabb csúcs és korábbi kiürülés. Meglepő, de mérésekkel igazolt: étel mellett a gyomor az alkohol egy részét már a felszívódás előtt lebontja (az app 5, 10 és 15 százalékkal számol), és ami be sem jutott, azt nem is kell lebontani.',
    'Elimination':
        'Lebontás',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Óránként kb. 0,15 ‰ (a szakirodalomban 0,10–0,25). Rendszeresen ivóknál gyorsabb, mert a máj enzimei alkalmazkodnak. Nullához közeledve lelassul (Michaelis–Menten-kinetika), így a görbe nem ér hirtelen véget, hanem fokozatosan lecseng.',
    'Computation':
        'Számítás',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'A görbe percenkénti felbontású numerikus szimulációból adódik.',
    'Why it is only an estimate':
        'Miért csak becslés',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Az app semmit sem mér. Amit mutat, az egy átlagos értékekkel számoló modell eredménye, és a valóság ettől eltérhet. A legnagyobb bizonytalanság az, hogy milyen gyorsan bontod le az alkoholt: a reális tartományon belül ez önmagában is akár 40 százalékkal megváltoztathatja ugyanannak az estének a csúcsát, a kiürülést pedig négy órával tolhatja el.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Számít a genetika, a máj állapota és a gyógyszerek is, valamint az, hogy mit ettél, mennyit aludtál és mennyire vagy fáradt – ezek közül az app egyiket sem ismeri. Pontos értéket csak hitelesített alkoholszonda vagy vérvizsgálat ad.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'A szám ettől még hasznos. Ha az app nálad következetesen kicsit többet vagy kevesebbet mutat, akkor minden este ugyanabba az irányba téved, így idővel megtanulod, mit jelent nálad egy adott érték. A Profilban a lebontási sebesség bizonytalanságát is megjelenítheted: ilyenkor egyetlen szám helyett tartományt látsz.',
    'Tips':
        'Tippek',
    'Favourite drink in one tap':
        'Kedvenc ital egy koppintással',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Állíts be egy kedvencet a Profilban, és az Élő képernyő gombjával egyetlen koppintással felviheted.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Add hozzá a zárolási képernyőhöz vagy a főképernyőhöz: egy koppintással felviheted a kedvencedet. Amíg alkohol van a szervezetedben, a widget a szintedet is mutatja, és azt, hogy emelkedik vagy csökken.',
    'How do I add it?':
        'Hogyan adhatom hozzá?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Mondd: „Hey Siri, LogMyDrink now”, és Siri felviszi a kedvencedet, majd megmondja, mekkora csúcsra számíthatsz. (A parancs angolul működik.)',
    'Looking back':
        'Visszatekintés',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        'Az Élő képernyő tetején a „Tegnap” gomb egy koppintással az előző napra visz; az Előzmény fülön heti, havi és éves bontásban látod a szokásaidat.',
    'Logging later':
        'Utólagos felvitel',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Ha egy italt utólag viszel fel, a − és + gombokkal állítsd vissza az időpontot; egy kimaradt napot az Előzmény fül Nap nézetében pótolhatsz.',
    'One tap and done':
        'Egy koppintás, és kész',
    'Your favourite from the Lock Screen':
        'A kedvenced a zárolási képernyőről',
    'Say it, don’t type it':
        'Mondd ki, ne gépeld',
    'See your patterns':
        'Nézd meg a szokásaidat',
    'Set what you drink most often and log it with a single tap.':
        'Állítsd be, mit iszol a leggyakrabban, és egyetlen koppintással felviheted.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Egy koppintás a widgeten, és a kedvenced már fel is került – nem kell keresgélned az appot. Este a widget a szintedet is mutatja.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now” – Siri felviszi a kedvencedet, és megmondja, mekkora csúcsra számíthatsz.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Az Előzményben heti, havi és éves bontásban látod, mennyit és milyen magas szintig iszol, és azt is, milyen irányba változik.',
    'Set favourite':
        'Kedvenc beállítása',
    'Add widget':
        'Widget hozzáadása',
    'Got it':
        'Rendben',
    'Open History':
        'Előzmény megnyitása',
    'Don’t show again':
        'Ne mutasd többé',
    'Lock Screen':
        'Zárolási képernyő',
    'Home Screen':
        'Főképernyő',
    'Where':
        'Hová',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Zárold le a telefont, majd tartsd nyomva a zárolási képernyőt.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Koppints a Testreszabás, majd a Zárolási képernyő elemre, végül az óra alatti widgetsorra.',
    'Choose LogMyDrink, then tap Done.':
        'Válaszd a LogMyDrinket, majd koppints a Kész gombra.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Tartsd nyomva a főképernyő egy üres részét, amíg az ikonok remegni nem kezdenek.',
    'Tap Edit, then Add Widget.':
        'Koppints a Szerkesztés, majd a Widget hozzáadása elemre.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Keresd meg a LogMyDrinket, válassz méretet, és koppints a Widget hozzáadása gombra.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'A widgetre koppintva megnyílik az app, és felviszi a kedvenc italodat. Amíg alkohol van a szervezetedben, a szintedet is mutatja, és azt, hogy emelkedik vagy csökken.',
    'Add the widget':
        'Widget hozzáadása',
    'Show tips':
        'Tippek mutatása',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Naponta legfeljebb egy tipp, az app megnyitásakor – soha, amíg alkohol van a szervezetedben.',
}
