"""
German.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promille",
    "Percent": "Prozent",

    # --- DrinkCatalog: drink types ---
    "Beer": "Bier",
    "Wine": "Wein",
    "Champagne": "Sekt",
    "Shot": "Kurzer",
    "Cocktail": "Cocktail",
    "Custom": "Eigenes",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Leerer Magen",
    "Moderately full": "Mäßig voll",
    "Full stomach": "Voller Magen",
    "Empty": "Leer",
    "Moderate": "Mäßig",
    "Full": "Voll",
    "Fast absorption, higher and earlier peak.":
        "Schnelle Aufnahme, höherer und früherer Höchstwert.",
    "Moderate absorption.": "Mäßige Aufnahme.",
    "Slow absorption, lower and later peak.":
        "Langsame Aufnahme, niedrigerer und späterer Höchstwert.",

    # --- DrinkingFrequency ---
    "Rarely": "Selten",
    "A few times a month": "Ein paar Mal im Monat",
    "Several times a week": "Mehrmals pro Woche",
    "Almost daily": "Fast täglich",
    "A few occasions a year": "Ein paar Mal im Jahr",
    "Social drinking": "Geselliges Trinken",
    "Weekly routine": "Wöchentliche Routine",
    "Daily or nearly daily": "Täglich oder fast täglich",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Zeit",
    "Level": "Alkoholspiegel",
    "Lower": "Untere",
    "Upper": "Obere",
    "Lower estimate": "Untere Schätzung",
    "Upper estimate": "Obere Schätzung",
    "Personal limit": "Persönliches Limit",
    "Drink": "Getränk",

    # --- BACChartView ---
    "Expected peak around %@": "Höchstwert voraussichtlich gegen %@",
    "Peaked around %@": "Höchstwert gegen %@",
    "No active session": "Keine aktive Sitzung",
    "Still rising": "Steigt noch",
    "YOUR LIMIT %@": "DEIN LIMIT %@",
    "possible range": "möglicher Bereich",

    # --- Live screen: the day with nothing on it ---
    "Live": "Live",
    "Nothing logged today": "Heute nichts eingetragen",
    "Add a drink when you have one.": "Trag ein Getränk ein, wenn du eines trinkst.",

    # --- Tabs and history ---
    "History": "Verlauf",
    "No past sessions yet": "Noch keine vergangenen Sitzungen",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Eine Sitzung erscheint hier, sobald sie beendet ist – wenn dein Alkohol abgebaut ist "
        "und ein paar Stunden vergangen sind.",
    "%@ drinks": "%@ Getränke",
    "peak": "Höchstwert",
    "Started": "Begonnen",
    "Lasted": "Dauer",
    "Duration": "Dauer",
    "Sober around": "Nüchtern ca.",
    "Sober at": "Nüchtern",
    "Remaining": "Verbleibend",
    "next day": "am nächsten Tag",
    "previous day": "am Vortag",
    "%@ days later": "%@ Tage später",
    "%@ days earlier": "%@ Tage früher",
    "Calculated with your profile at the time": "Berechnet mit deinem damaligen Profil",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Getränke",
    "Units": "Einheiten",
    "Drinks this session": "Getränke in dieser Sitzung",
    "Add drink": "Getränk hinzufügen",

    # --- Editing an already logged drink ---
    "Edit drink": "Getränk bearbeiten",
    "Save changes": "Änderungen sichern",
    "With this": "Mit diesem Getränk",
    "Delete": "Löschen",
    "tap to edit · swipe to delete": "zum Bearbeiten tippen · zum Löschen streichen",

    # --- Drinking pace ---
    "How fast": "Wie schnell",
    "In one go": "In einem Zug",
    "Counts as a single swallow — the steepest possible rise.":
        "Zählt als ein einziger Schluck – der steilstmögliche Anstieg.",
    "A quick drink. The level climbs fast.":
        "Schnell getrunken. Der Alkoholspiegel steigt rasch.",
    "A normal pace.": "Ein normales Tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Langsam getrunken. Deutlich sanfterer Anstieg bei gleicher Alkoholmenge.",

    # --- AddDrinkSheet ---
    "Cancel": "Abbrechen",
    "Now": "Jetzt",
    "Projected peak": "Erwarteter Höchstwert",
    "Peak at": "Höchstwert um",
    "Clears": "Abgebaut",
    "This would cross your limit": "Das würde dein Limit überschreiten",
    "Around %@, for up to %@.": "Etwa %@, für bis zu %@.",
    "This might cross your limit": "Das könnte dein Limit überschreiten",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Bei langsamerem Stoffwechsel ja, bei schnellerem nein. Das ist die Unsicherheit der "
        "Schätzung.",
    "Type": "Art",
    "Amount": "Menge",
    "Strength": "Stärke",
    "%@ units": "%@ Einheiten",
    "%@ g alcohol": "%@ g Alkohol",
    "Stomach": "Magen",
    "When": "Wann",
    "Done": "Fertig",
    "Add": "Hinzufügen",

    # --- ProfileSheet ---
    "Male": "Männlich",
    "Female": "Weiblich",
    "Sex": "Geschlecht",
    "Weight": "Gewicht",
    "Height": "Größe",
    "Age": "Alter",
    "kg": "kg",
    "cm": "cm",
    "yrs": "Jahre",
    "Body": "Körper",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Das Gesamtkörperwasser stammt aus den Watson-Gleichungen, die das Volumen festlegen, "
        "in dem sich der Alkohol verteilt.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Das Gesamtkörperwasser stammt aus den Watson-Gleichungen, die das Volumen festlegen, "
        "in dem sich der Alkohol verteilt. Die Gleichung für Frauen enthält kein Alter, eine "
        "Änderung wirkt sich daher nicht auf das Ergebnis aus.",
    "Drinking frequency": "Trinkhäufigkeit",
    "How often do you drink?": "Wie oft trinkst du?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "So schätzen wir deine Abbaurate. Regelmäßiges Trinken induziert den CYP2E1-Stoffwechselweg der Leber, deshalb bauen häufig Trinkende Alkohol schneller ab. Das ist die schwächste Stelle des Modells, und deshalb kannst du unter „Anzeige & Sprache“ einstellen, wie viel von dieser Unsicherheit die App dir zeigt.",
    "Your limit": "Dein Limit",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Deine eigene Bezugsgröße, kein gesetzlicher Grenzwert. Die App sagt dir Bescheid, wenn "
        "ein geplantes Getränk dich darüber bringen würde, und auch, wie lange du darüber "
        "bleiben würdest.",
    "Calculated values": "Berechnete Werte",
    "Total body water": "Gesamtkörperwasser",
    "Distribution volume": "Verteilungsvolumen",
    "Widmark factor": "Widmark-Faktor",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Der Widmark-Faktor liegt bei Männern typischerweise bei etwa 0,68, bei Frauen bei "
        "etwa 0,55. Wenn deiner weit davon entfernt ist, lohnt sich ein Blick auf die Werte oben.",
    "Elimination rate": "Abbaurate",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Wie schnell deine Leber Alkohol abbaut, sobald er aufgenommen ist – die Steigung der "
        "fallenden Seite der Kurve.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol wird pro Stunde in etwa gleichbleibender Menge abgebaut und nicht als Anteil, "
        "weil das abbauende Enzym schon bei fast jedem Spiegel mit voller Kapazität arbeitet. "
        "Nur deshalb gibt es Faustregeln wie „ein Getränk pro Stunde“.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Bei dieser Einstellung braucht %@ etwa %@ bis zum Abbau. Fast alle liegen zwischen %@ "
        "pro Stunde.",
    "How to find yours": "So findest du deine Rate",
    "With a breathalyser": "Mit einem Alkoholtester",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Blas zweimal, mit mindestens einer Stunde Abstand, auf der fallenden Seite – zwei "
        "Stunden oder mehr nach deinem letzten Getränk, ohne dazwischen etwas zu trinken. Zieh den "
        "zweiten Wert vom ersten ab und teile durch die Stunden dazwischen.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Zum Beispiel ergeben %@ und zwei Stunden später %@ einen Abbau von %@ pro Stunde.",
    "Without one": "Ohne Alkoholtester",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Die App sagt dir, wann sie mit dem vollständigen Abbau rechnet. Wenn du verlässlich "
        "deutlich früher wieder normal bist, ist deine Rate höher als eingestellt – stell sie "
        "eine Stufe höher und beobachte ein paar Sitzungen. Dauert es länger als vorhergesagt, "
        "stell sie eine Stufe niedriger.",
    "What moves it": "Was sie beeinflusst",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Regelmäßiges Trinken erhöht sie: Das Leberenzym, das die Arbeit macht, wird durch "
        "Gebrauch induziert. Bei Frauen liegt sie im Mittel etwas höher, auf leeren Magen oder "
        "bei Leberproblemen niedriger.",
    "Uncertainty": "Unsicherheit",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Bei null ist jeder Wert eine einzelne Zahl – die beste Schätzung der App. Über null "
        "werden dieselben Werte als Bereiche angezeigt, und das Band im Diagramm wird "
        "entsprechend breiter.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "An einer einzelnen Zahl lässt sich leichter lernen: Mit der Zeit findest du heraus, "
        "wie sich deine eigenen 0,6 anfühlen. Ein Bereich ist die ehrlichere Antwort, denn die "
        "Abbaurate ist tatsächlich unsicher. Beides lässt sich vertreten – das ist deine "
        "Entscheidung.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Die aus deiner Trinkhäufigkeit abgeleitete Spanne beträgt ± %@ pro Stunde.",
    "Rate": "Rate",
    "Range": "Bereich",
    "Advanced": "Erweitert",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Week": "Woche",
    "Month": "Monat",
    "Year": "Jahr",
    "Sober days": "Trockene Tage",
    "Change": "Veränderung",
    "before records": "vor Beginn der Aufzeichnung",
    "See further back": "Weiter zurückblicken",
    "Weeks, months and years side by side — and every evening older than seven days.": "Wochen, Monate und Jahre nebeneinander – und jeder Abend, der älter als sieben Tage ist.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Alles, was du bisher eingetragen hast, ist bereits gespeichert. Das Freischalten zeigt es nur an.",
    "Back up and restore": "Sichern und wiederherstellen",
    "Log for friends too": "Auch für Freunde eintragen",
    "Switch to someone else in one tap and log their drinks with their own body and limit — each person gets their own curve and history.": "Wechsle mit einem Tippen zu jemand anderem und trage seine Getränke mit seinem eigenen Körper und Limit ein – jede Person bekommt ihre eigene Kurve und ihren eigenen Verlauf.",
    "Save everything to a file, and read a backup back in — on this phone or on a new one.": "Speichere alles in einer Datei und lies eine Sicherung wieder ein – auf diesem Telefon oder auf einem neuen.",
    "Backup and restore are part of Pro.": "Sichern und Wiederherstellen sind Teil von Pro.",
    "Today": "Heute",
    "Day": "Tag",
    "Yesterday": "Gestern",
    "No drinks on this day": "Keine Getränke an diesem Tag",
    "Trend": "Trend",
    "day": "Tag",
    "Smoothing": "Glättung",
    "%@ sessions": "%@ Sitzungen",
    "No data before %@": "Keine Daten vor dem %@",
    "vs.": "vs.",
    "Grams": "Gramm",
    "Grams of alcohol": "Gramm Alkohol",
    "Standard units": "Standardeinheiten",
    "Unit size": "Einheitsgröße",
    "Automatic": "Automatisch",
    "UK": "Vereinigtes Königreich",
    "Nordic countries": "Nordische Länder",
    "US standard drink": "US-Standarddrink",
    "WHO, most of Europe": "WHO, der Großteil Europas",
    "Period": "Zeitraum",
    "Switch person": "Person wechseln",
    "Add person": "Person hinzufügen",
    "New person": "Neue Person",
    "You": "Du",
    "Name": "Name",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Alle vier verändern die Kurve, deshalb lässt sich keiner davon für jemand anderen "
        "schätzen.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Das eigene Limit und die feineren Einstellungen lassen sich später im Tab „Profil“ "
        "ändern, solange die Person ausgewählt ist.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Schnelleingabe",
    "Choose a favourite drink": "Lieblingsgetränk wählen",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Wähl das Getränk, das du sonst bestellst, dann trägt eine Taste auf dem "
        "Live-Bildschirm es mit einem Tippen ein.",
    "This is your quick-add drink": "Das ist dein Getränk für die Schnelleingabe",
    "Set as my quick-add drink": "Als Getränk für die Schnelleingabe festlegen",
    "This is now your usual": "Das ist jetzt dein Standardgetränk",
    "Remove favourite": "Favorit entfernen",
    "Always add this one": "Immer dieses hinzufügen",
    "Logs it straight away, without opening anything.":
        "Trägt es sofort ein, ohne dass sich etwas öffnet.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Ein Tippen auf dem Live-Bildschirm trägt das ein, mit dem erwarteten Höchstwert auf "
        "der Taste. Wie voll dein Magen ist, wird vom vorherigen Getränk übernommen und lässt "
        "sich direkt danach korrigieren.",
    "Peak %@": "Höchstwert %@",
    "%@ added": "%@ hinzugefügt",
    "Save": "Sichern",
    "Undo": "Rückgängig",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Backup",
    "Export a backup": "Backup exportieren",
    "Import a backup": "Backup importieren",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Ein Backup enthält alle Personen, Sitzungen und Getränke. Beim Import wird nur "
        "ergänzt, was fehlt – vorhandene Daten werden nie geändert oder entfernt.",
    "Import this backup?": "Dieses Backup importieren?",
    "Import": "Importieren",
    "Everything in this backup is already here.":
        "Alles aus diesem Backup ist bereits vorhanden.",
    "Import finished": "Import abgeschlossen",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Sprache",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Öffnet diese App in den Einstellungen, wo „Bevorzugte Sprache“ die Sprache der App "
        "festlegt – die des Systems bleibt, wie sie ist. iOS startet die App neu, wenn du sie "
        "änderst.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Import nicht möglich",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Diese Datei ist kein LogMyDrink-Backup oder sie ist beschädigt.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Dieses Backup wurde mit einer neueren Version von LogMyDrink erstellt. Aktualisiere "
        "die App und versuch es erneut.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Fügt %@ Sitzungen, %@ Getränke und %@ Monatssummen hinzu. Vorhandenes wird nicht geändert oder entfernt.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': '%@ Sitzungen, %@ Getränke und %@ Monatssummen hinzugefügt.',
    'months as totals': 'Monate nur als Summe',
    'by month only': 'nur monatsweise',
    'monthly total': 'Monatssumme',
    'No daily records for this day': 'Keine Tagesaufzeichnungen für diesen Tag',
    'Monthly total: %@': 'Monatssumme: %@',
    'A dry month': 'Ein trockener Monat',

    # --- RemovePersonSection ---
    'Remove %@?': '%@ entfernen?',
    'Remove': 'Entfernen',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Löscht %@ Sitzungen, %@ Getränke und %@ Monatssummen. Das lässt sich nicht rückgängig machen.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Löscht %@ Sitzungen und %@ Getränke. Das lässt sich nicht rückgängig machen.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Streiche bei einem Gast nach links, um ihn mit allem zu entfernen, was unter ihm aufgezeichnet wurde. Du selbst kannst nicht entfernt werden.',
    'People': 'Personen',
    'Owner': 'Besitzer',
    'Everyone this app records. Switch, add, or remove someone.': 'Alle, die diese App aufzeichnet. Wechseln, hinzufügen oder entfernen.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Übertrag vom Vorabend',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorien',
    'Sessions': 'Sitzungen',
    'Per session': 'Pro Sitzung',
    'Under the influence': 'Unter Alkoholeinfluss',
    '%@ of the time': '%@ der Zeit',
    'Days over limit': 'Tage über dem Limit',
    'Longest sober run': 'Längste trockene Phase',
    'Favourite drink': 'Lieblingsgetränk',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Anzeige & Sprache",
    "Data": "Daten",
    "Concentration": "Konzentration",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Überlass die Rate der Frage nach der Häufigkeit, es sei denn, du hast einen Messwert, an dem du sie ausrichten kannst.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Schätzung, keine Messung. Entscheide niemals anhand dieser App, ob du fahren kannst.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Geschätzter Bereich, keine Messung. Entscheide niemals anhand dieser App, ob du fahren kannst.',
    'How does the app calculate this?':
        'Wie berechnet die App das?',
    'approximately %@ %@':
        'ungefähr %@ %@',
    'How it works':
        'So funktioniert’s',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Entscheide niemals anhand dieser App, ob du fahren kannst. Die App schätzt, sie misst nicht, und dein tatsächlicher Wert kann erheblich abweichen.',
    'Why this app exists':
        'Wozu diese App',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink hilft dir, bewusster zu trinken und die Kontrolle zu behalten. Die Entscheidung fällt vor dem nächsten Glas – deshalb zeigt dir die App vorab, wohin ein weiteres Getränk deinen Alkoholspiegel bringen würde und wann er seinen Höchstwert erreicht.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Es geht aber nicht nur um heute Abend. Jedes eingetragene Getränk landet in deinem Verlauf, sodass du über Monate und Jahre siehst, wie viel, wie oft und wie hoch du trinkst. Daraus werden deine Muster sichtbar – und auch, in welche Richtung sie sich entwickeln, ob zum Besseren oder zum Schlechteren.',
    'How it calculates':
        'So wird gerechnet',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Die Schätzung beruht auf der Widmark-Methode, mit der der Blutalkohol seit den 1930er-Jahren geschätzt wird; die App verwendet eine verfeinerte Fassung davon.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Aus Gewicht, Größe, Alter und Geschlecht berechnet sie, wie viel Wasser dein Körper enthält, denn darin verteilt sich der Alkohol. Jedes Getränk wird einzeln verfolgt: wie viel Alkohol es enthielt, wie schnell du es getrunken hast und wie viel du gegessen hattest – davon hängt ab, wie schnell es aufgenommen wird.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Währenddessen baut deine Leber pro Stunde eine ungefähr gleichbleibende Menge ab; wie viel bei dir, wird aus deiner Trinkhäufigkeit geschätzt. So entsteht Minute für Minute eine Kurve: wo du jetzt stehst, wohin es geht und wann du wieder bei null bist.',
    'Details':
        'Details',
    'Body water':
        'Körperwasser',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Die Watson-Formel (1980) aus Gewicht, Größe, Alter und Geschlecht. Die Formel für Frauen enthält kein Alter – eine Eigenschaft der Formel, kein Fehler. Das Verteilungsvolumen ist das Körperwasser geteilt durch 0,85, den Wasseranteil des Blutes.',
    'Absorption':
        'Aufnahme',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Jedes Getränk hat seinen eigenen „Magen“. Auf leeren Magen wird die Hälfte des Alkohols in etwa 7 Minuten aufgenommen, auf vollen in etwa 21. Ein Getränk, an dem du nippst, gelangt gleichmäßig über die Trinkdauer in den Magen.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Ergibt einen niedrigeren Höchstwert und einen früheren Nullpunkt. Überraschend, aber gemessen: Mit Essen baut der Magen einen Teil des Alkohols ab, bevor er aufgenommen wird (die App rechnet mit 5, 10 und 15 Prozent), und was nie ins Blut gelangt, muss nicht abgebaut werden.',
    'Elimination':
        'Abbau',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Etwa 0,15 ‰ pro Stunde (Literaturbereich 0,10–0,25), bei regelmäßigem Trinken höher, weil sich die Leberenzyme anpassen. Nahe null verlangsamt sich der Abbau (Michaelis-Menten-Kinetik), sodass die Kurve sanft ausläuft, statt abrupt abzubrechen.',
    'Computation':
        'Berechnung',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Die Kurve stammt aus einer numerischen Simulation mit minütlicher Auflösung.',
    'Why it is only an estimate':
        'Warum es nur eine Schätzung ist',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Die App misst nichts. Was sie zeigt, ist das Ergebnis eines Modells mit Durchschnittswerten, und die Wirklichkeit kann abweichen. Die größte Unbekannte ist, wie schnell du Alkohol abbaust: Innerhalb des plausiblen Bereichs kann allein das den Höchstwert um 40 Prozent und den Nullpunkt um vier Stunden am selben Abend verschieben.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Auch Genetik, Lebergesundheit, Medikamente, Essen, Schlaf und Müdigkeit spielen eine Rolle – nichts davon kennt die App. Einen genauen Wert liefert nur ein geeichtes Atemalkoholmessgerät oder ein Bluttest.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Die Zahl ist trotzdem nützlich. Liegt die App bei dir durchgehend etwas zu hoch oder zu niedrig, irrt sie jeden Abend in dieselbe Richtung – so lernst du mit der Zeit, was ein bestimmter Wert für dich bedeutet. Im Profil kannst du auch die Unsicherheit der Abbaurate einblenden: Dann siehst du einen Bereich statt einer einzelnen Zahl.',
    'Tips':
        'Tipps',
    'Favourite drink in one tap':
        'Lieblingsgetränk mit einem Tippen',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Lege im Profil ein Lieblingsgetränk fest, und die Taste auf „Live“ trägt es mit einem einzigen Tippen ein.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Füge es deinem Sperrbildschirm oder Home-Bildschirm hinzu: Ein Tippen trägt dein Lieblingsgetränk ein. Mit Pro zeigt es, solange Alkohol in deinem Körper ist, auch deinen Alkoholspiegel und wohin er sich bewegt.',
    'How do I add it?':
        'Wie füge ich es hinzu?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Sag „Hey Siri, LogMyDrink now“, und Siri trägt dein Lieblingsgetränk ein und sagt dir, wohin sich dein Höchstwert entwickelt. (Der Befehl funktioniert auf Englisch.)',
    'Looking back':
        'Zurückblicken',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Gestern“ oben auf „Live“ bringt dich mit einem Tippen zum Vortag; der Tab „Verlauf“ zeigt deine Muster über Wochen, Monate und Jahre.',
    'Logging later':
        'Nachträglich eintragen',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Wenn du ein Getränk nachträglich einträgst, stell die Zeit mit den Tasten − und + zurück; einen vergessenen Tag kannst du im Verlauf in der Ansicht „Tag“ nachtragen.',
    'One tap and done':
        'Einmal tippen, fertig',
    'Your favourite from the Lock Screen':
        'Dein Lieblingsgetränk vom Sperrbildschirm',
    'Say it, don’t type it':
        'Sag es, statt zu tippen',
    'See your patterns':
        'Sieh dir deine Muster an',
    'Set what you drink most often and log it with a single tap.':
        'Lege fest, was du am häufigsten trinkst, und trag es mit einem einzigen Tippen ein.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Ein Tippen auf das Widget trägt dein Lieblingsgetränk ein, ohne dass du die App suchen musst. Abends zeigt es auch deinen Alkoholspiegel.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now“ – Siri trägt dein Lieblingsgetränk ein und sagt dir, wohin sich dein Höchstwert entwickelt.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Der Verlauf zeigt, wie viel und wie hoch du über Wochen, Monate und Jahre trinkst – und wohin es sich entwickelt.',
    'Set favourite':
        'Lieblingsgetränk festlegen',
    'Add widget':
        'Widget hinzufügen',
    'Got it':
        'Verstanden',
    'Open History':
        'Verlauf öffnen',
    'Don’t show again':
        'Nicht mehr anzeigen',
    'Lock Screen':
        'Sperrbildschirm',
    'Home Screen':
        'Home-Bildschirm',
    'Where':
        'Wo',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Sperre dein iPhone und halte dann den Sperrbildschirm gedrückt.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Tippe auf „Anpassen“, dann auf „Sperrbildschirm“ und dann auf die Widget-Zeile unter der Uhr.',
    'Choose LogMyDrink, then tap Done.':
        'Wähle LogMyDrink und tippe auf „Fertig“.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Halte eine leere Stelle des Home-Bildschirms gedrückt, bis die Apps wackeln.',
    'Tap Edit, then Add Widget.':
        'Tippe auf „Bearbeiten“ und dann auf „Widget hinzufügen“.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Suche nach LogMyDrink, wähle eine Größe und tippe auf „Widget hinzufügen“.',
    'A tap on the widget opens the app and logs your favourite drink. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Ein Tippen auf das Widget öffnet die App und trägt dein Lieblingsgetränk ein. Mit Pro zeigt es, solange Alkohol in deinem Körper ist, auch deinen Alkoholspiegel und wohin er sich bewegt.',
    'Add the widget':
        'Widget hinzufügen',
    'Show tips':
        'Tipps anzeigen',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Höchstens ein Tipp pro Tag beim Öffnen der App – nie, solange Alkohol in deinem Körper ist.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Was die Zahl zeigt',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Die Zahl ist eine Schätzung deiner Blutalkoholkonzentration (englisch BAC, blood alcohol concentration): wie viel Alkohol in deinem Blut ist.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'In Promille (‰) sind es Gramm Alkohol pro Liter Blut: 0,5 ‰ bedeutet ein halbes Gramm in jedem Liter. In Prozent sind es Gramm pro 100 Milliliter, derselbe Wert ist also ein Zehntel so groß: 0,5 ‰ sind 0,05 Prozent. Umschalten kannst du unter Profil › Anzeige & Sprache.',
    'The curve shows the same level over time, minute by minute.':
        'Die Kurve zeigt denselben Wert im Zeitverlauf, Minute für Minute.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promille (‰) sind Gramm Alkohol pro Liter Blut, Prozent sind Gramm pro 100 Milliliter: 0,5 ‰ sind 0,05 Prozent.',

    # --- ProPaywallSheet: plans and buying ---
    "Prices could not be loaded.": "Die Preise konnten nicht geladen werden.",
    "Try again": "Erneut versuchen",
    "Save %@": "%@ sparen",
    "About %@ a month": "Etwa %@ im Monat",
    "Yearly": "Jährlich",
    "Monthly": "Monatlich",
    "%@ / year": "%@ / Jahr",
    "%@ / month": "%@ / Monat",
    "Start my free month": "Gratismonat starten",
    "Subscribe": "Abonnieren",
    "Free for one month, then %@ a year.": "Einen Monat gratis, danach %@ pro Jahr.",
    "Free for one month, then %@ a month.": "Einen Monat gratis, danach %@ pro Monat.",
    "%@ a year.": "%@ pro Jahr.",
    "%@ a month.": "%@ pro Monat.",
    "Renews automatically until you cancel. Cancel anytime in Settings.": "Verlängert sich automatisch, bis du kündigst. Jederzeit in den Einstellungen kündbar.",
    "Restore purchases": "Käufe wiederherstellen",
    "Redeem code": "Code einlösen",
    "Terms of Use": "Nutzungsbedingungen",
    "Privacy Policy": "Datenschutz",
    "Waiting for approval. Pro opens as soon as the purchase goes through.": "Wartet auf Freigabe. Pro wird freigeschaltet, sobald der Kauf durch ist.",
    "The purchase did not go through. Please try again.": "Der Kauf hat nicht geklappt. Bitte versuch es noch einmal.",
    "No active subscription was found for this Apple ID.": "Für diese Apple-ID wurde kein aktives Abo gefunden.",
}
