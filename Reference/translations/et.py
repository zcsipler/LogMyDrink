"""
Estonian.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promill",
    "Percent": "Protsent",

    # --- DrinkCatalog: drink types ---
    "Beer": "Õlu",
    "Wine": "Vein",
    "Champagne": "Vahuvein",
    "Shot": "Pits",
    "Cocktail": "Kokteil",
    "Custom": "Kohandatud",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Tühi kõht",
    "Moderately full": "Keskmiselt täis",
    "Full stomach": "Täis kõht",
    "Empty": "Tühi",
    "Moderate": "Keskmine",
    "Full": "Täis",
    "Fast absorption, higher and earlier peak.": "Kiire imendumine, kõrgem ja varasem tipp.",
    "Moderate absorption.": "Keskmine imendumine.",
    "Slow absorption, lower and later peak.": "Aeglane imendumine, madalam ja hilisem tipp.",

    # --- DrinkingFrequency ---
    "Rarely": "Harva",
    "A few times a month": "Paar korda kuus",
    "Several times a week": "Mitu korda nädalas",
    "Almost daily": "Peaaegu iga päev",
    "A few occasions a year": "Paar korda aastas",
    "Social drinking": "Seltskondlik joomine",
    "Weekly routine": "Iganädalane rutiin",
    "Daily or nearly daily": "Iga päev või peaaegu iga päev",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Aeg",
    "Level": "Tase",
    "Lower": "Alumine",
    "Upper": "Ülemine",
    "Lower estimate": "Alumine hinnang",
    "Upper estimate": "Ülemine hinnang",
    "Personal limit": "Isiklik piir",
    "Drink": "Jook",

    # --- BACChartView ---
    "Expected peak around %@": "Eeldatav tipp umbes %@",
    "Peaked around %@": "Tipp oli umbes %@",
    "No active session": "Aktiivset joomiskorda pole",
    "Still rising": "Tõuseb veel",
    "YOUR LIMIT %@": "SINU PIIR %@",
    "possible range": "võimalik vahemik",

    # --- Live screen: the day with nothing on it ---
    "Live": "Hetkeseis",
    "Nothing logged today": "Täna pole midagi lisatud",
    "Add a drink when you have one.": "Lisa jook siis, kui selle võtad.",

    # --- Tabs and history ---
    "History": "Ajalugu",
    "No past sessions yet": "Varasemaid joomiskordi veel pole",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Joomiskord ilmub siia siis, kui see on lõppenud – kui su tase on langenud nulli ja "
        "möödunud on paar tundi.",
    "%@ drinks": "Joogid: %@",
    "peak": "tipp",
    "Started": "Algas",
    "Lasted": "Kestis",
    "Duration": "Kestus",
    "Sober around": "Kaine umbes",
    "Sober at": "Kaine",
    "Remaining": "Jäänud",
    "next day": "järgmisel päeval",
    "previous day": "eelmisel päeval",
    "%@ days later": "%@ päeva hiljem",
    "%@ days earlier": "%@ päeva varem",
    "Calculated with your profile at the time": "Arvutatud toonase profiiliga",

    # --- TodayView ---
    "Profile": "Profiil",
    "Drinks": "Joogid",
    "Units": "Ühikud",
    "Drinks this session": "Selle joomiskorra joogid",
    "Add drink": "Lisa jook",

    # --- Editing an already logged drink ---
    "Edit drink": "Muuda jooki",
    "Save changes": "Salvesta muudatused",
    "With this": "Selle joogiga",
    "Delete": "Kustuta",
    "tap to edit · swipe to delete": "puuduta muutmiseks · libista kustutamiseks",

    # --- Drinking pace ---
    "How fast": "Kui kiiresti",
    "In one go": "Ühe hooga",
    "Counts as a single swallow — the steepest possible rise.":
        "Loetakse üheks sõõmuks – järsim võimalik tõus.",
    "A quick drink. The level climbs fast.": "Kiiresti joodud. Tase tõuseb kiiresti.",
    "A normal pace.": "Tavaline tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Aeglaselt lonksutatud. Sama alkoholikoguse juures palju laugem tõus.",

    # --- AddDrinkSheet ---
    "Cancel": "Loobu",
    "Now": "Praegu",
    "Projected peak": "Prognoositav tipp",
    "Peak at": "Tipp kell",
    "Clears": "Nullis",
    "This would cross your limit": "See ületaks su piiri",
    "Around %@, for up to %@.": "Umbes %@, kuni %@ vältel.",
    "This might cross your limit": "See võib su piiri ületada",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Aeglasema ainevahetuse korral jah, kiirema korral ei. Selles ongi hinnangu "
        "ebakindlus.",
    "Type": "Tüüp",
    "Amount": "Kogus",
    "Strength": "Kangus",
    "%@ units": "Ühikud: %@",
    "%@ g alcohol": "%@ g alkoholi",
    "Stomach": "Kõht",
    "When": "Millal",
    "Done": "Valmis",
    "Add": "Lisa",

    # --- ProfileSheet ---
    "Male": "Mees",
    "Female": "Naine",
    "Sex": "Sugu",
    "Weight": "Kaal",
    "Height": "Pikkus",
    "Age": "Vanus",
    "kg": "kg",
    "cm": "cm",
    "yrs": "a",
    "Body": "Keha",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Keha koguvesi tuleneb Watsoni võrranditest, mis määravad ruumala, millesse alkohol "
        "jaotub.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Keha koguvesi tuleneb Watsoni võrranditest, mis määravad ruumala, millesse alkohol "
        "jaotub. Naiste võrrand ei sisalda vanust, seega selle muutmine tulemust ei mõjuta.",
    "Drinking frequency": "Joomise sagedus",
    "How often do you drink?": "Kui tihti sa jood?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Nii me sinu lagundamiskiirust hindamegi. Regulaarne joomine aktiveerib maksa CYP2E1-raja, seega lagundavad sagedased joojad alkoholi kiiremini. See on mudeli nõrgim koht ja just seepärast saad jaotises „Kuva ja keel“ määrata, kui palju sellest ebakindlusest rakendus sulle näitab.",
    "Your limit": "Sinu piir",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Sinu enda võrdlusarv, mitte seaduslik piirmäär. Rakendus ütleb, kui kavandatud jook "
        "viiks sind sellest üle ja kui kaua sa sellest kõrgemal püsiksid.",
    "Calculated values": "Arvutatud väärtused",
    "Total body water": "Keha koguvesi",
    "Distribution volume": "Jaotusruumala",
    "Widmark factor": "Widmarki tegur",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmarki tegur on meestel tavaliselt umbes 0,68 ja naistel 0,55. Kui sinu oma on "
        "sellest kaugel, tasub ülaltoodud väärtused üle vaadata.",
    "Elimination rate": "Lagundamiskiirus",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Kui kiiresti su maks juba imendunud alkoholi lagundab – kõvera langeva poole "
        "kalle.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol väljub kehast ligikaudu püsiva kogusena tunnis, mitte protsendina, "
        "sest ensüüm, mis seda lagundab, töötab peaaegu igal tasemel juba täisvõimsusel. Just "
        "seepärast on üldse olemas rusikareeglid nagu „üks jook tunnis“.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Selle seadega kulub taseme %@ nulli langemiseks umbes %@. Peaaegu kõigil on see "
        "vahemikus %@ tunnis.",
    "How to find yours": "Kuidas enda oma leida",
    "With a breathalyser": "Alkomeetriga",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Puhu kaks korda vähemalt tunnise vahega, kui tase juba langeb – kaks tundi või rohkem "
        "pärast viimast jooki, ilma vahepeal midagi joomata. Lahuta teine näit esimesest ja "
        "jaga mõõtmistevaheliste tundide arvuga.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Näiteks %@ ja kaks tundi hiljem %@ annab %@ tunnis.",
    "Without one": "Ilma alkomeetrita",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Rakendus näitab, millal su tase eeldatavasti nulli jõuab. Kui oled korduvalt juba "
        "tükk aega enne seda taas tavapärases seisundis, on su kiirus seadistatust suurem – "
        "nihuta seda samm ülespoole ja jälgi paari joomiskorra jooksul. Kui see võtab "
        "ennustatust kauem, nihuta seda allapoole.",
    "What moves it": "Mis seda mõjutab",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Regulaarne joomine tõstab seda: maksaensüüm, mis selle töö ära teeb, aktiveerub "
        "kasutamisest. Keskmiselt on see naistel veidi kõrgem ning tühja kõhuga või "
        "maksaprobleemide korral madalam.",
    "Uncertainty": "Ebakindlus",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Nulli juures on iga näit üks arv – rakenduse parim hinnang. Nullist ülalpool "
        "näidatakse samu näite vahemikena ja graafiku riba laieneb vastavalt.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Üksiku arvu järgi on lihtsam õppida: aja jooksul saad teada, kuidas sinu enda 0,6 "
        "tundub. Vahemik on otsesem vastus, sest kiirus ongi ebakindel. Mõlemad on "
        "põhjendatud – see on sinu valik.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Sinu joomise sagedusest tulenev hajuvus on ± %@ tunnis.",
    "Rate": "Kiirus",
    "Range": "Vahemik",
    "Advanced": "Täpsemad seaded",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Mitu inimest",
    "History trends": "Ajaloo suundumused",
    "Week": "Nädal",
    "Month": "Kuu",
    "Year": "Aasta",
    "Sober days": "Alkoholivabad päevad",
    "Change": "Muutus",
    "before records": "enne kirjete algust",
    "See further back": "Vaata kaugemale tagasi",
    "Weeks, months and years side by side — and every evening older than seven days.": "Nädalad, kuud ja aastad kõrvuti – ja iga üle seitsme päeva vanune õhtu.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Kõik, mille oled kirja pannud, on juba salvestatud. Avamine ainult näitab seda.",
    "Coming soon": "Peagi",
    "Today": "Täna",
    "Day": "Päev",
    "Yesterday": "Eile",
    "No drinks on this day": "Sel päeval jooke polnud",
    "Trend": "Trend",
    "day": "päev",
    "Smoothing": "Silumine",
    "%@ sessions": "%@ korda",
    "No data before %@": "Andmed puuduvad enne %@",
    "vs.": "vs",
    "Grams": "Grammid",
    "Grams of alcohol": "Alkohol grammides",
    "Standard units": "Standardühikud",
    "Unit size": "Ühiku suurus",
    "Automatic": "Automaatne",
    "UK": "Ühendkuningriik",
    "Nordic countries": "Põhjamaad",
    "US standard drink": "USA standardjook",
    "WHO, most of Europe": "WHO, suurem osa Euroopast",
    "Period": "Periood",
    "Switch person": "Vaheta inimest",
    "Add person": "Lisa inimene",
    "New person": "Uus inimene",
    "You": "Sina",
    "Name": "Nimi",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Kõik neli muudavad kõverat, nii et ühtegi neist ei saa kellegi teise eest ära arvata.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Tema enda piiri ja täpsemaid seadeid saab hiljem muuta Profiili vahekaardil, kui tema "
        "on valitud inimene.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Kiirlisamine",
    "Choose a favourite drink": "Vali lemmikjook",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Vali jook, mida tavaliselt tellid, ja Hetkeseisu ekraanil olev nupp lisab selle "
        "ühe puudutusega.",
    "This is your quick-add drink": "See on sinu kiirlisamise jook",
    "Set as my quick-add drink": "Määra kiirlisamise joogiks",
    "This is now your usual": "See on nüüd sinu tavajook",
    "Remove favourite": "Eemalda lemmik",
    "Always add this one": "Lisa alati see",
    "Logs it straight away, without opening anything.":
        "Lisab selle kohe, ilma midagi avamata.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Üks puudutus Hetkeseisu ekraanil lisab selle ja nupul on näha prognoositav tipp. "
        "Kõhutäius võetakse eelmiselt joogilt ja seda saab kohe pärast parandada.",
    "Peak %@": "Tipp %@",
    "%@ added": "%@ lisatud",
    "Save": "Salvesta",
    "Undo": "Võta tagasi",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Varukoopia",
    "Export a backup": "Ekspordi varukoopia",
    "Import a backup": "Impordi varukoopia",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Varukoopia sisaldab kõiki inimesi, joomiskordi ja jooke. Importimine lisab selle, mis "
        "puudub – see ei muuda ega eemalda kunagi midagi, mis siin juba on.",
    "Import this backup?": "Kas importida see varukoopia?",
    "Import": "Impordi",
    "Everything in this backup is already here.": "Kõik selles varukoopias on juba siin.",
    "Import finished": "Importimine lõpetatud",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Keel",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Avab selle rakenduse lehe rakenduses Settings, kus valik „Preferred Language“ määrab "
        "rakenduse enda keele – süsteemi keel jääb samaks. Kui keelt muudad, taaskäivitab iOS "
        "rakenduse.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Importimine ebaõnnestus",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "See fail ei ole LogMyDrinki varukoopia või on see kahjustatud.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "See varukoopia on tehtud LogMyDrinki uuema versiooniga. Uuenda rakendust ja proovi "
        "uuesti.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Lisatavad joomiskorrad: %@, joogid: %@, kuusummad: %@. Midagi siinolevast ei muudeta ega eemaldata.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Lisatud: %@ joomiskorda, %@ jooki ja %@ kuusummat.',
    'months as totals': 'kuud ainult summana',
    'by month only': 'ainult kuu kaupa',
    'monthly total': 'kuusumma',
    'No daily records for this day': 'Selle päeva kohta pole päevapõhiseid kirjeid',
    'Monthly total: %@': 'Kuusumma: %@',
    'A dry month': 'Kuiv kuu',

    # --- RemovePersonSection ---
    'Remove %@?': 'Kas eemaldada %@?',
    'Remove': 'Eemalda',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Kustutab joomiskorrad: %@, joogid: %@ ja kuusummad: %@. Seda ei saa tagasi võtta.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Kustutab joomiskorrad: %@ ja joogid: %@. Seda ei saa tagasi võtta.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Libista külalise real vasakule, et ta koos kõige tema nimele salvestatuga eemaldada. Sind eemaldada ei saa.',
    'People': 'Inimesed',
    'Owner': 'Omanik',
    'Everyone this app records. Switch, add, or remove someone.': 'Kõik, kelle andmeid see rakendus talletab. Vaheta, lisa või eemalda keegi.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Eelmiselt õhtult üle kantud',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorid',
    'Sessions': 'Korrad',
    'Per session': 'Korra kohta',
    'Under the influence': 'Joobes',
    '%@ of the time': '%@ ajast',
    'Days over limit': 'Päevad üle piiri',
    'Longest sober run': 'Pikim kaine periood',
    'Favourite drink': 'Lemmikjook',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Kuva ja keel",
    "Data": "Andmed",
    "Concentration": "Kontsentratsioon",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Jäta kiirus sageduse küsimuse hooleks, kui sul pole mõõtmist, millega seda võrrelda.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Hinnang, mitte mõõtmine. Ära kunagi otsusta selle põhjal, kas võid autot juhtida.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Hinnanguline vahemik, mitte mõõtmine. Ära kunagi otsusta selle põhjal, kas võid autot juhtida.',
    'How does the app calculate this?':
        'Kuidas rakendus seda arvutab?',
    'approximately %@ %@':
        'umbes %@ %@',
    'How it works':
        'Kuidas see töötab',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Ära kunagi otsusta selle põhjal, kas võid autot juhtida. Rakendus hindab, mitte ei mõõda, ja sinu tegelik tase võib märkimisväärselt erineda.',
    'Why this app exists':
        'Miks see rakendus on olemas',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink aitab sul teadlikumalt juua ja kontrolli säilitada. Otsus sünnib enne järgmist klaasi, seega näitab rakendus ette, kuhu järgmine jook su taseme viiks ja millal see tipu saavutaks.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Kuid see ei puuduta ainult tänast õhtut. Iga lisatud jook läheb sinu Ajalukku, nii et kuude ja aastate jooksul näed, kui palju ja kui sageli sa jood ning kui kõrgele su tase tõuseb. Sellest joonistuvad välja sinu mustrid ning ka suund, kuhu need liiguvad – kas asjad lähevad paremaks või halvemaks.',
    'How it calculates':
        'Kuidas see arvutab',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Hinnang põhineb Widmarki meetodil, millega on vere alkoholisisaldust hinnatud alates 1930. aastatest; rakendus kasutab selle täiustatud versiooni.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Sinu kaalu, pikkuse, vanuse ja soo põhjal arvutab see, kui palju vett su kehas on, sest alkohol jaotub just sinna. Iga jooki jälgitakse eraldi: kui palju alkoholi selles oli, kui kiiresti sa selle jõid ja kui palju olid söönud, sest see määrab imendumise kiiruse.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Samal ajal lagundab maks igas tunnis umbes ühesuguse koguse; sinu puhul hinnatakse seda kogust selle põhjal, kui sageli sa jood. Tulemuseks on kõver minut minuti haaval: kus sa praegu oled, kuhu liigud ja millal oled taas nullis.',
    'Details':
        'Üksikasjad',
    'Body water':
        'Keha vesi',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsoni valem (1980) kaalu, pikkuse, vanuse ja soo põhjal. Naiste valemis vanust ei ole – see on valemi omadus, mitte viga. Jaotusruumala on keha vesi jagatud 0,85-ga ehk vere veesisaldusega.',
    'Absorption':
        'Imendumine',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Igal joogil on oma „magu“. Tühja kõhuga imendub pool alkoholist umbes 7 minutiga, täis kõhuga umbes 21 minutiga. Lonksuhaaval joodud jook jõuab makku ühtlaselt kogu joomise aja jooksul.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Tipp on madalam ja nulli jõutakse varem. Üllatav, kuid mõõdetud: toiduga lagundab magu osa alkoholist enne imendumist (rakendus arvestab 5, 10 ja 15 protsendiga) ja seda, mis kunagi verre ei jõudnud, ei pea lagundama.',
    'Elimination':
        'Lagundamine',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Umbes 0,15 ‰ tunnis (avaldatud vahemik 0,10–0,25), regulaarselt jooval inimesel rohkem, sest maksa ensüümid kohanevad. Nulli lähedal see aeglustub (Michaelise-Menteni kineetika), nii et kõver sujub järk-järgult välja, mitte ei katke järsult.',
    'Computation':
        'Arvutus',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Kõver pärineb numbrilisest simulatsioonist minutilise täpsusega.',
    'Why it is only an estimate':
        'Miks see on vaid hinnang',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Rakendus ei mõõda midagi. See näitab keskmistel väärtustel põhineva mudeli tulemust ja tegelikkus võib erineda. Suurim tundmatu on see, kui kiiresti sa alkoholi lagundad: usutava vahemiku piires võib see üksi nihutada samal õhtul tippu 40 protsendi ja nulli jõudmise aega nelja tunni võrra.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Oma osa on ka geenidel, maksa tervisel, ravimitel, söödud toidul, unel ja väsimusel – mitte ühestki neist rakendus ei tea. Täpse väärtuse annab ainult taadeldud alkomeeter või vereanalüüs.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Arv on siiski kasulik. Kui rakendus näitab sinu puhul järjekindlalt veidi liiga palju või vähe, eksib see igal õhtul samas suunas, nii et aja jooksul õpid, mida konkreetne väärtus sinu jaoks tähendab. Profiilis saad näidata ka lagundamiskiiruse ebakindlust: siis näed ühe arvu asemel vahemikku.',
    'Tips':
        'Nõuanded',
    'Favourite drink in one tap':
        'Lemmikjook ühe puudutusega',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Vali Profiilis lemmik ja Hetkeseisu nupp lisab selle ühe puudutusega.',
    'Widget':
        'Vidin',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Lisa see Lock Screen-kuvale või Home Screen-kuvasse: üks puudutus lisab sinu lemmiku. Kuni su kehas on alkoholi, näitab see ka sinu taset ja selle suunda.',
    'How do I add it?':
        'Kuidas seda lisada?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Ütle „Hey Siri, LogMyDrink now“ ja Siri lisab sinu lemmiku ning ütleb, kuhu su tipp liigub. (Käsk toimib inglise keeles.)',
    'Looking back':
        'Tagasivaade',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        'Hetkeseisu ülaosas olev „Eile“ viib ühe puudutusega eelmisele päevale; vahekaart Ajalugu näitab sinu mustreid nädalate, kuude ja aastate lõikes.',
    'Logging later':
        'Hilisem lisamine',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Kui lisad joogi tagantjärele, sea aeg nuppudega − ja + tagasi; vahele jäänud päeva saad täiendada Ajaloo vaates Päev.',
    'One tap and done':
        'Üks puudutus ja valmis',
    'Your favourite from the Lock Screen':
        'Sinu lemmik Lock Screen-kuvalt',
    'Say it, don’t type it':
        'Ütle, ära trüki',
    'See your patterns':
        'Vaata oma mustreid',
    'Set what you drink most often and log it with a single tap.':
        'Määra, mida sa kõige sagedamini jood, ja lisa see ühe puudutusega.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Üks puudutus vidinal lisab sinu lemmiku, rakendust otsimata. Õhtul näitab see ka sinu taset.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now“ – Siri lisab sinu lemmiku ja ütleb, kuhu su tipp liigub.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Ajalugu näitab, kui palju sa nädalate, kuude ja aastate jooksul jood ja kui kõrgele su tase tõuseb ning mis suunas see muutub.',
    'Set favourite':
        'Määra lemmik',
    'Add widget':
        'Lisa vidin',
    'Got it':
        'Selge',
    'Open History':
        'Ava Ajalugu',
    'Don’t show again':
        'Ära enam näita',
    'Lock Screen':
        'Lock Screen-kuva',
    'Home Screen':
        'Home Screen-kuva',
    'Where':
        'Kuhu',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Lukusta iPhone ning seejärel puuduta ja hoia Lock Screen-kuva.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Puuduta valikut Customize, siis Lock Screen ja seejärel kella all olevat vidinarida.',
    'Choose LogMyDrink, then tap Done.':
        'Vali LogMyDrink ja puuduta valikut Done.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Puuduta ja hoia Home Screen-kuva tühja kohta, kuni ikoonid hakkavad värisema.',
    'Tap Edit, then Add Widget.':
        'Puuduta valikut Edit ja seejärel Add Widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Otsi rakendust LogMyDrink, vali suurus ja puuduta valikut Add Widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Vidina puudutus avab rakenduse ja lisab sinu lemmikjoogi. Kuni su kehas on alkoholi, näitab see ka sinu taset ja selle suunda.',
    'Add the widget':
        'Lisa vidin',
    'Show tips':
        'Näita nõuandeid',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Kõige rohkem üks nõuanne päevas rakenduse avamisel – mitte kunagi, kui su kehas on alkoholi.',
}
