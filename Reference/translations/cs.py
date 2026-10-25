"""
Czech.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promile",
    "Percent": "Procenta",

    # --- DrinkCatalog: drink types ---
    "Beer": "Pivo",
    "Wine": "Víno",
    "Champagne": "Šumivé víno",
    "Shot": "Panák",
    "Cocktail": "Koktejl",
    "Custom": "Vlastní",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Prázdný žaludek",
    "Moderately full": "Středně plný",
    "Full stomach": "Plný žaludek",
    "Empty": "Prázdný",
    "Moderate": "Střední",
    "Full": "Plný",
    "Fast absorption, higher and earlier peak.": "Rychlé vstřebávání, vyšší a dřívější vrchol.",
    "Moderate absorption.": "Středně rychlé vstřebávání.",
    "Slow absorption, lower and later peak.": "Pomalé vstřebávání, nižší a pozdější vrchol.",

    # --- DrinkingFrequency ---
    "Rarely": "Zřídka",
    "A few times a month": "Několikrát měsíčně",
    "Several times a week": "Několikrát týdně",
    "Almost daily": "Téměř denně",
    "A few occasions a year": "Několikrát ročně",
    "Social drinking": "Společenské pití",
    "Weekly routine": "Pravidelně každý týden",
    "Daily or nearly daily": "Denně nebo téměř denně",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Čas",
    "Level": "Hladina",
    "Lower": "Dolní",
    "Upper": "Horní",
    "Lower estimate": "Dolní odhad",
    "Upper estimate": "Horní odhad",
    "Personal limit": "Osobní limit",
    "Drink": "Nápoj",

    # --- BACChartView ---
    "Expected peak around %@": "Očekávaný vrchol kolem %@",
    "Peaked around %@": "Vrchol byl kolem %@",
    "No active session": "Žádné aktivní posezení",
    "Still rising": "Stále stoupá",
    "YOUR LIMIT %@": "TVŮJ LIMIT %@",
    "possible range": "možné rozpětí",

    # --- Live screen: the day with nothing on it ---
    "Live": "Aktuálně",
    "Nothing logged today": "Dnes nic nezaznamenáno",
    "Add a drink when you have one.": "Přidej nápoj, až si nějaký dáš.",

    # --- Tabs and history ---
    "History": "Historie",
    "No past sessions yet": "Zatím žádná minulá posezení",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Posezení se sem přidá, jakmile skončí – až hladina klesne na nulu a uplyne několik "
        "hodin.",
    "%@ drinks": "Nápoje: %@",
    "peak": "vrchol",
    "Started": "Začátek",
    "Lasted": "Trvalo",
    "Duration": "Trvání",
    "Sober around": "Střízlivý cca",
    "Sober at": "Střízlivý",
    "Remaining": "Zbývá",
    "next day": "následující den",
    "previous day": "předchozí den",
    "%@ days later": "o %@ dny později",
    "%@ days earlier": "o %@ dny dříve",
    "Calculated with your profile at the time": "Spočítáno podle tvého tehdejšího profilu",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Nápoje",
    "Units": "Jednotky",
    "Drinks this session": "Nápoje v tomto posezení",
    "Add drink": "Přidat nápoj",

    # --- Editing an already logged drink ---
    "Edit drink": "Upravit nápoj",
    "Save changes": "Uložit změny",
    "With this": "S ním",
    "Delete": "Smazat",
    "tap to edit · swipe to delete": "klepnutím upravíš · přejetím smažeš",

    # --- Drinking pace ---
    "How fast": "Jak rychle",
    "In one go": "Naráz",
    "Counts as a single swallow — the steepest possible rise.":
        "Počítá se jako jeden doušek – nejstrmější možný nárůst.",
    "A quick drink. The level climbs fast.": "Vypito rychle. Hladina rychle stoupá.",
    "A normal pace.": "Normální tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Popíjeno pomalu. Při stejném množství alkoholu mnohem mírnější nárůst.",

    # --- AddDrinkSheet ---
    "Cancel": "Zrušit",
    "Now": "Teď",
    "Projected peak": "Předpokládaný vrchol",
    "Peak at": "Vrchol v",
    "Clears": "Vystřízlivění",
    "This would cross your limit": "Tohle by překročilo tvůj limit",
    "Around %@, for up to %@.": "Kolem %@, nejdéle %@.",
    "This might cross your limit": "Tohle může překročit tvůj limit",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Při pomalejším metabolismu ano, při rychlejším ne. V tom je nejistota odhadu.",
    "Type": "Typ",
    "Amount": "Množství",
    "Strength": "Síla",
    "%@ units": "Jednotky: %@",
    "%@ g alcohol": "%@ g alkoholu",
    "Stomach": "Žaludek",
    "When": "Kdy",
    "Done": "Hotovo",
    "Add": "Přidat",

    # --- ProfileSheet ---
    "Male": "Muž",
    "Female": "Žena",
    "Sex": "Pohlaví",
    "Weight": "Hmotnost",
    "Height": "Výška",
    "Age": "Věk",
    "kg": "kg",
    "cm": "cm",
    "yrs": "let",
    "Body": "Tělo",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Celková tělesná voda vychází z Watsonových rovnic, které určují objem, do kterého se "
        "alkohol distribuuje.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Celková tělesná voda vychází z Watsonových rovnic, které určují objem, do kterého se "
        "alkohol distribuuje. Rovnice pro ženy věk nezahrnuje, takže jeho změna výsledek "
        "neovlivní.",
    "Drinking frequency": "Frekvence pití",
    "How often do you drink?": "Jak často piješ?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Takto odhadujeme tvoji rychlost odbourávání. Pravidelné pití indukuje jaterní dráhu CYP2E1, takže kdo pije často, odbourává alkohol rychleji. Je to nejslabší místo modelu – proto si můžeš v sekci Zobrazení a jazyk určit, kolik z této nejistoty ti aplikace ukáže.",
    "Your limit": "Tvůj limit",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Tvoje vlastní referenční hodnota, ne zákonný limit. Aplikace tě upozorní, když by tě "
        "plánovaný nápoj dostal nad ni, a řekne, jak dlouho bys nad ní zůstal.",
    "Calculated values": "Vypočtené hodnoty",
    "Total body water": "Celková tělesná voda",
    "Distribution volume": "Distribuční objem",
    "Widmark factor": "Widmarkův faktor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmarkův faktor bývá u mužů kolem 0,68 a u žen kolem 0,55. Pokud je ten tvůj hodně "
        "jinde, vyplatí se zkontrolovat hodnoty výše.",
    "Elimination rate": "Rychlost odbourávání",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Jak rychle tvá játra odbourávají alkohol, jakmile se vstřebá – sklon klesající části "
        "křivky.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol se odbourává zhruba stálým množstvím za hodinu, ne v procentech, protože "
        "enzym, který ho rozkládá, běží na plný výkon prakticky při jakékoli hladině. Právě "
        "proto vůbec existují poučky jako „jeden nápoj za hodinu“.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Při tomto nastavení se %@ odbourá přibližně za %@. Téměř všichni se pohybují mezi %@ "
        "za hodinu.",
    "How to find yours": "Jak zjistit tu svoji",
    "With a breathalyser": "S alkotesterem",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Foukni si dvakrát, s odstupem aspoň hodiny, na klesající straně – dvě hodiny a víc po "
        "posledním nápoji a mezitím nic nepij. Druhý naměřený údaj odečti od prvního a vyděl "
        "počtem hodin mezi nimi.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Například %@ a o dvě hodiny později %@ vychází na %@ za hodinu.",
    "Without one": "Bez něj",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Aplikace ti řekne, kdy očekává, že vystřízlivíš. Pokud jsi spolehlivě v normálu "
        "výrazně dřív, tvoje rychlost je vyšší než nastavená – posuň ji o stupeň nahoru a "
        "sleduj to několik posezení. Pokud to trvá déle, než aplikace předpovídá, posuň ji "
        "dolů.",
    "What moves it": "Co ji ovlivňuje",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Pravidelné pití ji zvyšuje: jaterní enzym, který práci odvádí, se používáním "
        "indukuje. U žen bývá v průměru mírně vyšší, nalačno nebo při potížích s játry naopak "
        "nižší.",
    "Uncertainty": "Nejistota",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Na nule je každý údaj jedno číslo – nejlepší odhad aplikace. Nad nulou se tytéž údaje "
        "zobrazují jako rozpětí a pás v grafu se tomu přizpůsobí.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Podle jednoho čísla se to učí snáz: časem zjistíš, jak se u tebe projevuje 0,6. "
        "Rozpětí je doslovnější odpověď, protože rychlost je opravdu nejistá. Obojí se dá "
        "obhájit – rozhodnutí je na tobě.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Rozptyl odpovídající tvé frekvenci pití je ± %@ za hodinu.",
    "Rate": "Rychlost",
    "Range": "Rozpětí",
    "Advanced": "Pokročilé",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Week": "Týden",
    "Month": "Měsíc",
    "Year": "Rok",
    "Sober days": "Dny bez alkoholu",
    "Change": "Změna",
    "before records": "před začátkem záznamů",
    "See further back": "Podívat se dál do minulosti",
    "Weeks, months and years side by side — and every evening older than seven days.": "Týdny, měsíce a roky vedle sebe – a každý večer starší než sedm dní.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Vše, co sis zaznamenal, je už uloženo. Odemknutí to jen zobrazí.",
    "Back up and restore": "Záloha a obnovení",
    "Log for friends too": "Zapisuj i za přátele",
    "Switch to someone else in one tap and log their drinks with their own body and limit — each person gets their own curve and history.": "Jedním klepnutím přepni na někoho jiného a zapisuj jeho nápoje s jeho vlastním tělem a limitem – každý má svou křivku i historii.",
    "Save everything to a file, and read a backup back in — on this phone or on a new one.": "Ulož všechno do souboru a načti zálohu zpět – na tomhle telefonu nebo na novém.",
    "Backup and restore are part of Pro.": "Záloha a obnovení jsou součástí Pro.",
    "Today": "Dnes",
    "Day": "Den",
    "Yesterday": "Včera",
    "No drinks on this day": "V tento den žádné nápoje",
    "Trend": "Trend",
    "day": "den",
    "Smoothing": "Vyhlazení",
    "%@ sessions": "%@ posezení",
    "No data before %@": "Žádná data před %@",
    "vs.": "oproti",
    "Grams": "Gramy",
    "Grams of alcohol": "Gramy alkoholu",
    "Standard units": "Standardní jednotky",
    "Unit size": "Velikost jednotky",
    "Automatic": "Automaticky",
    "UK": "Spojené království",
    "Nordic countries": "Severské země",
    "US standard drink": "Standardní nápoj v USA",
    "WHO, most of Europe": "WHO, většina Evropy",
    "Period": "Období",
    "Switch person": "Přepnout osobu",
    "Add person": "Přidat osobu",
    "New person": "Nová osoba",
    "You": "Ty",
    "Name": "Jméno",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Všechny čtyři hodnoty mění křivku, takže žádnou z nich nelze za někoho jiného odhadnout.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Vlastní limit a jemnější nastavení se dají změnit později na kartě Profil, když je "
        "tato osoba vybraná.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Rychlé přidání",
    "Choose a favourite drink": "Vyber oblíbený nápoj",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Vyber nápoj, který si dáváš nejčastěji, a tlačítko na obrazovce Aktuálně ho zaznamená "
        "jedním klepnutím.",
    "This is your quick-add drink": "Tohle je tvůj nápoj pro rychlé přidání",
    "Set as my quick-add drink": "Nastavit jako nápoj pro rychlé přidání",
    "This is now your usual": "Tohle je teď tvůj obvyklý nápoj",
    "Remove favourite": "Odebrat oblíbený nápoj",
    "Always add this one": "Vždy přidávat tento nápoj",
    "Logs it straight away, without opening anything.":
        "Zaznamená ho hned, bez otevírání čehokoli.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Jedno klepnutí na obrazovce Aktuálně tento nápoj zaznamená, na tlačítku je "
        "předpokládaný vrchol. Naplněnost žaludku se přebírá z předchozího nápoje a dá se hned "
        "potom opravit.",
    "Peak %@": "Vrchol %@",
    "%@ added": "Přidáno: %@",
    "Save": "Uložit",
    "Undo": "Zpět",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Záloha",
    "Export a backup": "Exportovat zálohu",
    "Import a backup": "Importovat zálohu",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Záloha obsahuje všechny osoby, posezení a nápoje. Import doplní, co chybí – nikdy "
        "nezmění ani neodstraní nic, co už tu je.",
    "Import this backup?": "Importovat tuto zálohu?",
    "Import": "Importovat",
    "Everything in this backup is already here.": "Všechno z této zálohy už tu je.",
    "Import finished": "Import dokončen",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Jazyk",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Otevře tuto aplikaci v Nastavení, kde volba „Preferovaný jazyk“ určuje jazyk samotné "
        "aplikace – jazyk systému zůstane beze změny. iOS aplikaci po změně restartuje.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Import se nezdařil",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Tento soubor není zálohou LogMyDrink, nebo je poškozený.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Tato záloha pochází z novější verze LogMyDrink. Aktualizuj aplikaci a zkus to znovu.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Přidá posezení (%@), nápoje (%@) a měsíční součty (%@). Nic, co už tu je, se nezmění ani neodstraní.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Přidána posezení (%@), nápoje (%@) a měsíční součty (%@).',
    'months as totals': 'měsíců jen jako součet',
    'by month only': 'jen po měsících',
    'monthly total': 'měsíční součet',
    'No daily records for this day': 'Pro tento den nejsou denní záznamy',
    'Monthly total: %@': 'Měsíční součet: %@',
    'A dry month': 'Suchý měsíc',

    # --- RemovePersonSection ---
    'Remove %@?': 'Odebrat %@?',
    'Remove': 'Odebrat',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Smaže posezení (%@), nápoje (%@) a měsíční součty (%@). Nelze vrátit zpět.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Smaže posezení (%@) a nápoje (%@). Nelze vrátit zpět.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Přejeď u hosta doleva, chceš-li ho odebrat se vším, co je u něj zaznamenáno. Tebe odebrat nelze.',
    'People': 'Lidé',
    'Owner': 'Vlastník',
    'Everyone this app records. Switch, add, or remove someone.': 'Všichni, které tato aplikace zaznamenává. Přepni, přidej nebo odeber někoho.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Přeneseno z předchozího večera',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorie',
    'Sessions': 'Posezení',
    'Per session': 'Na posezení',
    'Under the influence': 'Pod vlivem',
    '%@ of the time': '%@ času',
    'Days over limit': 'Dny nad limitem',
    'Longest sober run': 'Nejdelší série bez alkoholu',
    'Favourite drink': 'Oblíbený nápoj',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Zobrazení a jazyk",
    "Data": "Data",
    "Concentration": "Koncentrace",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Rychlost nech na otázce o frekvenci pití, pokud nemáš měření, se kterým bys ji mohl porovnat.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Odhad, ne měření. Nikdy podle toho nerozhoduj, jestli můžeš řídit.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Odhadované rozpětí, ne měření. Nikdy podle toho nerozhoduj, jestli můžeš řídit.',
    'How does the app calculate this?':
        'Jak to aplikace počítá?',
    'approximately %@ %@':
        'přibližně %@ %@',
    'How it works':
        'Jak to funguje',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nikdy podle toho nerozhoduj, jestli můžeš řídit. Aplikace odhaduje, neměří, a tvoje skutečná hladina se může výrazně lišit.',
    'Why this app exists':
        'Proč tato aplikace existuje',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink ti pomáhá pít vědoměji a mít pití pod kontrolou. Rozhodnutí padá před další sklenkou, proto ti aplikace předem ukáže, kam by tvou hladinu dostal další nápoj a kdy by vyvrcholila.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Nejde ale jen o dnešní večer. Každý zapsaný nápoj se uloží do Historie, takže v průběhu měsíců a let vidíš, kolik, jak často a do jaké hladiny piješ. Vynoří se z toho tvé vzorce i směr, kterým se mění – jestli se věci zlepšují, nebo zhoršují.',
    'How it calculates':
        'Jak aplikace počítá',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Odhad vychází z Widmarkovy metody, kterou se hladina alkoholu v krvi odhaduje od 30. let 20. století; aplikace používá její vylepšenou verzi.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Z tvé hmotnosti, výšky, věku a pohlaví spočítá, kolik vody tvé tělo obsahuje, protože v ní se alkohol rozptýlí. Každý nápoj sleduje zvlášť: kolik alkoholu obsahoval, jak rychle jsi ho vypil a kolik jsi předtím snědl, protože na tom závisí rychlost vstřebávání.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Mezitím játra každou hodinu odbourají zhruba stálé množství; kolik to je u tebe, se odhaduje podle toho, jak často piješ. Výsledkem je křivka minutu po minutě: kde jsi teď, kam směřuješ a kdy budeš zase na nule.',
    'Details':
        'Podrobnosti',
    'Body water':
        'Tělesná voda',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsonův vzorec (1980) z hmotnosti, výšky, věku a pohlaví. Vzorec pro ženy věk neobsahuje – je to vlastnost vzorce, ne chyba. Distribuční objem je tělesná voda dělená 0,85, tedy obsahem vody v krvi.',
    'Absorption':
        'Vstřebávání',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Každý nápoj má svůj vlastní „žaludek“. Nalačno se polovina alkoholu vstřebá asi za 7 minut, s plným žaludkem asi za 21. Nápoj, který usrkáváš, se do žaludku dostává rovnoměrně po celou dobu pití.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Dává nižší vrchol a dřívější návrat na nulu. Překvapivé, ale naměřené: s jídlem žaludek část alkoholu rozloží ještě před vstřebáním (aplikace počítá s 5, 10 a 15 procenty) a co se do krve nikdy nedostalo, není třeba odbourávat.',
    'Elimination':
        'Odbourávání',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Asi 0,15 ‰ za hodinu (rozpětí v literatuře 0,10–0,25), u pravidelně pijících víc, protože se jaterní enzymy přizpůsobí. Blízko nuly se zpomalí (Michaelisova–Mentenové kinetika), takže křivka plynule dobíhá místo náhlého zlomu.',
    'Computation':
        'Výpočet',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Křivka vzniká numerickou simulací s rozlišením jedné minuty.',
    'Why it is only an estimate':
        'Proč je to jen odhad',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Aplikace nic neměří. To, co ukazuje, je výsledek modelu s průměrnými hodnotami a skutečnost se může lišit. Největší neznámou je, jak rychle alkohol odbouráváš: v rámci věrohodného rozpětí to samo může posunout vrchol o 40 procent a návrat na nulu o čtyři hodiny během jediného večera.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Roli hraje i genetika, stav jater, léky, jídlo, spánek a únava – nic z toho aplikace nezná. Přesnou hodnotu dá jen ověřený dechový analyzátor nebo krevní test.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Číslo je přesto užitečné. Pokud aplikace u tebe ukazuje soustavně trochu víc nebo míň, mýlí se každý večer stejným směrem, takže se časem naučíš, co pro tebe daná hodnota znamená. V Profilu si můžeš zobrazit i nejistotu rychlosti odbourávání: místo jednoho čísla pak uvidíš rozpětí.',
    'Tips':
        'Tipy',
    'Favourite drink in one tap':
        'Oblíbený nápoj jedním klepnutím',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Nastav si v Profilu oblíbený nápoj a tlačítko na obrazovce Aktuálně ho zapíše jedním klepnutím.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Přidej ho na zamčenou obrazovku nebo na plochu: jedno klepnutí zapíše tvůj oblíbený nápoj. S Pro ukazuje, dokud máš v těle alkohol, i tvou hladinu a její směr.',
    'How do I add it?':
        'Jak ho přidám?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Řekni „Hey Siri, LogMyDrink now“ a Siri zapíše tvůj oblíbený nápoj a řekne ti, kam míří tvůj vrchol. (Příkaz funguje v angličtině.)',
    'Looking back':
        'Ohlédnutí',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Včera“ nahoře na obrazovce Aktuálně tě jedním klepnutím přenese na předchozí den; karta Historie ukazuje tvé vzorce za týdny, měsíce a roky.',
    'Logging later':
        'Dodatečný zápis',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Když zapisuješ nápoj dodatečně, posuň čas zpět tlačítky − a +; vynechaný den můžeš doplnit v zobrazení Den v Historii.',
    'One tap and done':
        'Jedno klepnutí a hotovo',
    'Your favourite from the Lock Screen':
        'Oblíbený nápoj ze zamčené obrazovky',
    'Say it, don’t type it':
        'Řekni to, nepiš to',
    'See your patterns':
        'Podívej se na své vzorce',
    'Set what you drink most often and log it with a single tap.':
        'Nastav, co piješ nejčastěji, a zapisuj to jedním klepnutím.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Jedno klepnutí na widget zapíše tvůj oblíbený nápoj, bez hledání aplikace. Večer ukazuje i tvou hladinu.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now“ – Siri zapíše tvůj oblíbený nápoj a řekne ti, kam míří tvůj vrchol.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Historie ukazuje, kolik a do jaké hladiny piješ za týdny, měsíce a roky, a kterým směrem se to mění.',
    'Set favourite':
        'Nastavit oblíbený',
    'Add widget':
        'Přidat widget',
    'Got it':
        'Rozumím',
    'Open History':
        'Otevřít Historii',
    'Don’t show again':
        'Už nezobrazovat',
    'Lock Screen':
        'Zamčená obrazovka',
    'Home Screen':
        'Plocha',
    'Where':
        'Kam',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Zamkni iPhone a pak podrž prst na zamčené obrazovce.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Klepni na Přizpůsobit, pak na Zamčená obrazovka a nakonec na řádek widgetů pod hodinami.',
    'Choose LogMyDrink, then tap Done.':
        'Vyber LogMyDrink a klepni na Hotovo.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Podrž prst na prázdném místě plochy, dokud se ikony nezačnou chvět.',
    'Tap Edit, then Add Widget.':
        'Klepni na Upravit a pak na Přidat widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Vyhledej LogMyDrink, vyber velikost a klepni na Přidat widget.',
    'A tap on the widget opens the app and logs your favourite drink. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Klepnutí na widget otevře aplikaci a zapíše tvůj oblíbený nápoj. S Pro ukazuje, dokud máš v těle alkohol, i tvou hladinu a její směr.',
    'Add the widget':
        'Přidat widget',
    'Show tips':
        'Zobrazovat tipy',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Nejvýš jeden tip denně při otevření aplikace – nikdy, dokud máš v těle alkohol.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Co číslo ukazuje',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Číslo je odhad koncentrace alkoholu ve tvé krvi (anglicky BAC, blood alcohol concentration): kolik alkoholu máš v krvi.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'V promilích (‰) jde o gramy alkoholu na litr krve: 0,5 ‰ znamená půl gramu v každém litru. V procentech jde o gramy na 100 mililitrů, takže stejná hladina dává desetkrát menší číslo: 0,5 ‰ je 0,05 procenta. Přepnout můžeš v části Profil › Zobrazení a jazyk.',
    'The curve shows the same level over time, minute by minute.':
        'Křivka ukazuje stejnou hladinu v čase, minutu po minutě.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promile (‰) jsou gramy alkoholu na litr krve, procenta gramy na 100 mililitrů: 0,5 ‰ je 0,05 procenta.',

    # --- ProPaywallSheet: plans and buying ---
    "Prices could not be loaded.": "Ceny se nepodařilo načíst.",
    "Try again": "Zkusit znovu",
    "Save %@": "Ušetříš %@",
    "About %@ a month": "Asi %@ měsíčně",
    "Yearly": "Roční",
    "Monthly": "Měsíční",
    "%@ / year": "%@ / rok",
    "%@ / month": "%@ / měs.",
    "Start my free month": "Začít měsíc zdarma",
    "Subscribe": "Předplatit",
    "Free for one month, then %@ a year.": "Měsíc zdarma, potom %@ ročně.",
    "Free for one month, then %@ a month.": "Měsíc zdarma, potom %@ měsíčně.",
    "%@ a year.": "%@ ročně.",
    "%@ a month.": "%@ měsíčně.",
    "Renews automatically until you cancel. Cancel anytime in Settings.": "Obnovuje se automaticky, dokud nezrušíš. Zrušit můžeš kdykoli v Nastavení.",
    "Restore purchases": "Obnovit nákupy",
    "Redeem code": "Uplatnit kód",
    "Terms of Use": "Podmínky použití",
    "Privacy Policy": "Soukromí",
    "Waiting for approval. Pro opens as soon as the purchase goes through.": "Čeká na schválení. Pro se odemkne, jakmile nákup proběhne.",
    "The purchase did not go through. Please try again.": "Nákup se nezdařil. Zkus to znovu.",
    "No active subscription was found for this Apple ID.": "Pro toto Apple ID nebylo nalezeno žádné aktivní předplatné.",
}
