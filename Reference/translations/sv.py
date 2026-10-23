"""
Swedish.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promille",
    "Percent": "Procent",

    # --- DrinkCatalog: drink types ---
    "Beer": "Öl",
    "Wine": "Vin",
    "Champagne": "Mousserande",
    "Shot": "Shot",
    "Cocktail": "Cocktail",
    "Custom": "Egen",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Tom mage",
    "Moderately full": "Måttligt fylld mage",
    "Full stomach": "Full mage",
    "Empty": "Tom",
    "Moderate": "Måttlig",
    "Full": "Full",
    "Fast absorption, higher and earlier peak.": "Snabbt upptag, högre och tidigare topp.",
    "Moderate absorption.": "Måttligt upptag.",
    "Slow absorption, lower and later peak.": "Långsamt upptag, lägre och senare topp.",

    # --- DrinkingFrequency ---
    "Rarely": "Sällan",
    "A few times a month": "Några gånger i månaden",
    "Several times a week": "Flera gånger i veckan",
    "Almost daily": "Nästan varje dag",
    "A few occasions a year": "Några tillfällen om året",
    "Social drinking": "Sällskapsdrickande",
    "Weekly routine": "Veckorutin",
    "Daily or nearly daily": "Dagligen eller nästan dagligen",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Tid",
    "Level": "Nivå",
    "Lower": "Nedre",
    "Upper": "Övre",
    "Lower estimate": "Nedre uppskattning",
    "Upper estimate": "Övre uppskattning",
    "Personal limit": "Personlig gräns",
    "Drink": "Dryck",

    # --- BACChartView ---
    "Expected peak around %@": "Förväntad topp omkring %@",
    "Peaked around %@": "Toppade omkring %@",
    "No active session": "Inget pågående tillfälle",
    "Still rising": "Stiger fortfarande",
    "YOUR LIMIT %@": "DIN GRÄNS %@",
    "possible range": "möjligt intervall",

    # --- Live screen: the day with nothing on it ---
    "Live": "Live",
    "Nothing logged today": "Inget loggat i dag",
    "Add a drink when you have one.": "Lägg till en dryck när du tar en.",

    # --- Tabs and history ---
    "History": "Historik",
    "No past sessions yet": "Inga tidigare tillfällen än",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Ett tillfälle dyker upp här när det har avslutats – när din nivå har nått noll och "
        "några timmar har gått.",
    "%@ drinks": "%@ drycker",
    "peak": "topp",
    "Started": "Startade",
    "Lasted": "Varade",
    "Duration": "Varaktighet",
    "Sober around": "Nykter ca",
    "Sober at": "Nykter",
    "Remaining": "Kvar",
    "next day": "nästa dag",
    "previous day": "dagen före",
    "%@ days later": "%@ dagar senare",
    "%@ days earlier": "%@ dagar tidigare",
    "Calculated with your profile at the time": "Beräknat med din profil vid det tillfället",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Drycker",
    "Units": "Enheter",
    "Drinks this session": "Drycker under tillfället",
    "Add drink": "Lägg till dryck",

    # --- Editing an already logged drink ---
    "Edit drink": "Redigera dryck",
    "Save changes": "Spara ändringar",
    "With this": "Med den här",
    "Delete": "Ta bort",
    "tap to edit · swipe to delete": "tryck för att redigera · svep för att ta bort",

    # --- Drinking pace ---
    "How fast": "Hur snabbt",
    "In one go": "I ett svep",
    "Counts as a single swallow — the steepest possible rise.":
        "Räknas som en enda klunk – den brantaste möjliga stigningen.",
    "A quick drink. The level climbs fast.": "En snabb dryck. Nivån stiger snabbt.",
    "A normal pace.": "Ett normalt tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Drucken långsamt. Mycket mjukare stigning för samma mängd alkohol.",

    # --- AddDrinkSheet ---
    "Cancel": "Avbryt",
    "Now": "Nu",
    "Projected peak": "Beräknad topp",
    "Peak at": "Topp kl.",
    "Clears": "Når noll",
    "This would cross your limit": "Det här skulle överskrida din gräns",
    "Around %@, for up to %@.": "Omkring %@, i upp till %@.",
    "This might cross your limit": "Det här kan överskrida din gräns",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Med långsammare ämnesomsättning ja, med snabbare nej. Det är osäkerheten i "
        "uppskattningen.",
    "Type": "Typ",
    "Amount": "Mängd",
    "Strength": "Styrka",
    "%@ units": "%@ enheter",
    "%@ g alcohol": "%@ g alkohol",
    "Stomach": "Mage",
    "When": "När",
    "Done": "Klar",
    "Add": "Lägg till",

    # --- ProfileSheet ---
    "Male": "Man",
    "Female": "Kvinna",
    "Sex": "Kön",
    "Weight": "Vikt",
    "Height": "Längd",
    "Age": "Ålder",
    "kg": "kg",
    "cm": "cm",
    "yrs": "år",
    "Body": "Kropp",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Totalt kroppsvatten kommer från Watson-ekvationerna, som anger volymen som alkoholen "
        "fördelar sig i.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Totalt kroppsvatten kommer från Watson-ekvationerna, som anger volymen som alkoholen "
        "fördelar sig i. Ekvationen för kvinnor innehåller inte ålder, så det påverkar "
        "inte resultatet om du ändrar den.",
    "Drinking frequency": "Dryckesfrekvens",
    "How often do you drink?": "Hur ofta dricker du?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Så här uppskattar vi din förbränningshastighet. Regelbundet drickande inducerar leverns CYP2E1-väg, så den som dricker ofta bryter ner alkohol snabbare. Det är modellens svagaste punkt, och därför kan du under Visning och språk ställa in hur mycket av den osäkerheten appen visar dig.",
    "Your limit": "Din gräns",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Ditt eget referensvärde, inte en lagstadgad gräns. Appen säger till om en planerad "
        "dryck skulle ta dig över den, och hur länge du skulle ligga över.",
    "Calculated values": "Beräknade värden",
    "Total body water": "Totalt kroppsvatten",
    "Distribution volume": "Distributionsvolym",
    "Widmark factor": "Widmarkfaktor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmarkfaktorn ligger vanligtvis runt 0,68 för män och 0,55 för kvinnor. Om din "
        "ligger långt ifrån det är det värt att kontrollera värdena ovan.",
    "Elimination rate": "Förbränningshastighet",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Hur snabbt levern bryter ner alkohol när den väl har tagits upp – lutningen på "
        "kurvans fallande sida.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol lämnar kroppen med en ungefär fast mängd per timme snarare än med en andel, "
        "eftersom enzymet som bryter ner den redan går för full kapacitet vid nästan varje "
        "nivå. Det är därför tumregler som ”en dryck i timmen” finns över huvud taget.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Med den här inställningen tar %@ ungefär %@ att brytas ned. Nästan alla ligger mellan %@ "
        "per timme.",
    "How to find yours": "Så hittar du din",
    "With a breathalyser": "Med en alkometer",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Blås två gånger, med minst en timme emellan, på den fallande sidan – två timmar eller "
        "mer efter din sista dryck, utan att dricka något däremellan. Dra det andra värdet från det "
        "första och dela med antalet timmar mellan dem.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Till exempel ger %@ och %@ två timmar senare %@ per timme.",
    "Without one": "Utan alkometer",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Appen talar om när den räknar med att du är nere på noll. Om du gång på gång är "
        "tillbaka i normalt skick en bra stund innan dess är din hastighet högre än "
        "inställningen – höj den ett steg och se hur det blir under några tillfällen. Om det "
        "tar längre tid än beräknat, sänk den ett steg.",
    "What moves it": "Vad som påverkar den",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Regelbundet drickande höjer den: leverenzymet som gör jobbet induceras av användning. "
        "Den är i genomsnitt också något högre hos kvinnor, och lägre på tom mage eller vid "
        "leverproblem.",
    "Uncertainty": "Osäkerhet",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Vid noll är varje siffra ett enda tal – appens bästa uppskattning. Över noll visas "
        "samma siffror som intervall, och bandet i diagrammet breddas på motsvarande sätt.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Ett enda tal är lättare att lära sig av: med tiden får du reda på hur din egen 0,6 "
        "känns. Ett intervall är det mer bokstavliga svaret, eftersom hastigheten verkligen är "
        "osäker. Båda går att försvara – det här är ditt val.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Spridningen som din dryckesfrekvens antyder är ± %@ per timme.",
    "Rate": "Hastighet",
    "Range": "Intervall",
    "Advanced": "Avancerat",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Week": "Vecka",
    "Month": "Månad",
    "Year": "År",
    "Sober days": "Dagar utan alkohol",
    "Change": "Förändring",
    "before records": "före registreringen började",
    "See further back": "Se längre tillbaka",
    "Weeks, months and years side by side — and every evening older than seven days.": "Veckor, månader och år sida vid sida – och varje kväll äldre än sju dagar.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Allt du har loggat är redan sparat. Upplåsningen gör bara att det visas.",
    "Coming soon": "Kommer snart",
    "Back up and restore": "Säkerhetskopiera och återställ",
    "Log for friends too": "Logga för vänner också",
    "Switch to someone else in one tap and log their drinks with their own body and limit — each person gets their own curve and history.": "Byt till någon annan med ett tryck och logga deras drycker med deras egen kropp och gräns – varje person får sin egen kurva och historik.",
    "Save everything to a file, and read a backup back in — on this phone or on a new one.": "Spara allt i en fil och läs in en säkerhetskopia igen – på den här telefonen eller på en ny.",
    "Backup and restore are part of Pro.": "Säkerhetskopiering och återställning ingår i Pro.",
    "Today": "Idag",
    "Day": "Dag",
    "Yesterday": "Igår",
    "No drinks on this day": "Inga drycker den här dagen",
    "Trend": "Trend",
    "day": "dag",
    "Smoothing": "Utjämning",
    "%@ sessions": "%@ tillfällen",
    "No data before %@": "Inga data före %@",
    "vs.": "jfr",
    "Grams": "Gram",
    "Grams of alcohol": "Gram alkohol",
    "Standard units": "Standardenheter",
    "Unit size": "Enhetsstorlek",
    "Automatic": "Automatisk",
    "UK": "Storbritannien",
    "Nordic countries": "Nordiska länder",
    "US standard drink": "Amerikanskt standardglas",
    "WHO, most of Europe": "WHO, större delen av Europa",
    "Period": "Period",
    "Switch person": "Byt person",
    "Add person": "Lägg till person",
    "New person": "Ny person",
    "You": "Du",
    "Name": "Namn",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Alla fyra påverkar kurvan, så ingen av dem går att gissa åt någon annan.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Personens egen gräns och de finare inställningarna kan ändras senare under fliken "
        "Profil, medan personen är vald.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Snabbval",
    "Choose a favourite drink": "Välj en favoritdryck",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Välj drycken du brukar beställa, så loggar en knapp på Live-skärmen den med ett "
        "tryck.",
    "This is your quick-add drink": "Det här är ditt snabbval",
    "Set as my quick-add drink": "Använd som mitt snabbval",
    "This is now your usual": "Det här är nu din vanliga dryck",
    "Remove favourite": "Ta bort favorit",
    "Always add this one": "Lägg alltid till den här",
    "Logs it straight away, without opening anything.":
        "Loggar den direkt, utan att öppna något.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Ett tryck på Live-skärmen loggar den här, med den beräknade toppen på knappen. Hur "
        "full din mage är hämtas från drycken före, och kan rättas direkt efteråt.",
    "Peak %@": "Topp %@",
    "%@ added": "%@ har lagts till",
    "Save": "Spara",
    "Undo": "Ångra",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Säkerhetskopia",
    "Export a backup": "Exportera en säkerhetskopia",
    "Import a backup": "Importera en säkerhetskopia",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "En säkerhetskopia innehåller alla personer, tillfällen och drycker. En import lägger "
        "till det som saknas – den ändrar eller tar aldrig bort något som redan finns här.",
    "Import this backup?": "Importera den här säkerhetskopian?",
    "Import": "Importera",
    "Everything in this backup is already here.":
        "Allt i den här säkerhetskopian finns redan här.",
    "Import finished": "Importen klar",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Språk",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Öppnar den här appen i Inställningar, där ”Föredraget språk” ställer in appens eget "
        "språk – systemets förblir som det är. iOS startar om appen när du ändrar det.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Kunde inte importera",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Den här filen är ingen säkerhetskopia från LogMyDrink, eller så är den skadad.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Den här säkerhetskopian skapades av en nyare version av LogMyDrink. Uppdatera appen "
        "och försök igen.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Lägger till %@ tillfällen, %@ drycker och %@ månadssummor. Inget som redan finns här ändras eller tas bort.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Lade till %@ tillfällen, %@ drycker och %@ månadssummor.',
    'months as totals': 'månader bara som summor',
    'by month only': 'bara per månad',
    'monthly total': 'månadssumma',
    'No daily records for this day': 'Inga dagliga poster för den här dagen',
    'Monthly total: %@': 'Månadssumma: %@',
    'A dry month': 'En torr månad',

    # --- RemovePersonSection ---
    'Remove %@?': 'Ta bort %@?',
    'Remove': 'Ta bort',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Raderar %@ tillfällen, %@ drycker och %@ månadssummor. Det går inte att ångra.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Raderar %@ tillfällen och %@ drycker. Det går inte att ångra.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Svep åt vänster på en gäst för att ta bort hen med allt som registrerats under hen. Du kan inte tas bort.',
    'People': 'Personer',
    'Owner': 'Ägare',
    'Everyone this app records. Switch, add, or remove someone.': 'Alla som den här appen registrerar. Byt, lägg till eller ta bort någon.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Kvar från kvällen innan',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorier',
    'Sessions': 'Tillfällen',
    'Per session': 'Per tillfälle',
    'Under the influence': 'Påverkad',
    '%@ of the time': '%@ av tiden',
    'Days over limit': 'Dagar över gränsen',
    'Longest sober run': 'Längsta nyktra period',
    'Favourite drink': 'Favoritdryck',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Visning och språk",
    "Data": "Data",
    "Concentration": "Koncentration",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Låt frågan om hur ofta du dricker styra hastigheten, om du inte har en mätning att jämföra den med.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Uppskattning, inte mätning. Använd aldrig detta för att avgöra om du kan köra.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Uppskattat intervall, inte mätning. Använd aldrig detta för att avgöra om du kan köra.',
    'How does the app calculate this?':
        'Hur beräknar appen detta?',
    'approximately %@ %@':
        'ungefär %@ %@',
    'How it works':
        'Så fungerar det',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Använd aldrig detta för att avgöra om du kan köra. Appen uppskattar, den mäter inte, och din verkliga nivå kan skilja sig avsevärt.',
    'Why this app exists':
        'Därför finns appen',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink hjälper dig att dricka mer medvetet och behålla kontrollen. Beslutet fattas före nästa glas, så appen visar i förväg vart ytterligare en dryck skulle ta din nivå och när den skulle nå sin topp.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Men det handlar inte bara om i kväll. Varje dryck du loggar hamnar i din historik, så över månader och år ser du hur mycket, hur ofta och hur högt du dricker. Dina mönster växer fram, och även vilket håll de rör sig åt – om det blir bättre eller sämre.',
    'How it calculates':
        'Så räknar den',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Uppskattningen bygger på Widmarks metod, som har använts för att uppskatta alkoholhalten i blodet sedan 1930-talet; appen använder en förfinad version av den.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Utifrån din vikt, längd, ålder och kön räknar den ut hur mycket vatten kroppen innehåller, eftersom det är där alkoholen sprids. Den följer varje dryck för sig: hur mycket alkohol den innehöll, hur snabbt du drack den och hur mycket du hade ätit, eftersom det avgör hur snabbt den tas upp.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Under tiden bryter levern ned en ungefär konstant mängd varje timme; hur mycket hos dig uppskattas utifrån hur ofta du dricker. Resultatet blir en kurva, minut för minut: var du är nu, vart du är på väg och när du är nere på noll.',
    'Details':
        'Detaljer',
    'Body water':
        'Kroppsvatten',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsons formel (1980), utifrån vikt, längd, ålder och kön. Formeln för kvinnor saknar ålder – en egenskap hos formeln, inte en bugg. Distributionsvolymen är kroppsvattnet delat med 0,85, blodets vattenhalt.',
    'Absorption':
        'Upptag',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Varje dryck har sin egen ”mage”. På fastande mage tas hälften av alkoholen upp på cirka 7 minuter, på full mage på cirka 21. En dryck du smuttar på når magen jämnt under tiden du dricker den.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Ger en lägre topp och gör att du når noll tidigare.Överraskande, men uppmätt: med mat bryter magen ned en del av alkoholen innan den tas upp (appen räknar med 5, 10 och 15 procent), och det som aldrig kom in behöver inte brytas ned.',
    'Elimination':
        'Nedbrytning',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Cirka 0,15 ‰ per timme (publicerat intervall 0,10–0,25), högre hos den som dricker regelbundet eftersom leverns enzymer anpassar sig. Nära noll saktar nedbrytningen in (Michaelis–Menten-kinetik), så kurvan planar ut i stället för att tvärstanna.',
    'Computation':
        'Beräkning',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Kurvan kommer från en numerisk simulering med en minuts upplösning.',
    'Why it is only an estimate':
        'Därför är det bara en uppskattning',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Appen mäter ingenting. Det den visar är resultatet av en modell med genomsnittsvärden, och verkligheten kan skilja sig. Den största okända faktorn är hur snabbt du bryter ned alkohol: inom det rimliga intervallet kan den ensam flytta toppen med 40 procent och tidpunkten då du når noll med fyra timmar samma kväll.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Även gener, leverns hälsa, läkemedel, vad du ätit, sömn och trötthet spelar in – inget av det känner appen till. Bara en kalibrerad alkometer eller ett blodprov ger ett exakt värde.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Siffran är ändå användbar. Om appen hos dig konsekvent visar lite för högt eller lågt, slår den fel åt samma håll varje kväll, så med tiden lär du dig vad ett visst värde betyder för dig. I Profil kan du också visa osäkerheten i förbränningshastigheten: då ser du ett intervall i stället för en enda siffra.',
    'Tips':
        'Tips',
    'Favourite drink in one tap':
        'Favoritdryck med ett tryck',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Välj en favorit i Profil så loggar knappen på Live den med ett enda tryck.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Lägg den på låsskärmen eller hemskärmen: ett tryck loggar din favorit. Med Pro visar den också din nivå och vart den är på väg, så länge det finns alkohol i kroppen.',
    'How do I add it?':
        'Hur lägger jag till den?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Säg ”Hey Siri, LogMyDrink now” så loggar Siri din favorit och berättar vart din topp är på väg. (Kommandot fungerar på engelska.)',
    'Looking back':
        'Se tillbaka',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '”Igår” överst på Live tar dig till föregående dag med ett tryck; fliken Historik visar dina mönster över veckor, månader och år.',
    'Logging later':
        'Logga i efterhand',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Om du loggar en dryck i efterhand, ställ tillbaka tiden med knapparna − och +; en missad dag kan fyllas i från vyn Dag i Historik.',
    'One tap and done':
        'Ett tryck och klart',
    'Your favourite from the Lock Screen':
        'Din favorit från låsskärmen',
    'Say it, don’t type it':
        'Säg det, skriv det inte',
    'See your patterns':
        'Se dina mönster',
    'Set what you drink most often and log it with a single tap.':
        'Ange vad du dricker oftast och logga det med ett enda tryck.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Ett tryck på widgeten loggar din favorit, utan att leta efter appen. På kvällen visar den även din nivå.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '”Hey Siri, LogMyDrink now” – Siri loggar din favorit och berättar vart din topp är på väg.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Historik visar hur mycket och hur högt du dricker över veckor, månader och år, och åt vilket håll det går.',
    'Set favourite':
        'Välj favorit',
    'Add widget':
        'Lägg till widget',
    'Got it':
        'Uppfattat',
    'Open History':
        'Öppna Historik',
    'Don’t show again':
        'Visa inte igen',
    'Lock Screen':
        'Låsskärm',
    'Home Screen':
        'Hemskärm',
    'Where':
        'Var',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Lås iPhone och håll sedan fingret på låsskärmen.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Tryck på Anpassa, sedan på Låsskärm och därefter på widgetraden under klockan.',
    'Choose LogMyDrink, then tap Done.':
        'Välj LogMyDrink och tryck på Klar.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Håll fingret på ett tomt område på hemskärmen tills apparna börjar vibrera.',
    'Tap Edit, then Add Widget.':
        'Tryck på Ändra och sedan på Lägg till widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Sök efter LogMyDrink, välj en storlek och tryck på Lägg till widget.',
    'A tap on the widget opens the app and logs your favourite drink. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Ett tryck på widgeten öppnar appen och loggar din favoritdryck. Med Pro visar den också din nivå och vart den är på väg, så länge det finns alkohol i kroppen.',
    'Add the widget':
        'Lägg till widgeten',
    'Show tips':
        'Visa tips',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Högst ett tips om dagen när du öppnar appen – aldrig så länge det finns alkohol i kroppen.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Vad siffran visar',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Siffran är en uppskattning av din alkoholkoncentration i blodet (på engelska BAC, blood alcohol concentration): hur mycket alkohol det finns i ditt blod.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'I promille (‰) är det gram alkohol per liter blod: 0,5 ‰ betyder ett halvt gram i varje liter. I procent är det gram per 100 milliliter, så samma nivå ger en tio gånger mindre siffra: 0,5 ‰ motsvarar 0,05 procent. Du växlar mellan dem under Profil › Visning och språk.',
    'The curve shows the same level over time, minute by minute.':
        'Kurvan visar samma nivå över tid, minut för minut.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promille (‰) är gram alkohol per liter blod, procent är gram per 100 milliliter: 0,5 ‰ motsvarar 0,05 procent.',
}
