"""
Slovak.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promile",
    "Percent": "Percento",

    # --- DrinkCatalog: drink types ---
    "Beer": "Pivo",
    "Wine": "Víno",
    "Champagne": "Šumivé víno",
    "Shot": "Poldeci",
    "Cocktail": "Kokteil",
    "Custom": "Vlastný",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Prázdny žalúdok",
    "Moderately full": "Stredne plný",
    "Full stomach": "Plný žalúdok",
    "Empty": "Prázdny",
    "Moderate": "Stredný",
    "Full": "Plný",
    "Fast absorption, higher and earlier peak.": "Rýchle vstrebávanie, vyšší a skorší vrchol.",
    "Moderate absorption.": "Stredne rýchle vstrebávanie.",
    "Slow absorption, lower and later peak.": "Pomalé vstrebávanie, nižší a neskorší vrchol.",

    # --- DrinkingFrequency ---
    "Rarely": "Zriedka",
    "A few times a month": "Niekoľkokrát do mesiaca",
    "Several times a week": "Niekoľkokrát do týždňa",
    "Almost daily": "Takmer denne",
    "A few occasions a year": "Niekoľkokrát do roka",
    "Social drinking": "Spoločenské pitie",
    "Weekly routine": "Týždenný zvyk",
    "Daily or nearly daily": "Denne alebo takmer denne",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Čas",
    "Level": "Hladina",
    "Lower": "Dolný",
    "Upper": "Horný",
    "Lower estimate": "Dolný odhad",
    "Upper estimate": "Horný odhad",
    "Personal limit": "Osobný limit",
    "Drink": "Nápoj",

    # --- BACChartView ---
    "Expected peak around %@": "Očakávaný vrchol okolo %@",
    "Peaked around %@": "Vrchol bol okolo %@",
    "No active session": "Žiadne aktívne posedenie",
    "Still rising": "Stále stúpa",
    "YOUR LIMIT %@": "TVOJ LIMIT %@",
    "possible range": "možné rozpätie",

    # --- Live screen: the day with nothing on it ---
    "Live": "Naživo",
    "Nothing logged today": "Dnes nič nezaznamenané",
    "Add a drink when you have one.": "Pridaj nápoj vždy, keď si nejaký dáš.",

    # --- Tabs and history ---
    "History": "História",
    "No past sessions yet": "Zatiaľ žiadne minulé posedenia",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Posedenie sa tu objaví, keď sa skončí – keď alkohol vyprchá a uplynie niekoľko hodín.",
    "%@ drinks": "Nápoje: %@",
    "peak": "vrchol",
    "Started": "Začiatok",
    "Lasted": "Trvalo",
    "Duration": "Trvanie",
    "Sober around": "Triezvy cca",
    "Sober at": "Triezvy",
    "Remaining": "Zostáva",
    "next day": "nasledujúci deň",
    "previous day": "predchádzajúci deň",
    "%@ days later": "o %@ dni neskôr",
    "%@ days earlier": "o %@ dni skôr",
    "Calculated with your profile at the time": "Vypočítané podľa tvojho vtedajšieho profilu",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Nápoje",
    "Units": "Jednotky",
    "Drinks this session": "Nápoje na tomto posedení",
    "Add drink": "Pridať nápoj",

    # --- Editing an already logged drink ---
    "Edit drink": "Upraviť nápoj",
    "Save changes": "Uložiť zmeny",
    "With this": "S týmto nápojom",
    "Delete": "Vymazať",
    "tap to edit · swipe to delete": "klepnutím upravíš · potiahnutím vymažeš",

    # --- Drinking pace ---
    "How fast": "Ako rýchlo",
    "In one go": "Naraz",
    "Counts as a single swallow — the steepest possible rise.":
        "Počíta sa ako jeden dúšok – najstrmší možný nárast.",
    "A quick drink. The level climbs fast.": "Rýchlo vypitý nápoj. Hladina stúpa rýchlo.",
    "A normal pace.": "Bežné tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Popíjané pomaly. Pri rovnakom množstve alkoholu oveľa miernejší nárast.",

    # --- AddDrinkSheet ---
    "Cancel": "Zrušiť",
    "Now": "Teraz",
    "Projected peak": "Predpokladaný vrchol",
    "Peak at": "Vrchol o",
    "Clears": "Vyprchá",
    "This would cross your limit": "Toto by prekročilo tvoj limit",
    "Around %@, for up to %@.": "Okolo %@, najviac na %@.",
    "This might cross your limit": "Toto by mohlo prekročiť tvoj limit",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Pri pomalšom metabolizme áno, pri rýchlejšom nie. To je neistota odhadu.",
    "Type": "Typ",
    "Amount": "Množstvo",
    "Strength": "Obsah alkoholu",
    "%@ units": "Jednotky: %@",
    "%@ g alcohol": "%@ g alkoholu",
    "Stomach": "Žalúdok",
    "When": "Kedy",
    "Done": "Hotovo",
    "Add": "Pridať",

    # --- ProfileSheet ---
    "Male": "Muž",
    "Female": "Žena",
    "Sex": "Pohlavie",
    "Weight": "Hmotnosť",
    "Height": "Výška",
    "Age": "Vek",
    "kg": "kg",
    "cm": "cm",
    "yrs": "r.",
    "Body": "Telo",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Celková telesná voda vychádza z Watsonových rovníc, ktoré určujú objem, v ktorom sa "
        "alkohol distribuuje.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Celková telesná voda vychádza z Watsonových rovníc, ktoré určujú objem, v ktorom sa "
        "alkohol distribuuje. Rovnica pre ženy nezahŕňa vek, takže jeho zmena výsledok "
        "neovplyvní.",
    "Drinking frequency": "Frekvencia pitia",
    "How often do you drink?": "Ako často piješ?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Takto odhadujeme tvoju rýchlosť odbúravania. Pravidelné pitie indukuje pečeňovú dráhu CYP2E1, takže kto pije často, odbúrava alkohol rýchlejšie. Je to najslabšie miesto modelu, a preto si v časti Zobrazenie a jazyk môžeš nastaviť, koľko z tejto neistoty ti aplikácia ukáže.",
    "Your limit": "Tvoj limit",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Tvoje vlastné referenčné číslo, nie zákonný limit. Aplikácia ti povie, keď by ťa "
        "plánovaný nápoj dostal nad neho a ako dlho by si nad ním zostal.",
    "Calculated values": "Vypočítané hodnoty",
    "Total body water": "Celková telesná voda",
    "Distribution volume": "Distribučný objem",
    "Widmark factor": "Widmarkov faktor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmarkov faktor býva zvyčajne okolo 0,68 u mužov a 0,55 u žien. Ak je ten tvoj od "
        "toho ďaleko, oplatí sa skontrolovať hodnoty vyššie.",
    "Elimination rate": "Rýchlosť odbúravania",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Ako rýchlo tvoja pečeň odbúrava alkohol po jeho vstrebaní – sklon klesajúcej časti "
        "krivky.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol sa odbúrava približne pevným množstvom za hodinu, nie percentuálnym podielom, "
        "pretože enzým, ktorý ho rozkladá, beží naplno už takmer pri každej hladine. Práve "
        "preto vôbec existujú pravidlá ako „jeden nápoj za hodinu“.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Pri tomto nastavení %@ vyprchá asi za %@. Takmer všetci sa pohybujú medzi %@ za "
        "hodinu.",
    "How to find yours": "Ako zistiť svoju rýchlosť",
    "With a breathalyser": "S alkoholtesterom",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Fúkni dvakrát, s odstupom aspoň jednej hodiny, na klesajúcej strane – dve alebo viac "
        "hodín po poslednom nápoji a medzitým nič nepi. Od prvej hodnoty odčítaj druhú a vydeľ "
        "počtom hodín medzi nimi.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Napríklad %@ a o dve hodiny neskôr %@ dáva %@ za hodinu.",
    "Without one": "Bez neho",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Aplikácia ti povie, kedy podľa nej alkohol vyprchá. Ak si spoľahlivo v normále "
        "výrazne skôr, tvoja rýchlosť je vyššia než nastavená – posuň ju o krok nahor a sleduj "
        "to počas niekoľkých posedení. Ak to trvá dlhšie, než predpovedá, posuň ju nadol.",
    "What moves it": "Čo ju ovplyvňuje",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Pravidelné pitie ju zvyšuje: pečeňový enzým, ktorý túto prácu robí, sa používaním "
        "indukuje. U žien býva v priemere mierne vyššia a na prázdny žalúdok alebo pri "
        "problémoch s pečeňou nižšia.",
    "Uncertainty": "Neistota",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Pri nule je každý údaj jediné číslo – najlepší odhad aplikácie. Nad nulou sa tie isté "
        "údaje zobrazujú ako rozpätia a pás v grafe sa tomu úmerne rozšíri.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Podľa jediného čísla sa to ľahšie naučíš: časom zistíš, ako sa cítiš pri svojich 0,6. Rozpätie je "
        "doslovnejšia odpoveď, pretože rýchlosť je naozaj neistá. Oboje sa dá obhájiť – "
        "rozhodnutie je na tebe.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Rozptyl, ktorý vyplýva z tvojej frekvencie pitia, je ± %@ za hodinu.",
    "Rate": "Rýchlosť",
    "Range": "Rozpätie",
    "Advanced": "Rozšírené",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Viac osôb",
    "History trends": "Trendy v histórii",
    "Week": "Týždeň",
    "Month": "Mesiac",
    "Year": "Rok",
    "Sober days": "Dni bez alkoholu",
    "Change": "Zmena",
    "before records": "pred začiatkom záznamov",
    "See further back": "Pozrieť sa ďalej do minulosti",
    "Weeks, months and years side by side — and every evening older than seven days.": "Týždne, mesiace a roky vedľa seba – a každý večer starší ako sedem dní.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Všetko, čo si zaznamenal, je už uložené. Odomknutie to len zobrazí.",
    "Coming soon": "Už čoskoro",
    "Today": "Dnes",
    "Day": "Deň",
    "Yesterday": "Včera",
    "No drinks on this day": "V tento deň žiadne nápoje",
    "Trend": "Trend",
    "day": "deň",
    "Smoothing": "Vyhladenie",
    "%@ sessions": "Posedenia: %@",
    "No data before %@": "Žiadne údaje pred %@",
    "vs.": "oproti",
    "Grams": "Gramy",
    "Grams of alcohol": "Gramy alkoholu",
    "Standard units": "Štandardné jednotky",
    "Unit size": "Veľkosť jednotky",
    "Automatic": "Automaticky",
    "UK": "Spojené kráľovstvo",
    "Nordic countries": "Severské krajiny",
    "US standard drink": "Štandardný nápoj v USA",
    "WHO, most of Europe": "WHO, väčšina Európy",
    "Period": "Obdobie",
    "Switch person": "Prepnúť osobu",
    "Add person": "Pridať osobu",
    "New person": "Nová osoba",
    "You": "Ty",
    "Name": "Meno",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Všetky štyri údaje menia krivku, takže ani jeden z nich sa nedá odhadnúť za niekoho "
        "iného.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Vlastný limit a jemnejšie nastavenia sa dajú zmeniť neskôr na karte Profil, keď je "
        "táto osoba vybraná.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Rýchle pridanie",
    "Choose a favourite drink": "Vyber si obľúbený nápoj",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Vyber si nápoj, ktorý si zvyčajne dávaš, a tlačidlo na obrazovke Naživo ho zaznamená "
        "jedným klepnutím.",
    "This is your quick-add drink": "Toto je tvoj nápoj na rýchle pridanie",
    "Set as my quick-add drink": "Nastaviť ako môj nápoj na rýchle pridanie",
    "This is now your usual": "Toto je odteraz tvoj obvyklý nápoj",
    "Remove favourite": "Odstrániť obľúbený nápoj",
    "Always add this one": "Vždy pridávať tento nápoj",
    "Logs it straight away, without opening anything.":
        "Zaznamená ho okamžite, bez otvárania čohokoľvek.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Jedno klepnutie na obrazovke Naživo ho zaznamená, na tlačidle je predpokladaný vrchol. "
        "Plnosť žalúdka sa prevezme z predchádzajúceho nápoja a hneď potom sa dá opraviť.",
    "Peak %@": "Vrchol %@",
    "%@ added": "Pridané: %@",
    "Save": "Uložiť",
    "Undo": "Späť",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Záloha",
    "Export a backup": "Exportovať zálohu",
    "Import a backup": "Importovať zálohu",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Záloha obsahuje všetky osoby, posedenia a nápoje. Import doplní to, čo chýba – nikdy "
        "nezmení ani neodstráni nič, čo tu už je.",
    "Import this backup?": "Importovať túto zálohu?",
    "Import": "Importovať",
    "Everything in this backup is already here.": "Všetko z tejto zálohy tu už je.",
    "Import finished": "Import dokončený",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Jazyk",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Otvorí túto aplikáciu v Nastaveniach, kde položka „Preferovaný jazyk“ nastaví jazyk "
        "samotnej aplikácie – jazyk systému zostane nezmenený. iOS po zmene aplikáciu "
        "reštartuje.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Import sa nepodaril",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Tento súbor nie je zálohou LogMyDrink alebo je poškodený.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Táto záloha pochádza z novšej verzie LogMyDrink. Aktualizuj aplikáciu a skús to "
        "znova.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Doplní: posedenia (%@), nápoje (%@), mesačné súčty (%@). Nič, čo tu už je, sa nezmení ani neodstráni.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Doplnené posedenia (%@), nápoje (%@) a mesačné súčty (%@).',
    'months as totals': 'mesiacov len ako súčet',
    'by month only': 'len po mesiacoch',
    'monthly total': 'mesačný súčet',
    'No daily records for this day': 'Pre tento deň nie sú denné záznamy',
    'Monthly total: %@': 'Mesačný súčet: %@',
    'A dry month': 'Suchý mesiac',

    # --- RemovePersonSection ---
    'Remove %@?': 'Odstrániť %@?',
    'Remove': 'Odstrániť',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Vymaže posedenia (%@), nápoje (%@) a mesačné súčty (%@). Nedá sa to vrátiť späť.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Vymaže posedenia (%@) a nápoje (%@). Nedá sa to vrátiť späť.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Potiahni hosťa doľava, ak ho chceš odstrániť so všetkým, čo je pri ňom zaznamenané. Teba odstrániť nemožno.',
    'People': 'Ľudia',
    'Owner': 'Vlastník',
    'Everyone this app records. Switch, add, or remove someone.': 'Všetci, ktorých táto aplikácia zaznamenáva. Prepni, pridaj alebo odstráň niekoho.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Prenesené z predchádzajúceho večera',
    # --- History, second card (5.24) ---
    'Calories': 'Kalórie',
    'Sessions': 'Posedenia',
    'Per session': 'Na posedenie',
    'Under the influence': 'Pod vplyvom',
    '%@ of the time': '%@ času',
    'Days over limit': 'Dni nad limitom',
    'Longest sober run': 'Najdlhšia séria bez alkoholu',
    'Favourite drink': 'Obľúbený nápoj',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Zobrazenie a jazyk",
    "Data": "Údaje",
    "Concentration": "Koncentrácia",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Rýchlosť nechaj na otázke o frekvencii, ak nemáš meranie, s ktorým by si ju mohol porovnať.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Odhad, nie meranie. Nikdy podľa toho nerozhoduj, či môžeš šoférovať.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Odhadované rozpätie, nie meranie. Nikdy podľa toho nerozhoduj, či môžeš šoférovať.',
    'How does the app calculate this?':
        'Ako to aplikácia počíta?',
    'approximately %@ %@':
        'približne %@ %@',
    'How it works':
        'Ako to funguje',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nikdy podľa toho nerozhoduj, či môžeš šoférovať. Aplikácia odhaduje, nemeria, a tvoja skutočná hladina sa môže výrazne líšiť.',
    'Why this app exists':
        'Prečo táto aplikácia existuje',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink ti pomáha piť vedomejšie a mať pitie pod kontrolou. Rozhodnutie padá pred ďalším pohárom, preto ti aplikácia vopred ukáže, kam by tvoju hladinu dostal ďalší nápoj a kedy by vyvrcholila.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Nejde však len o dnešný večer. Každý zapísaný nápoj sa uloží do Histórie, takže počas mesiacov a rokov vidíš, koľko, ako často a do akej hladiny piješ. Vynoria sa z toho tvoje vzorce aj smer, ktorým sa menia – či sa veci zlepšujú, alebo zhoršujú.',
    'How it calculates':
        'Ako aplikácia počíta',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Odhad vychádza z Widmarkovej metódy, ktorou sa hladina alkoholu v krvi odhaduje od 30. rokov 20. storočia; aplikácia používa jej vylepšenú verziu.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Z tvojej hmotnosti, výšky, veku a pohlavia vypočíta, koľko vody tvoje telo obsahuje, pretože v nej sa alkohol rozptýli. Každý nápoj sleduje zvlášť: koľko alkoholu obsahoval, ako rýchlo si ho vypil a koľko si predtým zjedol, lebo od toho závisí rýchlosť vstrebávania.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Medzitým pečeň každú hodinu odbúra zhruba stále množstvo; koľko je to u teba, sa odhaduje podľa toho, ako často piješ. Výsledkom je krivka minútu po minúte: kde si teraz, kam smeruješ a kedy budeš opäť na nule.',
    'Details':
        'Podrobnosti',
    'Body water':
        'Telesná voda',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsonov vzorec (1980) z hmotnosti, výšky, veku a pohlavia. Vzorec pre ženy vek neobsahuje – je to vlastnosť vzorca, nie chyba. Distribučný objem je telesná voda delená 0,85, teda obsahom vody v krvi.',
    'Absorption':
        'Vstrebávanie',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Každý nápoj má svoj vlastný „žalúdok“. Nalačno sa polovica alkoholu vstrebe asi za 7 minút, s plným žalúdkom asi za 21. Nápoj, ktorý popíjaš, sa do žalúdka dostáva rovnomerne počas celého pitia.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Dáva nižší vrchol a skorší návrat na nulu. Prekvapivé, ale namerané: s jedlom žalúdok časť alkoholu rozloží ešte pred vstrebaním (aplikácia počíta s 5, 10 a 15 percentami) a čo sa do krvi nikdy nedostalo, netreba odbúravať.',
    'Elimination':
        'Odbúravanie',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Asi 0,15 ‰ za hodinu (rozpätie v literatúre 0,10–0,25), u pravidelne pijúcich viac, pretože sa pečeňové enzýmy prispôsobia. Blízko nuly sa spomalí (Michaelisova-Mentenovej kinetika), takže krivka plynulo dobieha namiesto náhleho zlomu.',
    'Computation':
        'Výpočet',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Krivka vzniká numerickou simuláciou s rozlíšením jednej minúty.',
    'Why it is only an estimate':
        'Prečo je to len odhad',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Aplikácia nič nemeria. To, čo ukazuje, je výsledok modelu s priemernými hodnotami a skutočnosť sa môže líšiť. Najväčšou neznámou je, ako rýchlo alkohol odbúravaš: v rámci vierohodného rozpätia to samo môže posunúť vrchol o 40 percent a návrat na nulu o štyri hodiny počas jediného večera.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Úlohu hrá aj genetika, stav pečene, lieky, jedlo, spánok a únava – nič z toho aplikácia nepozná. Presnú hodnotu dá len overený dychový analyzátor alebo krvný test.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Číslo je napriek tomu užitočné. Ak aplikácia u teba sústavne ukazuje trochu viac alebo menej, mýli sa každý večer rovnakým smerom, takže sa časom naučíš, čo pre teba daná hodnota znamená. V Profile si môžeš zobraziť aj neistotu rýchlosti odbúravania: namiesto jedného čísla potom uvidíš rozpätie.',
    'Tips':
        'Tipy',
    'Favourite drink in one tap':
        'Obľúbený nápoj jedným klepnutím',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Nastav si v Profile obľúbený nápoj a tlačidlo na obrazovke Naživo ho zapíše jedným klepnutím.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Pridaj ho na zamknutú obrazovku alebo na plochu: jedno klepnutie zapíše tvoj obľúbený nápoj. Kým máš v tele alkohol, ukazuje aj tvoju hladinu a jej smer.',
    'How do I add it?':
        'Ako ho pridám?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Povedz „Hey Siri, LogMyDrink now“ a Siri zapíše tvoj obľúbený nápoj a povie ti, kam smeruje tvoj vrchol. (Príkaz funguje v angličtine.)',
    'Looking back':
        'Pohľad späť',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Včera“ hore na obrazovke Naživo ťa jedným klepnutím prenesie na predchádzajúci deň; karta História ukazuje tvoje vzorce za týždne, mesiace a roky.',
    'Logging later':
        'Dodatočný zápis',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Keď zapisuješ nápoj dodatočne, posuň čas späť tlačidlami − a +; vynechaný deň môžeš doplniť v zobrazení Deň v Histórii.',
    'One tap and done':
        'Jedno klepnutie a hotovo',
    'Your favourite from the Lock Screen':
        'Obľúbený nápoj zo zamknutej obrazovky',
    'Say it, don’t type it':
        'Povedz to, nepíš to',
    'See your patterns':
        'Pozri sa na svoje vzorce',
    'Set what you drink most often and log it with a single tap.':
        'Nastav, čo piješ najčastejšie, a zapisuj to jedným klepnutím.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Jedno klepnutie na widget zapíše tvoj obľúbený nápoj, bez hľadania aplikácie. Večer ukazuje aj tvoju hladinu.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now“ – Siri zapíše tvoj obľúbený nápoj a povie ti, kam smeruje tvoj vrchol.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'História ukazuje, koľko a do akej hladiny piješ za týždne, mesiace a roky, a ktorým smerom sa to mení.',
    'Set favourite':
        'Nastaviť obľúbený',
    'Add widget':
        'Pridať widget',
    'Got it':
        'Rozumiem',
    'Open History':
        'Otvoriť Históriu',
    'Don’t show again':
        'Už nezobrazovať',
    'Lock Screen':
        'Zamknutá obrazovka',
    'Home Screen':
        'Plocha',
    'Where':
        'Kam',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Zamkni iPhone a potom sa dotkni zamknutej obrazovky a podrž ju.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Klepni na Prispôsobiť, potom na Zamknutá obrazovka a nakoniec na riadok widgetov pod hodinami.',
    'Choose LogMyDrink, then tap Done.':
        'Vyber LogMyDrink a klepni na Hotovo.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Stlač a podrž prázdne miesto na ploche, kým sa ikony nezačnú triasť.',
    'Tap Edit, then Add Widget.':
        'Klepni na Upraviť a potom na Pridať widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Vyhľadaj LogMyDrink, vyber veľkosť a klepni na Pridať widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Klepnutie na widget otvorí aplikáciu a zapíše tvoj obľúbený nápoj. Kým máš v tele alkohol, ukazuje aj tvoju hladinu a jej smer.',
    'Add the widget':
        'Pridať widget',
    'Show tips':
        'Zobrazovať tipy',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Najviac jeden tip denne pri otvorení aplikácie – nikdy, kým máš v tele alkohol.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Čo číslo ukazuje',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Číslo je odhad koncentrácie alkoholu v tvojej krvi (po anglicky BAC, blood alcohol concentration): koľko alkoholu máš v krvi.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'V promile (‰) ide o gramy alkoholu na liter krvi: 0,5 ‰ znamená pol gramu v každom litri. V percentách ide o gramy na 100 mililitrov, takže rovnaká hladina dáva desaťkrát menšie číslo: 0,5 ‰ je 0,05 percenta. Prepnúť môžeš v časti Profil › Zobrazenie a jazyk.',
    'The curve shows the same level over time, minute by minute.':
        'Krivka ukazuje rovnakú hladinu v čase, minútu po minúte.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promile (‰) sú gramy alkoholu na liter krvi, percentá gramy na 100 mililitrov: 0,5 ‰ je 0,05 percenta.',
}
