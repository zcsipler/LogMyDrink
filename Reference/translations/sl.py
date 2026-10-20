"""
Slovene.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promil",
    "Percent": "Odstotek",

    # --- DrinkCatalog: drink types ---
    "Beer": "Pivo",
    "Wine": "Vino",
    "Champagne": "Peneče vino",
    "Shot": "Šilce",
    "Cocktail": "Koktajl",
    "Custom": "Po meri",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Prazen želodec",
    "Moderately full": "Srednje poln želodec",
    "Full stomach": "Poln želodec",
    "Empty": "Prazen",
    "Moderate": "Srednje poln",
    "Full": "Poln",
    "Fast absorption, higher and earlier peak.": "Hitra absorpcija, višji in zgodnejši vrh.",
    "Moderate absorption.": "Srednje hitra absorpcija.",
    "Slow absorption, lower and later peak.": "Počasna absorpcija, nižji in poznejši vrh.",

    # --- DrinkingFrequency ---
    "Rarely": "Redko",
    "A few times a month": "Nekajkrat na mesec",
    "Several times a week": "Večkrat na teden",
    "Almost daily": "Skoraj vsak dan",
    "A few occasions a year": "Nekajkrat na leto",
    "Social drinking": "Družabno pitje",
    "Weekly routine": "Tedenska rutina",
    "Daily or nearly daily": "Vsak dan ali skoraj vsak dan",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Čas",
    "Level": "Raven",
    "Lower": "Spodnja",
    "Upper": "Zgornja",
    "Lower estimate": "Spodnja ocena",
    "Upper estimate": "Zgornja ocena",
    "Personal limit": "Osebna meja",
    "Drink": "Pijača",

    # --- BACChartView ---
    "Expected peak around %@": "Pričakovani vrh okoli %@",
    "Peaked around %@": "Vrh je bil okoli %@",
    "No active session": "Ni aktivnega dogodka",
    "Still rising": "Še narašča",
    "YOUR LIMIT %@": "TVOJA MEJA %@",
    "possible range": "možni razpon",

    # --- Live screen: the day with nothing on it ---
    "Live": "V živo",
    "Nothing logged today": "Danes ni nič zabeleženega",
    "Add a drink when you have one.": "Vsako pijačo dodaj, ko jo piješ.",

    # --- Tabs and history ---
    "History": "Zgodovina",
    "No past sessions yet": "Še ni preteklih dogodkov",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Dogodek se prikaže tukaj, ko se konča – ko se alkohol izloči in mine nekaj ur.",
    "%@ drinks": "Pijače: %@",
    "peak": "vrh",
    "Started": "Začetek",
    "Lasted": "Trajanje",
    "Duration": "Trajanje",
    "Sober around": "Trezen pribl.",
    "Sober at": "Trezen ob",
    "Remaining": "Preostalo",
    "next day": "naslednji dan",
    "previous day": "prejšnji dan",
    "%@ days later": "%@ dni pozneje",
    "%@ days earlier": "%@ dni prej",
    "Calculated with your profile at the time": "Izračunano s tvojim takratnim profilom",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Pijače",
    "Units": "Enote",
    "Drinks this session": "Pijače na tem dogodku",
    "Add drink": "Dodaj pijačo",

    # --- Editing an already logged drink ---
    "Edit drink": "Uredi pijačo",
    "Save changes": "Shrani spremembe",
    "With this": "S to pijačo",
    "Delete": "Izbriši",
    "tap to edit · swipe to delete": "tapni za urejanje · podrsaj za brisanje",

    # --- Drinking pace ---
    "How fast": "Kako hitro",
    "In one go": "Na dušek",
    "Counts as a single swallow — the steepest possible rise.":
        "Šteje kot en sam požirek – najstrmejši možni vzpon.",
    "A quick drink. The level climbs fast.": "Hitro popita pijača. Raven hitro naraste.",
    "A normal pace.": "Običajen tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Počasi popita pijača. Precej blažji vzpon ob enaki količini alkohola.",

    # --- AddDrinkSheet ---
    "Cancel": "Prekliči",
    "Now": "Zdaj",
    "Projected peak": "Predvideni vrh",
    "Peak at": "Vrh ob",
    "Clears": "Izloči se",
    "This would cross your limit": "To bi preseglo tvojo mejo",
    "Around %@, for up to %@.": "Okoli %@, za največ %@.",
    "This might cross your limit": "To bi morda preseglo tvojo mejo",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Pri počasnejši presnovi da, pri hitrejši ne. To je negotovost ocene.",
    "Type": "Vrsta",
    "Amount": "Količina",
    "Strength": "Jakost",
    "%@ units": "Enote: %@",
    "%@ g alcohol": "%@ g alkohola",
    "Stomach": "Želodec",
    "When": "Kdaj",
    "Done": "Končano",
    "Add": "Dodaj",

    # --- ProfileSheet ---
    "Male": "Moški",
    "Female": "Ženski",
    "Sex": "Spol",
    "Weight": "Teža",
    "Height": "Višina",
    "Age": "Starost",
    "kg": "kg",
    "cm": "cm",
    "yrs": "let",
    "Body": "Telo",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Skupna telesna voda izhaja iz Watsonovih enačb, ki določajo volumen, v katerega se "
        "alkohol porazdeli.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Skupna telesna voda izhaja iz Watsonovih enačb, ki določajo volumen, v katerega se "
        "alkohol porazdeli. Ženska enačba ne vključuje starosti, zato njena sprememba ne bo "
        "vplivala na rezultat.",
    "Drinking frequency": "Pogostost pitja",
    "How often do you drink?": "Kako pogosto piješ?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Tako ocenimo tvojo hitrost izločanja. Redno pitje inducira jetrno pot CYP2E1, zato tisti, ki pijejo pogosto, izločajo alkohol hitreje. To je najšibkejša točka modela, zato lahko v razdelku Prikaz in jezik nastaviš, koliko te negotovosti ti aplikacija pokaže.",
    "Your limit": "Tvoja meja",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Tvoja lastna referenčna številka, ne zakonska meja. Aplikacija ti pove, kdaj bi te "
        "načrtovana pijača popeljala čeznjo in kako dolgo bi ostal nad njo.",
    "Calculated values": "Izračunane vrednosti",
    "Total body water": "Skupna telesna voda",
    "Distribution volume": "Porazdelitveni volumen",
    "Widmark factor": "Widmarkov faktor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmarkov faktor je pri moških običajno okoli 0,68, pri ženskah pa 0,55. Če je tvoj "
        "daleč od tega, je vredno preveriti zgornje vrednosti.",
    "Elimination rate": "Hitrost izločanja",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Kako hitro tvoja jetra izločijo alkohol, ko je ta absorbiran – naklon padajoče strani "
        "krivulje.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol se izloča v približno stalni količini na uro in ne v odstotkih, ker encim, ki "
        "ga razgrajuje, deluje s polno zmogljivostjo pri skoraj vsaki ravni. Prav zato sploh "
        "obstajajo pravila, kot je »ena pijača na uro«.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Pri tej nastavitvi se %@ izloči v približno %@. Skoraj vsi so v razponu %@ na uro.",
    "How to find yours": "Kako ugotoviti svojo hitrost",
    "With a breathalyser": "Z alkotestom",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Dvakrat pihni v alkotest, vsaj uro narazen, na padajoči strani – dve uri ali več po "
        "zadnji pijači in brez pijače vmes. Drugo meritev odštej od prve in rezultat deli s "
        "številom ur med njima.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Na primer %@ in %@ dve uri pozneje pomeni %@ na uro.",
    "Without one": "Brez alkotesta",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Aplikacija ti pove, kdaj pričakuje, da se bo alkohol izločil. Če se zanesljivo "
        "počutiš normalno že precej pred tem, je tvoja hitrost višja od nastavitve – premakni jo za eno "
        "stopnjo navzgor in spremljaj nekaj dogodkov. Če traja dlje od napovedi, jo premakni "
        "navzdol.",
    "What moves it": "Kaj vpliva nanjo",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Redno pitje jo zviša: jetrni encim, ki opravlja to delo, se z uporabo inducira. Pri "
        "ženskah je v povprečju tudi nekoliko višja, nižja pa na prazen želodec ali ob težavah "
        "z jetri.",
    "Uncertainty": "Negotovost",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Pri ničli je vsaka številka ena sama vrednost – najboljša ocena aplikacije. Nad ničlo "
        "so iste številke prikazane kot razponi, temu primerno pa se razširi tudi pas na "
        "grafu.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Ob eni sami številki se je lažje učiti: sčasoma spoznaš, kakšen občutek je pri tvojih "
        "0,6. Razpon je bolj dobesedni odgovor, ker je hitrost res negotova. Oboje je "
        "utemeljeno – odločitev je tvoja.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Razpon, ki ga nakazuje tvoja pogostost pitja, je ± %@ na uro.",
    "Rate": "Hitrost",
    "Range": "Razpon",
    "Advanced": "Napredno",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Več oseb",
    "History trends": "Trendi zgodovine",
    "Week": "Teden",
    "Month": "Mesec",
    "Year": "Leto",
    "Sober days": "Dnevi brez alkohola",
    "Change": "Sprememba",
    "before records": "pred začetkom beleženja",
    "See further back": "Poglej dlje nazaj",
    "Weeks, months and years side by side — and every evening older than seven days.": "Tedni, meseci in leta drug ob drugem – in vsak večer, starejši od sedmih dni.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Vse, kar si zabeležil, je že shranjeno. Odklep to le pokaže.",
    "Coming soon": "Kmalu",
    "Today": "Danes",
    "Day": "Dan",
    "Yesterday": "Včeraj",
    "No drinks on this day": "Ta dan ni bilo pijač",
    "Trend": "Trend",
    "day": "dan",
    "Smoothing": "Glajenje",
    "%@ sessions": "Dogodki: %@",
    "No data before %@": "Ni podatkov pred %@",
    "vs.": "glede na",
    "Grams": "Grami",
    "Grams of alcohol": "Grami alkohola",
    "Standard units": "Standardne enote",
    "Unit size": "Velikost enote",
    "Automatic": "Samodejno",
    "UK": "Združeno kraljestvo",
    "Nordic countries": "Nordijske države",
    "US standard drink": "Standardna pijača v ZDA",
    "WHO, most of Europe": "SZO, večina Evrope",
    "Period": "Obdobje",
    "Switch person": "Zamenjaj osebo",
    "Add person": "Dodaj osebo",
    "New person": "Nova oseba",
    "You": "Ti",
    "Name": "Ime",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Vse štiri vrednosti spremenijo krivuljo, zato nobene ni mogoče ugibati za nekoga "
        "drugega.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Lastno mejo te osebe in podrobnejše nastavitve lahko pozneje spremeniš v zavihku "
        "Profil, ko je ta oseba izbrana.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Hitro dodajanje",
    "Choose a favourite drink": "Izberi najljubšo pijačo",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Izberi pijačo, ki jo običajno naročiš, in gumb na zaslonu V živo jo bo zabeležil z "
        "enim dotikom.",
    "This is your quick-add drink": "To je tvoja pijača za hitro dodajanje",
    "Set as my quick-add drink": "Nastavi kot pijačo za hitro dodajanje",
    "This is now your usual": "To je zdaj tvoja običajna pijača",
    "Remove favourite": "Odstrani najljubšo pijačo",
    "Always add this one": "Vedno dodaj to pijačo",
    "Logs it straight away, without opening anything.":
        "Zabeleži jo takoj, brez odpiranja česar koli.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "En dotik na zaslonu V živo jo zabeleži, s predvidenim vrhom na gumbu. Napolnjenost "
        "želodca se prevzame od prejšnje pijače, popraviš pa jo lahko takoj zatem.",
    "Peak %@": "Vrh %@",
    "%@ added": "Dodano: %@",
    "Save": "Shrani",
    "Undo": "Razveljavi",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Varnostna kopija",
    "Export a backup": "Izvozi varnostno kopijo",
    "Import a backup": "Uvozi varnostno kopijo",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Varnostna kopija vsebuje vse osebe, dogodke in pijače. Uvoz doda le tisto, kar manjka "
        "– nikoli ne spremeni ali odstrani ničesar, kar je že tu.",
    "Import this backup?": "Uvozim to varnostno kopijo?",
    "Import": "Uvozi",
    "Everything in this backup is already here.": "Vse iz te varnostne kopije je že tu.",
    "Import finished": "Uvoz končan",
    "OK": "V redu",

    # --- LanguageSection: the app's language ---
    "Language": "Jezik",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Odpre to aplikacijo v Nastavitvah, kjer »Prednostni jezik« določi jezik same "
        "aplikacije – sistemski ostane nespremenjen. iOS ob spremembi znova zažene aplikacijo.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Uvoz ni uspel",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Ta datoteka ni varnostna kopija aplikacije LogMyDrink ali pa je poškodovana.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "To varnostno kopijo je ustvarila novejša različica aplikacije LogMyDrink. Posodobi "
        "aplikacijo in poskusi znova.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Dodani bodo dogodki: %@, pijače: %@ in mesečni seštevki: %@. Nič od tega, kar je že tu, ne bo spremenjeno ali odstranjeno.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Dodano – dogodki: %@, pijače: %@, mesečni seštevki: %@.',
    'months as totals': 'mesecev le kot seštevek',
    'by month only': 'le po mesecih',
    'monthly total': 'mesečni seštevek',
    'No daily records for this day': 'Za ta dan ni dnevnih zapisov',
    'Monthly total: %@': 'Mesečni seštevek: %@',
    'A dry month': 'Suh mesec',

    # --- RemovePersonSection ---
    'Remove %@?': 'Odstranim %@?',
    'Remove': 'Odstrani',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Izbriše dogodke: %@, pijače: %@ in mesečne seštevke: %@. Tega ni mogoče razveljaviti.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Izbriše dogodke: %@ in pijače: %@. Tega ni mogoče razveljaviti.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Podrsaj gosta v levo, da ga odstraniš skupaj z vsem, kar je zabeleženo zanj. Tebe ni mogoče odstraniti.',
    'People': 'Osebe',
    'Owner': 'Lastnik',
    'Everyone this app records. Switch, add, or remove someone.': 'Vsi, ki jih ta aplikacija beleži. Preklopi, dodaj ali odstrani koga.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Preneseno iz prejšnjega večera',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorije',
    'Sessions': 'Dogodki',
    'Per session': 'Na dogodek',
    'Under the influence': 'Pod vplivom',
    '%@ of the time': '%@ časa',
    'Days over limit': 'Dnevi nad mejo',
    'Longest sober run': 'Najdaljši niz brez alkohola',
    'Favourite drink': 'Najljubša pijača',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Prikaz in jezik",
    "Data": "Podatki",
    "Concentration": "Koncentracija",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Hitrost prepusti vprašanju o pogostosti, razen če imaš meritev, s katero jo lahko primerjaš.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Ocena, ne meritev. Nikoli se na podlagi tega ne odločaj, ali lahko voziš.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Ocenjen razpon, ne meritev. Nikoli se na podlagi tega ne odločaj, ali lahko voziš.',
    'How does the app calculate this?':
        'Kako aplikacija to izračuna?',
    'approximately %@ %@':
        'približno %@ %@',
    'How it works':
        'Kako deluje',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nikoli se na podlagi tega ne odločaj, ali lahko voziš. Aplikacija ocenjuje, ne meri, in tvoja dejanska raven se lahko precej razlikuje.',
    'Why this app exists':
        'Čemu ta aplikacija',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink ti pomaga piti bolj zavestno in ohraniti nadzor. Odločitev pade pred naslednjim kozarcem, zato ti aplikacija vnaprej pokaže, kam bi tvojo raven odnesla še ena pijača in kdaj bi dosegla vrh.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'A ne gre le za nocojšnji večer. Vsaka zabeležena pijača gre v Zgodovino, tako da skozi mesece in leta vidiš, koliko, kako pogosto in do kako visoke ravni piješ. Iz tega se izrišejo tvoji vzorci in tudi smer, v katero se spreminjajo – ali gre na bolje ali na slabše.',
    'How it calculates':
        'Kako računa',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Ocena temelji na Widmarkovi metodi, s katero alkohol v krvi ocenjujejo od tridesetih let 20. stoletja; aplikacija uporablja njeno izboljšano različico.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Iz tvoje teže, višine, starosti in spola izračuna, koliko vode je v tvojem telesu, saj se alkohol porazdeli prav v njej. Vsako pijačo spremlja posebej: koliko alkohola je vsebovala, kako hitro si jo popil in koliko si prej pojedel, saj to določa hitrost absorpcije.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Medtem jetra vsako uro razgradijo približno stalno količino; tvoja se oceni po tem, kako pogosto piješ. Rezultat je krivulja, minuto za minuto: kje si zdaj, kam greš in kdaj boš spet na ničli.',
    'Details':
        'Podrobnosti',
    'Body water':
        'Telesna voda',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsonova formula (1980) iz teže, višine, starosti in spola. Formula za ženske ne vsebuje starosti – to je lastnost formule, ne napaka. Porazdelitveni volumen je telesna voda, deljena z 0,85, vsebnostjo vode v krvi.',
    'Absorption':
        'Absorpcija',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Vsaka pijača ima svoj »želodec«. Na prazen želodec se polovica alkohola vsrka v približno 7 minutah, na poln v približno 21. Pijača, ki jo srkaš, pride v želodec enakomerno ves čas pitja.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Da nižji vrh in zgodnejšo ničlo. Presenetljivo, a izmerjeno: s hrano želodec del alkohola razgradi že pred absorpcijo (aplikacija računa s 5, 10 in 15 odstotki), in česar telo nikoli ne vsrka, mu ni treba razgraditi.',
    'Elimination':
        'Izločanje',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Približno 0,15 ‰ na uro (objavljeni razpon 0,10–0,25), pri tistih, ki redno pijejo, več, ker se jetrni encimi prilagodijo. Blizu ničle se upočasni (kinetika Michaelis-Menten), zato se krivulja postopoma izravna, namesto da bi se nenadoma prekinila.',
    'Computation':
        'Izračun',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Krivulja izhaja iz numerične simulacije z ločljivostjo ene minute.',
    'Why it is only an estimate':
        'Zakaj je to le ocena',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Aplikacija ničesar ne meri. Prikazuje rezultat modela s povprečnimi vrednostmi, resničnost pa se lahko razlikuje. Največja neznanka je, kako hitro razgrajuješ alkohol: v verjetnem razponu lahko že to samo isti večer premakne vrh za 40 odstotkov in ničlo za štiri ure.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Vlogo imajo tudi geni, zdravje jeter, zdravila, kaj si jedel, spanec in utrujenost – nič od tega aplikacija ne pozna. Natančno vrednost da le overjen alkotest ali krvni test.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Število je kljub temu uporabno. Če ti aplikacija dosledno kaže malo preveč ali premalo, se vsak večer zmoti v isto smer, zato se sčasoma naučiš, kaj določena vrednost pomeni zate. V Profilu lahko prikažeš tudi negotovost hitrosti izločanja: takrat namesto enega števila vidiš razpon.',
    'Tips':
        'Nasveti',
    'Favourite drink in one tap':
        'Najljubša pijača z enim dotikom',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'V Profilu nastavi najljubšo pijačo in gumb na zaslonu V živo jo zabeleži z enim samim dotikom.',
    'Widget':
        'Gradnik',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Dodaj ga na zaklenjeni ali domači zaslon: en dotik zabeleži tvojo najljubšo pijačo. Dokler imaš v telesu alkohol, prikazuje tudi tvojo raven in njeno smer.',
    'How do I add it?':
        'Kako ga dodam?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Reci »Hey Siri, LogMyDrink now« in Siri bo zabeležila tvojo najljubšo pijačo ter ti povedala, kakšen vrh lahko pričakuješ. (Ukaz deluje v angleščini.)',
    'Looking back':
        'Pogled nazaj',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '»Včeraj« na vrhu zaslona V živo te z enim dotikom pelje na prejšnji dan; zavihek Zgodovina prikazuje tvoje vzorce skozi tedne, mesece in leta.',
    'Logging later':
        'Naknadno beleženje',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Če pijačo zabeležiš naknadno, čas prestavi nazaj z gumboma − in +; izpuščen dan lahko dopolniš v pogledu Dan v Zgodovini.',
    'One tap and done':
        'En dotik in končano',
    'Your favourite from the Lock Screen':
        'Najljubša pijača z zaklenjenega zaslona',
    'Say it, don’t type it':
        'Povej, ne tipkaj',
    'See your patterns':
        'Oglej si svoje vzorce',
    'Set what you drink most often and log it with a single tap.':
        'Nastavi, kaj piješ najpogosteje, in to zabeleži z enim samim dotikom.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'En dotik gradnika zabeleži tvojo najljubšo pijačo, brez iskanja aplikacije. Zvečer prikazuje tudi tvojo raven.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '»Hey Siri, LogMyDrink now« – Siri zabeleži tvojo najljubšo pijačo in ti pove, kakšen vrh lahko pričakuješ.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Zgodovina prikazuje, koliko in do kako visoke ravni piješ skozi tedne, mesece in leta ter v katero smer se to spreminja.',
    'Set favourite':
        'Nastavi najljubšo',
    'Add widget':
        'Dodaj gradnik',
    'Got it':
        'Razumem',
    'Open History':
        'Odpri Zgodovino',
    'Don’t show again':
        'Ne prikazuj več',
    'Lock Screen':
        'Zaklenjeni zaslon',
    'Home Screen':
        'Domači zaslon',
    'Where':
        'Kam',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Zakleni iPhone, nato pridrži zaklenjeni zaslon.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Tapni Prilagodi, nato Zaklenjeni zaslon in še vrstico gradnikov pod uro.',
    'Choose LogMyDrink, then tap Done.':
        'Izberi LogMyDrink in tapni Končano.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Pridrži prazen del domačega zaslona, dokler se ikone ne začnejo tresti.',
    'Tap Edit, then Add Widget.':
        'Tapni Uredi in nato Dodaj gradnik.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Poišči LogMyDrink, izberi velikost in tapni Dodaj gradnik.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Dotik gradnika odpre aplikacijo in zabeleži tvojo najljubšo pijačo. Dokler imaš v telesu alkohol, prikazuje tudi tvojo raven in njeno smer.',
    'Add the widget':
        'Dodaj gradnik',
    'Show tips':
        'Prikazuj nasvete',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Največ en nasvet na dan ob odpiranju aplikacije – nikoli, dokler imaš v telesu alkohol.',
}
