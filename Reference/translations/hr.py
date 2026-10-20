"""
Croatian.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promil",
    "Percent": "Postotak",

    # --- DrinkCatalog: drink types ---
    "Beer": "Pivo",
    "Wine": "Vino",
    "Champagne": "Pjenušac",
    "Shot": "Žestica",
    "Cocktail": "Koktel",
    "Custom": "Prilagođeno",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Prazan želudac",
    "Moderately full": "Umjereno pun",
    "Full stomach": "Pun želudac",
    "Empty": "Prazan",
    "Moderate": "Umjereno pun",
    "Full": "Pun",
    "Fast absorption, higher and earlier peak.": "Brza apsorpcija, viši i raniji vrhunac.",
    "Moderate absorption.": "Umjerena apsorpcija.",
    "Slow absorption, lower and later peak.": "Spora apsorpcija, niži i kasniji vrhunac.",

    # --- DrinkingFrequency ---
    "Rarely": "Rijetko",
    "A few times a month": "Nekoliko puta mjesečno",
    "Several times a week": "Više puta tjedno",
    "Almost daily": "Gotovo svakodnevno",
    "A few occasions a year": "Nekoliko puta godišnje",
    "Social drinking": "Društveno pijenje",
    "Weekly routine": "Tjedna rutina",
    "Daily or nearly daily": "Svaki dan ili gotovo svaki dan",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Vrijeme",
    "Level": "Razina",
    "Lower": "Donja",
    "Upper": "Gornja",
    "Lower estimate": "Donja procjena",
    "Upper estimate": "Gornja procjena",
    "Personal limit": "Osobna granica",
    "Drink": "Piće",

    # --- BACChartView ---
    "Expected peak around %@": "Očekivani vrhunac oko %@",
    "Peaked around %@": "Vrhunac je bio oko %@",
    "No active session": "Nema aktivne sesije",
    "Still rising": "Još raste",
    "YOUR LIMIT %@": "TVOJA GRANICA %@",
    "possible range": "mogući raspon",

    # --- Live screen: the day with nothing on it ---
    "Live": "Uživo",
    "Nothing logged today": "Danas ništa nije zabilježeno",
    "Add a drink when you have one.": "Dodaj piće kad ga popiješ.",

    # --- Tabs and history ---
    "History": "Povijest",
    "No past sessions yet": "Još nema prošlih sesija",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Sesija se ovdje pojavljuje nakon što završi – kad ti razina padne na nulu i prođe "
        "nekoliko sati.",
    "%@ drinks": "Pića: %@",
    "peak": "vrhunac",
    "Started": "Počelo",
    "Lasted": "Trajalo",
    "Duration": "Trajanje",
    "Sober around": "Trijezan pribl.",
    "Sober at": "Trijezan u",
    "Remaining": "Preostalo",
    "next day": "sljedeći dan",
    "previous day": "prethodni dan",
    "%@ days later": "%@ dana kasnije",
    "%@ days earlier": "%@ dana ranije",
    "Calculated with your profile at the time": "Izračunato s tvojim tadašnjim profilom",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Pića",
    "Units": "Jedinice",
    "Drinks this session": "Pića u ovoj sesiji",
    "Add drink": "Dodaj piće",

    # --- Editing an already logged drink ---
    "Edit drink": "Uredi piće",
    "Save changes": "Spremi promjene",
    "With this": "S ovim pićem",
    "Delete": "Izbriši",
    "tap to edit · swipe to delete": "dodirni za uređivanje · povuci za brisanje",

    # --- Drinking pace ---
    "How fast": "Koliko brzo",
    "In one go": "Naiskap",
    "Counts as a single swallow — the steepest possible rise.":
        "Računa se kao jedan gutljaj – najstrmiji mogući porast.",
    "A quick drink. The level climbs fast.": "Brzo popijeno piće. Razina brzo raste.",
    "A normal pace.": "Uobičajen tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Polako pijuckano. Mnogo blaži porast za istu količinu alkohola.",

    # --- AddDrinkSheet ---
    "Cancel": "Odustani",
    "Now": "Sada",
    "Projected peak": "Predviđeni vrhunac",
    "Peak at": "Vrhunac u",
    "Clears": "Pad na nulu",
    "This would cross your limit": "Ovo bi prešlo tvoju granicu",
    "Around %@, for up to %@.": "Oko %@, u trajanju do %@.",
    "This might cross your limit": "Ovo bi moglo prijeći tvoju granicu",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Uz sporiji metabolizam da, uz brži ne. To je nesigurnost procjene.",
    "Type": "Vrsta",
    "Amount": "Količina",
    "Strength": "Jačina",
    "%@ units": "Jedinice: %@",
    "%@ g alcohol": "%@ g alkohola",
    "Stomach": "Želudac",
    "When": "Kada",
    "Done": "Gotovo",
    "Add": "Dodaj",

    # --- ProfileSheet ---
    "Male": "Muško",
    "Female": "Žensko",
    "Sex": "Spol",
    "Weight": "Težina",
    "Height": "Visina",
    "Age": "Dob",
    "kg": "kg",
    "cm": "cm",
    "yrs": "god.",
    "Body": "Tijelo",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Ukupna tjelesna voda proizlazi iz Watsonovih jednadžbi, koje određuju volumen u koji "
        "se alkohol raspoređuje.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Ukupna tjelesna voda proizlazi iz Watsonovih jednadžbi, koje određuju volumen u koji "
        "se alkohol raspoređuje. Ženska jednadžba ne uključuje dob, pa njezina promjena neće "
        "utjecati na rezultat.",
    "Drinking frequency": "Učestalost pijenja",
    "How often do you drink?": "Koliko često piješ?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Ovako procjenjujemo tvoju brzinu razgradnje. Redovito pijenje potiče jetreni put CYP2E1, pa redoviti konzumenti brže razgrađuju alkohol. To je najslabija točka modela, zbog čega u odjeljku Prikaz i jezik možeš postaviti koliko ti te nesigurnosti aplikacija prikazuje.",
    "Your limit": "Tvoja granica",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Tvoj vlastiti orijentacijski broj, a ne zakonska granica. Aplikacija ti javlja kad bi "
        "te planirano piće odvelo preko nje i koliko dugo bi razina ostala iznad.",
    "Calculated values": "Izračunate vrijednosti",
    "Total body water": "Ukupna tjelesna voda",
    "Distribution volume": "Volumen raspodjele",
    "Widmark factor": "Widmarkov faktor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmarkov faktor obično iznosi oko 0,68 za muškarce i 0,55 za žene. Ako je tvoj "
        "daleko od toga, vrijedi provjeriti gornje vrijednosti.",
    "Elimination rate": "Brzina razgradnje",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Koliko brzo tvoja jetra razgrađuju alkohol nakon što se apsorbira – nagib silazne "
        "strane krivulje.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol se razgrađuje u otprilike stalnoj količini na sat, a ne u postotku, jer enzim "
        "koji ga razgrađuje već radi punim kapacitetom pri gotovo svakoj razini. Zato uopće i "
        "postoje pravila poput „jedno piće na sat”.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Pri ovoj postavci %@ pada na nulu za otprilike %@. Gotovo svi su između %@ na sat.",
    "How to find yours": "Kako pronaći svoju",
    "With a breathalyser": "S alkometrom",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Puhni dvaput, s razmakom od najmanje sat vremena, na silaznoj strani – dva sata ili "
        "više nakon zadnjeg pića, a da u međuvremenu ništa ne popiješ. Oduzmi drugo očitanje od prvog i "
        "podijeli s brojem sati između njih.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Na primjer, %@ i %@ dva sata poslije daje %@ na sat.",
    "Without one": "Bez alkometra",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Aplikacija ti govori kad očekuje da ćeš biti na nuli. Ako se pouzdano osjećaš "
        "normalno znatno prije toga, tvoja je brzina veća od postavke – pomakni je stupanj gore "
        "i prati nekoliko sesija. Ako traje dulje od predviđenog, pomakni je stupanj dolje.",
    "What moves it": "Što na nju utječe",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Raste s redovitim pijenjem: jetreni enzim koji obavlja posao potiče se upotrebom. U "
        "prosjeku je nešto viša i kod žena, a niža na prazan želudac ili uz bolest jetre.",
    "Uncertainty": "Nesigurnost",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Na nuli je svaka brojka jedan broj – najbolja procjena aplikacije. Iznad nule iste se "
        "brojke prikazuju kao rasponi, a pojas na grafikonu proširuje se u skladu s tim.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Uz jedan broj lakše je učiti: s vremenom otkriješ kako se osjećaš na svojih 0,6. "
        "Raspon je doslovniji odgovor jer je brzina doista nesigurna. Oboje je opravdano – "
        "odluka je tvoja.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Raspon koji proizlazi iz tvoje učestalosti pijenja iznosi ± %@ na sat.",
    "Rate": "Brzina",
    "Range": "Raspon",
    "Advanced": "Napredno",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Više osoba",
    "History trends": "Trendovi povijesti",
    "Week": "Tjedan",
    "Month": "Mjesec",
    "Year": "Godina",
    "Sober days": "Dani bez alkohola",
    "Change": "Promjena",
    "before records": "prije početka bilježenja",
    "See further back": "Pogledaj dalje unatrag",
    "Weeks, months and years side by side — and every evening older than seven days.": "Tjedni, mjeseci i godine jedno uz drugo – i svaka večer starija od sedam dana.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Sve što si zabilježio već je spremljeno. Otključavanje to samo prikazuje.",
    "Coming soon": "Uskoro",
    "Today": "Danas",
    "Day": "Dan",
    "Yesterday": "Jučer",
    "No drinks on this day": "Nema pića ovog dana",
    "Trend": "Trend",
    "day": "dan",
    "Smoothing": "Izglađivanje",
    "%@ sessions": "Sesije: %@",
    "No data before %@": "Nema podataka prije %@",
    "vs.": "u odnosu na",
    "Grams": "Grami",
    "Grams of alcohol": "Grami alkohola",
    "Standard units": "Standardne jedinice",
    "Unit size": "Veličina jedinice",
    "Automatic": "Automatski",
    "UK": "Ujedinjeno Kraljevstvo",
    "Nordic countries": "Nordijske zemlje",
    "US standard drink": "Standardno piće u SAD-u",
    "WHO, most of Europe": "SZO, veći dio Europe",
    "Period": "Razdoblje",
    "Switch person": "Promijeni osobu",
    "Add person": "Dodaj osobu",
    "New person": "Nova osoba",
    "You": "Ti",
    "Name": "Ime",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Sve četiri vrijednosti mijenjaju krivulju, pa se nijedna ne može nagađati za nekog "
        "drugog.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Granicu te osobe i detaljnije postavke možeš kasnije promijeniti na kartici Profil "
        "dok je ta osoba odabrana.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Brzi unos",
    "Choose a favourite drink": "Odaberi omiljeno piće",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Odaberi piće koje obično naručuješ i gumb na zaslonu Uživo zabilježit će ga jednim "
        "dodirom.",
    "This is your quick-add drink": "Ovo je tvoje piće za brzi unos",
    "Set as my quick-add drink": "Postavi kao piće za brzi unos",
    "This is now your usual": "Ovo je sada tvoje uobičajeno piće",
    "Remove favourite": "Ukloni omiljeno piće",
    "Always add this one": "Uvijek dodaj ovo piće",
    "Logs it straight away, without opening anything.":
        "Bilježi ga odmah, bez otvaranja ičega.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Jedan dodir na zaslonu Uživo bilježi ovo piće, s predviđenim vrhuncem na gumbu. "
        "Koliko ti je želudac pun preuzima se od prethodnog pića i može se ispraviti odmah "
        "nakon toga.",
    "Peak %@": "Vrhunac %@",
    "%@ added": "Dodano: %@",
    "Save": "Spremi",
    "Undo": "Poništi",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Sigurnosna kopija",
    "Export a backup": "Izvezi sigurnosnu kopiju",
    "Import a backup": "Uvezi sigurnosnu kopiju",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Sigurnosna kopija sadrži sve osobe, sesije i pića. Uvoz dodaje ono što nedostaje – "
        "nikad ne mijenja ni ne uklanja ono što je već ovdje.",
    "Import this backup?": "Uvesti ovu sigurnosnu kopiju?",
    "Import": "Uvezi",
    "Everything in this backup is already here.": "Sve iz ove sigurnosne kopije već je ovdje.",
    "Import finished": "Uvoz završen",
    "OK": "U redu",

    # --- LanguageSection: the app's language ---
    "Language": "Jezik",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Otvara ovu aplikaciju u Postavkama, gdje „Željeni jezik” određuje jezik same "
        "aplikacije – jezik sustava ostaje nepromijenjen. iOS ponovno pokreće aplikaciju kad ga "
        "promijeniš.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Uvoz nije uspio",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Ova datoteka nije sigurnosna kopija aplikacije LogMyDrink ili je oštećena.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Ova sigurnosna kopija napravljena je novijom verzijom aplikacije LogMyDrink. Ažuriraj "
        "aplikaciju i pokušaj ponovno.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Dodat će se – sesije: %@, pića: %@, mjesečni zbrojevi: %@. Ništa što je već ovdje neće se promijeniti ni ukloniti.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Dodano – sesije: %@, pića: %@, mjesečni zbrojevi: %@.',
    'months as totals': 'mjeseci samo kao zbroj',
    'by month only': 'samo po mjesecima',
    'monthly total': 'mjesečni zbroj',
    'No daily records for this day': 'Za ovaj dan nema dnevnih zapisa',
    'Monthly total: %@': 'Mjesečni zbroj: %@',
    'A dry month': 'Suh mjesec',

    # --- RemovePersonSection ---
    'Remove %@?': 'Ukloniti %@?',
    'Remove': 'Ukloni',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Briše sesije: %@, pića: %@ i mjesečne zbrojeve: %@. Ovo se ne može poništiti.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Briše sesije: %@ i pića: %@. Ovo se ne može poništiti.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Povuci gosta ulijevo da ga ukloniš zajedno sa svime što je za njega zabilježeno. Tebe se ne može ukloniti.',
    'People': 'Osobe',
    'Owner': 'Vlasnik',
    'Everyone this app records. Switch, add, or remove someone.': 'Svi koje ova aplikacija bilježi. Prebaci, dodaj ili ukloni nekoga.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Preneseno iz prethodne večeri',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorije',
    'Sessions': 'Sesije',
    'Per session': 'Po sesiji',
    'Under the influence': 'Pod utjecajem',
    '%@ of the time': '%@ vremena',
    'Days over limit': 'Dani iznad granice',
    'Longest sober run': 'Najduži niz bez alkohola',
    'Favourite drink': 'Omiljeno piće',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Prikaz i jezik",
    "Data": "Podaci",
    "Concentration": "Koncentracija",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Brzinu prepusti pitanju o učestalosti, osim ako imaš mjerenje s kojim je možeš usporediti.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Procjena, ne mjerenje. Nikad na temelju ovoga ne odlučuj smiješ li voziti.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Procijenjeni raspon, ne mjerenje. Nikad na temelju ovoga ne odlučuj smiješ li voziti.',
    'How does the app calculate this?':
        'Kako aplikacija to izračunava?',
    'approximately %@ %@':
        'otprilike %@ %@',
    'How it works':
        'Kako radi',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nikad na temelju ovoga ne odlučuj smiješ li voziti. Aplikacija procjenjuje, ne mjeri, a tvoja stvarna razina može se znatno razlikovati.',
    'Why this app exists':
        'Čemu ova aplikacija',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink ti pomaže piti svjesnije i zadržati kontrolu. Odluka se donosi prije sljedeće čaše, pa ti aplikacija unaprijed pokazuje kamo bi tvoju razinu odvelo još jedno piće i kada bi dosegla vrhunac.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'No ne radi se samo o ovoj večeri. Svako zabilježeno piće ide u Povijest, pa kroz mjesece i godine vidiš koliko, koliko često i do koje razine piješ. Iz toga se iscrtavaju tvoji obrasci, ali i smjer u kojem se mijenjaju – idu li stvari nabolje ili nagore.',
    'How it calculates':
        'Kako računa',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Procjena se temelji na Widmarkovoj metodi kojom se alkohol u krvi procjenjuje od 1930-ih; aplikacija koristi njezinu poboljšanu inačicu.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Iz tvoje težine, visine, dobi i spola izračunava koliko vode ima u tvom tijelu, jer se alkohol raspoređuje upravo u njoj. Svako piće prati zasebno: koliko je alkohola sadržavalo, koliko si ga brzo popio i koliko si prije toga pojeo, jer o tome ovisi brzina apsorpcije.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Za to vrijeme jetra svaki sat razgrade otprilike stalnu količinu; tvoja se procjenjuje prema tome koliko često piješ. Rezultat je krivulja, minutu po minutu: gdje si sada, kamo ideš i kada ćeš opet biti na nuli.',
    'Details':
        'Pojedinosti',
    'Body water':
        'Tjelesna voda',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsonova formula (1980) iz težine, visine, dobi i spola. Formula za žene ne sadrži dob – to je svojstvo formule, a ne pogreška. Volumen raspodjele je tjelesna voda podijeljena s 0,85, udjelom vode u krvi.',
    'Absorption':
        'Apsorpcija',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Svako piće ima svoj „želudac”. Na prazan želudac polovica alkohola apsorbira se za oko 7 minuta, na pun za oko 21. Piće koje pijuckaš ulazi u želudac ravnomjerno tijekom cijelog pijenja.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Daje niži vrhunac i raniju nulu. Iznenađujuće, ali izmjereno: uz hranu želudac razgradi dio alkohola prije apsorpcije (aplikacija računa s 5, 10 i 15 posto), a ono što nikad nije ušlo ne treba razgraditi.',
    'Elimination':
        'Razgradnja',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Oko 0,15 ‰ na sat (objavljeni raspon 0,10–0,25), više kod onih koji redovito piju jer se enzimi jetre prilagode. Blizu nule usporava (Michaelis-Mentenina kinetika), pa se krivulja postupno izravnava umjesto da naglo stane.',
    'Computation':
        'Izračun',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Krivulja proizlazi iz numeričke simulacije s razlučivošću od jedne minute.',
    'Why it is only an estimate':
        'Zašto je to samo procjena',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Aplikacija ništa ne mjeri. Prikazuje rezultat modela s prosječnim vrijednostima, a stvarnost se može razlikovati. Najveća je nepoznanica koliko brzo razgrađuješ alkohol: unutar vjerojatnog raspona samo to iste večeri može pomaknuti vrhunac za 40 posto, a nulu za četiri sata.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Važni su i geni, zdravlje jetre, lijekovi, što si jeo, san i umor – ništa od toga aplikacija ne zna. Točnu vrijednost daje samo ovjereni alkometar ili krvna pretraga.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Broj je ipak koristan. Ako ti aplikacija dosljedno pokazuje malo previše ili premalo, svake večeri griješi u istom smjeru, pa s vremenom naučiš što određena vrijednost znači za tebe. U Profilu možeš prikazati i nesigurnost brzine razgradnje: tada umjesto jednog broja vidiš raspon.',
    'Tips':
        'Savjeti',
    'Favourite drink in one tap':
        'Omiljeno piće jednim dodirom',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Postavi omiljeno piće u Profilu i gumb na zaslonu Uživo zabilježit će ga jednim dodirom.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Dodaj ga na zaključani ili početni zaslon: jedan dodir bilježi tvoje omiljeno piće. Dok imaš alkohola u tijelu, prikazuje i tvoju razinu i njezin smjer.',
    'How do I add it?':
        'Kako ga dodati?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Reci „Hey Siri, LogMyDrink now” i Siri će zabilježiti tvoje omiljeno piće te ti reći kakav vrhunac možeš očekivati. (Naredba radi na engleskom.)',
    'Looking back':
        'Pogled unatrag',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Jučer” na vrhu zaslona Uživo te jednim dodirom vodi na prethodni dan; kartica Povijest prikazuje tvoje obrasce kroz tjedne, mjesece i godine.',
    'Logging later':
        'Naknadno bilježenje',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Ako piće bilježiš naknadno, vrati vrijeme unatrag gumbima − i +; propušteni dan možeš dopuniti u prikazu Dan u Povijesti.',
    'One tap and done':
        'Jedan dodir i gotovo',
    'Your favourite from the Lock Screen':
        'Omiljeno piće sa zaključanog zaslona',
    'Say it, don’t type it':
        'Reci, ne tipkaj',
    'See your patterns':
        'Pogledaj svoje obrasce',
    'Set what you drink most often and log it with a single tap.':
        'Postavi što najčešće piješ i bilježi to jednim dodirom.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Jedan dodir widgeta bilježi tvoje omiljeno piće, bez traženja aplikacije. Navečer prikazuje i tvoju razinu.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now” – Siri bilježi tvoje omiljeno piće i kaže ti kakav vrhunac možeš očekivati.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Povijest prikazuje koliko i do koje razine piješ kroz tjedne, mjesece i godine te u kojem se smjeru to mijenja.',
    'Set favourite':
        'Postavi omiljeno',
    'Add widget':
        'Dodaj widget',
    'Got it':
        'Razumijem',
    'Open History':
        'Otvori Povijest',
    'Don’t show again':
        'Ne prikazuj više',
    'Lock Screen':
        'Zaključani zaslon',
    'Home Screen':
        'Početni zaslon',
    'Where':
        'Gdje',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Zaključaj iPhone, zatim dodirni i drži zaključani zaslon.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Dodirni Prilagodi, zatim Zaključani zaslon pa red widgeta ispod sata.',
    'Choose LogMyDrink, then tap Done.':
        'Odaberi LogMyDrink i dodirni U redu.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Dodirni i drži prazan dio početnog zaslona dok ikone ne počnu titrati.',
    'Tap Edit, then Add Widget.':
        'Dodirni Uredi pa Dodaj widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Potraži LogMyDrink, odaberi veličinu i dodirni Dodaj widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Dodir widgeta otvara aplikaciju i bilježi tvoje omiljeno piće. Dok imaš alkohola u tijelu, prikazuje i tvoju razinu i njezin smjer.',
    'Add the widget':
        'Dodaj widget',
    'Show tips':
        'Prikazuj savjete',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Najviše jedan savjet dnevno pri otvaranju aplikacije – nikad dok imaš alkohola u tijelu.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Što broj pokazuje',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Broj je procjena koncentracije alkohola u tvojoj krvi (engleski BAC, blood alcohol concentration): koliko alkohola imaš u krvi.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'U promilima (‰) to su grami alkohola po litri krvi: 0,5 ‰ znači pola grama u svakoj litri. U postocima to su grami na 100 mililitara, pa ista razina daje deset puta manji broj: 0,5 ‰ je 0,05 posto. Između njih možeš prebaciti u Profil › Prikaz i jezik.',
    'The curve shows the same level over time, minute by minute.':
        'Krivulja prikazuje istu razinu kroz vrijeme, minutu po minutu.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promil (‰) su grami alkohola po litri krvi, postotak grami na 100 mililitara: 0,5 ‰ je 0,05 posto.',
}
