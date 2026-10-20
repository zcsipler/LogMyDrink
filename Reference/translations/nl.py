"""
Dutch.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promille",
    "Percent": "Procent",

    # --- DrinkCatalog: drink types ---
    "Beer": "Bier",
    "Wine": "Wijn",
    "Champagne": "Mousserend",
    "Shot": "Shotje",
    "Cocktail": "Cocktail",
    "Custom": "Aangepast",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Lege maag",
    "Moderately full": "Half volle maag",
    "Full stomach": "Volle maag",
    "Empty": "Leeg",
    "Moderate": "Half",
    "Full": "Vol",
    "Fast absorption, higher and earlier peak.": "Snelle opname, hogere en vroegere piek.",
    "Moderate absorption.": "Gemiddelde opname.",
    "Slow absorption, lower and later peak.": "Langzame opname, lagere en latere piek.",

    # --- DrinkingFrequency ---
    "Rarely": "Zelden",
    "A few times a month": "Een paar keer per maand",
    "Several times a week": "Meerdere keren per week",
    "Almost daily": "Bijna dagelijks",
    "A few occasions a year": "Een paar keer per jaar",
    "Social drinking": "Sociaal drinken",
    "Weekly routine": "Wekelijkse routine",
    "Daily or nearly daily": "Dagelijks of bijna dagelijks",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Tijd",
    "Level": "Niveau",
    "Lower": "Onder",
    "Upper": "Boven",
    "Lower estimate": "Onderste schatting",
    "Upper estimate": "Bovenste schatting",
    "Personal limit": "Persoonlijke limiet",
    "Drink": "Drankje",

    # --- BACChartView ---
    "Expected peak around %@": "Verwachte piek rond %@",
    "Peaked around %@": "Piek lag rond %@",
    "No active session": "Geen actieve sessie",
    "Still rising": "Nog stijgend",
    "YOUR LIMIT %@": "JE LIMIET %@",
    "possible range": "mogelijk bereik",

    # --- Live screen: the day with nothing on it ---
    "Live": "Live",
    "Nothing logged today": "Vandaag niets vastgelegd",
    "Add a drink when you have one.": "Voeg een drankje toe wanneer je er een neemt.",

    # --- Tabs and history ---
    "History": "Geschiedenis",
    "No past sessions yet": "Nog geen eerdere sessies",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Een sessie verschijnt hier zodra hij is afgelopen – wanneer je niveau weer op nul "
        "staat en er een paar uur voorbij zijn.",
    "%@ drinks": "%@ drankjes",
    "peak": "piek",
    "Started": "Begonnen",
    "Lasted": "Duurde",
    "Duration": "Duur",
    "Sober around": "Nuchter ca.",
    "Sober at": "Nuchter",
    "Remaining": "Resterend",
    "next day": "de volgende dag",
    "previous day": "de dag ervoor",
    "%@ days later": "%@ dagen later",
    "%@ days earlier": "%@ dagen eerder",
    "Calculated with your profile at the time": "Berekend met je profiel van dat moment",

    # --- TodayView ---
    "Profile": "Profiel",
    "Drinks": "Drankjes",
    "Units": "Eenheden",
    "Drinks this session": "Drankjes in deze sessie",
    "Add drink": "Drankje toevoegen",

    # --- Editing an already logged drink ---
    "Edit drink": "Drankje bewerken",
    "Save changes": "Wijzigingen bewaren",
    "With this": "Hiermee",
    "Delete": "Verwijderen",
    "tap to edit · swipe to delete": "tik om te bewerken · veeg om te verwijderen",

    # --- Drinking pace ---
    "How fast": "Hoe snel",
    "In one go": "In één keer",
    "Counts as a single swallow — the steepest possible rise.":
        "Telt als één slok – de steilst mogelijke stijging.",
    "A quick drink. The level climbs fast.": "Snel gedronken. Het niveau stijgt snel.",
    "A normal pace.": "Een normaal tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Langzaam gedronken.Veel vlakkere stijging bij dezelfde hoeveelheid alcohol.",

    # --- AddDrinkSheet ---
    "Cancel": "Annuleren",
    "Now": "Nu",
    "Projected peak": "Verwachte piek",
    "Peak at": "Piek om",
    "Clears": "Weer op nul",
    "This would cross your limit": "Hiermee kom je boven je limiet",
    "Around %@, for up to %@.": "Rond %@, gedurende maximaal %@.",
    "This might cross your limit": "Hiermee kom je mogelijk boven je limiet",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Bij een tragere stofwisseling wel, bij een snellere niet. Dat is de onzekerheid van "
        "de schatting.",
    "Type": "Soort",
    "Amount": "Hoeveelheid",
    "Strength": "Sterkte",
    "%@ units": "%@ eenheden",
    "%@ g alcohol": "%@ g alcohol",
    "Stomach": "Maag",
    "When": "Wanneer",
    "Done": "Gereed",
    "Add": "Toevoegen",

    # --- ProfileSheet ---
    "Male": "Man",
    "Female": "Vrouw",
    "Sex": "Geslacht",
    "Weight": "Gewicht",
    "Height": "Lengte",
    "Age": "Leeftijd",
    "kg": "kg",
    "cm": "cm",
    "yrs": "jr",
    "Body": "Lichaam",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Het totale lichaamswater komt uit de Watson-vergelijkingen, die het volume bepalen "
        "waarin alcohol zich verdeelt.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Het totale lichaamswater komt uit de Watson-vergelijkingen, die het volume bepalen "
        "waarin alcohol zich verdeelt. De vergelijking voor vrouwen bevat geen leeftijd, dus "
        "als je die wijzigt, verandert het resultaat niet.",
    "Drinking frequency": "Drinkfrequentie",
    "How often do you drink?": "Hoe vaak drink je?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Zo schatten we je afbraaksnelheid. Regelmatig drinken induceert de CYP2E1-route in de lever, waardoor frequente drinkers alcohol sneller afbreken. Het is het zwakste punt van het model, en daarom kun je onder Weergave en taal instellen hoeveel van die onzekerheid de app je laat zien.",
    "Your limit": "Je limiet",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Je eigen richtgetal, geen wettelijke limiet. De app vertelt je wanneer een gepland "
        "drankje je eroverheen zou brengen, en hoe lang je erboven zou blijven.",
    "Calculated values": "Berekende waarden",
    "Total body water": "Totaal lichaamswater",
    "Distribution volume": "Verdelingsvolume",
    "Widmark factor": "Widmark-factor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "De Widmark-factor ligt doorgaans rond 0,68 bij mannen en 0,55 bij vrouwen. Ligt die "
        "van jou daar ver vandaan, dan is het de moeite waard de waarden hierboven te "
        "controleren.",
    "Elimination rate": "Afbraaksnelheid",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Hoe snel je lever alcohol afbreekt zodra die is opgenomen – de helling van de dalende "
        "kant van de curve.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alcohol verdwijnt met een ongeveer vaste hoeveelheid per uur in plaats van met een "
        "percentage, omdat het enzym dat het afbreekt bij vrijwel elk niveau al op volle "
        "capaciteit draait. Daarom bestaan vuistregels als ‘één drankje per uur’ überhaupt.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Met deze instelling duurt het bij %@ ongeveer %@ voordat je weer op nul bent. Bijna "
        "iedereen zit tussen %@ per uur.",
    "How to find yours": "Zo vind je die van jou",
    "With a breathalyser": "Met een alcoholtester",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Blaas twee keer, met minstens een uur ertussen, op de dalende kant – twee uur of "
        "langer na je laatste drankje, zonder tussendoor iets te drinken. Trek de tweede meting van de "
        "eerste af en deel door het aantal uren ertussen.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Een meting van %@ en twee uur later %@ komt bijvoorbeeld neer op %@ per uur.",
    "Without one": "Zonder alcoholtester",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "De app vertelt je wanneer hij verwacht dat je weer op nul bent. Ben je steevast ruim "
        "daarvoor weer normaal, dan ligt je snelheid hoger dan de instelling – zet hem een "
        "stap omhoog en kijk een paar sessies hoe het gaat. Duurt het langer dan voorspeld, zet hem "
        "dan een stap omlaag.",
    "What moves it": "Wat hem beïnvloedt",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Regelmatig drinken verhoogt hem: het leverenzym dat het werk doet, wordt door gebruik "
        "geïnduceerd. Hij ligt gemiddeld ook iets hoger bij vrouwen, en lager op een lege maag "
        "of bij leverproblemen.",
    "Uncertainty": "Onzekerheid",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Op nul is elk cijfer één getal – de beste schatting van de app. Boven nul worden "
        "dezelfde cijfers als bereiken getoond, en de band op de grafiek wordt navenant "
        "breder.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Met één getal leer je makkelijker: na verloop van tijd weet je hoe jouw eigen 0,6 "
        "voelt. Een bereik is het letterlijkere antwoord, want de snelheid is werkelijk "
        "onzeker. Beide zijn te verdedigen – het is jouw keuze.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "De spreiding die je drinkfrequentie doet vermoeden, is ± %@ per uur.",
    "Rate": "Snelheid",
    "Range": "Bereik",
    "Advanced": "Geavanceerd",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Meerdere personen",
    "History trends": "Trends in geschiedenis",
    "Week": "Week",
    "Month": "Maand",
    "Year": "Jaar",
    "Sober days": "Droge dagen",
    "Change": "Verandering",
    "before records": "vóór de registratie",
    "See further back": "Verder terugkijken",
    "Weeks, months and years side by side — and every evening older than seven days.": "Weken, maanden en jaren naast elkaar – en elke avond ouder dan zeven dagen.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Alles wat je hebt vastgelegd, is al opgeslagen. Ontgrendelen laat het alleen zien.",
    "Coming soon": "Binnenkort",
    "Today": "Vandaag",
    "Day": "Dag",
    "Yesterday": "Gisteren",
    "No drinks on this day": "Geen drankjes op deze dag",
    "Trend": "Trend",
    "day": "dag",
    "Smoothing": "Afvlakking",
    "%@ sessions": "%@ sessies",
    "No data before %@": "Geen gegevens vóór %@",
    "vs.": "t.o.v.",
    "Grams": "Gram",
    "Grams of alcohol": "Gram alcohol",
    "Standard units": "Standaardeenheden",
    "Unit size": "Grootte van een eenheid",
    "Automatic": "Automatisch",
    "UK": "Verenigd Koninkrijk",
    "Nordic countries": "Noordse landen",
    "US standard drink": "Amerikaans standaardglas",
    "WHO, most of Europe": "WHO, het grootste deel van Europa",
    "Period": "Periode",
    "Switch person": "Van persoon wisselen",
    "Add person": "Persoon toevoegen",
    "New person": "Nieuwe persoon",
    "You": "Jij",
    "Name": "Naam",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Alle vier veranderen de curve, dus geen ervan valt voor iemand anders te raden.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Hun eigen limiet en de fijnere instellingen kun je later aanpassen op het tabblad "
        "Profiel, zolang zij de geselecteerde persoon zijn.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Snel toevoegen",
    "Choose a favourite drink": "Kies een favoriet drankje",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Kies het drankje dat je meestal bestelt, dan legt een knop op het Live-scherm het met "
        "één tik vast.",
    "This is your quick-add drink": "Dit is je drankje voor snel toevoegen",
    "Set as my quick-add drink": "Instellen als mijn drankje voor snel toevoegen",
    "This is now your usual": "Dit is nu je vaste drankje",
    "Remove favourite": "Favoriet verwijderen",
    "Always add this one": "Altijd deze toevoegen",
    "Logs it straight away, without opening anything.":
        "Legt het meteen vast, zonder iets te openen.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Eén tik op het Live-scherm legt dit vast, met de verwachte piek op de knop. Hoe vol "
        "je maag is, wordt overgenomen van het vorige drankje en kun je meteen daarna corrigeren.",
    "Peak %@": "Piek %@",
    "%@ added": "%@ toegevoegd",
    "Save": "Bewaren",
    "Undo": "Ongedaan maken",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Back-up",
    "Export a backup": "Back-up exporteren",
    "Import a backup": "Back-up importeren",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Een back-up bevat elke persoon, sessie en elk drankje. Importeren voegt toe wat "
        "ontbreekt – het verandert of verwijdert nooit iets wat er al staat.",
    "Import this backup?": "Deze back-up importeren?",
    "Import": "Importeren",
    "Everything in this backup is already here.": "Alles in deze back-up staat er al.",
    "Import finished": "Importeren voltooid",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Taal",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Opent deze app in Instellingen, waar ‘Voorkeurstaal’ de taal van de app zelf instelt "
        "– die van het systeem blijft zoals hij is. iOS start de app opnieuw wanneer je dit "
        "wijzigt.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Importeren mislukt",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Dit bestand is geen LogMyDrink-back-up, of het is beschadigd.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Deze back-up is gemaakt met een nieuwere versie van LogMyDrink. Werk de app bij en "
        "probeer het opnieuw.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Voegt %@ sessies, %@ drankjes en %@ maandtotalen toe. Er wordt niets veranderd of verwijderd wat er al staat.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': '%@ sessies, %@ drankjes en %@ maandtotalen toegevoegd.',
    'months as totals': 'maanden alleen als totaal',
    'by month only': 'alleen per maand',
    'monthly total': 'maandtotaal',
    'No daily records for this day': 'Geen dagelijkse registraties voor deze dag',
    'Monthly total: %@': 'Maandtotaal: %@',
    'A dry month': 'Een droge maand',

    # --- RemovePersonSection ---
    'Remove %@?': '%@ verwijderen?',
    'Remove': 'Verwijderen',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Wist %@ sessies, %@ drankjes en %@ maandtotalen. Dit kan niet ongedaan worden gemaakt.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Wist %@ sessies en %@ drankjes. Dit kan niet ongedaan worden gemaakt.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Veeg naar links op een gast om hen te verwijderen met alles wat onder hen is geregistreerd. Jij kunt niet worden verwijderd.',
    'People': 'Personen',
    'Owner': 'Eigenaar',
    'Everyone this app records. Switch, add, or remove someone.': 'Iedereen die deze app registreert. Wissel, voeg toe of verwijder iemand.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Overgebleven van de avond ervoor',
    # --- History, second card (5.24) ---
    'Calories': 'Calorieën',
    'Sessions': 'Sessies',
    'Per session': 'Per sessie',
    'Under the influence': 'Onder invloed',
    '%@ of the time': '%@ van de tijd',
    'Days over limit': 'Dagen boven je limiet',
    'Longest sober run': 'Langste droge periode',
    'Favourite drink': 'Favoriet drankje',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Weergave en taal",
    "Data": "Gegevens",
    "Concentration": "Concentratie",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Laat de snelheid over aan de vraag hoe vaak je drinkt, tenzij je een meting hebt om hem mee te vergelijken.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Schatting, geen meting. Gebruik dit nooit om te beslissen of je kunt rijden.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Geschat bereik, geen meting. Gebruik dit nooit om te beslissen of je kunt rijden.',
    'How does the app calculate this?':
        'Hoe berekent de app dit?',
    'approximately %@ %@':
        'ongeveer %@ %@',
    'How it works':
        'Zo werkt het',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Gebruik dit nooit om te beslissen of je kunt rijden. De app schat, hij meet niet, en je werkelijke waarde kan flink afwijken.',
    'Why this app exists':
        'Waarom deze app',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink helpt je bewuster te drinken en de controle te houden. De beslissing valt vóór het volgende glas, dus de app laat je vooraf zien waar een extra drankje je niveau naartoe brengt en wanneer het piekt.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Maar het gaat niet alleen om vanavond. Elk drankje dat je vastlegt, komt in je geschiedenis, zodat je over maanden en jaren ziet hoeveel, hoe vaak en hoe hoog je drinkt. Daaruit komen je patronen naar voren, en ook de richting waarin ze gaan: of het beter of slechter wordt.',
    'How it calculates':
        'Zo rekent de app',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'De schatting is gebaseerd op de methode van Widmark, die sinds de jaren dertig wordt gebruikt om het bloedalcoholgehalte te schatten; de app gebruikt een verfijnde versie ervan.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Uit je gewicht, lengte, leeftijd en geslacht berekent hij hoeveel water je lichaam bevat, want daarin verdeelt alcohol zich. Hij volgt elk drankje apart: hoeveel alcohol erin zat, hoe snel je het dronk en hoeveel je had gegeten, want dat bepaalt hoe snel het wordt opgenomen.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Ondertussen breekt je lever elk uur een ongeveer vaste hoeveelheid af; hoeveel bij jou, wordt geschat uit hoe vaak je drinkt. Het resultaat is een curve, minuut voor minuut: waar je nu bent, waar je naartoe gaat en wanneer je weer op nul staat.',
    'Details':
        'Details',
    'Body water':
        'Lichaamswater',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'De formule van Watson (1980), uit gewicht, lengte, leeftijd en geslacht. De formule voor vrouwen heeft geen leeftijdsterm – een eigenschap van de formule, geen fout. Het verdelingsvolume is het lichaamswater gedeeld door 0,85, het watergehalte van bloed.',
    'Absorption':
        'Opname',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Elk drankje heeft zijn eigen ‘maag’. Op een lege maag wordt de helft van de alcohol in ongeveer 7 minuten opgenomen, op een volle maag in ongeveer 21. Een drankje waar je van nipt, komt gelijkmatig in de maag terwijl je het drinkt.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Geeft een lagere piek en een eerder nulpunt. Verrassend, maar gemeten: met eten breekt de maag een deel van de alcohol af vóór de opname (de app rekent met 5, 10 en 15 procent), en wat nooit binnenkwam, hoeft niet te worden afgebroken.',
    'Elimination':
        'Afbraak',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Ongeveer 0,15 ‰ per uur (gepubliceerd bereik 0,10–0,25), hoger bij regelmatige drinkers doordat leverenzymen zich aanpassen. Dicht bij nul vertraagt de afbraak (Michaelis-Menten-kinetiek), zodat de curve geleidelijk afloopt in plaats van abrupt te stoppen.',
    'Computation':
        'Berekening',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'De curve komt uit een numerieke simulatie met een resolutie van één minuut.',
    'Why it is only an estimate':
        'Waarom het maar een schatting is',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'De app meet niets. Wat hij toont, is de uitkomst van een model met gemiddelde waarden, en de werkelijkheid kan afwijken. De grootste onbekende is hoe snel je alcohol afbreekt: binnen het aannemelijke bereik kan dat alleen al de piek 40 procent en het nulpunt vier uur verschuiven op dezelfde avond.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Ook erfelijkheid, levergezondheid, medicijnen, wat je hebt gegeten, slaap en vermoeidheid spelen mee – de app weet daar niets van. Alleen een geijkte alcoholtester of een bloedtest geeft een exacte waarde.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Het getal is toch nuttig. Zit de app bij jou steeds wat te hoog of te laag, dan zit hij er elke avond in dezelfde richting naast, zodat je na verloop van tijd leert wat een bepaalde waarde voor jou betekent. In Profiel kun je ook de onzekerheid van de afbraaksnelheid tonen: je ziet dan een bereik in plaats van één getal.',
    'Tips':
        'Tips',
    'Favourite drink in one tap':
        'Favoriet drankje met één tik',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Stel in Profiel een favoriet in, en de knop op Live legt hem met één tik vast.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Zet hem op je toegangsscherm of beginscherm: één tik legt je favoriet vast. Zolang er alcohol in je lichaam is, toont hij ook je niveau en welke kant het op gaat.',
    'How do I add it?':
        'Hoe voeg ik hem toe?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Zeg ‘Hey Siri, LogMyDrink now’ en Siri legt je favoriet vast en vertelt waar je piek naartoe gaat. (Het commando werkt in het Engels.)',
    'Looking back':
        'Terugkijken',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '‘Gisteren’ bovenaan Live brengt je met één tik naar de vorige dag; het tabblad Geschiedenis toont je patronen over weken, maanden en jaren.',
    'Logging later':
        'Achteraf vastleggen',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Leg je een drankje achteraf vast, zet de tijd dan terug met de knoppen − en +; een vergeten dag kun je aanvullen vanuit de weergave Dag in Geschiedenis.',
    'One tap and done':
        'Eén tik en klaar',
    'Your favourite from the Lock Screen':
        'Je favoriet vanaf het toegangsscherm',
    'Say it, don’t type it':
        'Zeg het, typ het niet',
    'See your patterns':
        'Bekijk je patronen',
    'Set what you drink most often and log it with a single tap.':
        'Stel in wat je het vaakst drinkt en leg het met één tik vast.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Eén tik op de widget legt je favoriet vast, zonder dat je de app hoeft te zoeken. ’s Avonds toont hij ook je niveau.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '‘Hey Siri, LogMyDrink now’ – Siri legt je favoriet vast en vertelt waar je piek naartoe gaat.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Geschiedenis laat zien hoeveel en hoe hoog je drinkt over weken, maanden en jaren, en welke kant het op gaat.',
    'Set favourite':
        'Favoriet instellen',
    'Add widget':
        'Widget toevoegen',
    'Got it':
        'Begrepen',
    'Open History':
        'Geschiedenis openen',
    'Don’t show again':
        'Niet meer tonen',
    'Lock Screen':
        'Toegangsscherm',
    'Home Screen':
        'Beginscherm',
    'Where':
        'Waar',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Vergrendel je iPhone en houd dan je vinger op het toegangsscherm.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Tik op ‘Pas aan’, dan op ‘Toegangsscherm’ en vervolgens op de widgetrij onder de klok.',
    'Choose LogMyDrink, then tap Done.':
        'Kies LogMyDrink en tik op ‘Gereed’.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Houd je vinger op een lege plek van het beginscherm totdat de apps gaan bewegen.',
    'Tap Edit, then Add Widget.':
        'Tik op ‘Wijzig’ en dan op ‘Voeg widget toe’.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Zoek LogMyDrink, kies een formaat en tik op ‘Voeg widget toe’.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Een tik op de widget opent de app en legt je favoriete drankje vast. Zolang er alcohol in je lichaam is, toont hij ook je niveau en welke kant het op gaat.',
    'Add the widget':
        'Widget toevoegen',
    'Show tips':
        'Tips tonen',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Hooguit één tip per dag, bij het openen van de app – nooit zolang er alcohol in je lichaam is.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Wat het getal laat zien',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Het getal is een schatting van je bloedalcoholgehalte (in het Engels BAC, blood alcohol concentration): hoeveel alcohol er in je bloed zit.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'In promille (‰) is het gram alcohol per liter bloed: 0,5 ‰ betekent een halve gram in elke liter. In procent is het gram per 100 milliliter, dus hetzelfde niveau geeft een tien keer kleiner getal: 0,5 ‰ is 0,05 procent. Je wisselt tussen de twee via Profiel › Weergave en taal.',
    'The curve shows the same level over time, minute by minute.':
        'De curve toont hetzelfde niveau in de tijd, minuut voor minuut.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promille (‰) is gram alcohol per liter bloed, procent is gram per 100 milliliter: 0,5 ‰ is 0,05 procent.',
}
