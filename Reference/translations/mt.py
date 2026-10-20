"""
Maltese.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Fil-elf",
    "Percent": "Fil-mija",

    # --- DrinkCatalog: drink types ---
    "Beer": "Birra",
    "Wine": "Inbid",
    "Champagne": "Xampanja",
    "Shot": "Shot",
    "Cocktail": "Kokteil",
    "Custom": "Personalizzat",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Stonku vojt",
    "Moderately full": "Moderatament mimli",
    "Full stomach": "Stonku mimli",
    "Empty": "Vojt",
    "Moderate": "Moderat",
    "Full": "Mimli",
    "Fast absorption, higher and earlier peak.":
        "Assorbiment mgħaġġel, quċċata ogħla u aktar kmieni.",
    "Moderate absorption.": "Assorbiment moderat.",
    "Slow absorption, lower and later peak.":
        "Assorbiment bil-mod, quċċata aktar baxxa u aktar tard.",

    # --- DrinkingFrequency ---
    "Rarely": "Rarament",
    "A few times a month": "Ftit drabi fix-xahar",
    "Several times a week": "Diversi drabi fil-ġimgħa",
    "Almost daily": "Kważi kuljum",
    "A few occasions a year": "Ftit okkażjonijiet fis-sena",
    "Social drinking": "Xorb soċjali",
    "Weekly routine": "Rutina ta' kull ġimgħa",
    "Daily or nearly daily": "Kuljum jew kważi kuljum",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Ħin",
    "Level": "Livell",
    "Lower": "Inferjuri",
    "Upper": "Superjuri",
    "Lower estimate": "Stima inferjuri",
    "Upper estimate": "Stima superjuri",
    "Personal limit": "Limitu personali",
    "Drink": "Xarba",

    # --- BACChartView ---
    "Expected peak around %@": "Quċċata mistennija madwar %@",
    "Peaked around %@": "Il-quċċata kienet madwar %@",
    "No active session": "L-ebda sessjoni attiva",
    "Still rising": "Għadu tiela'",
    "YOUR LIMIT %@": "IL-LIMITU TIEGĦEK %@",
    "possible range": "firxa possibbli",

    # --- Live screen: the day with nothing on it ---
    "Live": "Dirett",
    "Nothing logged today": "Xejn irreġistrat illum",
    "Add a drink when you have one.": "Żid xarba meta tixrob waħda.",

    # --- Tabs and history ---
    "History": "Storja",
    "No past sessions yet": "Għad m'hemm l-ebda sessjoni li għaddiet",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Sessjoni tidher hawn ladarba tkun intemmet — meta l-livell tiegħek ikun għadda u "
        "jkunu għaddew ftit sigħat.",
    "%@ drinks": "Xarbiet: %@",
    "peak": "quċċata",
    "Started": "Bdiet",
    "Lasted": "Damet",
    "Duration": "Tul",
    "Sober around": "Bla alkoħol madwar",
    "Sober at": "Bla alkoħol",
    "Remaining": "Fadal",
    "next day": "l-għada",
    "previous day": "il-jum ta' qabel",
    "%@ days later": "%@ jiem wara",
    "%@ days earlier": "%@ jiem qabel",
    "Calculated with your profile at the time":
        "Ikkalkulat bil-profil tiegħek ta' dak iż-żmien",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Xarbiet",
    "Units": "Unitajiet",
    "Drinks this session": "Xarbiet f'din is-sessjoni",
    "Add drink": "Żid xarba",

    # --- Editing an already logged drink ---
    "Edit drink": "Immodifika x-xarba",
    "Save changes": "Issejvja l-bidliet",
    "With this": "B'din",
    "Delete": "Ħassar",
    "tap to edit · swipe to delete": "agħfas biex timmodifika · swajpja biex tħassar",

    # --- Drinking pace ---
    "How fast": "Kemm malajr",
    "In one go": "F'daqqa",
    "Counts as a single swallow — the steepest possible rise.":
        "Jgħodd bħala belgħa waħda — l-aktar tlugħ qawwi possibbli.",
    "A quick drink. The level climbs fast.": "Xarba mgħaġġla. Il-livell jitla' malajr.",
    "A normal pace.": "Pass normali.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Mixruba bil-mod. Tlugħ ħafna aktar ħafif għall-istess alkoħol.",

    # --- AddDrinkSheet ---
    "Cancel": "Ikkanċella",
    "Now": "Issa",
    "Projected peak": "Quċċata prevista",
    "Peak at": "Ħin tal-quċċata",
    "Clears": "Jgħaddi",
    "This would cross your limit": "Din kienet taqbeż il-limitu tiegħek",
    "Around %@, for up to %@.": "Madwar %@, għal sa %@.",
    "This might cross your limit": "Din tista' taqbeż il-limitu tiegħek",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "B'metaboliżmu aktar bil-mod iva, b'wieħed aktar mgħaġġel le. Dik hi l-inċertezza "
        "tal-istima.",
    "Type": "Tip",
    "Amount": "Ammont",
    "Strength": "Qawwa",
    "%@ units": "Unitajiet: %@",
    "%@ g alcohol": "%@ g alkoħol",
    "Stomach": "Stonku",
    "When": "Meta",
    "Done": "Lest",
    "Add": "Żid",

    # --- ProfileSheet ---
    "Male": "Raġel",
    "Female": "Mara",
    "Sex": "Sess",
    "Weight": "Piż",
    "Height": "Tul",
    "Age": "Età",
    "kg": "kg",
    "cm": "cm",
    "yrs": "snin",
    "Body": "Ġisem",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "L-ilma totali tal-ġisem ġej mill-ekwazzjonijiet ta' Watson, li jiddeterminaw il-volum "
        "li fih jinfirex l-alkoħol.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "L-ilma totali tal-ġisem ġej mill-ekwazzjonijiet ta' Watson, li jiddeterminaw il-volum "
        "li fih jinfirex l-alkoħol. L-ekwazzjoni għan-nisa ma tinkludix l-età, għalhekk li "
        "tibdilha mhux se taffettwa r-riżultat.",
    "Drinking frequency": "Frekwenza tax-xorb",
    "How often do you drink?": "Kemm-il darba tixrob?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Hekk nistmaw ir-rata ta' eliminazzjoni tiegħek. Ix-xorb regolari jistimula l-mogħdija CYP2E1 tal-fwied, għalhekk min jixrob ta' spiss ineħħi l-alkoħol aktar malajr. Dan hu l-aktar punt dgħajjef tal-mudell, u għalhekk taħt Wiri u lingwa tista' tissettja kemm minn dik l-inċertezza turik l-app.",
    "Your limit": "Il-limitu tiegħek",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "In-numru ta' referenza tiegħek stess, mhux limitu legali. L-app tgħidlek meta xarba "
        "ppjanata kienet taqbżu, u għal kemm żmien kont tibqa' 'il fuq minnu.",
    "Calculated values": "Valuri kkalkulati",
    "Total body water": "Ilma totali tal-ġisem",
    "Distribution volume": "Volum ta' distribuzzjoni",
    "Widmark factor": "Fattur Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Il-fattur Widmark normalment ikun madwar 0.68 għall-irġiel u 0.55 għan-nisa. Jekk "
        "tiegħek hu 'il bogħod minn hekk, ta' min tiċċekkja l-valuri ta' fuq.",
    "Elimination rate": "Rata ta' eliminazzjoni",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Kemm malajr il-fwied tiegħek ineħħi l-alkoħol ladarba jkun ġie assorbit — ix-xaqliba "
        "tan-naħa niżla tal-kurva.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "L-alkoħol jitlaq b'ammont bejn wieħed u ieħor fiss kull siegħa, u mhux bħala "
        "perċentwali, għax l-enzima li tkissru diġà taħdem b'kapaċità sħiħa kważi "
        "f'kull livell. Huwa għalhekk li jeżistu regoli prattiċi bħal “xarba waħda "
        "fis-siegħa”.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "B'dan l-issettjar, %@ jieħu madwar %@ biex jgħaddi. Għal kważi kulħadd hija bejn "
        "%@ fis-siegħa.",
    "How to find yours": "Kif issib ir-rata tiegħek",
    "With a breathalyser": "B'test tan-nifs",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Onfoħ darbtejn, tal-anqas siegħa bejn waħda u oħra, fuq in-naħa niżla — sagħtejn jew "
        "aktar wara l-aħħar xarba, mingħajr ma tixrob xejn bejniethom. Naqqas it-tieni qari mill-ewwel "
        "wieħed u aqsam bis-sigħat ta' bejniethom.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Ngħidu aħna, %@ u %@ sagħtejn wara jagħtu %@ fis-siegħa.",
    "Without one": "Mingħajr wieħed",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "L-app tgħidlek meta tistenna li l-livell tiegħek jgħaddi. Jekk b'mod konsistenti "
        "terġa' lura għan-normal sew qabel dak il-ħin, ir-rata tiegħek hi ogħla mill-issettjar "
        "— għolliha pass wieħed u osserva għal ftit sessjonijiet. Jekk tieħu aktar milli "
        "kien imbassar, baxxiha.",
    "What moves it": "X'jibdilha",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Ix-xorb regolari jgħollieha: l-enzima tal-fwied li tagħmel ix-xogħol tiżdied bl-użu. "
        "Bħala medja tkun ukoll kemmxejn ogħla fin-nisa, u aktar baxxa fuq stonku vojt jew bi "
        "problemi fil-fwied.",
    "Uncertainty": "Inċertezza",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Fiż-żero kull ċifra hi numru wieħed — l-aħjar stima tal-app. 'Il fuq minn żero "
        "l-istess ċifri jintwerew bħala firxiet, u l-faxxa fuq il-graff titwessa' biex taqbel.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Numru wieħed hu eħfef biex titgħallem miegħu: maż-żmien issir taf kif tħossok bi 0.6 "
        "tiegħek. Firxa hi t-tweġiba aktar letterali, għax ir-rata tassew mhijiex ċerta. "
        "It-tnejn jistgħu jiġu difiżi — id-deċiżjoni hi tiegħek.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Il-firxa suġġerita mill-frekwenza tax-xorb tiegħek hi ± %@ fis-siegħa.",
    "Rate": "Rata",
    "Range": "Firxa",
    "Advanced": "Avvanzat",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Diversi persuni",
    "History trends": "Xejriet tal-istorja",
    "Week": "Ġimgħa",
    "Month": "Xahar",
    "Year": "Sena",
    "Sober days": "Jiem bla alkoħol",
    "Change": "Bidla",
    "before records": "qabel bdew ir-rekords",
    "See further back": "Ara iktar lura",
    "Weeks, months and years side by side — and every evening older than seven days.": "Ġimgħat, xhur u snin ħdejn xulxin – u kull lejla eqdem minn sebat ijiem.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Kulma rreġistrajt huwa diġà maħżun. L-iftuħ juri biss dan.",
    "Coming soon": "Dalwaqt",
    "Today": "Illum",
    "Day": "Jum",
    "Yesterday": "Ilbieraħ",
    "No drinks on this day": "L-ebda xorb f'dan il-jum",
    "Trend": "Xejra",
    "day": "jum",
    "Smoothing": "Twittija",
    "%@ sessions": "%@ sessjonijiet",
    "No data before %@": "L-ebda data qabel %@",
    "vs.": "kontra",
    "Grams": "Grammi",
    "Grams of alcohol": "Grammi ta’ alkoħol",
    "Standard units": "Unitajiet standard",
    "Unit size": "Daqs tal-unità",
    "Automatic": "Awtomatiku",
    "UK": "Ir-Renju Unit",
    "Nordic countries": "Il-pajjiżi Nordiċi",
    "US standard drink": "Xarba standard tal-Istati Uniti",
    "WHO, most of Europe": "WHO, il-biċċa l-kbira tal-Ewropa",
    "Period": "Perjodu",
    "Switch person": "Ibdel il-persuna",
    "Add person": "Żid persuna",
    "New person": "Persuna ġdida",
    "You": "Int",
    "Name": "Isem",
    "All four change the curve, so none of them can be guessed for someone else.":
        "L-erbgħa kollha jbiddlu l-kurva, għalhekk ebda wieħed minnhom ma jista' jitbassar "
        "għal ħaddieħor.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Il-limitu tagħhom u l-issettjar aktar dettaljat jistgħu jinbidlu aktar tard fit-tab "
        "Profil, sakemm tkun magħżula dik il-persuna.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Żieda mgħaġġla",
    "Choose a favourite drink": "Agħżel xarba favorita",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Agħżel ix-xarba li normalment tordna, u buttuna fuq l-iskrin Dirett tirreġistraha "
        "b'tektika waħda.",
    "This is your quick-add drink": "Din hi x-xarba tiegħek għaż-żieda mgħaġġla",
    "Set as my quick-add drink": "Agħmilha x-xarba tiegħi għaż-żieda mgħaġġla",
    "This is now your usual": "Din issa hi x-xarba tas-soltu tiegħek",
    "Remove favourite": "Neħħi l-favorita",
    "Always add this one": "Dejjem żid din",
    "Logs it straight away, without opening anything.":
        "Jirreġistraha mill-ewwel, mingħajr ma jiftaħ xejn.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Tektika waħda fuq l-iskrin Dirett tirreġistra din, bil-quċċata prevista fuq il-buttuna. "
        "Kemm hu mimli l-istonku tiegħek jittieħed mix-xarba ta' qabel, u jista' jiġi kkoreġut "
        "mill-ewwel wara.",
    "Peak %@": "Quċċata %@",
    "%@ added": "Żieda: %@",
    "Save": "Issejvja",
    "Undo": "Annulla",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Backup",
    "Export a backup": "Esporta backup",
    "Import a backup": "Importa backup",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Backup fih kull persuna, okkażjoni u xarba. L-importazzjoni żżid dak li hu nieqes — "
        "qatt ma tibdel jew tneħħi dak li diġà hawn.",
    "Import this backup?": "Timporta dan il-backup?",
    "Import": "Importa",
    "Everything in this backup is already here.": "Kollox f'dan il-backup diġà jinsab hawn.",
    "Import finished": "L-importazzjoni lestiet",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Lingwa",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Tiftaħ din l-app f'Settings, fejn “Preferred Language” jissettja l-lingwa tal-app "
        "innifisha — dik tas-sistema tibqa' kif inhi. iOS jerġa' jibda l-app meta tibdilha.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "L-importazzjoni ma rnexxietx",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Dan il-fajl mhuwiex backup ta' LogMyDrink, jew inkella hu korrott.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Dan il-backup sar b'verżjoni aktar ġdida ta' LogMyDrink. Aġġorna l-app u erġa' "
        "pprova.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        "Okkażjonijiet li se jiżdiedu: %@. Xarbiet: %@. Totali ta' kull xahar: %@. Xejn minn dak li diġà hawn ma jinbidel jew jitneħħa.",
    'Added %@ occasions, %@ drinks and %@ monthly totals.': "Żdiedu %@ okkażjonijiet, %@ xarbiet u %@ totali ta' kull xahar.",
    'months as totals': 'xhur bħala totali biss',
    'by month only': 'skont ix-xahar biss',
    'monthly total': 'total tax-xahar',
    'No daily records for this day': "M'hemmx rekords ta' kuljum għal dan il-jum",
    'Monthly total: %@': 'Total tax-xahar: %@',
    'A dry month': 'Xahar mingħajr alkoħol',

    # --- RemovePersonSection ---
    'Remove %@?': 'Tneħħi lil %@?',
    'Remove': 'Neħħi',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        "Iħassar %@ okkażjonijiet, %@ xarbiet u %@ totali ta' kull xahar. Dan ma jistax jitreġġa' lura.",
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': "Iħassar %@ okkażjonijiet u %@ xarbiet. Dan ma jistax jitreġġa' lura.",

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        "Iswajpja lejn ix-xellug fuq mistieden biex tneħħih ma' kulma ġie rreġistrat taħtu. Int ma tistax titneħħa.",
    'People': 'Persuni',
    'Owner': 'Sid',
    'Everyone this app records. Switch, add, or remove someone.': 'Kulħadd li din l-app tirreġistra. Aqleb, żid jew neħħi lil xi ħadd.',
    # --- Day window (5.22) ---
    "Carried over from the night before": "Miġjub mil-lejla ta' qabel",
    # --- History, second card (5.24) ---
    'Calories': 'Kaloriji',
    'Sessions': 'Sessjonijiet',
    'Per session': 'Għal kull sessjoni',
    'Under the influence': 'Taħt l-effett tal-alkoħol',
    '%@ of the time': '%@ tal-ħin',
    'Days over limit': "Jiem 'il fuq mil-limitu",
    'Longest sober run': 'L-itwal sensiela bla alkoħol',
    'Favourite drink': 'Xarba favorita',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Wiri u lingwa",
    "Data": "Data",
    "Concentration": "Konċentrazzjoni",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Ħalli r-rata f'idejn il-mistoqsija dwar kemm-il darba tixrob, sakemm ma jkollokx kejl biex tqabbilha miegħu.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Stima, mhux kejl. Qatt tuża dan biex tiddeċiedi jekk tistax issuq.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Firxa stmata, mhux kejl. Qatt tuża dan biex tiddeċiedi jekk tistax issuq.',
    'How does the app calculate this?':
        'Kif tikkalkulah l-app?',
    'approximately %@ %@':
        'madwar %@ %@',
    'How it works':
        'Kif taħdem',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Qatt tuża dan biex tiddeċiedi jekk tistax issuq. L-app tistma, ma tkejjilx, u l-livell reali tiegħek jista’ jkun differenti ħafna.',
    'Why this app exists':
        'Għaliex teżisti din l-app',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink tgħinek tixrob b’mod aktar konxju u żżomm il-kontroll. Id-deċiżjoni tittieħed qabel it-tazza li jmiss, għalhekk l-app turik minn qabel fejn xarba oħra tieħu l-livell tiegħek u meta jilħaq il-quċċata.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Iżda mhix kwistjoni tal-lejla biss. Kull xarba li tirreġistra tmur fl-Istorja tiegħek, u għalhekk matul xhur u snin tara kemm tixrob, kemm-il darba u kemm jogħla l-livell tiegħek. Minn hemm joħorġu x-xejriet tiegħek, u wkoll id-direzzjoni li qed jieħdu – jekk l-affarijiet qed jitjiebu jew jiggravaw.',
    'How it calculates':
        'Kif tikkalkula',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'L-istima hija bbażata fuq il-metodu ta’ Widmark, użat mis-snin tletin biex jiġi stmat l-alkoħol fid-demm; l-app tuża verżjoni rfinata tiegħu.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Mill-piż, it-tul, l-età u s-sess tiegħek tikkalkula kemm fih ilma ġismek, għax hemm jinfirex l-alkoħol. Issegwi kull xarba għaliha: kemm kien fiha alkoħol, kemm xrobtha malajr u kemm kont kilt, għax dan jiddetermina kemm tiġi assorbita malajr.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Sadanittant il-fwied ikisser kull siegħa ammont bejn wieħed u ieħor kostanti; l-ammont tiegħek jiġi stmat minn kemm-il darba tixrob. Ir-riżultat huwa kurva, minuta b’minuta: fejn int issa, lejn fejn sejjer u meta terġa’ tasal għal żero.',
    'Details':
        'Dettalji',
    'Body water':
        'Ilma tal-ġisem',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Il-formula ta’ Watson (1980), mill-piż, it-tul, l-età u s-sess. Il-formula għan-nisa m’għandhiex terminu tal-età – karatteristika tal-formula, mhux żball. Il-volum tad-distribuzzjoni huwa l-ilma tal-ġisem diviż b’0.85, il-kontenut ta’ ilma fid-demm.',
    'Absorption':
        'Assorbiment',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Kull xarba għandha l-“istonku” tagħha. Fuq stonku vojt nofs l-alkoħol jiġi assorbit f’madwar 7 minuti, fuq stonku mimli f’madwar 21. Xarba li tixrobha bil-mod tidħol fl-istonku b’mod uniformi waqt li tixrobha.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Jagħti quċċata aktar baxxa u l-alkoħol jgħaddi aktar kmieni. Sorprendenti, iżda mkejjel: bl-ikel l-istonku jkisser parti mill-alkoħol qabel jiġi assorbit (l-app tuża 5, 10 u 15 fil-mija), u dak li qatt ma daħal m’hemmx għalfejn jitkisser.',
    'Elimination':
        'Eliminazzjoni',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Madwar 0.15 ‰ fis-siegħa (firxa ppubblikata 0.10–0.25), ogħla f’min jixrob regolarment għax l-enzimi tal-fwied jadattaw. Qrib iż-żero tonqos (kinetika ta’ Michaelis–Menten), u għalhekk il-kurva tinżel bil-mod minflok ma tieqaf f’daqqa.',
    'Computation':
        'Kalkolu',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Il-kurva ġejja minn simulazzjoni numerika b’riżoluzzjoni ta’ minuta.',
    'Why it is only an estimate':
        'Għaliex hija biss stima',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'L-app ma tkejjel xejn. Dak li turi huwa r-riżultat ta’ mudell b’valuri medji, u r-realtà tista’ tkun differenti. L-akbar inċertezza hija kemm tkisser l-alkoħol malajr: fil-firxa plawżibbli, dan waħdu jista’ jċaqlaq il-quċċata b’40 fil-mija u l-ħin meta jgħaddi l-alkoħol b’erba’ sigħat fl-istess serata.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Jgħoddu wkoll il-ġenetika, is-saħħa tal-fwied, il-mediċini, x’kilt, l-irqad u l-għeja – l-app ma taf xejn minn dawn. Valur eżatt jagħtih biss apparat iċċertifikat tat-test tan-nifs jew test tad-demm.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'In-numru xorta huwa utli. Jekk l-app tagħtik b’mod konsistenti valur ftit għoli jew ftit baxx, tiżbalja fl-istess direzzjoni kull filgħaxija, u għalhekk maż-żmien titgħallem xi jfisser valur partikolari għalik. Fil-Profil tista’ wkoll turi l-inċertezza tar-rata tal-eliminazzjoni: imbagħad tara firxa minflok numru wieħed.',
    'Tips':
        'Pariri',
    'Favourite drink in one tap':
        'Xarba favorita b’tektika waħda',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Agħżel favorita fil-Profil u l-buttuna fuq l-iskrin Dirett tirreġistraha b’tektika waħda.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Żidu mal-Lock Screen jew mal-Home Screen: tektika waħda tirreġistra l-favorita tiegħek. Sakemm ikun hemm alkoħol f’ġismek, juri wkoll il-livell tiegħek u d-direzzjoni tiegħu.',
    'How do I add it?':
        'Kif inżidu?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Għid “Hey Siri, LogMyDrink now” u Siri tirreġistra l-favorita tiegħek u tgħidlek lejn fejn sejra l-quċċata tiegħek. (Il-kmand jaħdem bl-Ingliż.)',
    'Looking back':
        'Ħarsa lura',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '“Ilbieraħ” fin-naħa ta’ fuq tal-iskrin Dirett jeħdok għall-ġurnata ta’ qabel b’tektika waħda; it-tab Storja turi x-xejriet tiegħek matul ġimgħat, xhur u snin.',
    'Logging later':
        'Reġistrazzjoni wara',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Jekk tirreġistra xarba wara, ressaq il-ħin lura bil-buttuni − u +; ġurnata li qbiżt tista’ timliha mill-veduta Jum fl-Istorja.',
    'One tap and done':
        'Tektika waħda u lest',
    'Your favourite from the Lock Screen':
        'Il-favorita tiegħek mil-Lock Screen',
    'Say it, don’t type it':
        'Għidha, tiktibhiex',
    'See your patterns':
        'Ara x-xejriet tiegħek',
    'Set what you drink most often and log it with a single tap.':
        'Agħżel x’tixrob l-aktar spiss u rreġistrah b’tektika waħda.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Tektika waħda fuq il-widget tirreġistra l-favorita tiegħek, mingħajr ma tfittex l-app. Filgħaxija juri wkoll il-livell tiegħek.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '“Hey Siri, LogMyDrink now” – Siri tirreġistra l-favorita tiegħek u tgħidlek lejn fejn sejra l-quċċata tiegħek.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'L-Istorja turi kemm tixrob u kemm jogħla l-livell tiegħek matul ġimgħat, xhur u snin, u f’liema direzzjoni qed tinbidel.',
    'Set favourite':
        'Agħżel favorita',
    'Add widget':
        'Żid widget',
    'Got it':
        'Fhimt',
    'Open History':
        'Iftaħ l-Istorja',
    'Don’t show again':
        'Turihx aktar',
    'Lock Screen':
        'Lock Screen',
    'Home Screen':
        'Home Screen',
    'Where':
        'Fejn',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Sakkar it-telefon, imbagħad żomm subgħajk fuq il-Lock Screen.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Agħfas Customize, imbagħad Lock Screen, u mbagħad ir-ringiela tal-widgets taħt l-arloġġ.',
    'Choose LogMyDrink, then tap Done.':
        'Agħżel LogMyDrink, imbagħad agħfas Done.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Żomm subgħajk fuq post vojt tal-Home Screen sakemm l-ikoni jibdew jitriegħdu.',
    'Tap Edit, then Add Widget.':
        'Agħfas Edit, imbagħad Add Widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Fittex LogMyDrink, agħżel daqs u agħfas Add Widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Tektika fuq il-widget tiftaħ l-app u tirreġistra x-xarba favorita tiegħek. Sakemm ikun hemm alkoħol f’ġismek, juri wkoll il-livell tiegħek u d-direzzjoni tiegħu.',
    'Add the widget':
        'Żid il-widget',
    'Show tips':
        'Uri pariri',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'L-aktar parir wieħed kuljum, meta tiftaħ l-app – imma qatt waqt li jkun hemm alkoħol f’ġismek.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'X’juri n-numru',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'In-numru huwa stima tal-konċentrazzjoni tal-alkoħol fid-demm tiegħek (bl-Ingliż BAC, blood alcohol concentration): kemm hemm alkoħol fid-demm tiegħek.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'F’kull elf (‰) huma grammi ta’ alkoħol għal kull litru ta’ demm: 0.5 ‰ tfisser nofs gramm f’kull litru. F’perċentwal huma grammi għal kull 100 millilitru, għalhekk l-istess livell jagħti numru għaxar darbiet iżgħar: 0.5 ‰ huwa 0.05 fil-mija. Tista’ taqleb bejniethom f’Profil › Wiri u lingwa.',
    'The curve shows the same level over time, minute by minute.':
        'Il-kurva turi l-istess livell maż-żmien, minuta b’minuta.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Il-‰ huma grammi ta’ alkoħol għal kull litru ta’ demm, il-perċentwal grammi għal kull 100 millilitru: 0.5 ‰ huwa 0.05 fil-mija.',
}
