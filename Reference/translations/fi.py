"""
Finnish.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promille",
    "Percent": "Prosentti",

    # --- DrinkCatalog: drink types ---
    "Beer": "Olut",
    "Wine": "Viini",
    "Champagne": "Kuohuviini",
    "Shot": "Shotti",
    "Cocktail": "Cocktail",
    "Custom": "Oma",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Tyhjä vatsa",
    "Moderately full": "Kohtalaisen täysi",
    "Full stomach": "Täysi vatsa",
    "Empty": "Tyhjä",
    "Moderate": "Kohtalainen",
    "Full": "Täysi",
    "Fast absorption, higher and earlier peak.":
        "Nopea imeytyminen, korkeampi ja aikaisempi huippu.",
    "Moderate absorption.": "Kohtalainen imeytyminen.",
    "Slow absorption, lower and later peak.":
        "Hidas imeytyminen, matalampi ja myöhempi huippu.",

    # --- DrinkingFrequency ---
    "Rarely": "Harvoin",
    "A few times a month": "Muutaman kerran kuukaudessa",
    "Several times a week": "Useita kertoja viikossa",
    "Almost daily": "Lähes päivittäin",
    "A few occasions a year": "Muutaman kerran vuodessa",
    "Social drinking": "Seurustelujuominen",
    "Weekly routine": "Viikoittainen tapa",
    "Daily or nearly daily": "Päivittäin tai lähes päivittäin",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Aika",
    "Level": "Taso",
    "Lower": "Alempi",
    "Upper": "Ylempi",
    "Lower estimate": "Alempi arvio",
    "Upper estimate": "Ylempi arvio",
    "Personal limit": "Oma raja",
    "Drink": "Juoma",

    # --- BACChartView ---
    "Expected peak around %@": "Huippu odotettavissa noin %@",
    "Peaked around %@": "Huippu oli noin %@",
    "No active session": "Ei aktiivista juomakertaa",
    "Still rising": "Yhä nousussa",
    "YOUR LIMIT %@": "OMA RAJASI %@",
    "possible range": "mahdollinen vaihteluväli",

    # --- Live screen: the day with nothing on it ---
    "Live": "Live",
    "Nothing logged today": "Ei kirjauksia tänään",
    "Add a drink when you have one.": "Lisää juoma, kun juot sellaisen.",

    # --- Tabs and history ---
    "History": "Historia",
    "No past sessions yet": "Ei vielä aiempia juomakertoja",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Juomakerta ilmestyy tähän, kun se on päättynyt – kun tasosi on nollautunut ja muutama "
        "tunti on kulunut.",
    "%@ drinks": "%@ juomaa",
    "peak": "huippu",
    "Started": "Alkoi",
    "Lasted": "Kesto",
    "Duration": "Kesto",
    "Sober around": "Selvin päin noin",
    "Sober at": "Selvin päin",
    "Remaining": "Jäljellä",
    "next day": "seuraavana päivänä",
    "previous day": "edellisenä päivänä",
    "%@ days later": "%@ päivää myöhemmin",
    "%@ days earlier": "%@ päivää aiemmin",
    "Calculated with your profile at the time": "Laskettu silloisella profiilillasi",

    # --- TodayView ---
    "Profile": "Profiili",
    "Drinks": "Juomat",
    "Units": "Annokset",
    "Drinks this session": "Tämän juomakerran juomat",
    "Add drink": "Lisää juoma",

    # --- Editing an already logged drink ---
    "Edit drink": "Muokkaa juomaa",
    "Save changes": "Tallenna muutokset",
    "With this": "Tämän kanssa",
    "Delete": "Poista",
    "tap to edit · swipe to delete": "napauta muokataksesi · pyyhkäise poistaaksesi",

    # --- Drinking pace ---
    "How fast": "Kuinka nopeasti",
    "In one go": "Kerralla",
    "Counts as a single swallow — the steepest possible rise.":
        "Lasketaan yhdeksi kulaukseksi – jyrkin mahdollinen nousu.",
    "A quick drink. The level climbs fast.": "Nopeasti juotu. Taso nousee nopeasti.",
    "A normal pace.": "Tavallinen tahti.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Siemailtu hitaasti. Paljon loivempi nousu samalla alkoholimäärällä.",

    # --- AddDrinkSheet ---
    "Cancel": "Peruuta",
    "Now": "Nyt",
    "Projected peak": "Ennustettu huippu",
    "Peak at": "Huippu klo",
    "Clears": "Nollautuu",
    "This would cross your limit": "Tämä ylittäisi rajasi",
    "Around %@, for up to %@.": "Noin %@, enintään %@ ajan.",
    "This might cross your limit": "Tämä saattaa ylittää rajasi",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Hitaammalla aineenvaihdunnalla kyllä, nopeammalla ei. Se on arvion epävarmuus.",
    "Type": "Tyyppi",
    "Amount": "Määrä",
    "Strength": "Vahvuus",
    "%@ units": "%@ annosta",
    "%@ g alcohol": "%@ g alkoholia",
    "Stomach": "Vatsa",
    "When": "Milloin",
    "Done": "Valmis",
    "Add": "Lisää",

    # --- ProfileSheet ---
    "Male": "Mies",
    "Female": "Nainen",
    "Sex": "Sukupuoli",
    "Weight": "Paino",
    "Height": "Pituus",
    "Age": "Ikä",
    "kg": "kg",
    "cm": "cm",
    "yrs": "v",
    "Body": "Keho",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Kehon kokonaisvesimäärä lasketaan Watsonin yhtälöillä, jotka määrittävät tilavuuden, "
        "johon alkoholi jakautuu.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Kehon kokonaisvesimäärä lasketaan Watsonin yhtälöillä, jotka määrittävät tilavuuden, "
        "johon alkoholi jakautuu. Naisten yhtälö ei sisällä ikää, joten sen muuttaminen ei "
        "vaikuta tulokseen.",
    "Drinking frequency": "Juomistiheys",
    "How often do you drink?": "Kuinka usein juot?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Näin arvioimme palamisnopeutesi. Säännöllinen juominen indusoi maksan CYP2E1-reittiä, joten usein juovilla alkoholi palaa nopeammin. Tämä on mallin heikoin kohta, ja siksi voit määrittää kohdassa Esitystapa ja kieli, kuinka paljon tästä epävarmuudesta sovellus näyttää sinulle.",
    "Your limit": "Rajasi",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Oma viitearvosi, ei lakisääteinen raja. Sovellus kertoo, jos suunniteltu juoma veisi "
        "sinut sen yli ja kuinka kauan pysyisit sen yläpuolella.",
    "Calculated values": "Lasketut arvot",
    "Total body water": "Kehon kokonaisvesimäärä",
    "Distribution volume": "Jakautumistilavuus",
    "Widmark factor": "Widmarkin kerroin",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Widmarkin kerroin on tyypillisesti noin 0,68 miehillä ja 0,55 naisilla. Jos omasi "
        "poikkeaa siitä paljon, yllä olevat arvot kannattaa tarkistaa.",
    "Elimination rate": "Palamisnopeus",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Kuinka nopeasti maksasi polttaa alkoholin sen imeydyttyä – käyrän laskevan puolen "
        "jyrkkyys.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkoholi poistuu suunnilleen kiinteänä määränä tunnissa eikä prosenttiosuutena, koska "
        "sitä hajottava entsyymi toimii jo täydellä teholla lähes millä tahansa tasolla. Juuri "
        "siksi nyrkkisäännöt, kuten ”yksi annos tunnissa”, ovat ylipäätään olemassa.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Tällä asetuksella tason %@ poistuminen kestää noin %@. Lähes kaikilla nopeus on "
        "välillä %@ tunnissa.",
    "How to find yours": "Näin löydät omasi",
    "With a breathalyser": "Alkometrillä",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Puhalla kahdesti vähintään tunnin välein tason laskiessa – vähintään kaksi tuntia "
        "viimeisen juoman jälkeen, äläkä juo välillä mitään. Vähennä jälkimmäinen lukema "
        "ensimmäisestä ja jaa erotus mittausten välisillä tunneilla.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Esimerkiksi %@ ja kaksi tuntia myöhemmin %@ tekee %@ tunnissa.",
    "Without one": "Ilman alkometriä",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Sovellus kertoo, milloin tasosi arviolta nollautuu. Jos olet toistuvasti normaalissa "
        "kunnossa selvästi ennen sitä, palamisnopeutesi on asetusta suurempi – nosta sitä "
        "pykälän verran ja seuraa tilannetta muutaman juomakerran ajan. Jos nollautuminen "
        "kestää ennustettua kauemmin, laske sitä.",
    "What moves it": "Mikä siihen vaikuttaa",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Säännöllinen juominen nostaa sitä: työn tekevä maksaentsyymi indusoituu käytöstä. Se "
        "on myös keskimäärin hieman korkeampi naisilla ja matalampi tyhjällä vatsalla tai "
        "maksavaivojen yhteydessä.",
    "Uncertainty": "Epävarmuus",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Nollassa jokainen luku on yksi arvo – sovelluksen paras arvio. Nollan yläpuolella "
        "samat luvut näytetään vaihteluväleinä, ja kuvaajan vyöhyke levenee vastaavasti.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Yhteen lukuun on helpompi oppia suhtautumaan: ajan myötä huomaat, miltä oma 0,6 "
        "tuntuu. Vaihteluväli on kirjaimellisempi vastaus, koska palamisnopeus on todella "
        "epävarma. Molemmat ovat perusteltuja – valinta on sinun.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Juomistiheytesi perusteella hajonta on ± %@ tunnissa.",
    "Rate": "Nopeus",
    "Range": "Vaihteluväli",
    "Advanced": "Lisäasetukset",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Useita henkilöitä",
    "History trends": "Historian trendit",
    "Week": "Viikko",
    "Month": "Kuukausi",
    "Year": "Vuosi",
    "Sober days": "Alkoholittomat päivät",
    "Change": "Muutos",
    "before records": "ennen kirjausten alkua",
    "See further back": "Katso kauemmas taaksepäin",
    "Weeks, months and years side by side — and every evening older than seven days.": "Viikot, kuukaudet ja vuodet rinnakkain – ja jokainen yli seitsemän päivää vanha ilta.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Kaikki kirjaamasi on jo tallennettu. Avaaminen vain näyttää sen.",
    "Coming soon": "Tulossa pian",
    "Today": "Tänään",
    "Day": "Päivä",
    "Yesterday": "Eilen",
    "No drinks on this day": "Ei juomia tänä päivänä",
    "Trend": "Trendi",
    "day": "päivä",
    "Smoothing": "Tasoitus",
    "%@ sessions": "%@ kertaa",
    "No data before %@": "Ei tietoja ennen %@",
    "vs.": "vrt.",
    "Grams": "Grammat",
    "Grams of alcohol": "Alkoholigrammat",
    "Standard units": "Vakioannokset",
    "Unit size": "Annoksen koko",
    "Automatic": "Automaattinen",
    "UK": "Iso-Britannia",
    "Nordic countries": "Pohjoismaat",
    "US standard drink": "Yhdysvaltain vakioannos",
    "WHO, most of Europe": "WHO, suurin osa Eurooppaa",
    "Period": "Jakso",
    "Switch person": "Vaihda henkilöä",
    "Add person": "Lisää henkilö",
    "New person": "Uusi henkilö",
    "You": "Sinä",
    "Name": "Nimi",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Kaikki neljä muuttavat käyrää, joten mitään niistä ei voi arvata toisen puolesta.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Hänen oman rajansa ja tarkemmat asetuksensa voi muuttaa myöhemmin "
        "Profiili-välilehdellä silloin, kun hän on valittuna henkilönä.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Pikalisäys",
    "Choose a favourite drink": "Valitse suosikkijuoma",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Valitse juoma, jonka yleensä tilaat, niin Live-näkymän painike kirjaa sen yhdellä "
        "napautuksella.",
    "This is your quick-add drink": "Tämä on pikalisäysjuomasi",
    "Set as my quick-add drink": "Aseta pikalisäysjuomakseni",
    "This is now your usual": "Tämä on nyt vakiojuomasi",
    "Remove favourite": "Poista suosikki",
    "Always add this one": "Lisää aina tämä",
    "Logs it straight away, without opening anything.": "Kirjaa sen heti avaamatta mitään.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Yksi napautus Live-näkymässä kirjaa tämän, ja painikkeessa näkyy ennustettu huippu. "
        "Vatsan täyteys periytyy sitä edeltäneestä juomasta, ja sen voi korjata heti "
        "jälkeenpäin.",
    "Peak %@": "Huippu %@",
    "%@ added": "%@ lisätty",
    "Save": "Tallenna",
    "Undo": "Kumoa",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Varmuuskopio",
    "Export a backup": "Vie varmuuskopio",
    "Import a backup": "Tuo varmuuskopio",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Varmuuskopio sisältää kaikki henkilöt, juomakerrat ja juomat. Tuonti lisää sen, mikä "
        "puuttuu – se ei koskaan muuta eikä poista mitään, mikä on jo tallennettu.",
    "Import this backup?": "Tuodaanko tämä varmuuskopio?",
    "Import": "Tuo",
    "Everything in this backup is already here.":
        "Kaikki tässä varmuuskopiossa on jo tallennettu.",
    "Import finished": "Tuonti valmis",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Kieli",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Avaa tämän sovelluksen Asetuksissa, jossa ”Ensisijainen kieli” määrittää sovelluksen "
        "oman kielen – järjestelmän kieli pysyy ennallaan. iOS käynnistää sovelluksen "
        "uudelleen, kun vaihdat sitä.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Tuonti ei onnistunut",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Tämä tiedosto ei ole LogMyDrink-varmuuskopio tai se on vaurioitunut.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Tämä varmuuskopio on tehty LogMyDrinkin uudemmalla versiolla. Päivitä sovellus ja "
        "yritä uudelleen.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Lisää %@ juomakertaa, %@ juomaa ja %@ kuukausisummaa. Mitään jo tallennettua ei muuteta eikä poisteta.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Lisätty %@ juomakertaa, %@ juomaa ja %@ kuukausisummaa.',
    'months as totals': 'kuukautta vain summina',
    'by month only': 'vain kuukausitasolla',
    'monthly total': 'kuukausisumma',
    'No daily records for this day': 'Tältä päivältä ei ole päiväkohtaisia merkintöjä',
    'Monthly total: %@': 'Kuukausisumma: %@',
    'A dry month': 'Tipaton kuukausi',

    # --- RemovePersonSection ---
    'Remove %@?': 'Poistetaanko %@?',
    'Remove': 'Poista',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Poistaa %@ juomakertaa, %@ juomaa ja %@ kuukausisummaa. Tätä ei voi kumota.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Poistaa %@ juomakertaa ja %@ juomaa. Tätä ei voi kumota.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Pyyhkäise vierasta vasemmalle poistaaksesi hänet ja kaiken hänelle kirjatun. Sinua ei voi poistaa.',
    'People': 'Henkilöt',
    'Owner': 'Omistaja',
    'Everyone this app records. Switch, add, or remove someone.': 'Kaikki, joita tämä sovellus kirjaa. Vaihda, lisää tai poista joku.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Siirtynyt edellisillasta',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorit',
    'Sessions': 'Kerrat',
    'Per session': 'Kertaa kohden',
    'Under the influence': 'Vaikutuksen alaisena',
    '%@ of the time': '%@ ajasta',
    'Days over limit': 'Rajan ylittäneet päivät',
    'Longest sober run': 'Pisin raitis jakso',
    'Favourite drink': 'Suosikkijuoma',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Esitystapa ja kieli",
    "Data": "Tiedot",
    "Concentration": "Pitoisuus",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Anna juomistiheyttä koskevan kysymyksen määrittää nopeus, ellei sinulla ole mittausta, johon sitä verrata.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Arvio, ei mittaus. Älä koskaan päätä tämän perusteella, voitko ajaa.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Arvioitu vaihteluväli, ei mittaus. Älä koskaan päätä tämän perusteella, voitko ajaa.',
    'How does the app calculate this?':
        'Miten sovellus laskee tämän?',
    'approximately %@ %@':
        'noin %@ %@',
    'How it works':
        'Näin se toimii',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Älä koskaan päätä tämän perusteella, voitko ajaa. Sovellus arvioi, se ei mittaa, ja todellinen tasosi voi poiketa huomattavasti.',
    'Why this app exists':
        'Miksi tämä sovellus',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink auttaa sinua juomaan tietoisemmin ja pitämään juomisen hallinnassa. Päätös tehdään ennen seuraavaa lasia, joten sovellus näyttää etukäteen, mihin uusi juoma veisi tasosi ja milloin se olisi huipussaan.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Kyse ei kuitenkaan ole vain tästä illasta. Jokainen kirjaamasi juoma tallentuu Historiaan, joten kuukausien ja vuosien mittaan näet, kuinka paljon ja kuinka usein juot ja kuinka korkealle tasosi nousee. Siitä erottuvat tapasi – ja myös se, mihin suuntaan ne ovat menossa: paremmaksi vai huonommaksi.',
    'How it calculates':
        'Näin se laskee',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Arvio perustuu Widmarkin menetelmään, jolla veren alkoholipitoisuutta on arvioitu 1930-luvulta lähtien; sovellus käyttää siitä hiottua versiota.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Painostasi, pituudestasi, iästäsi ja sukupuolestasi se laskee, kuinka paljon vettä kehossasi on, sillä alkoholi jakautuu siihen. Se seuraa jokaista juomaa erikseen: kuinka paljon alkoholia siinä oli, kuinka nopeasti joit sen ja kuinka paljon olit syönyt, sillä se ratkaisee imeytymisen nopeuden.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Samaan aikaan maksa poistaa tunnissa suunnilleen vakiomäärän; sinun määräsi arvioidaan sen perusteella, kuinka usein juot. Tuloksena on käyrä minuutti minuutilta: missä olet nyt, mihin olet menossa ja milloin olet taas nollassa.',
    'Details':
        'Lisätiedot',
    'Body water':
        'Kehon vesi',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Watsonin kaava (1980) painon, pituuden, iän ja sukupuolen perusteella. Naisten kaavassa ei ole ikää – se on kaavan ominaisuus, ei virhe. Jakautumistilavuus on kehon vesi jaettuna luvulla 0,85, veren vesipitoisuudella.',
    'Absorption':
        'Imeytyminen',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Jokaisella juomalla on oma ”vatsansa”. Tyhjään vatsaan puolet alkoholista imeytyy noin 7 minuutissa, täyteen vatsaan noin 21 minuutissa. Siemailtu juoma kulkeutuu vatsaan tasaisesti koko juomisen ajan.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Antaa matalamman huipun, ja taso nollautuu aiemmin. Yllättävää, mutta mitattua: ruoan kanssa vatsa hajottaa osan alkoholista ennen imeytymistä (sovellus käyttää 5, 10 ja 15 prosenttia), eikä sitä, mikä ei koskaan päässyt vereen, tarvitse poistaa.',
    'Elimination':
        'Palaminen',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Noin 0,15 ‰ tunnissa (julkaistu vaihteluväli 0,10–0,25), säännöllisesti juovilla enemmän, koska maksan entsyymit mukautuvat. Lähellä nollaa se hidastuu (Michaelis–Menten-kinetiikka), joten käyrä loivenee eikä katkea äkisti.',
    'Computation':
        'Laskenta',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Käyrä syntyy numeerisesta simulaatiosta minuutin tarkkuudella.',
    'Why it is only an estimate':
        'Miksi tämä on vain arvio',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Sovellus ei mittaa mitään. Se näyttää keskiarvoihin perustuvan mallin tuloksen, ja todellisuus voi poiketa siitä. Suurin tuntematon on, kuinka nopeasti alkoholi sinulla palaa: uskottavan vaihteluvälin sisällä pelkästään se voi siirtää huippua 40 prosenttia ja nollautumishetkeä neljä tuntia saman illan aikana.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Myös perimä, maksan kunto, lääkkeet, syömäsi ruoka, uni ja väsymys vaikuttavat – sovellus ei tiedä niistä mitään. Tarkan arvon antaa vain sertifioitu alkometri tai verikoe.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Luku on silti hyödyllinen. Jos sovellus näyttää sinulle johdonmukaisesti vähän liikaa tai liian vähän, se erehtyy joka ilta samaan suuntaan, joten opit ajan mittaan, mitä tietty arvo sinulle tarkoittaa. Profiilissa voit myös näyttää palamisnopeuden epävarmuuden: näet silloin vaihteluvälin yhden luvun sijaan.',
    'Tips':
        'Vinkit',
    'Favourite drink in one tap':
        'Suosikkijuoma yhdellä napautuksella',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Valitse suosikki Profiilissa, niin Live-näkymän painike kirjaa sen yhdellä napautuksella.',
    'Widget':
        'Widgetti',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Lisää se lukittuun näyttöön tai Koti-valikkoon: yksi napautus kirjaa suosikkisi. Kun kehossasi on alkoholia, se näyttää myös tasosi ja sen suunnan.',
    'How do I add it?':
        'Miten lisään sen?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Sano ”Hey Siri, LogMyDrink now”, niin Siri kirjaa suosikkisi ja kertoo, mihin huippusi on nousemassa. (Komento toimii englanniksi.)',
    'Looking back':
        'Katse taaksepäin',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        'Live-näkymän yläreunan ”Eilen” vie edelliseen päivään yhdellä napautuksella; Historia-välilehti näyttää tapasi viikkojen, kuukausien ja vuosien ajalta.',
    'Logging later':
        'Kirjaaminen jälkikäteen',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Jos kirjaat juoman jälkikäteen, siirrä aikaa taaksepäin painikkeilla − ja +; väliin jääneen päivän voit täydentää Historian Päivä-näkymässä.',
    'One tap and done':
        'Yksi napautus ja valmista',
    'Your favourite from the Lock Screen':
        'Suosikkisi lukitulta näytöltä',
    'Say it, don’t type it':
        'Sano se, älä kirjoita',
    'See your patterns':
        'Tarkastele tapojasi',
    'Set what you drink most often and log it with a single tap.':
        'Valitse, mitä juot useimmin, ja kirjaa se yhdellä napautuksella.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Yksi napautus widgetissä kirjaa suosikkisi etsimättä sovellusta. Illalla se näyttää myös tasosi.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '”Hey Siri, LogMyDrink now” – Siri kirjaa suosikkisi ja kertoo, mihin huippusi on nousemassa.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Historia näyttää, kuinka paljon juot ja kuinka korkealle tasosi nousee viikkojen, kuukausien ja vuosien aikana, ja mihin suuntaan se muuttuu.',
    'Set favourite':
        'Valitse suosikki',
    'Add widget':
        'Lisää widgetti',
    'Got it':
        'Selvä',
    'Open History':
        'Avaa Historia',
    'Don’t show again':
        'Älä näytä uudelleen',
    'Lock Screen':
        'Lukittu näyttö',
    'Home Screen':
        'Koti-valikko',
    'Where':
        'Minne',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Lukitse iPhone ja pidä sitten lukittua näyttöä painettuna.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Napauta Muokkaa, sitten Lukittu näyttö ja lopuksi kellon alla olevaa widgettiriviä.',
    'Choose LogMyDrink, then tap Done.':
        'Valitse LogMyDrink ja napauta Valmis.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Pidä Koti-valikon tyhjää kohtaa painettuna, kunnes apit alkavat heilua.',
    'Tap Edit, then Add Widget.':
        'Napauta Muokkaa ja sitten Lisää widgetti.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Hae LogMyDrink, valitse koko ja napauta Lisää widgetti.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Widgetin napautus avaa sovelluksen ja kirjaa suosikkijuomasi. Kun kehossasi on alkoholia, se näyttää myös tasosi ja sen suunnan.',
    'Add the widget':
        'Lisää widgetti',
    'Show tips':
        'Näytä vinkit',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Enintään yksi vinkki päivässä, kun avaat sovelluksen – ei koskaan, kun kehossasi on alkoholia.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Mitä luku näyttää',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Luku on arvio veresi alkoholipitoisuudesta (englanniksi BAC, blood alcohol concentration): kuinka paljon alkoholia veressäsi on.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'Promilleina (‰) se on grammaa alkoholia litrassa verta: 0,5 ‰ tarkoittaa puolta grammaa jokaisessa litrassa. Prosentteina se on grammaa 100 millilitrassa, joten sama taso on kymmenesosa luvusta: 0,5 ‰ on 0,05 prosenttia. Voit vaihtaa näiden välillä kohdassa Profiili › Esitystapa ja kieli.',
    'The curve shows the same level over time, minute by minute.':
        'Käyrä näyttää saman tason ajan mittaan, minuutti minuutilta.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promille (‰) on grammaa alkoholia litrassa verta, prosentti grammaa 100 millilitrassa: 0,5 ‰ on 0,05 prosenttia.',
}
