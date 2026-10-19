"""
Latvian.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promiles",
    "Percent": "Procenti",

    # --- DrinkCatalog: drink types ---
    "Beer": "Alus",
    "Wine": "Vīns",
    "Champagne": "Dzirkstošvīns",
    "Shot": "Šots",
    "Cocktail": "Kokteilis",
    "Custom": "Pielāgots",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Tukšs kuņģis",
    "Moderately full": "Vidēji pilns",
    "Full stomach": "Pilns kuņģis",
    "Empty": "Tukšs",
    "Moderate": "Vidēji",
    "Full": "Pilns",
    "Fast absorption, higher and earlier peak.":
        "Ātra uzsūkšanās, augstāks un agrāks maksimums.",
    "Moderate absorption.": "Vidēja uzsūkšanās.",
    "Slow absorption, lower and later peak.": "Lēna uzsūkšanās, zemāks un vēlāks maksimums.",

    # --- DrinkingFrequency ---
    "Rarely": "Reti",
    "A few times a month": "Dažas reizes mēnesī",
    "Several times a week": "Vairākas reizes nedēļā",
    "Almost daily": "Gandrīz katru dienu",
    "A few occasions a year": "Dažas reizes gadā",
    "Social drinking": "Dzeršana kompānijā",
    "Weekly routine": "Iknedēļas ieradums",
    "Daily or nearly daily": "Katru dienu vai gandrīz katru dienu",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Laiks",
    "Level": "Līmenis",
    "Lower": "Zemākais",
    "Upper": "Augstākais",
    "Lower estimate": "Zemākais novērtējums",
    "Upper estimate": "Augstākais novērtējums",
    "Personal limit": "Personīgā robeža",
    "Drink": "Dzēriens",

    # --- BACChartView ---
    "Expected peak around %@": "Gaidāmais maksimums ap %@",
    "Peaked around %@": "Maksimums bija ap %@",
    "No active session": "Nav aktīvas reizes",
    "Still rising": "Vēl kāpj",
    "YOUR LIMIT %@": "TAVA ROBEŽA %@",
    "possible range": "iespējamais diapazons",

    # --- Live screen: the day with nothing on it ---
    "Live": "Šobrīd",
    "Nothing logged today": "Šodien nekas nav pierakstīts",
    "Add a drink when you have one.": "Pievieno dzērienu, kad to iedzer.",

    # --- Tabs and history ---
    "History": "Vēsture",
    "No past sessions yet": "Vēl nav iepriekšējo reižu",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Reize šeit parādās, kad tā ir beigusies — kad tavs līmenis ir nokrities līdz nullei "
        "un pagājušas dažas stundas.",
    "%@ drinks": "Dzērieni: %@",
    "peak": "maksimums",
    "Started": "Sākums",
    "Lasted": "Ilgums",
    "Duration": "Ilgums",
    "Sober around": "Skaidrā apm.",
    "Sober at": "Skaidrā",
    "Remaining": "Atlicis",
    "next day": "nākamajā dienā",
    "previous day": "iepriekšējā dienā",
    "%@ days later": "pēc %@ dienām",
    "%@ days earlier": "pirms %@ dienām",
    "Calculated with your profile at the time": "Aprēķināts pēc tā brīža profila",

    # --- TodayView ---
    "Profile": "Profils",
    "Drinks": "Dzērieni",
    "Units": "Vienības",
    "Drinks this session": "Šīs reizes dzērieni",
    "Add drink": "Pievienot dzērienu",

    # --- Editing an already logged drink ---
    "Edit drink": "Rediģēt dzērienu",
    "Save changes": "Saglabāt izmaiņas",
    "With this": "Ar šo",
    "Delete": "Dzēst",
    "tap to edit · swipe to delete": "pieskaries, lai rediģētu · pavelc, lai dzēstu",

    # --- Drinking pace ---
    "How fast": "Cik ātri",
    "In one go": "Vienā paņēmienā",
    "Counts as a single swallow — the steepest possible rise.":
        "Tiek uzskatīts par vienu malku — visstraujākais iespējamais kāpums.",
    "A quick drink. The level climbs fast.": "Ātri izdzerts. Līmenis strauji kāpj.",
    "A normal pace.": "Parasts temps.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Lēni izbaudīts. Daudz maigāks kāpums pie tāda paša alkohola daudzuma.",

    # --- AddDrinkSheet ---
    "Cancel": "Atcelt",
    "Now": "Tagad",
    "Projected peak": "Prognozētais maksimums",
    "Peak at": "Maksimums plkst.",
    "Clears": "Izvadīts",
    "This would cross your limit": "Šis pārsniegtu tavu robežu",
    "Around %@, for up to %@.": "Aptuveni %@, līdz pat %@.",
    "This might cross your limit": "Šis varētu pārsniegt tavu robežu",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Ar lēnāku vielmaiņu — jā, ar ātrāku — nē. Tāda ir šī novērtējuma nenoteiktība.",
    "Type": "Veids",
    "Amount": "Daudzums",
    "Strength": "Stiprums",
    "%@ units": "Vienības: %@",
    "%@ g alcohol": "%@ g alkohola",
    "Stomach": "Kuņģis",
    "When": "Kad",
    "Done": "Gatavs",
    "Add": "Pievienot",

    # --- ProfileSheet ---
    "Male": "Vīrietis",
    "Female": "Sieviete",
    "Sex": "Dzimums",
    "Weight": "Svars",
    "Height": "Augums",
    "Age": "Vecums",
    "kg": "kg",
    "cm": "cm",
    "yrs": "gadi",
    "Body": "Ķermenis",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Kopējais ķermeņa ūdens tiek aprēķināts pēc Watson vienādojumiem, kas nosaka tilpumu, "
        "kurā alkohols izkliedējas.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Kopējais ķermeņa ūdens tiek aprēķināts pēc Watson vienādojumiem, kas nosaka tilpumu, "
        "kurā alkohols izkliedējas. Sieviešu vienādojumā vecums netiek izmantots, tāpēc tā "
        "maiņa rezultātu neietekmēs.",
    "Drinking frequency": "Dzeršanas biežums",
    "How often do you drink?": "Cik bieži tu dzer?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Šādi mēs novērtējam tavu izvadīšanas ātrumu. Regulāra dzeršana inducē aknu CYP2E1 ceļu, tāpēc biežiem dzērājiem alkohols tiek izvadīts ātrāk. Tas ir modeļa vājākais punkts, un tieši tāpēc sadaļā Attēlojums un valoda tu vari norādīt, cik daudz no šīs nenoteiktības lietotne tev rāda.",
    "Your limit": "Tava robeža",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Tavs paša atskaites skaitlis, nevis likumā noteiktā robeža. Lietotne norāda, kad "
        "plānotais dzēriens to pārsniegtu un cik ilgi tu paliktu virs tās.",
    "Calculated values": "Aprēķinātās vērtības",
    "Total body water": "Kopējais ķermeņa ūdens",
    "Distribution volume": "Izkliedes tilpums",
    "Widmark factor": "Widmark faktors",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmark faktors vīriešiem parasti ir ap 0,68, sievietēm — ap 0,55. Ja tavējais no tā "
        "stipri atšķiras, ir vērts pārbaudīt augstāk norādītās vērtības.",
    "Elimination rate": "Izvadīšanas ātrums",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Cik ātri tavas aknas izvada alkoholu pēc tā uzsūkšanās — līknes krītošās daļas "
        "slīpums.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohols tiek izvadīts aptuveni nemainīgā daudzumā stundā, nevis procentuālā daļā, jo "
        "enzīms, kas to noārda, jau gandrīz jebkurā līmenī strādā ar pilnu jaudu. Tieši tāpēc "
        "vispār pastāv īkšķa likumi, piemēram, „viens dzēriens stundā“.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Ar šo iestatījumu %@ izvadīšana aizņem aptuveni %@. Gandrīz visiem tas ir diapazonā "
        "%@ stundā.",
    "How to find yours": "Kā noskaidrot savējo",
    "With a breathalyser": "Ar alkometru",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Izpūt divreiz ar vismaz stundas starplaiku līknes krītošajā daļā — divas vai vairāk "
        "stundas pēc pēdējā dzēriena, neko pa vidu nedzerot. Atņem otro rādījumu no pirmā un "
        "izdali ar stundu skaitu starp tiem.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Piemēram, %@ un %@ divas stundas vēlāk dod %@ stundā.",
    "Without one": "Bez tā",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Lietotne norāda, kad paredz, ka alkohols būs izvadīts. Ja tu regulāri esi atpakaļ "
        "normā krietni ātrāk, tavs ātrums ir lielāks nekā iestatījumā — palielini to par vienu "
        "soli un novēro dažas reizes. Ja tas prasa ilgāk, nekā prognozēts, samazini to.",
    "What moves it": "Kas to ietekmē",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Regulāra dzeršana to paaugstina: aknu enzīmu, kas veic šo darbu, inducē pati "
        "lietošana. Sievietēm tas vidēji ir nedaudz augstāks, bet tukšā dūšā vai ar aknu "
        "problēmām — zemāks.",
    "Uncertainty": "Nenoteiktība",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Pie nulles katrs rādītājs ir viens skaitlis — lietotnes labākais novērtējums. Virs "
        "nulles tie paši rādītāji tiek rādīti kā diapazoni, un josla diagrammā attiecīgi "
        "paplašinās.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Pēc viena skaitļa ir vieglāk mācīties: laika gaitā tu uzzini, kā jūties tieši pie "
        "savām 0,6. Diapazons ir burtiskāka atbilde, jo ātrums tiešām ir nenoteikts. Abi "
        "varianti ir pamatoti — izvēle ir tava.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Izkliede, ko norāda tavs dzeršanas biežums, ir ± %@ stundā.",
    "Rate": "Ātrums",
    "Range": "Diapazons",
    "Advanced": "Papildu",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Vairākas personas",
    "History trends": "Vēstures tendences",
    "Week": "Nedēļa",
    "Month": "Mēnesis",
    "Year": "Gads",
    "Sober days": "Dienas bez alkohola",
    "Change": "Izmaiņas",
    "before records": "pirms ierakstu sākuma",
    "See further back": "Skatīt tālāk atpakaļ",
    "Weeks, months and years side by side — and every evening older than seven days.": "Nedēļas, mēneši un gadi blakus – un katrs vakars, vecāks par septiņām dienām.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Viss, ko esi ierakstījis, jau ir saglabāts. Atbloķēšana to tikai parāda.",
    "Coming soon": "Drīzumā",
    "Today": "Šodien",
    "Day": "Diena",
    "Yesterday": "Vakar",
    "No drinks on this day": "Šajā dienā dzērienu nav",
    "Trend": "Tendence",
    "day": "diena",
    "Smoothing": "Izlīdzināšana",
    "%@ sessions": "%@ reizes",
    "No data before %@": "Nav datu pirms %@",
    "vs.": "pret",
    "Grams": "Grami",
    "Grams of alcohol": "Grami alkohola",
    "Standard units": "Standarta vienības",
    "Unit size": "Vienības lielums",
    "Automatic": "Automātiski",
    "UK": "Apvienotā Karaliste",
    "Nordic countries": "Ziemeļvalstis",
    "US standard drink": "ASV standarta dzēriens",
    "WHO, most of Europe": "PVO, lielākā daļa Eiropas",
    "Period": "Periods",
    "Switch person": "Mainīt personu",
    "Add person": "Pievienot personu",
    "New person": "Jauna persona",
    "You": "Tu",
    "Name": "Vārds",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Visi četri maina līkni, tāpēc nevienu no tiem nevar uzminēt cita cilvēka vietā.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Viņu pašu robežu un smalkākos iestatījumus vēlāk var mainīt cilnē Profils, kamēr viņi "
        "ir izvēlētā persona.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Ātrā pievienošana",
    "Choose a favourite drink": "Izvēlies iecienītāko dzērienu",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Izvēlies dzērienu, ko parasti pasūti, un poga ekrānā Šobrīd to pierakstīs ar vienu "
        "pieskārienu.",
    "This is your quick-add drink": "Šis ir tavs ātrās pievienošanas dzēriens",
    "Set as my quick-add drink": "Iestatīt kā ātrās pievienošanas dzērienu",
    "This is now your usual": "Tagad šis ir tavs ierastais",
    "Remove favourite": "Noņemt iecienītāko",
    "Always add this one": "Vienmēr pievienot šo",
    "Logs it straight away, without opening anything.": "Pieraksta to uzreiz, neko neatverot.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Viens pieskāriens ekrānā Šobrīd pieraksta šo dzērienu, un uz pogas redzams "
        "prognozētais maksimums. Kuņģa pildījums tiek pārņemts no iepriekšējā dzēriena, un to "
        "var izlabot uzreiz pēc tam.",
    "Peak %@": "Maksimums %@",
    "%@ added": "%@ pievienots",
    "Save": "Saglabāt",
    "Undo": "Atsaukt",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Dublējums",
    "Export a backup": "Eksportēt dublējumu",
    "Import a backup": "Importēt dublējumu",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Dublējumā ir visas personas, reizes un dzērieni. Importēšana pievieno trūkstošo — tā "
        "nekad nemaina un nedzēš neko no jau esošā.",
    "Import this backup?": "Importēt šo dublējumu?",
    "Import": "Importēt",
    "Everything in this backup is already here.": "Viss no šī dublējuma jau ir šeit.",
    "Import finished": "Importēšana pabeigta",
    "OK": "Labi",

    # --- LanguageSection: the app's language ---
    "Language": "Valoda",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Atver šo lietotni sadaļā Iestatījumi, kur „Vēlamā valoda“ nosaka pašas lietotnes "
        "valodu — sistēmas valoda paliek nemainīga. Kad to maini, iOS lietotni restartē.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Neizdevās importēt",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Šis fails nav LogMyDrink dublējums vai arī ir bojāts.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Šis dublējums ir izveidots jaunākā LogMyDrink versijā. Atjaunini lietotni un mēģini "
        "vēlreiz.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Tiks pievienotas reizes: %@, dzērieni: %@ un mēneša kopsummas: %@. Nekas no jau esošā netiek mainīts vai dzēsts.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Pievienots: %@ reizes, %@ dzērieni un %@ mēneša kopsummas.',
    'months as totals': 'mēneši tikai kā kopsummas',
    'by month only': 'tikai pa mēnešiem',
    'monthly total': 'mēneša kopsumma',
    'No daily records for this day': 'Par šo dienu nav dienas ierakstu',
    'Monthly total: %@': 'Mēneša kopsumma: %@',
    'A dry month': 'Sauss mēnesis',

    # --- RemovePersonSection ---
    'Remove %@?': 'Vai noņemt %@?',
    'Remove': 'Noņemt',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Dzēš reizes: %@, dzērienus: %@ un mēneša kopsummas: %@. To nevar atsaukt.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Dzēš reizes: %@ un dzērienus: %@. To nevar atsaukt.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Pavelc pa kreisi uz viesa, lai noņemtu viņu ar visu, kas ierakstīts zem viņa. Tevi noņemt nevar.',
    'People': 'Personas',
    'Owner': 'Īpašnieks',
    'Everyone this app records. Switch, add, or remove someone.': 'Visi, ko šī lietotne ieraksta. Pārslēdz, pievieno vai noņem kādu.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Pārnests no iepriekšējā vakara',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorijas',
    'Sessions': 'Reizes',
    'Per session': 'Uz reizi',
    'Under the influence': 'Reibumā',
    '%@ of the time': '%@ laika',
    'Days over limit': 'Dienas virs robežas',
    'Longest sober run': 'Garākā skaidrā sērija',
    'Favourite drink': 'Iecienītākais dzēriens',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Attēlojums un valoda",
    "Data": "Dati",
    "Concentration": "Koncentrācija",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Atstāj ātrumu biežuma jautājuma ziņā, ja vien tev nav mērījuma, ar ko to salīdzināt.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Aplēse, nevis mērījums. Nekad neizlem pēc šī, vai drīksti vadīt auto.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Aplēstais diapazons, nevis mērījums. Nekad neizlem pēc šī, vai drīksti vadīt auto.',
    'How does the app calculate this?':
        'Kā lietotne aprēķina?',
    'approximately %@ %@':
        'aptuveni %@ %@',
    'How it works':
        'Kā tas darbojas',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nekad neizlem pēc šī, vai drīksti vadīt auto. Lietotne aplēš, nevis mēra, un tavs patiesais līmenis var būtiski atšķirties.',
    'Why this app exists':
        'Kāpēc šī lietotne',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink palīdz dzert apzinātāk un saglabāt kontroli. Lēmums tiek pieņemts pirms nākamās glāzes, tāpēc lietotne iepriekš parāda, kur tavu līmeni aizvestu vēl viens dzēriens un kad tas sasniegtu maksimumu.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Taču runa nav tikai par šo vakaru. Katrs pievienotais dzēriens nonāk vēsturē, tāpēc mēnešu un gadu gaitā redzi, cik daudz, cik bieži un cik augstu tu dzer. No tā izkristalizējas tavi paradumi un arī virziens, kurā tie mainās – vai situācija uzlabojas vai pasliktinās.',
    'How it calculates':
        'Kā tā aprēķina',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Aplēse balstās uz Vidmarka metodi, ar kuru alkohola koncentrāciju asinīs aplēš kopš 20. gadsimta 30. gadiem; lietotne izmanto tās pilnveidotu versiju.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'No tava svara, auguma, vecuma un dzimuma tā aprēķina, cik daudz ūdens ir tavā ķermenī, jo tieši tajā izplatās alkohols. Tā seko katram dzērienam atsevišķi: cik daudz alkohola tajā bija, cik ātri tu to izdzēri un cik daudz biji ēdis, jo no tā atkarīgs uzsūkšanās ātrums.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Tikmēr aknas katru stundu noārda aptuveni nemainīgu daudzumu; tavs daudzums tiek aplēsts pēc tā, cik bieži tu dzer. Rezultāts ir līkne minūti pa minūtei: kur tu esi tagad, uz kurieni dodies un kad atkal būsi uz nulles.',
    'Details':
        'Sīkāka informācija',
    'Body water':
        'Ķermeņa ūdens',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Vatsona formula (1980) no svara, auguma, vecuma un dzimuma. Sieviešu formulā nav vecuma – tā ir formulas īpatnība, nevis kļūda. Izkliedes tilpums ir ķermeņa ūdens, dalīts ar 0,85 – asins ūdens saturu.',
    'Absorption':
        'Uzsūkšanās',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Katram dzērienam ir savs „kuņģis“. Tukšā dūšā puse alkohola uzsūcas aptuveni 7 minūtēs, ar pilnu kuņģi – aptuveni 21 minūtē. Malkos dzerts dzēriens nonāk kuņģī vienmērīgi visu dzeršanas laiku.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Dod zemāku maksimumu un agrāku nulli. Pārsteidzoši, bet izmērīti: ar ēdienu kuņģis daļu alkohola noārda pirms uzsūkšanās (lietotne rēķina ar 5, 10 un 15 procentiem), un to, kas nekad nenonāca asinīs, nav jānoārda.',
    'Elimination':
        'Noārdīšana',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Aptuveni 0,15 ‰ stundā (publicētais diapazons 0,10–0,25), regulāri dzerošiem vairāk, jo aknu enzīmi pielāgojas. Tuvu nullei tā palēninās (Mihaelisa–Mentenas kinētika), tāpēc līkne pakāpeniski izlīdzinās, nevis pēkšņi pārtrūkst.',
    'Computation':
        'Aprēķins',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Līkne iegūta ar skaitlisku simulāciju ar vienas minūtes izšķirtspēju.',
    'Why it is only an estimate':
        'Kāpēc tā ir tikai aplēse',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Lietotne neko nemēra. Tā rāda modeļa rezultātu ar vidējām vērtībām, un realitāte var atšķirties. Lielākais nezināmais ir tas, cik ātri tu noārdi alkoholu: ticamā diapazona robežās tas viens pats vienā vakarā var pārbīdīt maksimumu par 40 procentiem un nulli par četrām stundām.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Nozīme ir arī ģenētikai, aknu veselībai, zālēm, apēstajam, miegam un nogurumam – neko no tā lietotne nezina. Precīzu vērtību dod tikai verificēts alkometrs vai asins analīze.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Skaitlis tomēr ir noderīgs. Ja lietotne tev konsekventi rāda nedaudz par daudz vai par maz, tā katru vakaru kļūdās vienā virzienā, tāpēc laika gaitā tu iemācies, ko konkrēta vērtība nozīmē tieši tev. Profilā vari parādīt arī noārdīšanas ātruma nenoteiktību: tad viena skaitļa vietā redzēsi diapazonu.',
    'Tips':
        'Padomi',
    'Favourite drink in one tap':
        'Iecienītais dzēriens ar vienu pieskārienu',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Iestati iecienīto dzērienu Profilā, un poga ekrānā Šobrīd to pievienos ar vienu pieskārienu.',
    'Widget':
        'Logrīks',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Pievieno to bloķēšanas ekrānam vai sākuma ekrānam: viens pieskāriens pievieno tavu iecienīto dzērienu. Kamēr organismā ir alkohols, tas rāda arī tavu līmeni un tā virzienu.',
    'How do I add it?':
        'Kā to pievienot?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Saki „Hey Siri, LogMyDrink now“, un Siri pievienos tavu iecienīto dzērienu un pateiks, uz kurieni virzās tavs maksimums.',
    'Looking back':
        'Atskats',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Vakar“ ekrāna Šobrīd augšā ar vienu pieskārienu aizved uz iepriekšējo dienu; cilnē Vēsture redzami tavi paradumi nedēļu, mēnešu un gadu griezumā.',
    'Logging later':
        'Pievienošana vēlāk',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Ja dzērienu pievieno vēlāk, pagriez laiku atpakaļ ar pogām − un +; izlaistu dienu vari papildināt Vēstures dienas skatā.',
    'One tap and done':
        'Viens pieskāriens, un gatavs',
    'Your favourite from the Lock Screen':
        'Tavs iecienītais no bloķēšanas ekrāna',
    'Say it, don’t type it':
        'Pasaki, neraksti',
    'See your patterns':
        'Apskati savus paradumus',
    'Set what you drink most often and log it with a single tap.':
        'Iestati, ko dzer visbiežāk, un pievieno to ar vienu pieskārienu.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Viens pieskāriens logrīkam pievieno tavu iecienīto dzērienu, nemeklējot lietotni. Vakarā tas rāda arī tavu līmeni.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now“ – Siri pievienos tavu iecienīto dzērienu un pateiks, uz kurieni virzās tavs maksimums.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Vēsture rāda, cik daudz un cik augstu tu dzer nedēļu, mēnešu un gadu laikā un kurā virzienā tas mainās.',
    'Set favourite':
        'Iestatīt iecienīto',
    'Add widget':
        'Pievienot logrīku',
    'Got it':
        'Skaidrs',
    'Open History':
        'Atvērt vēsturi',
    'Later':
        'Vēlāk',
    'Don’t show again':
        'Vairs nerādīt',
    'Lock Screen':
        'Bloķēšanas ekrāns',
    'Home Screen':
        'Sākuma ekrāns',
    'Where':
        'Kur',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Bloķē iPhone un tad turi pirkstu uz bloķēšanas ekrāna.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Pieskaries Pielāgot, tad Bloķēšanas ekrāns un pēc tam logrīku rindai zem pulksteņa.',
    'Choose LogMyDrink, then tap Done.':
        'Izvēlies LogMyDrink un pieskaries Gatavs.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Turi pirkstu uz tukšas sākuma ekrāna vietas, līdz ikonas sāk kustēties.',
    'Tap Edit, then Add Widget.':
        'Pieskaries Rediģēt un pēc tam Pievienot logrīku.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Meklē LogMyDrink, izvēlies izmēru un pieskaries Pievienot logrīku.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Pieskāriens logrīkam atver lietotni un pievieno tavu iecienīto dzērienu. Kamēr organismā ir alkohols, tas rāda arī tavu līmeni un tā virzienu.',
    'Add the widget':
        'Pievienot logrīku',
    'Show tips':
        'Rādīt padomus',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Ne vairāk kā viens padoms dienā, atverot lietotni, – nekad, kamēr organismā ir alkohols.',
}
