"""
Italian.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Per mille",
    "Percent": "Percentuale",

    # --- DrinkCatalog: drink types ---
    "Beer": "Birra",
    "Wine": "Vino",
    "Champagne": "Spumante",
    "Shot": "Shot",
    "Cocktail": "Cocktail",
    "Custom": "Personalizzato",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Stomaco vuoto",
    "Moderately full": "Moderatamente pieno",
    "Full stomach": "Stomaco pieno",
    "Empty": "Vuoto",
    "Moderate": "Moderato",
    "Full": "Pieno",
    "Fast absorption, higher and earlier peak.":
        "Assorbimento rapido, picco più alto e più precoce.",
    "Moderate absorption.": "Assorbimento moderato.",
    "Slow absorption, lower and later peak.":
        "Assorbimento lento, picco più basso e più tardivo.",

    # --- DrinkingFrequency ---
    "Rarely": "Raramente",
    "A few times a month": "Qualche volta al mese",
    "Several times a week": "Più volte a settimana",
    "Almost daily": "Quasi ogni giorno",
    "A few occasions a year": "Qualche occasione all’anno",
    "Social drinking": "Bere in compagnia",
    "Weekly routine": "Abitudine settimanale",
    "Daily or nearly daily": "Ogni giorno o quasi",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Ora",
    "Level": "Livello",
    "Lower": "Inferiore",
    "Upper": "Superiore",
    "Lower estimate": "Stima inferiore",
    "Upper estimate": "Stima superiore",
    "Personal limit": "Limite personale",
    "Drink": "Drink",

    # --- BACChartView ---
    "Expected peak around %@": "Picco previsto intorno a %@",
    "Peaked around %@": "Picco intorno a %@",
    "No active session": "Nessuna sessione attiva",
    "Still rising": "Ancora in salita",
    "YOUR LIMIT %@": "IL TUO LIMITE %@",
    "possible range": "intervallo possibile",

    # --- Live screen: the day with nothing on it ---
    "Live": "Live",
    "Nothing logged today": "Niente registrato oggi",
    "Add a drink when you have one.": "Aggiungi un drink quando ne bevi uno.",

    # --- Tabs and history ---
    "History": "Cronologia",
    "No past sessions yet": "Ancora nessuna sessione passata",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Una sessione compare qui quando è finita: quando hai smaltito l’alcol e sono passate "
        "alcune ore.",
    "%@ drinks": "%@ drink",
    "peak": "picco",
    "Started": "Inizio",
    "Lasted": "Durata",
    "Duration": "Durata",
    "Sober around": "Sobrio ca.",
    "Sober at": "Sobrio",
    "Remaining": "Rimanente",
    "next day": "il giorno dopo",
    "previous day": "il giorno prima",
    "%@ days later": "%@ giorni dopo",
    "%@ days earlier": "%@ giorni prima",
    "Calculated with your profile at the time": "Calcolato con il tuo profilo di allora",

    # --- TodayView ---
    "Profile": "Profilo",
    "Drinks": "Drink",
    "Units": "Unità",
    "Drinks this session": "Drink di questa sessione",
    "Add drink": "Aggiungi drink",

    # --- Editing an already logged drink ---
    "Edit drink": "Modifica drink",
    "Save changes": "Salva le modifiche",
    "With this": "Con questo",
    "Delete": "Elimina",
    "tap to edit · swipe to delete": "tocca per modificare · scorri per eliminare",

    # --- Drinking pace ---
    "How fast": "Quanto in fretta",
    "In one go": "Tutto d’un fiato",
    "Counts as a single swallow — the steepest possible rise.":
        "Conta come un solo sorso: la salita più ripida possibile.",
    "A quick drink. The level climbs fast.": "Un drink veloce. Il livello sale in fretta.",
    "A normal pace.": "Un ritmo normale.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Bevuto con calma. Salita molto più dolce a parità di alcol.",

    # --- AddDrinkSheet ---
    "Cancel": "Annulla",
    "Now": "Adesso",
    "Projected peak": "Picco previsto",
    "Peak at": "Picco alle",
    "Clears": "Smaltimento",
    "This would cross your limit": "Questo ti farebbe superare il limite",
    "Around %@, for up to %@.": "Intorno a %@, per un massimo di %@.",
    "This might cross your limit": "Questo potrebbe farti superare il limite",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Con un metabolismo più lento sì, con uno più rapido no. È l’incertezza della stima.",
    "Type": "Tipo",
    "Amount": "Quantità",
    "Strength": "Gradazione",
    "%@ units": "%@ unità",
    "%@ g alcohol": "%@ g di alcol",
    "Stomach": "Stomaco",
    "When": "Quando",
    "Done": "Fine",
    "Add": "Aggiungi",

    # --- ProfileSheet ---
    "Male": "Maschio",
    "Female": "Femmina",
    "Sex": "Sesso",
    "Weight": "Peso",
    "Height": "Altezza",
    "Age": "Età",
    "kg": "kg",
    "cm": "cm",
    "yrs": "anni",
    "Body": "Corpo",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "L’acqua corporea totale deriva dalle equazioni di Watson, che definiscono il volume "
        "in cui l’alcol si distribuisce.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "L’acqua corporea totale deriva dalle equazioni di Watson, che definiscono il volume "
        "in cui l’alcol si distribuisce. L’equazione femminile non include l’età, quindi "
        "modificarla non cambierà il risultato.",
    "Drinking frequency": "Frequenza di consumo",
    "How often do you drink?": "Quanto spesso bevi?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "È così che stimiamo la tua velocità di eliminazione. Bere regolarmente induce la via epatica del CYP2E1, quindi chi beve spesso smaltisce l’alcol più in fretta. È il punto più debole del modello, ed è per questo che in Visualizzazione e lingua puoi impostare quanta parte di quell’incertezza l’app ti mostra.",
    "Your limit": "Il tuo limite",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Un tuo valore di riferimento, non un limite legale. L’app ti dice quando un drink in "
        "programma te lo farebbe superare, e per quanto tempo resteresti sopra.",
    "Calculated values": "Valori calcolati",
    "Total body water": "Acqua corporea totale",
    "Distribution volume": "Volume di distribuzione",
    "Widmark factor": "Fattore di Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Il fattore di Widmark è di solito intorno a 0,68 per gli uomini e 0,55 per le donne. "
        "Se il tuo è molto distante, vale la pena controllare i valori qui sopra.",
    "Elimination rate": "Velocità di eliminazione",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Quanto in fretta il fegato smaltisce l’alcol una volta assorbito: la pendenza del "
        "versante discendente della curva.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "L’alcol se ne va a una quantità all’incirca fissa all’ora, non in percentuale, perché "
        "l’enzima che lo scompone lavora già a pieno regime a quasi qualsiasi livello. È per "
        "questo che esistono regole empiriche come «un drink all’ora».",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Con questa impostazione, per smaltire %@ servono circa %@. Quasi tutti rientrano tra "
        "%@ all’ora.",
    "How to find yours": "Come trovare la tua",
    "With a breathalyser": "Con un etilometro",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Soffia due volte, a distanza di almeno un’ora, sul versante discendente: due ore o "
        "più dopo l’ultimo drink, senza bere nulla nel frattempo. Sottrai la seconda lettura "
        "dalla prima e dividi per le ore che le separano.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Per esempio %@ e %@ due ore dopo danno %@ all’ora.",
    "Without one": "Senza",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "L’app ti dice quando prevede che avrai smaltito tutto. Se torni regolarmente alla "
        "normalità ben prima, la tua velocità è più alta dell’impostazione: alzala di un passo "
        "e osserva per qualche sessione. Se ci vuole più tempo del previsto, abbassala.",
    "What moves it": "Cosa la cambia",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Bere regolarmente la alza: l’enzima epatico che svolge il lavoro viene indotto "
        "dall’uso. In media è anche un po’ più alta nelle donne, e più bassa a stomaco vuoto o "
        "in presenza di problemi al fegato.",
    "Uncertainty": "Incertezza",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "A zero ogni valore è un numero singolo: la stima migliore dell’app. Sopra lo zero gli "
        "stessi valori sono mostrati come intervalli, e la banda sul grafico si allarga di "
        "conseguenza.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Su un numero singolo è più facile farsi l’occhio: col tempo scopri come ti senti al "
        "tuo 0,6. Un intervallo è la risposta più fedele, perché la velocità è davvero "
        "incerta. Entrambe le scelte sono valide: decidi tu.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "La dispersione suggerita dalla tua frequenza di consumo è ± %@ all’ora.",
    "Rate": "Velocità",
    "Range": "Intervallo",
    "Advanced": "Avanzate",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Più persone",
    "History trends": "Tendenze della cronologia",
    "Week": "Settimana",
    "Month": "Mese",
    "Year": "Anno",
    "Sober days": "Giorni senza alcol",
    "Change": "Variazione",
    "before records": "prima della registrazione",
    "See further back": "Guarda più indietro",
    "Weeks, months and years side by side — and every evening older than seven days.": "Settimane, mesi e anni affiancati, e ogni serata più vecchia di sette giorni.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Tutto ciò che hai registrato è già salvato. Sbloccare serve solo a mostrarlo.",
    "Coming soon": "Prossimamente",
    "Today": "Oggi",
    "Day": "Giorno",
    "Yesterday": "Ieri",
    "No drinks on this day": "Nessun drink in questo giorno",
    "Trend": "Tendenza",
    "day": "giorno",
    "Smoothing": "Livellamento",
    "%@ sessions": "%@ occasioni",
    "No data before %@": "Nessun dato prima del %@",
    "vs.": "vs.",
    "Grams": "Grammi",
    "Grams of alcohol": "Grammi di alcol",
    "Standard units": "Unità standard",
    "Unit size": "Dimensione dell’unità",
    "Automatic": "Automatica",
    "UK": "Regno Unito",
    "Nordic countries": "Paesi nordici",
    "US standard drink": "Drink standard USA",
    "WHO, most of Europe": "OMS, gran parte d’Europa",
    "Period": "Periodo",
    "Switch person": "Cambia persona",
    "Add person": "Aggiungi persona",
    "New person": "Nuova persona",
    "You": "Tu",
    "Name": "Nome",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Tutti e quattro cambiano la curva, quindi nessuno di essi può essere indovinato per "
        "un’altra persona.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Il suo limite e le impostazioni più fini si possono cambiare in seguito nella scheda "
        "Profilo, mentre è la persona selezionata.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Aggiunta rapida",
    "Choose a favourite drink": "Scegli un drink preferito",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Scegli il drink che ordini di solito e un pulsante sulla schermata Live lo registrerà "
        "con un tocco.",
    "This is your quick-add drink": "È il tuo drink per l’aggiunta rapida",
    "Set as my quick-add drink": "Imposta come drink per l’aggiunta rapida",
    "This is now your usual": "Ora è il tuo drink abituale",
    "Remove favourite": "Rimuovi preferito",
    "Always add this one": "Aggiungi sempre questo",
    "Logs it straight away, without opening anything.":
        "Lo registra subito, senza aprire nulla.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Un tocco sulla schermata Live lo registra, con il picco previsto sul pulsante. Quanto "
        "è pieno lo stomaco viene dal drink precedente e si può correggere subito dopo.",
    "Peak %@": "Picco %@",
    "%@ added": "Hai aggiunto %@",
    "Save": "Salva",
    "Undo": "Annulla",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Backup",
    "Export a backup": "Esporta un backup",
    "Import a backup": "Importa un backup",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Un backup contiene tutte le persone, le occasioni e i drink. L’importazione aggiunge "
        "ciò che manca: non modifica né rimuove mai nulla di quanto è già qui.",
    "Import this backup?": "Importare questo backup?",
    "Import": "Importa",
    "Everything in this backup is already here.":
        "Tutto ciò che c’è in questo backup è già qui.",
    "Import finished": "Importazione completata",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Lingua",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Apre questa app in Impostazioni, dove «Lingua preferita» imposta la lingua dell’app: "
        "quella del sistema resta com’è. iOS riavvia l’app quando la cambi.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Importazione non riuscita",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Questo file non è un backup di LogMyDrink, oppure è danneggiato.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Questo backup è stato creato da una versione più recente di LogMyDrink. Aggiorna "
        "l’app e riprova.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Aggiunge %@ occasioni, %@ drink e %@ totali mensili. Nulla di quanto è già qui viene modificato o rimosso.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Aggiunti %@ occasioni, %@ drink e %@ totali mensili.',
    'months as totals': 'mesi solo come totali',
    'by month only': 'solo per mese',
    'monthly total': 'totale mensile',
    'No daily records for this day': 'Nessuna registrazione giornaliera per questo giorno',
    'Monthly total: %@': 'Totale mensile: %@',
    'A dry month': 'Un mese senza alcol',

    # --- RemovePersonSection ---
    'Remove %@?': 'Rimuovere %@?',
    'Remove': 'Rimuovi',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Elimina %@ occasioni, %@ drink e %@ totali mensili. Non è possibile annullare.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Elimina %@ occasioni e %@ drink. Non è possibile annullare.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Scorri a sinistra su un ospite per rimuoverlo con tutto ciò che è stato registrato a suo nome. Tu non puoi essere rimosso.',
    'People': 'Persone',
    'Owner': 'Titolare',
    'Everyone this app records. Switch, add, or remove someone.': 'Tutte le persone che questa app registra. Cambia, aggiungi o rimuovi qualcuno.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Riportato dalla sera prima',
    # --- History, second card (5.24) ---
    'Calories': 'Calorie',
    'Sessions': 'Occasioni',
    'Per session': 'Per occasione',
    'Under the influence': 'Sotto l’effetto',
    '%@ of the time': '%@ del tempo',
    'Days over limit': 'Giorni oltre il limite',
    'Longest sober run': 'Serie sobria più lunga',
    'Favourite drink': 'Bevanda preferita',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Visualizzazione e lingua",
    "Data": "Dati",
    "Concentration": "Concentrazione",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Lascia la velocità alla domanda sulla frequenza, a meno che tu non abbia una misurazione con cui confrontarla.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Stima, non una misurazione. Non usare mai questa app per decidere se puoi guidare.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Intervallo stimato, non una misurazione. Non usare mai questa app per decidere se puoi guidare.',
    'How does the app calculate this?':
        'Come calcola l’app?',
    'approximately %@ %@':
        'circa %@ %@',
    'How it works':
        'Come funziona',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Non usare mai questa app per decidere se puoi guidare. L’app stima, non misura, e il tuo livello reale può essere molto diverso.',
    'Why this app exists':
        'Perché esiste questa app',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink ti aiuta a bere in modo più consapevole e a mantenere il controllo. La decisione si prende prima del bicchiere successivo, quindi l’app ti mostra in anticipo dove porterebbe il tuo livello un altro drink e quando raggiungerebbe il picco.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Ma non riguarda solo stasera. Ogni drink registrato finisce nella cronologia, così nel corso di mesi e anni vedi quanto, quanto spesso e fino a che livello bevi. Ne emergono le tue abitudini, e anche la direzione in cui cambiano: se le cose migliorano o peggiorano.',
    'How it calculates':
        'Come calcola',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'La stima si basa sul metodo di Widmark, usato dagli anni Trenta per stimare il tasso alcolemico; l’app ne usa una versione perfezionata.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Da peso, altezza, età e sesso calcola quanta acqua contiene il tuo corpo, perché è lì che l’alcol si distribuisce. Segue ogni drink separatamente: quanto alcol conteneva, quanto in fretta l’hai bevuto e quanto avevi mangiato, perché da questo dipende la velocità di assorbimento.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Nel frattempo il fegato smaltisce ogni ora una quantità più o meno costante; la tua viene stimata dalla frequenza con cui bevi. Il risultato è una curva, minuto per minuto: dove sei ora, dove stai andando e quando tornerai a zero.',
    'Details':
        'Dettagli',
    'Body water':
        'Acqua corporea',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'La formula di Watson (1980), da peso, altezza, età e sesso. La formula femminile non contiene l’età: è una caratteristica della formula, non un errore. Il volume di distribuzione è l’acqua corporea divisa per 0,85, il contenuto d’acqua del sangue.',
    'Absorption':
        'Assorbimento',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Ogni drink ha il suo «stomaco». A stomaco vuoto metà dell’alcol viene assorbita in circa 7 minuti, a stomaco pieno in circa 21. Un drink sorseggiato arriva nello stomaco in modo uniforme mentre lo bevi.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Dà un picco più basso e un ritorno a zero anticipato. Sorprendente, ma misurato: con il cibo lo stomaco scompone una parte dell’alcol prima che venga assorbita (l’app usa 5, 10 e 15 per cento), e ciò che non entra non va smaltito.',
    'Elimination':
        'Smaltimento',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Circa 0,15 ‰ all’ora (intervallo pubblicato 0,10–0,25), di più in chi beve regolarmente perché gli enzimi del fegato si adattano. Vicino allo zero rallenta (cinetica di Michaelis-Menten), così la curva si smorza invece di interrompersi di colpo.',
    'Computation':
        'Calcolo',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'La curva deriva da una simulazione numerica con risoluzione di un minuto.',
    'Why it is only an estimate':
        'Perché è solo una stima',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'L’app non misura nulla. Ciò che mostra è il risultato di un modello basato su valori medi, e la realtà può differire. La maggiore incognita è la velocità con cui smaltisci l’alcol: nell’intervallo plausibile, da sola può spostare il picco del 40 per cento e il ritorno a zero di quattro ore nella stessa serata.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Contano anche genetica, salute del fegato, farmaci, cosa hai mangiato, sonno e stanchezza, e l’app non ne sa nulla. Solo un etilometro omologato o un esame del sangue danno un valore esatto.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Il numero resta comunque utile. Se l’app con te segna sempre un po’ di più o un po’ di meno, sbaglia nella stessa direzione ogni sera: col tempo impari che cosa significa un certo valore per te. Nel Profilo puoi anche mostrare l’incertezza della velocità di smaltimento: vedrai un intervallo invece di un singolo numero.',
    'Tips':
        'Suggerimenti',
    'Favourite drink in one tap':
        'Drink preferito con un tocco',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Scegli un preferito nel Profilo e il pulsante di Live lo registra con un solo tocco.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Aggiungilo alla schermata di blocco o alla schermata Home: un tocco registra il tuo preferito. Finché c’è alcol nel tuo corpo, mostra anche il livello e la sua direzione.',
    'How do I add it?':
        'Come lo aggiungo?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Di’ «Ehi Siri, LogMyDrink now»: Siri registra il tuo preferito e ti dice verso quale picco stai andando.',
    'Looking back':
        'Guardare indietro',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '«Ieri» in cima a Live ti porta al giorno precedente con un tocco; la scheda Cronologia mostra le tue abitudini nell’arco di settimane, mesi e anni.',
    'Logging later':
        'Registrare dopo',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Se registri un drink in un secondo momento, riporta indietro l’ora con i pulsanti − e +; un giorno dimenticato si può completare dalla vista Giorno della cronologia.',
    'One tap and done':
        'Un tocco e fatto',
    'Your favourite from the Lock Screen':
        'Il tuo preferito dalla schermata di blocco',
    'Say it, don’t type it':
        'Dillo, non scriverlo',
    'See your patterns':
        'Scopri le tue abitudini',
    'Set what you drink most often and log it with a single tap.':
        'Indica cosa bevi più spesso e registralo con un solo tocco.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Un tocco sul widget registra il tuo preferito, senza cercare l’app. La sera mostra anche il tuo livello.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '«Ehi Siri, LogMyDrink now»: Siri registra il tuo preferito e ti dice verso quale picco stai andando.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'La cronologia mostra quanto e fino a che livello bevi nell’arco di settimane, mesi e anni, e in che direzione cambia.',
    'Set favourite':
        'Scegli il preferito',
    'Add widget':
        'Aggiungi widget',
    'Got it':
        'Ho capito',
    'Open History':
        'Apri la cronologia',
    'Don’t show again':
        'Non mostrare più',
    'Lock Screen':
        'Schermata di blocco',
    'Home Screen':
        'Schermata Home',
    'Where':
        'Dove',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Blocca l’iPhone, poi tieni premuto sulla schermata di blocco.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Tocca Personalizza, poi Schermata di blocco, quindi la riga dei widget sotto l’ora.',
    'Choose LogMyDrink, then tap Done.':
        'Scegli LogMyDrink, poi tocca Fine.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Tieni premuto su un’area vuota della schermata Home finché le icone non tremolano.',
    'Tap Edit, then Add Widget.':
        'Tocca Modifica, poi Aggiungi widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Cerca LogMyDrink, scegli una dimensione e tocca Aggiungi widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Un tocco sul widget apre l’app e registra il tuo drink preferito. Finché c’è alcol nel tuo corpo, mostra anche il livello e la sua direzione.',
    'Add the widget':
        'Aggiungi il widget',
    'Show tips':
        'Mostra suggerimenti',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Al massimo un suggerimento al giorno, all’apertura dell’app: mai finché c’è alcol nel tuo corpo.',
}
