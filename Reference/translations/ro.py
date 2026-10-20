"""
Romanian.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promile",
    "Percent": "Procent",

    # --- DrinkCatalog: drink types ---
    "Beer": "Bere",
    "Wine": "Vin",
    "Champagne": "Spumant",
    "Shot": "Shot",
    "Cocktail": "Cocktail",
    "Custom": "Personalizat",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Stomac gol",
    "Moderately full": "Stomac parțial plin",
    "Full stomach": "Stomac plin",
    "Empty": "Gol",
    "Moderate": "Moderat",
    "Full": "Plin",
    "Fast absorption, higher and earlier peak.":
        "Absorbție rapidă, vârf mai ridicat și mai devreme.",
    "Moderate absorption.": "Absorbție moderată.",
    "Slow absorption, lower and later peak.": "Absorbție lentă, vârf mai scăzut și mai târziu.",

    # --- DrinkingFrequency ---
    "Rarely": "Rar",
    "A few times a month": "De câteva ori pe lună",
    "Several times a week": "De câteva ori pe săptămână",
    "Almost daily": "Aproape zilnic",
    "A few occasions a year": "Câteva ocazii pe an",
    "Social drinking": "Consum social",
    "Weekly routine": "Rutină săptămânală",
    "Daily or nearly daily": "Zilnic sau aproape zilnic",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Oră",
    "Level": "Nivel",
    "Lower": "Inferior",
    "Upper": "Superior",
    "Lower estimate": "Estimare inferioară",
    "Upper estimate": "Estimare superioară",
    "Personal limit": "Limită personală",
    "Drink": "Băutură",

    # --- BACChartView ---
    "Expected peak around %@": "Vârf estimat în jurul orei %@",
    "Peaked around %@": "Vârf atins în jurul orei %@",
    "No active session": "Nicio sesiune activă",
    "Still rising": "Încă în creștere",
    "YOUR LIMIT %@": "LIMITA TA %@",
    "possible range": "interval posibil",

    # --- Live screen: the day with nothing on it ---
    "Live": "Live",
    "Nothing logged today": "Nimic înregistrat azi",
    "Add a drink when you have one.": "Adaugă o băutură atunci când bei una.",

    # --- Tabs and history ---
    "History": "Istoric",
    "No past sessions yet": "Încă nicio sesiune anterioară",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "O sesiune apare aici după ce s-a încheiat — când alcoolul s-a eliminat complet și au "
        "trecut câteva ore.",
    "%@ drinks": "Băuturi: %@",
    "peak": "vârf",
    "Started": "A început",
    "Lasted": "A durat",
    "Duration": "Durată",
    "Sober around": "Treaz aprox.",
    "Sober at": "Treaz",
    "Remaining": "Rămas",
    "next day": "a doua zi",
    "previous day": "ziua precedentă",
    "%@ days later": "%@ zile mai târziu",
    "%@ days earlier": "cu %@ zile înainte",
    "Calculated with your profile at the time": "Calculat cu profilul tău de la acel moment",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Băuturi",
    "Units": "Unități",
    "Drinks this session": "Băuturi în această sesiune",
    "Add drink": "Adaugă băutură",

    # --- Editing an already logged drink ---
    "Edit drink": "Editează băutura",
    "Save changes": "Salvează modificările",
    "With this": "Cu aceasta",
    "Delete": "Șterge",
    "tap to edit · swipe to delete": "atinge pentru editare · glisează pentru ștergere",

    # --- Drinking pace ---
    "How fast": "Cât de repede",
    "In one go": "Dintr-o suflare",
    "Counts as a single swallow — the steepest possible rise.":
        "Se consideră o singură înghițitură — cea mai abruptă creștere posibilă.",
    "A quick drink. The level climbs fast.": "O băutură consumată repede. Nivelul urcă rapid.",
    "A normal pace.": "Un ritm normal.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Băută încet. Creștere mult mai lină pentru aceeași cantitate de alcool.",

    # --- AddDrinkSheet ---
    "Cancel": "Renunță",
    "Now": "Acum",
    "Projected peak": "Vârf estimat",
    "Peak at": "Vârf la ora",
    "Clears": "Eliminare completă",
    "This would cross your limit": "Ți-ai depăși limita",
    "Around %@, for up to %@.": "În jurul orei %@, timp de cel mult %@.",
    "This might cross your limit": "Ți-ai putea depăși limita",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Cu un metabolism mai lent, da; cu unul mai rapid, nu. Aceasta este incertitudinea "
        "estimării.",
    "Type": "Tip",
    "Amount": "Cantitate",
    "Strength": "Tărie alcoolică",
    "%@ units": "Unități: %@",
    "%@ g alcohol": "%@ g alcool",
    "Stomach": "Stomac",
    "When": "Când",
    "Done": "OK",
    "Add": "Adaugă",

    # --- ProfileSheet ---
    "Male": "Masculin",
    "Female": "Feminin",
    "Sex": "Sex",
    "Weight": "Greutate",
    "Height": "Înălțime",
    "Age": "Vârstă",
    "kg": "kg",
    "cm": "cm",
    "yrs": "ani",
    "Body": "Corp",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Apa totală din organism provine din ecuațiile Watson, care stabilesc volumul în care "
        "se distribuie alcoolul.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Apa totală din organism provine din ecuațiile Watson, care stabilesc volumul în care "
        "se distribuie alcoolul. Ecuația pentru femei nu include vârsta, așa că modificarea ei "
        "nu va afecta rezultatul.",
    "Drinking frequency": "Frecvența consumului",
    "How often do you drink?": "Cât de des bei?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Așa estimăm rata ta de eliminare. Consumul regulat induce calea hepatică CYP2E1, așa că persoanele care beau frecvent elimină alcoolul mai repede. Este punctul cel mai slab al modelului, motiv pentru care poți stabili în secțiunea Afișare și limbă cât din această incertitudine îți arată aplicația.",
    "Your limit": "Limita ta",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Un reper stabilit de tine, nu o limită legală. Aplicația îți spune când o băutură "
        "planificată te-ar duce peste el și cât timp ai rămâne deasupra.",
    "Calculated values": "Valori calculate",
    "Total body water": "Apa totală din organism",
    "Distribution volume": "Volum de distribuție",
    "Widmark factor": "Factorul Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Factorul Widmark este de obicei în jur de 0,68 la bărbați și 0,55 la femei. Dacă al "
        "tău este departe de aceste valori, merită să verifici valorile de mai sus.",
    "Elimination rate": "Rata de eliminare",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Cât de repede elimină ficatul tău alcoolul după ce a fost absorbit — panta părții "
        "descendente a curbei.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alcoolul se elimină într-o cantitate aproximativ fixă pe oră, nu ca procent, pentru "
        "că enzima care îl descompune funcționează deja la capacitate maximă la aproape orice "
        "nivel. De aceea există reguli empirice precum „o băutură pe oră”.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "La această setare, %@ se elimină în aproximativ %@. Aproape toată lumea se încadrează "
        "între %@ pe oră.",
    "How to find yours": "Cum să o afli pe a ta",
    "With a breathalyser": "Cu un etilotest",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Suflă de două ori, la cel puțin o oră distanță, pe partea descendentă — la două ore "
        "sau mai mult după ultima băutură, fără să mai bei nimic între timp. Scade a doua valoare din "
        "prima și împarte la numărul de ore dintre ele.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "De exemplu, %@ și, două ore mai târziu, %@ înseamnă %@ pe oră.",
    "Without one": "Fără etilotest",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Aplicația îți spune când estimează că alcoolul se va elimina complet. Dacă revii "
        "constant la normal cu mult înainte de acel moment, rata ta este mai mare decât "
        "setarea — crește-o cu o treaptă și urmărește câteva sesiuni. Dacă durează mai mult "
        "decât estimarea, scade-o.",
    "What moves it": "Ce o influențează",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Consumul regulat o crește: enzima hepatică ce face această treabă este indusă de "
        "utilizare. În medie, este ușor mai mare la femei și mai mică pe stomacul gol sau în "
        "caz de probleme hepatice.",
    "Uncertainty": "Incertitudine",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "La zero, fiecare valoare este un singur număr — cea mai bună estimare a aplicației. "
        "Peste zero, aceleași valori sunt afișate ca intervale, iar banda de pe grafic se "
        "lărgește corespunzător.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Un singur număr e mai ușor de folosit ca reper: cu timpul afli cum se simte propriul "
        "tău 0,6. Un interval e răspunsul mai fidel realității, pentru că rata chiar este "
        "incertă. Ambele variante se susțin — tu decizi.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Marja sugerată de frecvența consumului tău este de ± %@ pe oră.",
    "Rate": "Rată",
    "Range": "Interval",
    "Advanced": "Avansat",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Mai multe persoane",
    "History trends": "Tendințe ale istoricului",
    "Week": "Săptămână",
    "Month": "Lună",
    "Year": "An",
    "Sober days": "Zile fără alcool",
    "Change": "Schimbare",
    "before records": "înainte de începerea înregistrărilor",
    "See further back": "Privește mai departe în urmă",
    "Weeks, months and years side by side — and every evening older than seven days.": "Săptămâni, luni și ani în paralel — și fiecare seară mai veche de șapte zile.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Tot ce ai înregistrat este deja salvat. Deblocarea doar îl afișează.",
    "Coming soon": "În curând",
    "Today": "Astăzi",
    "Day": "Zi",
    "Yesterday": "Ieri",
    "No drinks on this day": "Nicio băutură în această zi",
    "Trend": "Tendință",
    "day": "zi",
    "Smoothing": "Netezire",
    "%@ sessions": "Sesiuni: %@",
    "No data before %@": "Nicio dată înainte de %@",
    "vs.": "față de",
    "Grams": "Grame",
    "Grams of alcohol": "Grame de alcool",
    "Standard units": "Unități standard",
    "Unit size": "Mărimea unității",
    "Automatic": "Automat",
    "UK": "Regatul Unit",
    "Nordic countries": "Țările nordice",
    "US standard drink": "Băutura standard din SUA",
    "WHO, most of Europe": "OMS, cea mai mare parte a Europei",
    "Period": "Perioadă",
    "Switch person": "Schimbă persoana",
    "Add person": "Adaugă persoană",
    "New person": "Persoană nouă",
    "You": "Tu",
    "Name": "Nume",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Toate cele patru valori modifică curba, așa că niciuna nu poate fi ghicită pentru "
        "altcineva.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Limita proprie și setările mai fine pot fi modificate ulterior în fila Profil, cât "
        "timp este persoana selectată.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Adăugare rapidă",
    "Choose a favourite drink": "Alege o băutură preferată",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Alege băutura pe care o comanzi de obicei, iar un buton de pe ecranul Live o va "
        "înregistra dintr-o singură atingere.",
    "This is your quick-add drink": "Aceasta este băutura ta pentru adăugare rapidă",
    "Set as my quick-add drink": "Setează ca băutură pentru adăugare rapidă",
    "This is now your usual": "Aceasta este acum băutura ta obișnuită",
    "Remove favourite": "Elimină băutura preferată",
    "Always add this one": "Adaugă mereu această băutură",
    "Logs it straight away, without opening anything.":
        "O înregistrează imediat, fără să deschidă nimic.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "O atingere pe ecranul Live o înregistrează, cu vârful estimat afișat pe buton. Cât de "
        "plin e stomacul se preia de la băutura anterioară și poate fi corectat imediat după.",
    "Peak %@": "Vârf %@",
    "%@ added": "S-a adăugat %@",
    "Save": "Salvează",
    "Undo": "Anulează",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Copie de rezervă",
    "Export a backup": "Exportă o copie de rezervă",
    "Import a backup": "Importă o copie de rezervă",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "O copie de rezervă conține fiecare persoană, ocazie și băutură. Importul adaugă ce "
        "lipsește — nu modifică și nu șterge niciodată nimic din ce există deja aici.",
    "Import this backup?": "Imporți această copie de rezervă?",
    "Import": "Importă",
    "Everything in this backup is already here.":
        "Tot ce se află în această copie de rezervă există deja aici.",
    "Import finished": "Import finalizat",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Limbă",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Deschide această aplicație în Configurări, unde „Limbă preferată” stabilește limba "
        "aplicației — cea a sistemului rămâne neschimbată. iOS repornește aplicația când o "
        "modifici.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Importul nu a reușit",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Acest fișier nu este o copie de rezervă LogMyDrink sau este deteriorat.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Această copie de rezervă a fost creată cu o versiune mai nouă a LogMyDrink. "
        "Actualizează aplicația și încearcă din nou.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Ocazii de adăugat: %@. Băuturi: %@. Totaluri lunare: %@. Nimic din ce există deja nu este modificat sau șters.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Adăugate: %@ ocazii, %@ băuturi și %@ totaluri lunare.',
    'months as totals': 'luni doar ca totaluri',
    'by month only': 'doar pe lună',
    'monthly total': 'total lunar',
    'No daily records for this day': 'Nu există înregistrări zilnice pentru această zi',
    'Monthly total: %@': 'Total lunar: %@',
    'A dry month': 'O lună fără alcool',

    # --- RemovePersonSection ---
    'Remove %@?': 'Elimini %@?',
    'Remove': 'Elimină',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Șterge %@ ocazii, %@ băuturi și %@ totaluri lunare. Nu se poate anula.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Șterge %@ ocazii și %@ băuturi. Nu se poate anula.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Glisează la stânga pe un invitat pentru a-l elimina cu tot ce a fost înregistrat pentru el. Tu nu poți fi eliminat.',
    'People': 'Persoane',
    'Owner': 'Proprietar',
    'Everyone this app records. Switch, add, or remove someone.': 'Toți cei pe care îi înregistrează această aplicație. Schimbă, adaugă sau elimină pe cineva.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Rămas din seara precedentă',
    # --- History, second card (5.24) ---
    'Calories': 'Calorii',
    'Sessions': 'Sesiuni',
    'Per session': 'Pe sesiune',
    'Under the influence': 'Sub influența alcoolului',
    '%@ of the time': '%@ din timp',
    'Days over limit': 'Zile peste limită',
    'Longest sober run': 'Cea mai lungă serie fără alcool',
    'Favourite drink': 'Băutura preferată',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Afișare și limbă",
    "Data": "Date",
    "Concentration": "Concentrație",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Lasă rata în seama întrebării despre frecvență, dacă nu ai o măsurătoare cu care s-o compari.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Estimare, nu măsurătoare. Nu te baza niciodată pe ea ca să decizi dacă poți conduce.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Interval estimat, nu măsurătoare. Nu te baza niciodată pe el ca să decizi dacă poți conduce.',
    'How does the app calculate this?':
        'Cum face aplicația acest calcul?',
    'approximately %@ %@':
        'aproximativ %@ %@',
    'How it works':
        'Cum funcționează',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nu te baza niciodată pe asta ca să decizi dacă poți conduce. Aplicația estimează, nu măsoară, iar nivelul tău real poate diferi considerabil.',
    'Why this app exists':
        'De ce există această aplicație',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink te ajută să bei mai conștient și să păstrezi controlul. Decizia se ia înainte de paharul următor, așa că aplicația îți arată dinainte unde ți-ar duce nivelul încă o băutură și când ar atinge vârful.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Dar nu e vorba doar de seara asta. Fiecare băutură înregistrată ajunge în Istoric, așa că de-a lungul lunilor și anilor vezi cât bei, cât de des și până la ce nivel ajungi. De aici se conturează tiparele tale, dar și direcția în care se schimbă — dacă lucrurile merg spre bine sau spre rău.',
    'How it calculates':
        'Cum calculează',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Estimarea se bazează pe metoda Widmark, folosită din anii 1930 pentru a estima alcoolemia; aplicația folosește o versiune rafinată a ei.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Din greutatea, înălțimea, vârsta și sexul tău calculează câtă apă conține corpul tău, pentru că acolo se distribuie alcoolul. Urmărește fiecare băutură separat: cât alcool a avut, cât de repede ai băut-o și cât mâncaseși, pentru că de asta depinde viteza de absorbție.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Între timp, ficatul elimină în fiecare oră o cantitate aproximativ constantă; a ta este estimată după cât de des bei. Rezultatul este o curbă, minut cu minut: unde ești acum, încotro te îndrepți și când vei fi din nou la zero.',
    'Details':
        'Detalii',
    'Body water':
        'Apa din corp',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Formula Watson (1980), pe baza greutății, înălțimii, vârstei și sexului. Formula pentru femei nu conține vârsta — e o proprietate a formulei, nu o eroare. Volumul de distribuție este apa din corp împărțită la 0,85, conținutul de apă al sângelui.',
    'Absorption':
        'Absorbție',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Fiecare băutură are propriul „stomac”. Pe stomacul gol, jumătate din alcool se absoarbe în circa 7 minute, pe stomacul plin în circa 21. O băutură pe care o sorbi ajunge în stomac uniform cât timp o bei.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Dă un vârf mai mic și o revenire mai rapidă la zero. Surprinzător, dar confirmat de măsurători: cu mâncare, stomacul descompune o parte din alcool înainte de absorbție (aplicația folosește 5, 10 și 15 la sută), iar ce n-a intrat niciodată nu mai trebuie eliminat.',
    'Elimination':
        'Eliminare',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Circa 0,15 ‰ pe oră (interval publicat 0,10–0,25), mai mare la cei care beau regulat, deoarece enzimele ficatului se adaptează. Aproape de zero încetinește (cinetică Michaelis-Menten), așa că curba se domolește treptat în loc să se oprească brusc.',
    'Computation':
        'Calcul',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Curba provine dintr-o simulare numerică cu rezoluție de un minut.',
    'Why it is only an estimate':
        'De ce e doar o estimare',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Aplicația nu măsoară nimic. Ce arată este rezultatul unui model cu valori medii, iar realitatea poate fi diferită. Cea mai mare necunoscută este cât de repede elimini alcoolul: în intervalul plauzibil, doar acest factor poate modifica, în aceeași seară, vârful cu 40 la sută și momentul revenirii la zero cu patru ore.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Contează și genetica, sănătatea ficatului, medicamentele, ce ai mâncat, somnul și oboseala — aplicația nu știe nimic din toate astea. Doar un etilotest omologat sau o analiză de sânge dau o valoare exactă.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Numărul rămâne totuși util. Dacă aplicația arată la tine constant puțin prea mult sau prea puțin, greșește în aceeași direcție în fiecare seară, așa că în timp înveți ce înseamnă o anumită valoare pentru tine. În Profil poți afișa și incertitudinea ratei de eliminare: vei vedea atunci un interval în loc de un singur număr.',
    'Tips':
        'Sfaturi',
    'Favourite drink in one tap':
        'Băutura preferată dintr-o atingere',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Setează o băutură preferată în Profil, iar butonul de pe ecranul Live o înregistrează dintr-o singură atingere.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Adaugă-l pe ecranul de blocare sau pe ecranul principal: o atingere înregistrează băutura preferată. Cât timp ai alcool în organism, arată și nivelul tău și dacă urcă sau coboară.',
    'How do I add it?':
        'Cum îl adaug?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Spune „Hey Siri, LogMyDrink now” și Siri înregistrează băutura preferată, apoi îți spune spre ce vârf te îndrepți. (Comanda funcționează în engleză.)',
    'Looking back':
        'Privire înapoi',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Ieri” din partea de sus a ecranului Live te duce la ziua precedentă dintr-o atingere; fila Istoric îți arată tiparele de-a lungul săptămânilor, lunilor și anilor.',
    'Logging later':
        'Înregistrare ulterioară',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Dacă înregistrezi o băutură ulterior, dă ora înapoi cu butoanele − și +; o zi omisă poate fi completată din vizualizarea Zi din Istoric.',
    'One tap and done':
        'O atingere și gata',
    'Your favourite from the Lock Screen':
        'Băutura preferată de pe ecranul de blocare',
    'Say it, don’t type it':
        'Spune, nu scrie',
    'See your patterns':
        'Vezi-ți tiparele',
    'Set what you drink most often and log it with a single tap.':
        'Setează ce bei cel mai des și înregistrează-l dintr-o singură atingere.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'O atingere pe widget înregistrează băutura preferată, fără să cauți aplicația. Seara arată și nivelul tău.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now” — Siri înregistrează băutura preferată și îți spune spre ce vârf te îndrepți.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Istoricul arată cât bei și până la ce nivel ajungi de-a lungul săptămânilor, lunilor și anilor, și în ce direcție se schimbă.',
    'Set favourite':
        'Setează băutura preferată',
    'Add widget':
        'Adaugă widget',
    'Got it':
        'Am înțeles',
    'Open History':
        'Deschide Istoricul',
    'Don’t show again':
        'Nu mai afișa',
    'Lock Screen':
        'Ecran de blocare',
    'Home Screen':
        'Ecran principal',
    'Where':
        'Unde',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Blochează iPhone-ul, apoi ține apăsat pe ecranul de blocare.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Atinge Personalizați, apoi Ecran de blocare și apoi rândul de widgeturi de sub ceas.',
    'Choose LogMyDrink, then tap Done.':
        'Alege LogMyDrink, apoi atinge OK.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Ține apăsat pe o zonă goală a ecranului principal până când pictogramele încep să tremure.',
    'Tap Edit, then Add Widget.':
        'Atinge Editați, apoi Adăugați widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Caută LogMyDrink, alege o dimensiune și atinge Adăugați widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'O atingere pe widget deschide aplicația și înregistrează băutura preferată. Cât timp ai alcool în organism, arată și nivelul tău și dacă urcă sau coboară.',
    'Add the widget':
        'Adaugă widgetul',
    'Show tips':
        'Afișează sfaturi',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Cel mult un sfat pe zi, la deschiderea aplicației — niciodată cât timp ai alcool în organism.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Ce arată numărul',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Numărul este o estimare a alcoolemiei tale (în engleză BAC, blood alcohol concentration): cât alcool ai în sânge.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'În promile (‰) înseamnă grame de alcool la litrul de sânge: 0,5 ‰ înseamnă o jumătate de gram în fiecare litru. În procente înseamnă grame la 100 de mililitri, deci același nivel dă un număr de zece ori mai mic: 0,5 ‰ înseamnă 0,05 la sută. Poți comuta între ele în Profil › Afișare și limbă.',
    'The curve shows the same level over time, minute by minute.':
        'Curba arată același nivel în timp, minut cu minut.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promilele (‰) sunt grame de alcool la litrul de sânge, procentele grame la 100 de mililitri: 0,5 ‰ înseamnă 0,05 la sută.',
}
