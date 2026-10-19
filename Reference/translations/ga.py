"""
Irish.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Sa mhíle",
    "Percent": "Faoin gcéad",

    # --- DrinkCatalog: drink types ---
    "Beer": "Beoir",
    "Wine": "Fíon",
    "Champagne": "Súilíneach",
    "Shot": "Shot",
    "Cocktail": "Manglam",
    "Custom": "Saincheaptha",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Goile folamh",
    "Moderately full": "Measartha lán",
    "Full stomach": "Goile lán",
    "Empty": "Folamh",
    "Moderate": "Measartha",
    "Full": "Lán",
    "Fast absorption, higher and earlier peak.":
        "Ionsú tapa, buaic níos airde agus níos luaithe.",
    "Moderate absorption.": "Ionsú measartha.",
    "Slow absorption, lower and later peak.": "Ionsú mall, buaic níos ísle agus níos déanaí.",

    # --- DrinkingFrequency ---
    "Rarely": "Is annamh",
    "A few times a month": "Cúpla uair sa mhí",
    "Several times a week": "Roinnt uaireanta sa tseachtain",
    "Almost daily": "Beagnach gach lá",
    "A few occasions a year": "Cúpla ócáid sa bhliain",
    "Social drinking": "Ól sóisialta",
    "Weekly routine": "Gnás seachtainiúil",
    "Daily or nearly daily": "Gach lá nó beagnach gach lá",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Am",
    "Level": "Leibhéal",
    "Lower": "Íochtar",
    "Upper": "Uachtar",
    "Lower estimate": "Meastachán íochtair",
    "Upper estimate": "Meastachán uachtair",
    "Personal limit": "Teorainn phearsanta",
    "Drink": "Deoch",

    # --- BACChartView ---
    "Expected peak around %@": "Táthar ag súil le buaic thart ar %@",
    "Peaked around %@": "Bhí an bhuaic thart ar %@",
    "No active session": "Níl seisiún gníomhach ann",
    "Still rising": "Ag ardú fós",
    "YOUR LIMIT %@": "DO THEORAINN %@",
    "possible range": "raon féideartha",

    # --- Live screen: the day with nothing on it ---
    "Live": "Beo",
    "Nothing logged today": "Níor logáladh aon rud inniu",
    "Add a drink when you have one.": "Cuir deoch leis nuair a bhíonn ceann agat.",

    # --- Tabs and history ---
    "History": "Stair",
    "No past sessions yet": "Níl aon seisiún caite ann fós",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Taispeántar seisiún anseo a luaithe atá deireadh leis — nuair atá do leibhéal glanta "
        "agus cúpla uair an chloig imithe thart.",
    "%@ drinks": "Deochanna: %@",
    "peak": "buaic",
    "Started": "Thosaigh",
    "Lasted": "Mhair",
    "Duration": "Fad",
    "Sober around": "Stuama timpeall",
    "Sober at": "Stuama",
    "Remaining": "Fágtha",
    "next day": "an lá dár gcionn",
    "previous day": "an lá roimhe",
    "%@ days later": "%@ lá ina dhiaidh",
    "%@ days earlier": "%@ lá roimhe",
    "Calculated with your profile at the time": "Ríofa le do phróifíl mar a bhí ag an am",

    # --- TodayView ---
    "Profile": "Próifíl",
    "Drinks": "Deochanna",
    "Units": "Aonaid",
    "Drinks this session": "Deochanna sa seisiún seo",
    "Add drink": "Cuir deoch leis",

    # --- Editing an already logged drink ---
    "Edit drink": "Cuir deoch in eagar",
    "Save changes": "Sábháil na hathruithe",
    "With this": "Leis an gceann seo",
    "Delete": "Scrios",
    "tap to edit · swipe to delete": "tapáil chun eagrú · svaidhpeáil chun scriosadh",

    # --- Drinking pace ---
    "How fast": "Cé chomh tapa",
    "In one go": "D'aon iarraidh",
    "Counts as a single swallow — the steepest possible rise.":
        "Áirítear é mar bholgam amháin — an t-ardú is géire is féidir.",
    "A quick drink. The level climbs fast.": "Deoch sciobtha. Ardaíonn an leibhéal go tapa.",
    "A normal pace.": "Luas gnách.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Á ól go mall. Ardú i bhfad níos míne don mhéid céanna alcóil.",

    # --- AddDrinkSheet ---
    "Cancel": "Cealaigh",
    "Now": "Anois",
    "Projected peak": "Buaic mheasta",
    "Peak at": "Buaic ag",
    "Clears": "Glanann",
    "This would cross your limit": "Rachadh sé seo thar do theorainn",
    "Around %@, for up to %@.": "Timpeall %@, ar feadh suas le %@.",
    "This might cross your limit": "D'fhéadfadh sé seo dul thar do theorainn",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Le meitibileacht níos moille, rachadh; le ceann níos tapúla, ní rachadh. Sin "
        "éiginnteacht an mheastacháin.",
    "Type": "Cineál",
    "Amount": "Méid",
    "Strength": "Neart",
    "%@ units": "Aonaid: %@",
    "%@ g alcohol": "%@ g alcóil",
    "Stomach": "Goile",
    "When": "Cathain",
    "Done": "Déanta",
    "Add": "Cuir leis",

    # --- ProfileSheet ---
    "Male": "Fireann",
    "Female": "Baineann",
    "Sex": "Gnéas",
    "Weight": "Meáchan",
    "Height": "Airde",
    "Age": "Aois",
    "kg": "kg",
    "cm": "cm",
    "yrs": "bl",
    "Body": "Corp",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Tagann uisce iomlán an choirp ó chothromóidí Watson, a shocraíonn an toirt ina "
        "ndáiltear an t-alcól.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Tagann uisce iomlán an choirp ó chothromóidí Watson, a shocraíonn an toirt ina "
        "ndáiltear an t-alcól. Níl an aois san áireamh sa chothromóid do mhná, agus mar sin ní "
        "bheidh tionchar ag athrú uirthi ar an toradh.",
    "Drinking frequency": "Minicíocht óil",
    "How often do you drink?": "Cé chomh minic a ólann tú?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Seo mar a dhéanaimid do ráta glanta a mheas. Spreagann ól rialta conair CYP2E1 an ae, agus mar sin glanann daoine a ólann go minic alcól níos tapúla. Seo an pointe is laige sa tsamhail, agus sin an fáth gur féidir leat a shocrú faoi Taispeáint agus teanga cé mhéad den éiginnteacht sin a thaispeánann an aip duit.",
    "Your limit": "Do theorainn",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "D'uimhir thagartha féin, ní teorainn dhlíthiúil. Insíonn an aip duit nuair a "
        "thabharfadh deoch bheartaithe thairsti thú, agus cé chomh fada a d'fhanfá os a cionn.",
    "Calculated values": "Luachanna ríofa",
    "Total body water": "Uisce iomlán an choirp",
    "Distribution volume": "Toirt dáileacháin",
    "Widmark factor": "Fachtóir Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Bíonn fachtóir Widmark thart ar 0.68 d'fhir agus 0.55 do mhná de ghnáth. Má tá do "
        "cheannsa i bhfad ó sin, is fiú na luachanna thuas a sheiceáil.",
    "Elimination rate": "Ráta glanta",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Cé chomh tapa a ghlanann d'ae an t-alcól a luaithe atá sé ionsúite — fána an taoibh "
        "íslithigh den chuar.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Imíonn an t-alcól ag méid réasúnta seasta in aghaidh na huaire seachas mar chéatadán, "
        "toisc go bhfuil an einsím a bhriseann síos é ag obair ar a lánacmhainn cheana féin ag "
        "beagnach aon leibhéal. Sin an fáth a bhfuil rialacha ordóige ar nós “deoch amháin san "
        "uair” ann ar chor ar bith.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Leis an socrú seo, glanann %@ i gceann thart ar %@. Titeann beagnach gach duine idir "
        "%@ in aghaidh na huaire.",
    "How to find yours": "Conas do cheann féin a aimsiú",
    "With a breathalyser": "Le hanálaitheoir",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Séid faoi dhó, uair an chloig ar a laghad eatarthu, ar an taobh íslitheach — dhá uair "
        "an chloig nó níos mó tar éis do dheoch dheireanach, gan aon rud eatarthu. Bain an "
        "dara léamh ón gcéad cheann agus roinn ar líon na n-uaireanta eatarthu.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Mar shampla, %@ agus ansin %@ dhá uair an chloig ina dhiaidh sin: sin %@ in aghaidh "
        "na huaire.",
    "Without one": "Gan ceann",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Insíonn an aip duit cathain a bhfuil sí ag súil go nglanfaidh tú. Má bhíonn tú ar ais "
        "mar is gnách go hiontaofa i bhfad roimhe sin, tá do ráta níos airde ná an socrú — "
        "ardaigh céim amháin é agus coinnigh súil air ar feadh cúpla seisiún. Má thógann sé "
        "níos faide ná mar a tuaradh, ísligh céim amháin é.",
    "What moves it": "Cad a athraíonn é",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Ardaíonn ól rialta é: spreagtar einsím an ae a dhéanann an obair tríd an úsáid. Bíonn "
        "sé beagán níos airde i mná ar an meán freisin, agus níos ísle ar ghoile folamh nó le "
        "fadhbanna ae.",
    "Uncertainty": "Éiginnteacht",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Ag nialas is uimhir aonair gach figiúr — an meastachán is fearr atá ag an aip. Os "
        "cionn nialais taispeántar na figiúirí céanna mar raonta, agus leathnaíonn an banda ar "
        "an gcairt dá réir.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Is fusa foghlaim ó uimhir amháin: le himeacht ama tuigfidh tú cén chaoi a mbraitheann "
        "do 0.6 féin. Is é an raon an freagra is litriúla, mar tá an ráta éiginnte go deimhin. "
        "Tá an dá rud inchosanta — is fútsa atá sé.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Is é ± %@ in aghaidh na huaire an scaipeadh a mholann do mhinicíocht óil.",
    "Rate": "Ráta",
    "Range": "Raon",
    "Advanced": "Ardroghanna",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Roinnt daoine",
    "History trends": "Treochtaí staire",
    "Week": "Seachtain",
    "Month": "Mí",
    "Year": "Bliain",
    "Sober days": "Laethanta gan alcól",
    "Change": "Athrú",
    "before records": "roimh thús na dtaifead",
    "See further back": "Féach níos faide siar",
    "Weeks, months and years side by side — and every evening older than seven days.": "Seachtainí, míonna agus blianta taobh le taobh – agus gach oíche níos sine ná seacht lá.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Tá gach rud a logáil tú sábháilte cheana féin. Ní dhéanann an díghlasáil ach é a thaispeáint.",
    "Coming soon": "Ag teacht go luath",
    "Today": "Inniu",
    "Day": "Lá",
    "Yesterday": "Inné",
    "No drinks on this day": "Gan deochanna an lá seo",
    "Trend": "Treocht",
    "day": "lá",
    "Smoothing": "Smúdáil",
    "%@ sessions": "%@ ócáid",
    "No data before %@": "Gan sonraí roimh %@",
    "vs.": "i gcomparáid le",
    "Grams": "Graim",
    "Grams of alcohol": "Graim alcóil",
    "Standard units": "Aonaid chaighdeánacha",
    "Unit size": "Méid an aonaid",
    "Automatic": "Uathoibríoch",
    "UK": "An Ríocht Aontaithe",
    "Nordic countries": "Tíortha Nordacha",
    "US standard drink": "Deoch chaighdeánach SAM",
    "WHO, most of Europe": "EDS, an chuid is mó den Eoraip",
    "Period": "Tréimhse",
    "Switch person": "Athraigh duine",
    "Add person": "Cuir duine leis",
    "New person": "Duine nua",
    "You": "Tusa",
    "Name": "Ainm",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Athraíonn na ceithre cinn an cuar, agus mar sin ní féidir buille faoi thuairim a "
        "thabhairt faoi cheann ar bith acu do dhuine eile.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Is féidir a dteorainn féin agus na socruithe míne a athrú níos déanaí ar an gcluaisín "
        "Próifíl, fad is iad an duine roghnaithe.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Mearchur",
    "Choose a favourite drink": "Roghnaigh deoch is fearr leat",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Roghnaigh an deoch a ordaíonn tú de ghnáth, agus logálfaidh cnaipe ar an scáileán Beo "
        "í le tapáil amháin.",
    "This is your quick-add drink": "Seo do dheoch mhearchuir",
    "Set as my quick-add drink": "Socraigh mar mo dheoch mhearchuir",
    "This is now your usual": "Seo do ghnáthdheoch anois",
    "Remove favourite": "Bain an deoch is fearr leat",
    "Always add this one": "Cuir an ceann seo leis i gcónaí",
    "Logs it straight away, without opening anything.":
        "Logálann sé láithreach é, gan aon rud a oscailt.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Logálann tapáil amháin ar an scáileán Beo é seo, agus an bhuaic mheasta ar an "
        "gcnaipe. Tagann an méid atá i do ghoile ón deoch roimhe, agus is féidir é a cheartú "
        "díreach ina dhiaidh sin.",
    "Peak %@": "Buaic %@",
    "%@ added": "%@ curtha leis",
    "Save": "Sábháil",
    "Undo": "Cuir ar ceal",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Cúltaca",
    "Export a backup": "Easpórtáil cúltaca",
    "Import a backup": "Iompórtáil cúltaca",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Coinníonn cúltaca gach duine, gach ócáid agus gach deoch. Cuireann an iompórtáil leis "
        "an méid atá in easnamh — ní athraíonn agus ní bhaineann sí riamh aon rud atá anseo "
        "cheana.",
    "Import this backup?": "An cúltaca seo a iompórtáil?",
    "Import": "Iompórtáil",
    "Everything in this backup is already here.": "Tá gach rud sa chúltaca seo anseo cheana.",
    "Import finished": "Iompórtáil críochnaithe",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Teanga",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Osclaíonn sé seo an aip seo sna Socruithe, áit a socraíonn “Teanga Roghnaithe” teanga "
        "na haipe féin — fanann teanga an chórais mar atá. Atosaíonn iOS an aip nuair a "
        "athraíonn tú í.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Níorbh fhéidir iompórtáil",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Ní cúltaca LogMyDrink é an comhad seo, nó tá sé damáistithe.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Rinneadh an cúltaca seo le leagan níos nuaí de LogMyDrink. Nuashonraigh an aip agus "
        "bain triail eile as.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Cuirfidh sé seo %@ ócáid, %@ deoch agus %@ iomlán míosúil leis. Ní athrófar agus ní bhainfear aon rud atá anseo cheana.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Cuireadh %@ ócáid, %@ deoch agus %@ iomlán míosúil leis.',
    'months as totals': 'mí mar iomláin amháin',
    'by month only': 'de réir míosa amháin',
    'monthly total': 'iomlán míosúil',
    'No daily records for this day': 'Níl aon taifead laethúil don lá seo',
    'Monthly total: %@': 'Iomlán míosúil: %@',
    'A dry month': 'Mí thirim',

    # --- RemovePersonSection ---
    'Remove %@?': 'Bain %@?',
    'Remove': 'Bain',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Scriosann sé %@ ócáid, %@ deoch agus %@ iomlán míosúil. Ní féidir é seo a chealú.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Scriosann sé %@ ócáid agus %@ deoch. Ní féidir é seo a chealú.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Svaidhpeáil ar chlé ar aoi chun é a bhaint le gach rud a taifeadadh faoi. Ní féidir tusa a bhaint.',
    'People': 'Daoine',
    'Owner': 'Úinéir',
    'Everyone this app records. Switch, add, or remove someone.': 'Gach duine a thaifeadann an aip seo. Athraigh, cuir leis nó bain duine.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Tugtha anall ón oíche roimhe',
    # --- History, second card (5.24) ---
    'Calories': 'Calraí',
    'Sessions': 'Ócáidí',
    'Per session': 'In aghaidh na hócáide',
    'Under the influence': 'Faoi thionchar',
    '%@ of the time': '%@ den am',
    'Days over limit': 'Laethanta os cionn na teorann',
    'Longest sober run': 'An tréimhse stuama is faide',
    'Favourite drink': 'An deoch is fearr leat',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Taispeáint agus teanga",
    "Data": "Sonraí",
    "Concentration": "Tiúchan",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Fág an ráta faoin gceist faoi mhinicíocht, mura bhfuil tomhas agat le hé a chur i gcomparáid leis.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Meastachán, ní tomhas. Ná húsáid é seo riamh chun cinneadh a dhéanamh an féidir leat tiomáint.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Raon measta, ní tomhas. Ná húsáid é seo riamh chun cinneadh a dhéanamh an féidir leat tiomáint.',
    'How does the app calculate this?':
        'Conas a ríomhann an aip é seo?',
    'approximately %@ %@':
        'timpeall %@ %@',
    'How it works':
        'Conas a oibríonn sé',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Ná húsáid é seo riamh chun cinneadh a dhéanamh an féidir leat tiomáint. Déanann an aip meastachán, ní thomhaiseann sí, agus d’fhéadfadh do leibhéal iarbhír a bheith an-difriúil.',
    'Why this app exists':
        'Cén fáth a bhfuil an aip seo ann',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'Cabhraíonn LogMyDrink leat ól ar bhealach níos feasaí agus smacht a choinneáil. Déantar an cinneadh roimh an gcéad ghloine eile, mar sin taispeánann an aip roimh ré cá dtabharfadh deoch eile do leibhéal agus cathain a bheadh sé ag a bhuaic.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Ach ní bhaineann sé leis an oíche anocht amháin. Téann gach deoch a chláraíonn tú isteach i do Stair, mar sin thar mhíonna agus bhlianta feiceann tú cé mhéad, cé chomh minic agus cé chomh hard a ólann tú. Tagann do phatrúin chun solais as sin, chomh maith leis an treo ina bhfuil siad ag bogadh – an bhfuil cúrsaí ag feabhsú nó ag dul in olcas.',
    'How it calculates':
        'Conas a ríomhann sí',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Tá an meastachán bunaithe ar mhodh Widmark, a úsáidtear ó na 1930idí chun alcól san fhuil a mheas; úsáideann an aip leagan scagtha de.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Ó do mheáchan, d’airde, d’aois agus do ghnéas ríomhann sí cé mhéad uisce atá i do chorp, mar is ann a scaipeann an t-alcól. Leanann sí gach deoch ar leith: cé mhéad alcóil a bhí inti, cé chomh tapa a d’ól tú í agus cé mhéad a bhí ite agat, mar socraíonn sé sin cé chomh tapa a ionsúitear í.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Idir an dá linn, briseann d’ae síos méid atá thart ar sheasmhach gach uair an chloig; meastar do mhéid féin ón minicíocht a ólann tú. Is é an toradh cuar, nóiméad ar nóiméad: cá bhfuil tú anois, cá bhfuil tú ag dul agus cathain a bheidh tú ar ais ag nialas.',
    'Details':
        'Sonraí',
    'Body water':
        'Uisce coirp',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Foirmle Watson (1980), ó mheáchan, airde, aois agus gnéas. Níl aois i bhfoirmle na mban – airí den fhoirmle é sin, ní fabht. Is é an toirt dáilte an t-uisce coirp roinnte ar 0.85, cion uisce na fola.',
    'Absorption':
        'Ionsú',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Tá a “goile” féin ag gach deoch. Ar ghoile folamh ionsúitear leath an alcóil i thart ar 7 nóiméad, ar ghoile lán i thart ar 21. Téann deoch a bhíonn tú a sú isteach sa ghoile go cothrom fad is atá tú á hól.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Tugann sé buaic níos ísle agus nialas níos luaithe. Ionadh, ach tomhaiste: le bia briseann an goile cuid den alcól síos sula n-ionsúitear é (úsáideann an aip 5, 10 agus 15 faoin gcéad), agus ní gá an méid nár tháinig isteach riamh a bhriseadh síos.',
    'Elimination':
        'Díothú',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Thart ar 0.15 ‰ san uair (raon foilsithe 0.10–0.25), níos airde i measc daoine a ólann go rialta toisc go n-oiriúnaíonn einsímí an ae. Gar do nialas moillíonn sé (cinéitic Michaelis–Menten), mar sin éiríonn an cuar níos réidhe in ionad stopadh go tobann.',
    'Computation':
        'Ríomh',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Tagann an cuar ó insamhladh uimhriúil ag taifeach nóiméid.',
    'Why it is only an estimate':
        'Cén fáth nach bhfuil ann ach meastachán',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Ní thomhaiseann an aip aon rud. Is é an rud a thaispeánann sí toradh múnla a úsáideann meánluachanna, agus d’fhéadfadh an réaltacht a bheith difriúil. Is é an rud is mó nach eol cé chomh tapa a bhriseann tú alcól síos: laistigh den raon sochreidte, d’fhéadfadh sé sin leis féin an bhuaic a bhogadh 40 faoin gcéad agus an nialas ceithre huaire an chloig ar an oíche chéanna.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Bíonn tionchar ag géineolaíocht, sláinte an ae, cógais, an bia a d’ith tú, codladh agus tuirse freisin – níl aon cheann díobh sin ar eolas ag an aip. Ní thugann ach anáileadán deimhnithe nó tástáil fola luach beacht.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Tá an uimhir úsáideach mar sin féin. Má léann an aip beagán ró-ard nó ró-íseal duit go comhsheasmhach, bíonn sí mícheart sa treo céanna gach oíche, mar sin le himeacht ama foghlaimíonn tú cad a chiallaíonn luach áirithe duitse. I bPróifíl is féidir leat éiginnteacht an ráta díothaithe a thaispeáint freisin: feicfidh tú raon ansin in ionad uimhir amháin.',
    'Tips':
        'Leideanna',
    'Favourite drink in one tap':
        'Deoch is fearr leat le tapáil amháin',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Socraigh deoch is fearr leat i bPróifíl agus cláróidh an cnaipe ar Beo í le tapáil amháin.',
    'Widget':
        'Giuirléid',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Cuir le do Scáileán Glasála nó le do Scáileán Baile í: cláraíonn tapáil amháin an deoch is fearr leat. Fad is atá alcól i do chorp, taispeánann sí do leibhéal agus a threo freisin.',
    'How do I add it?':
        'Conas a chuirim leis í?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Abair “Hey Siri, LogMyDrink now” agus cláróidh Siri an deoch is fearr leat, agus inseoidh sí duit cá bhfuil do bhuaic ag dul.',
    'Looking back':
        'Ag féachaint siar',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        'Tugann “Inné” ag barr Beo chuig an lá roimhe tú le tapáil amháin; taispeánann an cluaisín Stair do phatrúin thar sheachtainí, mhíonna agus bhlianta.',
    'Logging later':
        'Clárú níos déanaí',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Má chláraíonn tú deoch ina dhiaidh sin, cuir an t-am siar leis na cnaipí − agus +; is féidir lá a cailleadh a líonadh ón amharc Lá sa Stair.',
    'One tap and done':
        'Tapáil amháin agus déanta',
    'Your favourite from the Lock Screen':
        'An deoch is fearr leat ón Scáileán Glasála',
    'Say it, don’t type it':
        'Abair é, ná clóscríobh é',
    'See your patterns':
        'Féach ar do phatrúin',
    'Set what you drink most often and log it with a single tap.':
        'Socraigh cad a ólann tú is minice agus cláraigh é le tapáil amháin.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Cláraíonn tapáil amháin ar an ngiuirléid an deoch is fearr leat, gan an aip a chuardach. San oíche taispeánann sí do leibhéal freisin.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '“Hey Siri, LogMyDrink now” – cláraíonn Siri an deoch is fearr leat agus insíonn sí duit cá bhfuil do bhuaic ag dul.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Taispeánann an Stair cé mhéad agus cé chomh hard a ólann tú thar sheachtainí, mhíonna agus bhlianta, agus cén treo ina bhfuil sé ag athrú.',
    'Set favourite':
        'Socraigh an ceann is fearr leat',
    'Add widget':
        'Cuir giuirléid leis',
    'Got it':
        'Tuigim',
    'Open History':
        'Oscail an Stair',
    'Later':
        'Níos déanaí',
    'Don’t show again':
        'Ná taispeáin arís',
    'Lock Screen':
        'Scáileán Glasála',
    'Home Screen':
        'Scáileán Baile',
    'Where':
        'Cá háit',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Glasáil do iPhone, ansin coinnigh do mhéar ar an Scáileán Glasála.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Tapáil Customize, ansin Lock Screen, ansin an tsraith giuirléidí faoin gclog.',
    'Choose LogMyDrink, then tap Done.':
        'Roghnaigh LogMyDrink, ansin tapáil Done.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Coinnigh do mhéar ar spás folamh ar an Scáileán Baile go dtí go dtosaíonn na deilbhíní ag crith.',
    'Tap Edit, then Add Widget.':
        'Tapáil Edit, ansin Add Widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Cuardaigh LogMyDrink, roghnaigh méid agus tapáil Add Widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Osclaíonn tapáil ar an ngiuirléid an aip agus cláraíonn sí an deoch is fearr leat. Fad is atá alcól i do chorp, taispeánann sí do leibhéal agus a threo freisin.',
    'Add the widget':
        'Cuir an ghiuirléid leis',
    'Show tips':
        'Taispeáin leideanna',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Leid amháin sa lá ar a mhéad, nuair a osclaíonn tú an aip – riamh fad is atá alcól i do chorp.',
}
