"""
Danish.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promille",
    "Percent": "Procent",

    # --- DrinkCatalog: drink types ---
    "Beer": "Øl",
    "Wine": "Vin",
    "Champagne": "Mousserende",
    "Shot": "Shot",
    "Cocktail": "Cocktail",
    "Custom": "Egen",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Tom mave",
    "Moderately full": "Delvist fyldt",
    "Full stomach": "Fuld mave",
    "Empty": "Tom",
    "Moderate": "Middel",
    "Full": "Fuld",
    "Fast absorption, higher and earlier peak.": "Hurtig optagelse, højere og tidligere top.",
    "Moderate absorption.": "Moderat optagelse.",
    "Slow absorption, lower and later peak.": "Langsom optagelse, lavere og senere top.",

    # --- DrinkingFrequency ---
    "Rarely": "Sjældent",
    "A few times a month": "Et par gange om måneden",
    "Several times a week": "Flere gange om ugen",
    "Almost daily": "Næsten dagligt",
    "A few occasions a year": "Et par gange om året",
    "Social drinking": "Ved sociale lejligheder",
    "Weekly routine": "Ugentlig rutine",
    "Daily or nearly daily": "Dagligt eller næsten dagligt",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Tidspunkt",
    "Level": "Niveau",
    "Lower": "Nedre",
    "Upper": "Øvre",
    "Lower estimate": "Nedre skøn",
    "Upper estimate": "Øvre skøn",
    "Personal limit": "Personlig grænse",
    "Drink": "Drink",

    # --- BACChartView ---
    "Expected peak around %@": "Forventet top omkring %@",
    "Peaked around %@": "Toppede omkring %@",
    "No active session": "Ingen aktiv session",
    "Still rising": "Stiger stadig",
    "YOUR LIMIT %@": "DIN GRÆNSE %@",
    "possible range": "muligt interval",

    # --- Live screen: the day with nothing on it ---
    "Live": "Live",
    "Nothing logged today": "Intet registreret i dag",
    "Add a drink when you have one.": "Tilføj en drink, når du får en.",

    # --- Tabs and history ---
    "History": "Historik",
    "No past sessions yet": "Ingen tidligere sessioner endnu",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "En session vises her, når den er slut — når dit niveau er nede på nul, og der er gået "
        "et par timer.",
    "%@ drinks": "%@ drinks",
    "peak": "top",
    "Started": "Startede",
    "Lasted": "Varede",
    "Duration": "Varighed",
    "Sober around": "Ædru ca.",
    "Sober at": "Ædru",
    "Remaining": "Tilbage",
    "next day": "næste dag",
    "previous day": "dagen før",
    "%@ days later": "%@ dage senere",
    "%@ days earlier": "%@ dage tidligere",
    "Calculated with your profile at the time": "Beregnet med din profil på det tidspunkt",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Drinks",
    "Units": "Genstande",
    "Drinks this session": "Drinks i denne session",
    "Add drink": "Tilføj drink",

    # --- Editing an already logged drink ---
    "Edit drink": "Rediger drink",
    "Save changes": "Gem ændringer",
    "With this": "Med denne",
    "Delete": "Slet",
    "tap to edit · swipe to delete": "tryk for at redigere · stryg for at slette",

    # --- Drinking pace ---
    "How fast": "Hvor hurtigt",
    "In one go": "På én gang",
    "Counts as a single swallow — the steepest possible rise.":
        "Tæller som en enkelt slurk — den stejlest mulige stigning.",
    "A quick drink. The level climbs fast.": "En hurtig drink. Niveauet stiger hurtigt.",
    "A normal pace.": "Et normalt tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Drukket langsomt. Meget blidere stigning for den samme mængde alkohol.",

    # --- AddDrinkSheet ---
    "Cancel": "Annuller",
    "Now": "Nu",
    "Projected peak": "Forventet top",
    "Peak at": "Top kl.",
    "Clears": "Alkoholfri",
    "This would cross your limit": "Dette vil overskride din grænse",
    "Around %@, for up to %@.": "Omkring %@, i op til %@.",
    "This might cross your limit": "Dette kan overskride din grænse",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Med en langsommere forbrænding ja, med en hurtigere nej. Det er skønnets usikkerhed.",
    "Type": "Type",
    "Amount": "Mængde",
    "Strength": "Styrke",
    "%@ units": "%@ genstande",
    "%@ g alcohol": "%@ g alkohol",
    "Stomach": "Mave",
    "When": "Hvornår",
    "Done": "Færdig",
    "Add": "Tilføj",

    # --- ProfileSheet ---
    "Male": "Mand",
    "Female": "Kvinde",
    "Sex": "Køn",
    "Weight": "Vægt",
    "Height": "Højde",
    "Age": "Alder",
    "kg": "kg",
    "cm": "cm",
    "yrs": "år",
    "Body": "Krop",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Samlet kropsvand kommer fra Watson-ligningerne, som fastsætter det volumen, alkohol "
        "fordeler sig i.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Samlet kropsvand kommer fra Watson-ligningerne, som fastsætter det volumen, alkohol "
        "fordeler sig i. Ligningen for kvinder medregner ikke alder, så en ændring af den "
        "påvirker ikke resultatet.",
    "Drinking frequency": "Drikkefrekvens",
    "How often do you drink?": "Hvor ofte drikker du?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Sådan skønner vi din forbrændingshastighed. Regelmæssig indtagelse inducerer leverens CYP2E1-vej, så hyppige drikkere nedbryder alkohol hurtigere. Det er modellens svageste punkt, og derfor kan du under Visning og sprog bestemme, hvor meget af den usikkerhed appen viser dig.",
    "Your limit": "Din grænse",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Dit eget referencetal, ikke en lovbestemt grænse. Appen fortæller dig, hvornår en "
        "planlagt drink vil føre dig over den, og hvor længe du vil ligge over.",
    "Calculated values": "Beregnede værdier",
    "Total body water": "Samlet kropsvand",
    "Distribution volume": "Fordelingsvolumen",
    "Widmark factor": "Widmark-faktor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmark-faktoren ligger typisk omkring 0,68 for mænd og 0,55 for kvinder. Hvis din "
        "ligger langt fra det, er det værd at tjekke værdierne ovenfor.",
    "Elimination rate": "Forbrændingshastighed",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Hvor hurtigt din lever nedbryder alkohol, når den først er optaget — hældningen på "
        "kurvens faldende side.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol forsvinder med en nogenlunde fast mængde i timen frem for med en procentdel, "
        "fordi det enzym, der nedbryder den, allerede kører for fuld kraft ved næsten alle "
        "niveauer. Det er derfor, tommelfingerregler som »én genstand i timen« overhovedet "
        "findes.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Ved denne indstilling tager %@ omkring %@ at nedbryde. Næsten alle ligger mellem %@ i "
        "timen.",
    "How to find yours": "Sådan finder du din",
    "With a breathalyser": "Med et alkometer",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Pust to gange med mindst en times mellemrum på den faldende side — to timer eller "
        "mere efter din sidste drink, uden noget ind imellem. Træk den anden måling fra den "
        "første, og divider med antallet af timer imellem dem.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "For eksempel giver %@ og %@ to timer senere %@ i timen.",
    "Without one": "Uden den",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Appen fortæller dig, hvornår den forventer, at du er alkoholfri. Hvis du konsekvent "
        "er tilbage til normal et godt stykke før det, er din hastighed højere end "
        "indstillingen — skru den et trin op, og hold øje i et par sessioner. Tager det "
        "længere end forudsagt, så skru den ned.",
    "What moves it": "Hvad påvirker den",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Regelmæssig indtagelse hæver den: det leverenzym, der udfører arbejdet, induceres af "
        "brug. Den er også en anelse højere hos kvinder i gennemsnit og lavere på tom mave "
        "eller ved leverproblemer.",
    "Uncertainty": "Usikkerhed",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Ved nul er hvert tal et enkelt tal — appens bedste skøn. Over nul vises de samme tal "
        "som intervaller, og båndet på grafen bliver tilsvarende bredere.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Et enkelt tal er nemmere at lære af: med tiden finder du ud af, hvordan din egen 0,6 "
        "føles. Et interval er det mere bogstavelige svar, for hastigheden er reelt usikker. "
        "Begge dele kan forsvares — det er dit valg.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Spredningen, som din drikkefrekvens peger på, er ± %@ i timen.",
    "Rate": "Hastighed",
    "Range": "Interval",
    "Advanced": "Avanceret",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Flere personer",
    "History trends": "Tendenser i historikken",
    "Week": "Uge",
    "Month": "Måned",
    "Year": "År",
    "Sober days": "Dage uden alkohol",
    "Change": "Ændring",
    "before records": "før registreringen begyndte",
    "See further back": "Se længere tilbage",
    "Weeks, months and years side by side — and every evening older than seven days.": "Uger, måneder og år side om side – og hver aften ældre end syv dage.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Alt, du har registreret, er allerede gemt. At låse op viser det blot.",
    "Coming soon": "Kommer snart",
    "Today": "I dag",
    "Day": "Dag",
    "Yesterday": "I går",
    "No drinks on this day": "Ingen drinks denne dag",
    "Trend": "Tendens",
    "day": "dag",
    "Smoothing": "Udjævning",
    "%@ sessions": "%@ lejligheder",
    "No data before %@": "Ingen data før %@",
    "vs.": "ift.",
    "Grams": "Gram",
    "Grams of alcohol": "Gram alkohol",
    "Standard units": "Standardenheder",
    "Unit size": "Enhedsstørrelse",
    "Automatic": "Automatisk",
    "UK": "Storbritannien",
    "Nordic countries": "Nordiske lande",
    "US standard drink": "Amerikansk standarddrink",
    "WHO, most of Europe": "WHO, det meste af Europa",
    "Period": "Periode",
    "Switch person": "Skift person",
    "Add person": "Tilføj person",
    "New person": "Ny person",
    "You": "Dig",
    "Name": "Navn",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Alle fire ændrer kurven, så ingen af dem kan gættes for en anden person.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Deres egen grænse og de finere indstillinger kan ændres senere under fanen Profil, "
        "mens de er den valgte person.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Hurtigvalg",
    "Choose a favourite drink": "Vælg en yndlingsdrink",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Vælg den drink, du plejer at bestille, så registrerer en knap på Live-skærmen den med "
        "ét tryk.",
    "This is your quick-add drink": "Dette er din hurtigvalg-drink",
    "Set as my quick-add drink": "Vælg som min hurtigvalg-drink",
    "This is now your usual": "Dette er nu din faste drink",
    "Remove favourite": "Fjern yndlingsdrink",
    "Always add this one": "Tilføj altid denne",
    "Logs it straight away, without opening anything.":
        "Registrerer den med det samme, uden at åbne noget.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Ét tryk på Live-skærmen registrerer den, med den forventede top på knappen. Hvor fuld "
        "din mave er, kommer fra den foregående drink og kan rettes lige efter.",
    "Peak %@": "Top %@",
    "%@ added": "%@ tilføjet",
    "Save": "Gem",
    "Undo": "Fortryd",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Sikkerhedskopi",
    "Export a backup": "Eksporter en sikkerhedskopi",
    "Import a backup": "Importer en sikkerhedskopi",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "En sikkerhedskopi indeholder alle personer, sessioner og drinks. Import tilføjer det, "
        "der mangler — den ændrer eller fjerner aldrig noget, der allerede er her.",
    "Import this backup?": "Vil du importere denne sikkerhedskopi?",
    "Import": "Importer",
    "Everything in this backup is already here.":
        "Alt i denne sikkerhedskopi findes allerede her.",
    "Import finished": "Import afsluttet",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Sprog",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Åbner denne app i Indstillinger, hvor »Foretrukket sprog« bestemmer appens eget sprog "
        "— systemets forbliver, som det er. iOS genstarter appen, når du ændrer det.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Kunne ikke importere",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Denne fil er ikke en LogMyDrink-sikkerhedskopi, eller den er beskadiget.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Denne sikkerhedskopi er lavet af en nyere version af LogMyDrink. Opdater appen, og "
        "prøv igen.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Tilføjer %@ sessioner, %@ drinks og %@ månedstotaler. Intet af det, der allerede er her, ændres eller fjernes.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Tilføjede %@ sessioner, %@ drinks og %@ månedstotaler.',
    'months as totals': 'måneder kun som totaler',
    'by month only': 'kun pr. måned',
    'monthly total': 'månedstotal',
    'No daily records for this day': 'Ingen daglige optegnelser for denne dag',
    'Monthly total: %@': 'Månedstotal: %@',
    'A dry month': 'En tør måned',

    # --- RemovePersonSection ---
    'Remove %@?': 'Fjern %@?',
    'Remove': 'Fjern',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Sletter %@ sessioner, %@ drinks og %@ månedstotaler. Dette kan ikke fortrydes.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Sletter %@ sessioner og %@ drinks. Dette kan ikke fortrydes.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Stryg til venstre på en gæst for at fjerne dem med alt, der er registreret under dem. Du kan ikke fjernes.',
    'People': 'Personer',
    'Owner': 'Ejer',
    'Everyone this app records. Switch, add, or remove someone.': 'Alle, som denne app registrerer. Skift, tilføj eller fjern nogen.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Overført fra aftenen før',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorier',
    'Sessions': 'Anledninger',
    'Per session': 'Pr. anledning',
    'Under the influence': 'Påvirket',
    '%@ of the time': '%@ af tiden',
    'Days over limit': 'Dage over grænsen',
    'Longest sober run': 'Længste ædru periode',
    'Favourite drink': 'Yndlingsdrik',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Visning og sprog",
    "Data": "Data",
    "Concentration": "Koncentration",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Lad hastigheden følge spørgsmålet om hyppighed, medmindre du har en måling at holde den op imod.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Skøn, ikke måling. Brug aldrig dette til at afgøre, om du kan køre.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Skønnet interval, ikke måling. Brug aldrig dette til at afgøre, om du kan køre.',
    'How does the app calculate this?':
        'Hvordan regner appen?',
    'approximately %@ %@':
        'cirka %@ %@',
    'How it works':
        'Sådan virker det',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Brug aldrig dette til at afgøre, om du kan køre. Appen skønner, den måler ikke, og dit faktiske niveau kan afvige betydeligt.',
    'Why this app exists':
        'Derfor findes appen',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink hjælper dig med at drikke mere bevidst og bevare kontrollen. Beslutningen træffes før næste glas, så appen viser dig på forhånd, hvor endnu en drink ville bringe dit niveau hen, og hvornår det ville toppe.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Men det handler ikke kun om i aften. Hver drink, du registrerer, havner i din historik, så over måneder og år kan du se, hvor meget, hvor ofte og hvor højt du drikker. Dine mønstre træder frem, og det samme gør retningen, de bevæger sig i – om det går bedre eller værre.',
    'How it calculates':
        'Sådan regner den',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Skønnet bygger på Widmarks metode, som er brugt til at skønne alkoholpromillen siden 1930’erne; appen bruger en forfinet udgave af den.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Ud fra din vægt, højde, alder og køn regner den ud, hvor meget vand din krop indeholder, for det er her, alkoholen fordeler sig. Den følger hver drink for sig: hvor meget alkohol den indeholdt, hvor hurtigt du drak den, og hvor meget du havde spist, for det afgør, hvor hurtigt den optages.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Imens nedbryder leveren en nogenlunde konstant mængde hver time; hvor meget hos dig, skønnes ud fra, hvor ofte du drikker. Resultatet er en kurve, minut for minut: hvor du er nu, hvor du er på vej hen, og hvornår du er nede på nul.',
    'Details':
        'Detaljer',
    'Body water':
        'Kropsvæske',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsons formel (1980) ud fra vægt, højde, alder og køn. Formlen for kvinder har ikke alder med – en egenskab ved formlen, ikke en fejl. Fordelingsvolumenet er kropsvæsken divideret med 0,85, blodets vandindhold.',
    'Absorption':
        'Optagelse',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Hver drink har sin egen ”mave”. På tom mave optages halvdelen af alkoholen på cirka 7 minutter, på fuld mave på cirka 21. En drink, du nipper til, når jævnt ned i maven, mens du drikker den.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Giver en lavere top og et tidligere nulpunkt. Overraskende, men målt: med mad nedbryder maven en del af alkoholen, før den optages (appen regner med 5, 10 og 15 procent), og det, der aldrig kom ind, skal ikke nedbrydes.',
    'Elimination':
        'Nedbrydning',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Cirka 0,15 ‰ i timen (publiceret interval 0,10–0,25), højere hos dem, der drikker regelmæssigt, fordi leverens enzymer tilpasser sig. Tæt på nul går det langsommere (Michaelis-Menten-kinetik), så kurven flader ud i stedet for at stoppe brat.',
    'Computation':
        'Beregning',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Kurven kommer fra en numerisk simulering med et minuts opløsning.',
    'Why it is only an estimate':
        'Derfor er det kun et skøn',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Appen måler ingenting. Det, den viser, er resultatet af en model med gennemsnitsværdier, og virkeligheden kan afvige. Den største ubekendte er, hvor hurtigt du nedbryder alkohol: inden for det plausible interval kan det alene flytte toppen 40 procent og nulpunktet fire timer samme aften.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Gener, leverens tilstand, medicin, hvad du har spist, søvn og træthed spiller også ind – intet af det kender appen. Kun et godkendt alkometer eller en blodprøve giver en nøjagtig værdi.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Tallet er alligevel nyttigt. Hvis appen hos dig konsekvent viser lidt for højt eller lavt, tager den fejl i samme retning hver aften, så med tiden lærer du, hvad en given værdi betyder for dig. Under Profil kan du også vise usikkerheden på nedbrydningshastigheden: så ser du et interval i stedet for ét tal.',
    'Tips':
        'Tips',
    'Favourite drink in one tap':
        'Favoritdrink med ét tryk',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Vælg en favorit under Profil, så registrerer knappen på Live den med ét tryk.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Føj den til låseskærmen eller hjemmeskærmen: ét tryk registrerer din favorit. Så længe der er alkohol i kroppen, viser den også dit niveau og retningen.',
    'How do I add it?':
        'Hvordan tilføjer jeg den?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Sig ”Hey Siri, LogMyDrink now”, så registrerer Siri din favorit og fortæller, hvor din top er på vej hen.',
    'Looking back':
        'Se tilbage',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '”I går” øverst på Live fører dig til dagen før med ét tryk; fanen Historik viser dine mønstre over uger, måneder og år.',
    'Logging later':
        'Registrér bagefter',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Hvis du registrerer en drink bagefter, så stil tiden tilbage med knapperne − og +; en glemt dag kan udfyldes fra dagsvisningen i Historik.',
    'One tap and done':
        'Ét tryk, så er det klaret',
    'Your favourite from the Lock Screen':
        'Din favorit fra låseskærmen',
    'Say it, don’t type it':
        'Sig det, skriv det ikke',
    'See your patterns':
        'Se dine mønstre',
    'Set what you drink most often and log it with a single tap.':
        'Angiv, hvad du oftest drikker, og registrér det med ét tryk.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Ét tryk på widgetten registrerer din favorit, uden at du skal lede efter appen. Om aftenen viser den også dit niveau.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '”Hey Siri, LogMyDrink now” – Siri registrerer din favorit og fortæller, hvor din top er på vej hen.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Historik viser, hvor meget og hvor højt du drikker over uger, måneder og år, og hvilken vej det går.',
    'Set favourite':
        'Vælg favorit',
    'Add widget':
        'Tilføj widget',
    'Got it':
        'Forstået',
    'Open History':
        'Åbn Historik',
    'Later':
        'Senere',
    'Don’t show again':
        'Vis ikke igen',
    'Lock Screen':
        'Låseskærm',
    'Home Screen':
        'Hjemmeskærm',
    'Where':
        'Hvor',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Lås din iPhone, og hold derefter fingeren på låseskærmen.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Tryk på Tilpas, derefter på Låseskærm og så på widgetrækken under uret.',
    'Choose LogMyDrink, then tap Done.':
        'Vælg LogMyDrink, og tryk på OK.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Hold fingeren på et tomt område af hjemmeskærmen, til symbolerne begynder at vrikke.',
    'Tap Edit, then Add Widget.':
        'Tryk på Rediger og derefter på Tilføj widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Søg efter LogMyDrink, vælg en størrelse, og tryk på Tilføj widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Et tryk på widgetten åbner appen og registrerer din favoritdrink. Så længe der er alkohol i kroppen, viser den også dit niveau og retningen.',
    'Add the widget':
        'Tilføj widgetten',
    'Show tips':
        'Vis tips',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Højst ét tip om dagen, når du åbner appen – aldrig så længe der er alkohol i kroppen.',
}
