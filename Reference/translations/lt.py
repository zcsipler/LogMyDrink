"""
Lithuanian.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promilės",
    "Percent": "Procentai",

    # --- DrinkCatalog: drink types ---
    "Beer": "Alus",
    "Wine": "Vynas",
    "Champagne": "Putojantis",
    "Shot": "Taurelė",
    "Cocktail": "Kokteilis",
    "Custom": "Pasirinktinis",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Tuščias skrandis",
    "Moderately full": "Vidutiniškai pilnas",
    "Full stomach": "Pilnas skrandis",
    "Empty": "Tuščias",
    "Moderate": "Vidutinis",
    "Full": "Pilnas",
    "Fast absorption, higher and earlier peak.":
        "Greita absorbcija, aukštesnė ir ankstesnė viršūnė.",
    "Moderate absorption.": "Vidutinė absorbcija.",
    "Slow absorption, lower and later peak.": "Lėta absorbcija, žemesnė ir vėlesnė viršūnė.",

    # --- DrinkingFrequency ---
    "Rarely": "Retai",
    "A few times a month": "Kelis kartus per mėnesį",
    "Several times a week": "Kelis kartus per savaitę",
    "Almost daily": "Beveik kasdien",
    "A few occasions a year": "Kelis kartus per metus",
    "Social drinking": "Proginis gėrimas",
    "Weekly routine": "Kassavaitinis įprotis",
    "Daily or nearly daily": "Kasdien arba beveik kasdien",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Laikas",
    "Level": "Lygis",
    "Lower": "Apatinis",
    "Upper": "Viršutinis",
    "Lower estimate": "Apatinis įvertis",
    "Upper estimate": "Viršutinis įvertis",
    "Personal limit": "Asmeninė riba",
    "Drink": "Gėrimas",

    # --- BACChartView ---
    "Expected peak around %@": "Numatoma viršūnė apie %@",
    "Peaked around %@": "Viršūnė buvo apie %@",
    "No active session": "Nėra aktyvios sesijos",
    "Still rising": "Vis dar kyla",
    "YOUR LIMIT %@": "TAVO RIBA %@",
    "possible range": "galimas intervalas",

    # --- Live screen: the day with nothing on it ---
    "Live": "Tiesiogiai",
    "Nothing logged today": "Šiandien nieko neįrašyta",
    "Add a drink when you have one.": "Pridėk gėrimą, kai jį išgeri.",

    # --- Tabs and history ---
    "History": "Istorija",
    "No past sessions yet": "Praėjusių sesijų dar nėra",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Sesija čia atsiranda jai pasibaigus — kai alkoholis išnyksta ir praeina kelios "
        "valandos.",
    "%@ drinks": "Gėrimų: %@",
    "peak": "viršūnė",
    "Started": "Pradėta",
    "Lasted": "Truko",
    "Duration": "Trukmė",
    "Sober around": "Blaivus apyt.",
    "Sober at": "Blaivus",
    "Remaining": "Liko",
    "next day": "kitą dieną",
    "previous day": "ankstesnę dieną",
    "%@ days later": "po %@ d.",
    "%@ days earlier": "prieš %@ d.",
    "Calculated with your profile at the time": "Apskaičiuota pagal tuometinį tavo profilį",

    # --- TodayView ---
    "Profile": "Profilis",
    "Drinks": "Gėrimai",
    "Units": "Vienetai",
    "Drinks this session": "Šios sesijos gėrimai",
    "Add drink": "Pridėti gėrimą",

    # --- Editing an already logged drink ---
    "Edit drink": "Redaguoti gėrimą",
    "Save changes": "Išsaugoti pakeitimus",
    "With this": "Su šiuo gėrimu",
    "Delete": "Ištrinti",
    "tap to edit · swipe to delete": "bakstelėk, kad redaguotum · perbrauk, kad ištrintum",

    # --- Drinking pace ---
    "How fast": "Kaip greitai",
    "In one go": "Vienu mauku",
    "Counts as a single swallow — the steepest possible rise.":
        "Skaičiuojama kaip vienas gurkšnis — sparčiausias įmanomas kilimas.",
    "A quick drink. The level climbs fast.": "Greitai išgertas gėrimas. Lygis kyla sparčiai.",
    "A normal pace.": "Įprastas tempas.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Geriama lėtai. Tas pats alkoholio kiekis kyla daug švelniau.",

    # --- AddDrinkSheet ---
    "Cancel": "Atšaukti",
    "Now": "Dabar",
    "Projected peak": "Numatoma viršūnė",
    "Peak at": "Viršūnė",
    "Clears": "Išnyks",
    "This would cross your limit": "Tai peržengtų tavo ribą",
    "Around %@, for up to %@.": "Apie %@, ne ilgiau kaip %@.",
    "This might cross your limit": "Tai gali peržengti tavo ribą",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Esant lėtesnei medžiagų apykaitai — taip, esant greitesnei — ne. Toks yra šio įverčio "
        "neapibrėžtumas.",
    "Type": "Tipas",
    "Amount": "Kiekis",
    "Strength": "Stiprumas",
    "%@ units": "Vienetų: %@",
    "%@ g alcohol": "%@ g alkoholio",
    "Stomach": "Skrandis",
    "When": "Kada",
    "Done": "Atlikta",
    "Add": "Pridėti",

    # --- ProfileSheet ---
    "Male": "Vyras",
    "Female": "Moteris",
    "Sex": "Lytis",
    "Weight": "Svoris",
    "Height": "Ūgis",
    "Age": "Amžius",
    "kg": "kg",
    "cm": "cm",
    "yrs": "m.",
    "Body": "Kūnas",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Bendras kūno vandens kiekis apskaičiuojamas pagal Watson lygtis, kurios nustato tūrį, "
        "kuriame pasiskirsto alkoholis.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Bendras kūno vandens kiekis apskaičiuojamas pagal Watson lygtis, kurios nustato tūrį, "
        "kuriame pasiskirsto alkoholis. Moterų lygtyje amžius neįtraukiamas, todėl jo keitimas "
        "rezultato nepakeis.",
    "Drinking frequency": "Gėrimo dažnis",
    "How often do you drink?": "Kaip dažnai geri?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Taip vertiname tavo šalinimo greitį. Reguliarus gėrimas suaktyvina kepenų CYP2E1 kelią, todėl dažnai geriantieji alkoholį pašalina greičiau. Tai silpniausia modelio vieta — todėl skiltyje „Rodymas ir kalba“ gali pasirinkti, kiek to neapibrėžtumo programėlė tau rodo.",
    "Your limit": "Tavo riba",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Tai tavo paties orientacinis skaičius, o ne teisinė riba. Programėlė pasako, kada "
        "planuojamas gėrimas ją peržengtų ir kiek laiko liktum virš jos.",
    "Calculated values": "Apskaičiuotos reikšmės",
    "Total body water": "Bendras kūno vandens kiekis",
    "Distribution volume": "Pasiskirstymo tūris",
    "Widmark factor": "Widmark faktorius",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmark faktorius paprastai yra apie 0,68 vyrams ir 0,55 moterims. Jei tavasis nuo to "
        "labai skiriasi, verta patikrinti aukščiau esančias reikšmes.",
    "Elimination rate": "Šalinimo greitis",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Kaip greitai tavo kepenys pašalina alkoholį po to, kai jis įsisavinamas, — "
        "krintančios kreivės dalies nuolydis.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkoholis pasišalina maždaug pastoviu kiekiu per valandą, o ne procentais, nes jį "
        "skaidantis fermentas beveik esant bet kokiam lygiui jau dirba visu pajėgumu. Būtent "
        "todėl apskritai egzistuoja tokios praktinės taisyklės kaip „vienas gėrimas per "
        "valandą“.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Esant šiam nustatymui, %@ išnyksta maždaug per %@. Beveik visi patenka į intervalą %@ "
        "per valandą.",
    "How to find yours": "Kaip sužinoti savąjį",
    "With a breathalyser": "Su alkotesteriu",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Papūsk du kartus, bent valandos skirtumu, krintančioje kreivės dalyje — praėjus dviem "
        "ar daugiau valandų po paskutinio gėrimo ir nieko negeriant tarp matavimų. Iš pirmojo "
        "rodmens atimk antrąjį ir padalyk iš valandų skaičiaus tarp jų.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Pavyzdžiui, %@ ir %@ po dviejų valandų duoda %@ per valandą.",
    "Without one": "Be jo",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Programėlė pasako, kada, jos skaičiavimu, alkoholis turėtų išnykti. Jei nuolat "
        "pasijunti visiškai blaivus gerokai anksčiau, tavo greitis didesnis nei nustatyta — "
        "pakelk jį vienu žingsniu ir stebėk kelias sesijas. Jei tai trunka ilgiau, nei "
        "prognozuojama, sumažink.",
    "What moves it": "Kas jį keičia",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Reguliarus gėrimas jį didina: darbą atliekantis kepenų fermentas suaktyvėja nuo "
        "naudojimo. Vidutiniškai jis taip pat šiek tiek didesnis moterims, o tuščiu skrandžiu "
        "ar esant kepenų sutrikimų — mažesnis.",
    "Uncertainty": "Neapibrėžtumas",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Ties nuliu kiekviena reikšmė rodoma kaip vienas skaičius — geriausias programėlės "
        "įvertis. Virš nulio tos pačios reikšmės rodomos kaip intervalai, o juosta diagramoje "
        "atitinkamai praplatėja.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Iš vieno skaičiaus lengviau mokytis: laikui bėgant sužinai, kaip jautiesi, kai tavo "
        "lygis yra 0,6. Intervalas yra tikslesnis atsakymas, nes greitis iš tiesų nėra "
        "tiksliai žinomas. Abu variantai pagrįsti — spręsk pats.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Pagal tavo gėrimo dažnį siūloma sklaida yra ± %@ per valandą.",
    "Rate": "Greitis",
    "Range": "Intervalas",
    "Advanced": "Išplėstiniai nustatymai",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Keli žmonės",
    "History trends": "Istorijos tendencijos",
    "Week": "Savaitė",
    "Month": "Mėnuo",
    "Year": "Metai",
    "Sober days": "Dienos be alkoholio",
    "Change": "Pokytis",
    "before records": "prieš įrašų pradžią",
    "See further back": "Pažvelkite toliau atgal",
    "Weeks, months and years side by side — and every evening older than seven days.": "Savaitės, mėnesiai ir metai vienas šalia kito – ir kiekvienas vakaras, senesnis nei septynios dienos.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Viskas, ką įrašėte, jau išsaugota. Atrakinimas tik tai parodo.",
    "Coming soon": "Netrukus",
    "Today": "Šiandien",
    "Day": "Diena",
    "Yesterday": "Vakar",
    "No drinks on this day": "Šią dieną gėrimų nebuvo",
    "Trend": "Tendencija",
    "day": "diena",
    "Smoothing": "Glodinimas",
    "%@ sessions": "%@ progos",
    "No data before %@": "Nėra duomenų iki %@",
    "vs.": "palyginti su",
    "Grams": "Gramai",
    "Grams of alcohol": "Gramai alkoholio",
    "Standard units": "Standartiniai vienetai",
    "Unit size": "Vieneto dydis",
    "Automatic": "Automatiškai",
    "UK": "Jungtinė Karalystė",
    "Nordic countries": "Šiaurės šalys",
    "US standard drink": "JAV standartinis gėrimas",
    "WHO, most of Europe": "PSO, didžioji Europos dalis",
    "Period": "Laikotarpis",
    "Switch person": "Keisti žmogų",
    "Add person": "Pridėti žmogų",
    "New person": "Naujas žmogus",
    "You": "Tu",
    "Name": "Vardas",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Visi keturi keičia kreivę, todėl nė vieno iš jų negalima atspėti už kitą žmogų.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Jo asmeninę ribą ir smulkesnius nustatymus vėliau gali pakeisti skiltyje „Profilis“, "
        "kai jis yra pasirinktas žmogus.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Greitasis pridėjimas",
    "Choose a favourite drink": "Pasirink mėgstamą gėrimą",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Pasirink gėrimą, kurį dažniausiai užsisakai, ir mygtukas ekrane „Tiesiogiai“ įrašys "
        "jį vienu bakstelėjimu.",
    "This is your quick-add drink": "Tai tavo greitojo pridėjimo gėrimas",
    "Set as my quick-add drink": "Nustatyti kaip greitojo pridėjimo gėrimą",
    "This is now your usual": "Nuo šiol tai tavo įprastas gėrimas",
    "Remove favourite": "Pašalinti mėgstamą",
    "Always add this one": "Visada pridėti šį",
    "Logs it straight away, without opening anything.":
        "Iš karto jį įrašo, nieko papildomai neatidarant.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Vienu bakstelėjimu ekrane „Tiesiogiai“ šis gėrimas įrašomas, o ant mygtuko matai "
        "numatomą viršūnę. Skrandžio pilnumas paimamas iš ankstesnio gėrimo ir gali būti "
        "pataisytas iš karto po to.",
    "Peak %@": "Viršūnė %@",
    "%@ added": "Pridėta: %@",
    "Save": "Išsaugoti",
    "Undo": "Atšaukti veiksmą",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Atsarginė kopija",
    "Export a backup": "Eksportuoti atsarginę kopiją",
    "Import a backup": "Importuoti atsarginę kopiją",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Atsarginėje kopijoje yra visi žmonės, sesijos ir gėrimai. Importavimas prideda tai, "
        "ko trūksta, — jis niekada nekeičia ir nepašalina to, kas jau yra.",
    "Import this backup?": "Importuoti šią atsarginę kopiją?",
    "Import": "Importuoti",
    "Everything in this backup is already here.": "Viskas iš šios atsarginės kopijos jau yra.",
    "Import finished": "Importavimas baigtas",
    "OK": "Gerai",

    # --- LanguageSection: the app's language ---
    "Language": "Kalba",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Atveria šią programėlę Nustatymuose, kur „Pageidaujama kalba“ nustato pačios "
        "programėlės kalbą — sistemos kalba lieka tokia pati. Pakeitus ją, iOS paleidžia "
        "programėlę iš naujo.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Nepavyko importuoti",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Šis failas nėra „LogMyDrink“ atsarginė kopija arba yra sugadintas.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Ši atsarginė kopija sukurta naujesne „LogMyDrink“ versija. Atnaujink programėlę ir "
        "bandyk dar kartą.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Bus pridėta sesijų: %@, gėrimų: %@ ir mėnesio sumų: %@. Niekas, kas jau yra, nebus pakeista ar pašalinta.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Pridėta: %@ sesijos, %@ gėrimai ir %@ mėnesio sumos.',
    'months as totals': 'mėn. tik kaip sumos',
    'by month only': 'tik pagal mėnesį',
    'monthly total': 'mėnesio suma',
    'No daily records for this day': 'Šiai dienai nėra dienos įrašų',
    'Monthly total: %@': 'Mėnesio suma: %@',
    'A dry month': 'Blaivus mėnuo',

    # --- RemovePersonSection ---
    'Remove %@?': 'Pašalinti %@?',
    'Remove': 'Pašalinti',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Ištrina sesijas: %@, gėrimus: %@ ir mėnesio sumas: %@. To atšaukti negalima.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Ištrina sesijas: %@ ir gėrimus: %@. To atšaukti negalima.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Braukite kairėn ant svečio, kad pašalintumėte jį su viskuo, kas jam užfiksuota. Jūsų pašalinti negalima.',
    'People': 'Žmonės',
    'Owner': 'Savininkas',
    'Everyone this app records. Switch, add, or remove someone.': 'Visi, kuriuos fiksuoja ši programa. Perjunkite, pridėkite arba pašalinkite ką nors.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Perkelta iš praėjusio vakaro',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorijos',
    'Sessions': 'Progos',
    'Per session': 'Per progą',
    'Under the influence': 'Apsvaigęs',
    '%@ of the time': '%@ laiko',
    'Days over limit': 'Dienos virš ribos',
    'Longest sober run': 'Ilgiausia blaivi serija',
    'Favourite drink': 'Mėgstamiausias gėrimas',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Rodymas ir kalba",
    "Data": "Duomenys",
    "Concentration": "Koncentracija",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Greitį palik dažnumo klausimui, nebent turi matavimą, su kuriuo jį galėtum palyginti.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Įvertis, ne matavimas. Niekada pagal tai nespręsk, ar gali vairuoti.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Įvertintas intervalas, ne matavimas. Niekada pagal tai nespręsk, ar gali vairuoti.',
    'How does the app calculate this?':
        'Kaip programėlė skaičiuoja?',
    'approximately %@ %@':
        'apie %@ %@',
    'How it works':
        'Kaip tai veikia',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Niekada pagal tai nespręsk, ar gali vairuoti. Programėlė vertina, o ne matuoja, ir tavo tikrasis lygis gali labai skirtis.',
    'Why this app exists':
        'Kam ši programėlė',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink padeda gerti sąmoningiau ir išlaikyti kontrolę. Sprendimas priimamas prieš kitą taurę, todėl programėlė iš anksto parodo, kur dar vienas gėrimas nuvestų tavo lygį ir kada jis pasiektų piką.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Tačiau kalba ne tik apie šį vakarą. Kiekvienas įrašytas gėrimas patenka į istoriją, tad per mėnesius ir metus matai, kiek, kaip dažnai ir kaip aukštai geri. Iš to išryškėja tavo įpročiai ir kryptis, kuria jie keičiasi – ar padėtis gerėja, ar blogėja.',
    'How it calculates':
        'Kaip ji skaičiuoja',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Įvertis remiasi Widmarko metodu, kuriuo alkoholio koncentracija kraujyje vertinama nuo XX a. 4-ojo dešimtmečio; programėlė naudoja patobulintą jo versiją.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Pagal tavo svorį, ūgį, amžių ir lytį ji apskaičiuoja, kiek vandens yra tavo kūne, nes būtent jame pasiskirsto alkoholis. Kiekvieną gėrimą ji seka atskirai: kiek jame buvo alkoholio, kaip greitai jį išgėrei ir kiek buvai valgęs, nes nuo to priklauso įsigėrimo greitis.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Tuo metu kepenys kas valandą suskaido maždaug pastovų kiekį; tavo kiekis vertinamas pagal tai, kaip dažnai geri. Rezultatas – kreivė minutė po minutės: kur esi dabar, kur link eini ir kada vėl būsi ties nuliu.',
    'Details':
        'Išsamiau',
    'Body water':
        'Kūno vanduo',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsono formulė (1980) pagal svorį, ūgį, amžių ir lytį. Moterų formulėje amžiaus nėra – tai formulės savybė, ne klaida. Pasiskirstymo tūris – kūno vanduo, padalytas iš 0,85, t. y. vandens kiekio kraujyje.',
    'Absorption':
        'Įsigėrimas',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Kiekvienas gėrimas turi savo „skrandį“. Tuščiu skrandžiu pusė alkoholio įsigeria maždaug per 7 minutes, pilnu – maždaug per 21. Gurkšnojamas gėrimas į skrandį patenka tolygiai visą gėrimo laiką.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Duoda žemesnį piką ir ankstesnį nulį. Stebina, bet išmatuota: su maistu skrandis dalį alkoholio suskaido dar prieš įsigėrimą (programėlė skaičiuoja 5, 10 ir 15 procentų), o to, kas niekada nepateko į kraują, skaidyti nereikia.',
    'Elimination':
        'Skaidymas',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Apie 0,15 ‰ per valandą (skelbiamas intervalas 0,10–0,25), reguliariai geriantiems daugiau, nes kepenų fermentai prisitaiko. Arti nulio jis sulėtėja (Michaelio–Menten kinetika), todėl kreivė palaipsniui išsilygina, o ne staiga nutrūksta.',
    'Computation':
        'Skaičiavimas',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Kreivė gaunama skaitmeniniu modeliavimu vienos minutės tikslumu.',
    'Why it is only an estimate':
        'Kodėl tai tik įvertis',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Programėlė nieko nematuoja. Ji rodo vidutinėmis reikšmėmis pagrįsto modelio rezultatą, o tikrovė gali skirtis. Didžiausias nežinomasis – kaip greitai skaidai alkoholį: tikėtino intervalo ribose vien tai tą patį vakarą gali paslinkti piką 40 procentų, o nulį – keturiomis valandomis.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Reikšmės turi ir genetika, kepenų sveikata, vaistai, ką valgei, miegas ir nuovargis – nieko iš to programėlė nežino. Tikslią reikšmę duoda tik patikrintas alkotesteris arba kraujo tyrimas.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Vis dėlto skaičius naudingas. Jei programėlė tau nuolat rodo šiek tiek per daug ar per mažai, ji kiekvieną vakarą klysta ta pačia kryptimi, tad ilgainiui išmoksti, ką tam tikra reikšmė reiškia būtent tau. Profilyje gali parodyti ir skaidymo greičio neapibrėžtį: tada vietoj vieno skaičiaus matysi intervalą.',
    'Tips':
        'Patarimai',
    'Favourite drink in one tap':
        'Mėgstamas gėrimas vienu palietimu',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Nustatyk mėgstamą gėrimą Profilyje, ir ekrano Tiesiogiai mygtukas jį įrašys vienu palietimu.',
    'Widget':
        'Valdiklis',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Pridėk jį prie užrakinimo ar pradžios ekrano: vienas palietimas įrašo tavo mėgstamą gėrimą. Kol organizme yra alkoholio, jis rodo ir tavo lygį bei jo kryptį.',
    'How do I add it?':
        'Kaip jį pridėti?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Pasakyk „Hey Siri, LogMyDrink now“, ir Siri įrašys tavo mėgstamą gėrimą bei pasakys, kur link eina tavo pikas.',
    'Looking back':
        'Žvilgsnis atgal',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Vakar“ ekrano Tiesiogiai viršuje vienu palietimu nuveda į ankstesnę dieną; skirtukas Istorija rodo tavo įpročius per savaites, mėnesius ir metus.',
    'Logging later':
        'Įrašymas vėliau',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Jei gėrimą įrašai vėliau, atsuk laiką atgal mygtukais − ir +; praleistą dieną gali papildyti Istorijos dienos rodinyje.',
    'One tap and done':
        'Vienas palietimas – ir viskas',
    'Your favourite from the Lock Screen':
        'Mėgstamas gėrimas iš užrakinimo ekrano',
    'Say it, don’t type it':
        'Pasakyk, nerašyk',
    'See your patterns':
        'Pažiūrėk savo įpročius',
    'Set what you drink most often and log it with a single tap.':
        'Nustatyk, ką geri dažniausiai, ir įrašyk tai vienu palietimu.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Vienas palietimas valdiklyje įrašo tavo mėgstamą gėrimą be programėlės paieškos. Vakare jis rodo ir tavo lygį.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now“ – Siri įrašys tavo mėgstamą gėrimą ir pasakys, kur link eina tavo pikas.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Istorija rodo, kiek ir kaip aukštai geri per savaites, mėnesius ir metus ir kuria kryptimi tai keičiasi.',
    'Set favourite':
        'Nustatyti mėgstamą',
    'Add widget':
        'Pridėti valdiklį',
    'Got it':
        'Supratau',
    'Open History':
        'Atidaryti istoriją',
    'Don’t show again':
        'Daugiau nerodyti',
    'Lock Screen':
        'Užrakinimo ekranas',
    'Home Screen':
        'Pradžios ekranas',
    'Where':
        'Kur',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Užrakink „iPhone“ ir palaikyk pirštą ant užrakinimo ekrano.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Paliesk Tinkinti, tada Užrakinimo ekranas, o paskui valdiklių eilutę po laikrodžiu.',
    'Choose LogMyDrink, then tap Done.':
        'Pasirink LogMyDrink ir paliesk Atlikta.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Palaikyk pirštą tuščioje pradžios ekrano vietoje, kol piktogramos ims kraipytis.',
    'Tap Edit, then Add Widget.':
        'Paliesk Redaguoti, tada Pridėti valdiklį.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Surask LogMyDrink, pasirink dydį ir paliesk Pridėti valdiklį.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Palietus valdiklį atsidaro programėlė ir įrašomas tavo mėgstamas gėrimas. Kol organizme yra alkoholio, jis rodo ir tavo lygį bei jo kryptį.',
    'Add the widget':
        'Pridėti valdiklį',
    'Show tips':
        'Rodyti patarimus',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Ne daugiau kaip vienas patarimas per dieną atidarant programėlę – niekada, kol organizme yra alkoholio.',
}
