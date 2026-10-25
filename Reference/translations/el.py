"""
Greek.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Τοις χιλίοις",
    "Percent": "Τοις εκατό",

    # --- DrinkCatalog: drink types ---
    "Beer": "Μπίρα",
    "Wine": "Κρασί",
    "Champagne": "Αφρώδες",
    "Shot": "Σφηνάκι",
    "Cocktail": "Κοκτέιλ",
    "Custom": "Προσαρμοσμένο",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Άδειο στομάχι",
    "Moderately full": "Μέτρια γεμάτο",
    "Full stomach": "Γεμάτο στομάχι",
    "Empty": "Άδειο",
    "Moderate": "Μέτριο",
    "Full": "Γεμάτο",
    "Fast absorption, higher and earlier peak.":
        "Γρήγορη απορρόφηση, υψηλότερη και πιο πρώιμη αιχμή.",
    "Moderate absorption.": "Μέτρια απορρόφηση.",
    "Slow absorption, lower and later peak.":
        "Αργή απορρόφηση, χαμηλότερη και πιο όψιμη αιχμή.",

    # --- DrinkingFrequency ---
    "Rarely": "Σπάνια",
    "A few times a month": "Λίγες φορές τον μήνα",
    "Several times a week": "Αρκετές φορές την εβδομάδα",
    "Almost daily": "Σχεδόν καθημερινά",
    "A few occasions a year": "Λίγες φορές τον χρόνο",
    "Social drinking": "Κοινωνική κατανάλωση",
    "Weekly routine": "Εβδομαδιαία συνήθεια",
    "Daily or nearly daily": "Καθημερινά ή σχεδόν καθημερινά",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Ώρα",
    "Level": "Επίπεδο",
    "Lower": "Κάτω",
    "Upper": "Άνω",
    "Lower estimate": "Χαμηλή εκτίμηση",
    "Upper estimate": "Υψηλή εκτίμηση",
    "Personal limit": "Προσωπικό όριο",
    "Drink": "Ποτό",

    # --- BACChartView ---
    "Expected peak around %@": "Αναμενόμενη αιχμή γύρω στις %@",
    "Peaked around %@": "Έφτασε στην αιχμή γύρω στις %@",
    "No active session": "Καμία ενεργή βραδιά",
    "Still rising": "Ακόμη ανεβαίνει",
    "YOUR LIMIT %@": "ΤΟ ΟΡΙΟ ΣΟΥ %@",
    "possible range": "πιθανό εύρος",

    # --- Live screen: the day with nothing on it ---
    "Live": "Ζωντανά",
    "Nothing logged today": "Καμία καταγραφή σήμερα",
    "Add a drink when you have one.": "Πρόσθεσε ένα ποτό όταν πιεις κάτι.",

    # --- Tabs and history ---
    "History": "Ιστορικό",
    "No past sessions yet": "Δεν υπάρχουν ακόμη προηγούμενες βραδιές",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Μια βραδιά εμφανίζεται εδώ μόλις ολοκληρωθεί — όταν το επίπεδό σου έχει μηδενιστεί "
        "και έχουν περάσει μερικές ώρες.",
    "%@ drinks": "%@ ποτά",
    "peak": "αιχμή",
    "Started": "Ξεκίνησε",
    "Lasted": "Διήρκεσε",
    "Duration": "Διάρκεια",
    "Sober around": "Νηφάλιος περίπου",
    "Sober at": "Νηφάλιος",
    "Remaining": "Απομένει",
    "next day": "την επόμενη μέρα",
    "previous day": "την προηγούμενη μέρα",
    "%@ days later": "%@ μέρες μετά",
    "%@ days earlier": "%@ μέρες πριν",
    "Calculated with your profile at the time":
        "Υπολογίστηκε με το προφίλ που είχες τότε",

    # --- TodayView ---
    "Profile": "Προφίλ",
    "Drinks": "Ποτά",
    "Units": "Μονάδες",
    "Drinks this session": "Ποτά αυτή τη βραδιά",
    "Add drink": "Προσθήκη ποτού",

    # --- Editing an already logged drink ---
    "Edit drink": "Επεξεργασία ποτού",
    "Save changes": "Αποθήκευση αλλαγών",
    "With this": "Με αυτό",
    "Delete": "Διαγραφή",
    "tap to edit · swipe to delete": "πάτα για επεξεργασία · σύρε για διαγραφή",

    # --- Drinking pace ---
    "How fast": "Πόσο γρήγορα",
    "In one go": "Μονορούφι",
    "Counts as a single swallow — the steepest possible rise.":
        "Μετράει ως μία γουλιά — η πιο απότομη δυνατή άνοδος.",
    "A quick drink. The level climbs fast.": "Γρήγορο ποτό. Το επίπεδο ανεβαίνει γρήγορα.",
    "A normal pace.": "Κανονικός ρυθμός.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Πίνεται αργά. Πολύ πιο ήπια άνοδος για το ίδιο αλκοόλ.",

    # --- AddDrinkSheet ---
    "Cancel": "Άκυρο",
    "Now": "Τώρα",
    "Projected peak": "Προβλεπόμενη αιχμή",
    "Peak at": "Αιχμή στις",
    "Clears": "Μηδενίζεται",
    "This would cross your limit": "Θα ξεπερνούσες το όριό σου",
    "Around %@, for up to %@.": "Γύρω στις %@, για έως και %@.",
    "This might cross your limit": "Μπορεί να ξεπεράσεις το όριό σου",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Με πιο αργό μεταβολισμό ναι, με πιο γρήγορο όχι. Αυτή είναι η αβεβαιότητα της "
        "εκτίμησης.",
    "Type": "Τύπος",
    "Amount": "Ποσότητα",
    "Strength": "Περιεκτικότητα σε αλκοόλ",
    "%@ units": "%@ μονάδες",
    "%@ g alcohol": "%@ g αλκοόλ",
    "Stomach": "Στομάχι",
    "When": "Πότε",
    "Done": "Τέλος",
    "Add": "Προσθήκη",

    # --- ProfileSheet ---
    "Male": "Άνδρας",
    "Female": "Γυναίκα",
    "Sex": "Φύλο",
    "Weight": "Βάρος",
    "Height": "Ύψος",
    "Age": "Ηλικία",
    "kg": "kg",
    "cm": "cm",
    "yrs": "έτη",
    "Body": "Σώμα",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Το ολικό σωματικό νερό προκύπτει από τις εξισώσεις Watson, οι οποίες ορίζουν τον όγκο "
        "στον οποίο κατανέμεται το αλκοόλ.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Το ολικό σωματικό νερό προκύπτει από τις εξισώσεις Watson, οι οποίες ορίζουν τον όγκο "
        "στον οποίο κατανέμεται το αλκοόλ. Η εξίσωση για τις γυναίκες δεν περιλαμβάνει την "
        "ηλικία, οπότε η αλλαγή της δεν θα επηρεάσει το αποτέλεσμα.",
    "Drinking frequency": "Συχνότητα κατανάλωσης",
    "How often do you drink?": "Πόσο συχνά πίνεις;",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Έτσι εκτιμούμε τον ρυθμό αποβολής σου. Η τακτική κατανάλωση επάγει το μονοπάτι CYP2E1 του ήπατος, οπότε όσοι πίνουν συχνά αποβάλλουν το αλκοόλ γρηγορότερα. Είναι το πιο αδύναμο σημείο του μοντέλου, γι’ αυτό μπορείς να ορίσεις στην ενότητα «Εμφάνιση και γλώσσα» πόση από αυτή την αβεβαιότητα σού δείχνει η εφαρμογή.",
    "Your limit": "Το όριό σου",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Ο δικός σου αριθμός αναφοράς, όχι νόμιμο όριο. Η εφαρμογή σού λέει πότε ένα ποτό που "
        "σχεδιάζεις θα σε περνούσε πάνω από αυτό και για πόση ώρα θα έμενες από πάνω.",
    "Calculated values": "Υπολογισμένες τιμές",
    "Total body water": "Ολικό σωματικό νερό",
    "Distribution volume": "Όγκος κατανομής",
    "Widmark factor": "Παράγοντας Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Ο παράγοντας Widmark είναι συνήθως γύρω στο 0,68 για τους άνδρες και 0,55 για τις "
        "γυναίκες. Αν ο δικός σου απέχει πολύ από αυτά, αξίζει να ελέγξεις τις παραπάνω τιμές.",
    "Elimination rate": "Ρυθμός αποβολής",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Πόσο γρήγορα το συκώτι σου αποβάλλει το αλκοόλ αφού απορροφηθεί — η κλίση της "
        "κατιούσας πλευράς της καμπύλης.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Το αλκοόλ αποβάλλεται σε περίπου σταθερή ποσότητα ανά ώρα και όχι ως ποσοστό, επειδή "
        "το ένζυμο που το διασπά λειτουργεί ήδη στο μέγιστο σχεδόν σε κάθε επίπεδο. Γι’ αυτό "
        "υπάρχουν εξαρχής εμπειρικοί κανόνες όπως «ένα ποτό την ώρα».",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Με αυτή τη ρύθμιση, %@ χρειάζεται περίπου %@ για να μηδενιστεί. Σχεδόν όλοι "
        "βρίσκονται μεταξύ %@ ανά ώρα.",
    "How to find yours": "Πώς να βρεις τον δικό σου",
    "With a breathalyser": "Με αλκοτέστ",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Φύσα δύο φορές, με απόσταση τουλάχιστον μίας ώρας, στην κατιούσα πλευρά — δύο ώρες ή "
        "περισσότερο μετά το τελευταίο σου ποτό, χωρίς να πιεις τίποτα ενδιάμεσα. Αφαίρεσε τη δεύτερη "
        "ένδειξη από την πρώτη και διαίρεσε με τις ώρες που μεσολάβησαν.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Για παράδειγμα, %@ και, δύο ώρες αργότερα, %@ βγάζει %@ ανά ώρα.",
    "Without one": "Χωρίς αλκοτέστ",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Η εφαρμογή σού λέει πότε αναμένει να μηδενιστεί το επίπεδό σου. Αν σταθερά επανέρχεσαι στο "
        "φυσιολογικό αρκετά πριν από τότε, ο ρυθμός σου είναι υψηλότερος από τη ρύθμιση — "
        "ανέβασέ την ένα βήμα και παρακολούθησε για μερικές βραδιές. Αν χρειάζεται περισσότερο "
        "απ’ ό,τι προβλέπεται, κατέβασέ την.",
    "What moves it": "Τι τον μεταβάλλει",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Η τακτική κατανάλωση τον αυξάνει: το ηπατικό ένζυμο που κάνει τη δουλειά επάγεται από "
        "τη χρήση. Είναι επίσης κατά μέσο όρο ελαφρώς υψηλότερος στις γυναίκες και χαμηλότερος "
        "με άδειο στομάχι ή όταν υπάρχουν προβλήματα στο συκώτι.",
    "Uncertainty": "Αβεβαιότητα",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Στο μηδέν κάθε τιμή είναι ένας μόνο αριθμός — η καλύτερη εκτίμηση της εφαρμογής. Πάνω "
        "από το μηδέν οι ίδιες τιμές εμφανίζονται ως εύρη και η ζώνη στο γράφημα πλαταίνει "
        "ανάλογα.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Με έναν μόνο αριθμό μαθαίνεις πιο εύκολα: με τον καιρό ανακαλύπτεις πώς νιώθεις στο "
        "δικό σου 0,6. Το εύρος είναι η πιο κυριολεκτική απάντηση, γιατί ο ρυθμός είναι όντως "
        "αβέβαιος. Και τα δύο στέκουν — η επιλογή είναι δική σου.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Η διασπορά που προκύπτει από τη συχνότητα κατανάλωσής σου είναι ± %@ ανά ώρα.",
    "Rate": "Ρυθμός",
    "Range": "Εύρος",
    "Advanced": "Για προχωρημένους",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Week": "Εβδομάδα",
    "Month": "Μήνας",
    "Year": "Έτος",
    "Sober days": "Ημέρες χωρίς αλκοόλ",
    "Change": "Μεταβολή",
    "before records": "πριν από την έναρξη καταγραφής",
    "See further back": "Δες πιο πίσω",
    "Weeks, months and years side by side — and every evening older than seven days.": "Εβδομάδες, μήνες και χρόνια το ένα δίπλα στο άλλο — και κάθε βραδιά παλαιότερη από επτά ημέρες.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Όλα όσα έχεις καταγράψει είναι ήδη αποθηκευμένα. Το ξεκλείδωμα απλώς τα εμφανίζει.",
    "Back up and restore": "Αντίγραφο ασφαλείας και επαναφορά",
    "Log for friends too": "Κατέγραψε και για φίλους",
    "Switch to someone else in one tap and log their drinks with their own body and limit — each person gets their own curve and history.": "Άλλαξε σε κάποιον άλλον με ένα πάτημα και κατέγραψε τα ποτά του με το δικό του σώμα και όριο – κάθε άτομο έχει τη δική του καμπύλη και ιστορικό.",
    "Save everything to a file, and read a backup back in — on this phone or on a new one.": "Αποθήκευσε τα πάντα σε ένα αρχείο και φόρτωσε ξανά ένα αντίγραφο ασφαλείας – σε αυτό το τηλέφωνο ή σε ένα καινούργιο.",
    "Backup and restore are part of Pro.": "Το αντίγραφο ασφαλείας και η επαναφορά είναι μέρος του Pro.",
    "Today": "Σήμερα",
    "Day": "Ημέρα",
    "Yesterday": "Χθες",
    "No drinks on this day": "Κανένα ποτό αυτή την ημέρα",
    "Trend": "Τάση",
    "day": "ημέρα",
    "Smoothing": "Εξομάλυνση",
    "%@ sessions": "%@ βραδιές",
    "No data before %@": "Δεν υπάρχουν δεδομένα πριν από %@",
    "vs.": "έναντι",
    "Grams": "Γραμμάρια",
    "Grams of alcohol": "Γραμμάρια αλκοόλ",
    "Standard units": "Τυπικές μονάδες",
    "Unit size": "Μέγεθος μονάδας",
    "Automatic": "Αυτόματα",
    "UK": "Ηνωμένο Βασίλειο",
    "Nordic countries": "Σκανδιναβικές χώρες",
    "US standard drink": "Τυπικό ποτό ΗΠΑ",
    "WHO, most of Europe": "ΠΟΥ, το μεγαλύτερο μέρος της Ευρώπης",
    "Period": "Περίοδος",
    "Switch person": "Αλλαγή ατόμου",
    "Add person": "Προσθήκη ατόμου",
    "New person": "Νέο άτομο",
    "You": "Εσύ",
    "Name": "Όνομα",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Και τα τέσσερα αλλάζουν την καμπύλη, οπότε κανένα δεν μπορεί να μαντευτεί για κάποιον "
        "άλλον.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Το δικό τους όριο και οι λεπτομερέστερες ρυθμίσεις μπορούν να αλλάξουν αργότερα στην "
        "καρτέλα «Προφίλ», όσο είναι το επιλεγμένο άτομο.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Γρήγορη προσθήκη",
    "Choose a favourite drink": "Διάλεξε ένα αγαπημένο ποτό",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Διάλεξε το ποτό που συνήθως παραγγέλνεις και ένα κουμπί στην οθόνη «Ζωντανά» θα το "
        "καταγράφει με ένα πάτημα.",
    "This is your quick-add drink": "Αυτό είναι το ποτό γρήγορης προσθήκης σου",
    "Set as my quick-add drink": "Ορισμός ως ποτό γρήγορης προσθήκης",
    "This is now your usual": "Αυτό είναι πλέον το συνηθισμένο σου",
    "Remove favourite": "Αφαίρεση αγαπημένου",
    "Always add this one": "Να προστίθεται πάντα αυτό",
    "Logs it straight away, without opening anything.":
        "Το καταγράφει αμέσως, χωρίς να ανοίξει τίποτα.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Ένα πάτημα στην οθόνη «Ζωντανά» το καταγράφει, με την προβλεπόμενη αιχμή πάνω στο "
        "κουμπί. Το πόσο γεμάτο είναι το στομάχι σου προκύπτει από το προηγούμενο ποτό και "
        "μπορεί να διορθωθεί αμέσως μετά.",
    "Peak %@": "Αιχμή %@",
    "%@ added": "Προστέθηκε %@",
    "Save": "Αποθήκευση",
    "Undo": "Αναίρεση",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Αντίγραφο ασφαλείας",
    "Export a backup": "Εξαγωγή αντιγράφου ασφαλείας",
    "Import a backup": "Εισαγωγή αντιγράφου ασφαλείας",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Ένα αντίγραφο ασφαλείας περιέχει κάθε άτομο, βραδιά και ποτό. Η εισαγωγή προσθέτει "
        "ό,τι λείπει — δεν αλλάζει και δεν αφαιρεί ποτέ κάτι που υπάρχει ήδη εδώ.",
    "Import this backup?": "Εισαγωγή αυτού του αντιγράφου ασφαλείας;",
    "Import": "Εισαγωγή",
    "Everything in this backup is already here.":
        "Όλα όσα περιέχει αυτό το αντίγραφο ασφαλείας υπάρχουν ήδη εδώ.",
    "Import finished": "Η εισαγωγή ολοκληρώθηκε",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Γλώσσα",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Ανοίγει αυτή την εφαρμογή στις Ρυθμίσεις, όπου η «Προτιμώμενη γλώσσα» ορίζει τη "
        "γλώσσα της ίδιας της εφαρμογής — η γλώσσα του συστήματος παραμένει ως έχει. Το iOS κάνει "
        "επανεκκίνηση της εφαρμογής όταν την αλλάζεις.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Δεν ήταν δυνατή η εισαγωγή",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Αυτό το αρχείο δεν είναι αντίγραφο ασφαλείας του LogMyDrink ή είναι κατεστραμμένο.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Αυτό το αντίγραφο ασφαλείας δημιουργήθηκε από νεότερη έκδοση του LogMyDrink. "
        "Ενημέρωσε την εφαρμογή και δοκίμασε ξανά.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Προσθέτει %@ βραδιές, %@ ποτά και %@ μηνιαία σύνολα. Τίποτα από όσα υπάρχουν ήδη δεν αλλάζει ούτε αφαιρείται.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Προστέθηκαν %@ βραδιές, %@ ποτά και %@ μηνιαία σύνολα.',
    'months as totals': 'μήνες μόνο ως σύνολα',
    'by month only': 'μόνο ανά μήνα',
    'monthly total': 'μηνιαίο σύνολο',
    'No daily records for this day': 'Δεν υπάρχουν ημερήσιες εγγραφές για αυτή τη μέρα',
    'Monthly total: %@': 'Μηνιαίο σύνολο: %@',
    'A dry month': 'Ένας μήνας χωρίς αλκοόλ',

    # --- RemovePersonSection ---
    'Remove %@?': 'Να αφαιρεθεί ο/η %@;',
    'Remove': 'Αφαίρεση',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Διαγράφει %@ βραδιές, %@ ποτά και %@ μηνιαία σύνολα. Αυτό δεν μπορεί να αναιρεθεί.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Διαγράφει %@ βραδιές και %@ ποτά. Αυτό δεν μπορεί να αναιρεθεί.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Σύρε αριστερά σε έναν επισκέπτη για να τον αφαιρέσεις μαζί με ό,τι έχει καταγραφεί για εκείνον. Εσύ δεν μπορείς να αφαιρεθείς.',
    'People': 'Άτομα',
    'Owner': 'Κάτοχος',
    'Everyone this app records. Switch, add, or remove someone.': 'Όλοι όσους καταγράφει αυτή η εφαρμογή. Άλλαξε, πρόσθεσε ή αφαίρεσε κάποιον.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Μεταφέρθηκε από την προηγούμενη βραδιά',
    # --- History, second card (5.24) ---
    'Calories': 'Θερμίδες',
    'Sessions': 'Βραδιές',
    'Per session': 'Ανά βραδιά',
    'Under the influence': 'Υπό την επήρεια αλκοόλ',
    '%@ of the time': '%@ του χρόνου',
    'Days over limit': 'Ημέρες πάνω από το όριο',
    'Longest sober run': 'Μεγαλύτερο διάστημα χωρίς αλκοόλ',
    'Favourite drink': 'Αγαπημένο ποτό',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Εμφάνιση και γλώσσα",
    "Data": "Δεδομένα",
    "Concentration": "Συγκέντρωση",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Άφησε τον ρυθμό να καθορίζεται από την ερώτηση για τη συχνότητα, εκτός αν έχεις μέτρηση για να τον συγκρίνεις.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Εκτίμηση, όχι μέτρηση. Μη βασίζεσαι ποτέ σε αυτήν για να αποφασίσεις αν μπορείς να οδηγήσεις.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Εκτιμώμενο εύρος, όχι μέτρηση. Μη βασίζεσαι ποτέ σε αυτό για να αποφασίσεις αν μπορείς να οδηγήσεις.',
    'How does the app calculate this?':
        'Πώς το υπολογίζει η εφαρμογή;',
    'approximately %@ %@':
        'περίπου %@ %@',
    'How it works':
        'Πώς λειτουργεί',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Μη βασίζεσαι ποτέ σε αυτό για να αποφασίσεις αν μπορείς να οδηγήσεις. Η εφαρμογή εκτιμά, δεν μετρά, και το πραγματικό σου επίπεδο μπορεί να διαφέρει σημαντικά.',
    'Why this app exists':
        'Γιατί υπάρχει αυτή η εφαρμογή',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'Το LogMyDrink σε βοηθά να πίνεις πιο συνειδητά και να διατηρείς τον έλεγχο. Η απόφαση παίρνεται πριν από το επόμενο ποτήρι, γι’ αυτό η εφαρμογή σού δείχνει από πριν πού θα πήγαινε το επίπεδό σου με ένα ακόμη ποτό και πότε θα έφτανε στην αιχμή.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Δεν αφορά όμως μόνο την αποψινή βραδιά. Κάθε ποτό που καταγράφεις μπαίνει στο Ιστορικό, οπότε μέσα σε μήνες και χρόνια βλέπεις πόσο πίνεις, πόσο συχνά και πόσο ψηλά φτάνει το επίπεδό σου. Από εκεί αναδύονται τα μοτίβα σου, αλλά και η κατεύθυνση προς την οποία κινούνται — αν τα πράγματα βελτιώνονται ή χειροτερεύουν.',
    'How it calculates':
        'Πώς υπολογίζει',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Η εκτίμηση βασίζεται στη μέθοδο Widmark, που χρησιμοποιείται από τη δεκαετία του 1930 για την εκτίμηση του αλκοόλ στο αίμα· η εφαρμογή χρησιμοποιεί μια βελτιωμένη εκδοχή της.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Από το βάρος, το ύψος, την ηλικία και το φύλο σου υπολογίζει πόσο νερό περιέχει το σώμα σου, γιατί εκεί κατανέμεται το αλκοόλ. Παρακολουθεί κάθε ποτό χωριστά: πόσο αλκοόλ είχε, πόσο γρήγορα το ήπιες και πόσο είχες φάει, γιατί αυτό καθορίζει πόσο γρήγορα απορροφάται.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Στο μεταξύ, το συκώτι διασπά κάθε ώρα μια περίπου σταθερή ποσότητα· η δική σου εκτιμάται από το πόσο συχνά πίνεις. Το αποτέλεσμα είναι μια καμπύλη, λεπτό προς λεπτό: πού βρίσκεσαι τώρα, πού πας και πότε θα είσαι πάλι στο μηδέν.',
    'Details':
        'Λεπτομέρειες',
    'Body water':
        'Νερό σώματος',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Ο τύπος του Watson (1980), με βάση το βάρος, το ύψος, την ηλικία και το φύλο. Ο τύπος για γυναίκες δεν περιέχει την ηλικία — είναι ιδιότητα του τύπου, όχι σφάλμα. Ο όγκος κατανομής είναι το νερό του σώματος διαιρεμένο με 0,85, την περιεκτικότητα του αίματος σε νερό.',
    'Absorption':
        'Απορρόφηση',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Κάθε ποτό έχει το δικό του «στομάχι». Με άδειο στομάχι το μισό αλκοόλ απορροφάται σε περίπου 7 λεπτά, με γεμάτο σε περίπου 21. Ένα ποτό που πίνεις γουλιά γουλιά φτάνει στο στομάχι ομοιόμορφα όσο το πίνεις.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Δίνει χαμηλότερη αιχμή και νωρίτερο μηδενισμό. Παράξενο, αλλά επιβεβαιωμένο με μετρήσεις: με φαγητό, το στομάχι διασπά μέρος του αλκοόλ πριν απορροφηθεί (η εφαρμογή χρησιμοποιεί 5, 10 και 15 τοις εκατό), και ό,τι δεν μπήκε ποτέ δεν χρειάζεται να διασπαστεί.',
    'Elimination':
        'Αποβολή',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Περίπου 0,15 ‰ την ώρα (δημοσιευμένο εύρος 0,10–0,25), υψηλότερος σε όσους πίνουν τακτικά, επειδή τα ένζυμα του ήπατος προσαρμόζονται. Κοντά στο μηδέν επιβραδύνεται (κινητική Michaelis–Menten), οπότε η καμπύλη εξασθενεί σταδιακά αντί να σταματά απότομα.',
    'Computation':
        'Υπολογισμός',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Η καμπύλη προκύπτει από αριθμητική προσομοίωση με ανάλυση ενός λεπτού.',
    'Why it is only an estimate':
        'Γιατί είναι μόνο εκτίμηση',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Η εφαρμογή δεν μετρά τίποτα. Αυτό που δείχνει είναι το αποτέλεσμα ενός μοντέλου με μέσες τιμές, και η πραγματικότητα μπορεί να διαφέρει. Ο μεγαλύτερος άγνωστος είναι πόσο γρήγορα διασπάς το αλκοόλ: μέσα στο εύλογο εύρος, μόνο αυτό μπορεί, την ίδια βραδιά, να μεταβάλει την αιχμή κατά 40 τοις εκατό και να μετατοπίσει τον μηδενισμό κατά τέσσερις ώρες.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Μετράνε επίσης η γενετική, η υγεία του ήπατος, τα φάρμακα, τι έφαγες, ο ύπνος και η κούραση — η εφαρμογή δεν γνωρίζει τίποτα από αυτά. Ακριβή τιμή δίνει μόνο πιστοποιημένο αλκοτέστ ή εξέταση αίματος.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Ο αριθμός παραμένει χρήσιμος. Αν η εφαρμογή δείχνει σε σένα σταθερά λίγο παραπάνω ή λίγο λιγότερο, κάνει λάθος προς την ίδια κατεύθυνση κάθε βράδυ, οπότε με τον καιρό μαθαίνεις τι σημαίνει μια τιμή για σένα. Στο Προφίλ μπορείς επίσης να εμφανίσεις την αβεβαιότητα του ρυθμού αποβολής: τότε βλέπεις εύρος αντί για έναν αριθμό.',
    'Tips':
        'Συμβουλές',
    'Favourite drink in one tap':
        'Αγαπημένο ποτό με ένα πάτημα',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Όρισε ένα αγαπημένο στο Προφίλ και το κουμπί στην οθόνη «Ζωντανά» θα το καταγράφει με ένα μόνο πάτημα.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Πρόσθεσέ το στην οθόνη κλειδώματος ή στην οθόνη Αφετηρίας: ένα πάτημα καταγράφει το αγαπημένο σου. Με το Pro, όσο υπάρχει αλκοόλ στον οργανισμό σου, δείχνει και το επίπεδό σου και αν ανεβαίνει ή πέφτει.',
    'How do I add it?':
        'Πώς το προσθέτω;',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Πες «Hey Siri, LogMyDrink now» και η Siri καταγράφει το αγαπημένο σου και μετά σου λέει πού θα φτάσει η αιχμή σου. (Η εντολή λειτουργεί στα αγγλικά.)',
    'Looking back':
        'Αναδρομή',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        'Το «Χθες» στο πάνω μέρος της οθόνης «Ζωντανά» σε πηγαίνει στην προηγούμενη μέρα με ένα πάτημα· η καρτέλα «Ιστορικό» δείχνει τα μοτίβα σου σε εβδομάδες, μήνες και χρόνια.',
    'Logging later':
        'Καταγραφή αργότερα',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Αν καταγράφεις ένα ποτό εκ των υστέρων, γύρνα την ώρα πίσω με τα κουμπιά − και +· μια ξεχασμένη μέρα συμπληρώνεται από την προβολή «Ημέρα» του Ιστορικού.',
    'One tap and done':
        'Ένα πάτημα και τέλος',
    'Your favourite from the Lock Screen':
        'Το αγαπημένο σου από την οθόνη κλειδώματος',
    'Say it, don’t type it':
        'Πες το, μην το πληκτρολογείς',
    'See your patterns':
        'Δες τα μοτίβα σου',
    'Set what you drink most often and log it with a single tap.':
        'Όρισε τι πίνεις πιο συχνά και κατέγραψέ το με ένα μόνο πάτημα.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Ένα πάτημα στο widget καταγράφει το αγαπημένο σου, χωρίς να ψάχνεις την εφαρμογή. Το βράδυ δείχνει και το επίπεδό σου.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '«Hey Siri, LogMyDrink now» — η Siri καταγράφει το αγαπημένο σου και σου λέει πού θα φτάσει η αιχμή σου.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Το Ιστορικό δείχνει πόσο πίνεις και πόσο ψηλά φτάνει το επίπεδό σου σε εβδομάδες, μήνες και χρόνια, και προς τα πού αλλάζει.',
    'Set favourite':
        'Ορισμός αγαπημένου',
    'Add widget':
        'Προσθήκη widget',
    'Got it':
        'Κατάλαβα',
    'Open History':
        'Άνοιγμα Ιστορικού',
    'Don’t show again':
        'Να μην εμφανιστεί ξανά',
    'Lock Screen':
        'Οθόνη κλειδώματος',
    'Home Screen':
        'Οθόνη Αφετηρίας',
    'Where':
        'Πού',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Κλείδωσε το iPhone και μετά άγγιξε παρατεταμένα την οθόνη κλειδώματος.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Πάτησε «Προσαρμογή», μετά «Οθόνη κλειδώματος» και έπειτα τη σειρά widget κάτω από το ρολόι.',
    'Choose LogMyDrink, then tap Done.':
        'Διάλεξε το LogMyDrink και πάτησε «Τέλος».',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Άγγιξε παρατεταμένα ένα κενό σημείο της οθόνης Αφετηρίας μέχρι να αρχίσουν να αναπηδούν τα εικονίδια.',
    'Tap Edit, then Add Widget.':
        'Πάτησε «Επεξεργασία» και μετά «Προσθήκη widget».',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Αναζήτησε το LogMyDrink, διάλεξε μέγεθος και πάτησε «Προσθήκη widget».',
    'A tap on the widget opens the app and logs your favourite drink. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Ένα πάτημα στο widget ανοίγει την εφαρμογή και καταγράφει το αγαπημένο σου ποτό. Με το Pro, όσο υπάρχει αλκοόλ στον οργανισμό σου, δείχνει και το επίπεδό σου και αν ανεβαίνει ή πέφτει.',
    'Add the widget':
        'Προσθήκη του widget',
    'Show tips':
        'Εμφάνιση συμβουλών',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Το πολύ μία συμβουλή την ημέρα, όταν ανοίγεις την εφαρμογή — ποτέ όσο υπάρχει αλκοόλ στον οργανισμό σου.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Τι δείχνει ο αριθμός',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Ο αριθμός είναι μια εκτίμηση της συγκέντρωσης αλκοόλ στο αίμα σου (στα αγγλικά BAC, blood alcohol concentration): πόσο αλκοόλ έχεις στο αίμα σου.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'Σε τοις χιλίοις (‰) είναι γραμμάρια αλκοόλ ανά λίτρο αίματος: 0,5 ‰ σημαίνει μισό γραμμάριο σε κάθε λίτρο. Σε τοις εκατό είναι γραμμάρια ανά 100 χιλιοστόλιτρα, οπότε το ίδιο επίπεδο δίνει δέκα φορές μικρότερο αριθμό: 0,5 ‰ ισοδυναμεί με 0,05 τοις εκατό. Μπορείς να αλλάξεις μεταξύ τους στο Προφίλ › Εμφάνιση και γλώσσα.',
    'The curve shows the same level over time, minute by minute.':
        'Η καμπύλη δείχνει το ίδιο επίπεδο στον χρόνο, λεπτό προς λεπτό.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Το τοις χιλίοις (‰) είναι γραμμάρια αλκοόλ ανά λίτρο αίματος, το τοις εκατό γραμμάρια ανά 100 χιλιοστόλιτρα: 0,5 ‰ ισοδυναμεί με 0,05 τοις εκατό.',

    # --- ProPaywallSheet: plans and buying ---
    "Prices could not be loaded.": "Δεν ήταν δυνατή η φόρτωση των τιμών.",
    "Try again": "Δοκίμασε ξανά",
    "Save %@": "Εξοικονόμησε %@",
    "About %@ a month": "Περίπου %@ τον μήνα",
    "Yearly": "Ετήσια",
    "Monthly": "Μηνιαία",
    "%@ / year": "%@ / έτος",
    "%@ / month": "%@ / μήνα",
    "Start my free month": "Ξεκίνα τον δωρεάν μήνα",
    "Subscribe": "Εγγραφή",
    "Free for one month, then %@ a year.": "Δωρεάν για έναν μήνα, μετά %@ τον χρόνο.",
    "Free for one month, then %@ a month.": "Δωρεάν για έναν μήνα, μετά %@ τον μήνα.",
    "%@ a year.": "%@ τον χρόνο.",
    "%@ a month.": "%@ τον μήνα.",
    "Renews automatically until you cancel. Cancel anytime in Settings.": "Ανανεώνεται αυτόματα μέχρι να την ακυρώσεις. Ακύρωσε όποτε θέλεις από τις Ρυθμίσεις.",
    "Restore purchases": "Επαναφορά αγορών",
    "Redeem code": "Εξαργύρωση κωδικού",
    "Terms of Use": "Όροι χρήσης",
    "Privacy Policy": "Απόρρητο",
    "Waiting for approval. Pro opens as soon as the purchase goes through.": "Αναμένεται έγκριση. Το Pro ξεκλειδώνει μόλις ολοκληρωθεί η αγορά.",
    "The purchase did not go through. Please try again.": "Η αγορά δεν ολοκληρώθηκε. Δοκίμασε ξανά.",
    "No active subscription was found for this Apple ID.": "Δεν βρέθηκε ενεργή συνδρομή για αυτό το Apple ID.",
}
