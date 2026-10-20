"""
French.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Pour mille",
    "Percent": "Pourcentage",

    # --- DrinkCatalog: drink types ---
    "Beer": "Bière",
    "Wine": "Vin",
    "Champagne": "Mousseux",
    "Shot": "Shot",
    "Cocktail": "Cocktail",
    "Custom": "Personnalisé",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Estomac vide",
    "Moderately full": "Moyennement plein",
    "Full stomach": "Estomac plein",
    "Empty": "Vide",
    "Moderate": "Moyen",
    "Full": "Plein",
    "Fast absorption, higher and earlier peak.":
        "Absorption rapide, pic plus haut et plus précoce.",
    "Moderate absorption.": "Absorption modérée.",
    "Slow absorption, lower and later peak.": "Absorption lente, pic plus bas et plus tardif.",

    # --- DrinkingFrequency ---
    "Rarely": "Rarement",
    "A few times a month": "Quelques fois par mois",
    "Several times a week": "Plusieurs fois par semaine",
    "Almost daily": "Presque tous les jours",
    "A few occasions a year": "Quelques fois par an",
    "Social drinking": "Consommation sociale",
    "Weekly routine": "Rythme hebdomadaire",
    "Daily or nearly daily": "Tous les jours ou presque",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Heure",
    "Level": "Taux",
    "Lower": "Basse",
    "Upper": "Haute",
    "Lower estimate": "Estimation basse",
    "Upper estimate": "Estimation haute",
    "Personal limit": "Limite personnelle",
    "Drink": "Verre",

    # --- BACChartView ---
    "Expected peak around %@": "Pic attendu vers %@",
    "Peaked around %@": "Pic atteint vers %@",
    "No active session": "Aucune session en cours",
    "Still rising": "Encore en hausse",
    "YOUR LIMIT %@": "TA LIMITE %@",
    "possible range": "fourchette possible",

    # --- Live screen: the day with nothing on it ---
    "Live": "Direct",
    "Nothing logged today": "Rien d’enregistré aujourd’hui",
    "Add a drink when you have one.": "Ajoute un verre quand tu en bois un.",

    # --- Tabs and history ---
    "History": "Historique",
    "No past sessions yet": "Aucune session passée pour l’instant",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Une session apparaît ici une fois terminée – quand ton taux est redescendu à zéro et "
        "que quelques heures se sont écoulées.",
    "%@ drinks": "%@ verres",
    "peak": "pic",
    "Started": "Début",
    "Lasted": "Durée",
    "Duration": "Durée",
    "Sober around": "Sobre env.",
    "Sober at": "Sobre",
    "Remaining": "Restant",
    "next day": "le lendemain",
    "previous day": "la veille",
    "%@ days later": "%@ jours plus tard",
    "%@ days earlier": "%@ jours plus tôt",
    "Calculated with your profile at the time": "Calculé avec le profil que tu avais alors",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Verres",
    "Units": "Unités",
    "Drinks this session": "Verres de cette session",
    "Add drink": "Ajouter un verre",

    # --- Editing an already logged drink ---
    "Edit drink": "Modifier le verre",
    "Save changes": "Enregistrer les modifications",
    "With this": "Avec ce verre",
    "Delete": "Supprimer",
    "tap to edit · swipe to delete": "touche pour modifier · balaie pour supprimer",

    # --- Drinking pace ---
    "How fast": "À quelle vitesse",
    "In one go": "D’un trait",
    "Counts as a single swallow — the steepest possible rise.":
        "Compte comme une seule gorgée – la montée la plus raide possible.",
    "A quick drink. The level climbs fast.": "Un verre bu vite. Le taux monte rapidement.",
    "A normal pace.": "Un rythme normal.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Bu lentement. Montée bien plus douce pour la même quantité d’alcool.",

    # --- AddDrinkSheet ---
    "Cancel": "Annuler",
    "Now": "Maintenant",
    "Projected peak": "Pic prévu",
    "Peak at": "Pic à",
    "Clears": "Retour à zéro",
    "This would cross your limit": "Cela dépasserait ta limite",
    "Around %@, for up to %@.": "Vers %@, pendant %@ au maximum.",
    "This might cross your limit": "Cela pourrait dépasser ta limite",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Avec un métabolisme plus lent, oui ; avec un plus rapide, non. C’est l’incertitude de "
        "l’estimation.",
    "Type": "Type",
    "Amount": "Quantité",
    "Strength": "Degré",
    "%@ units": "%@ unités",
    "%@ g alcohol": "%@ g d’alcool",
    "Stomach": "Estomac",
    "When": "Quand",
    "Done": "OK",
    "Add": "Ajouter",

    # --- ProfileSheet ---
    "Male": "Homme",
    "Female": "Femme",
    "Sex": "Sexe",
    "Weight": "Poids",
    "Height": "Taille",
    "Age": "Âge",
    "kg": "kg",
    "cm": "cm",
    "yrs": "ans",
    "Body": "Corps",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "L’eau corporelle totale vient des équations de Watson, qui déterminent le volume dans "
        "lequel l’alcool se répartit.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "L’eau corporelle totale vient des équations de Watson, qui déterminent le volume dans "
        "lequel l’alcool se répartit. L’équation féminine ne tient pas compte de l’âge : le "
        "modifier n’aura donc aucun effet sur le résultat.",
    "Drinking frequency": "Fréquence de consommation",
    "How often do you drink?": "À quelle fréquence bois-tu ?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "C’est ainsi que nous estimons ta vitesse d’élimination. Une consommation régulière induit la voie CYP2E1 du foie : les buveurs fréquents éliminent donc l’alcool plus vite. C’est le point le plus faible du modèle, et c’est pourquoi tu peux régler dans Affichage et langue la part de cette incertitude que l’app te montre.",
    "Your limit": "Ta limite",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Ton propre repère, pas une limite légale. L’app t’indique quand un verre envisagé te "
        "ferait la dépasser, et pendant combien de temps tu resterais au-dessus.",
    "Calculated values": "Valeurs calculées",
    "Total body water": "Eau corporelle totale",
    "Distribution volume": "Volume de distribution",
    "Widmark factor": "Facteur de Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Le facteur de Widmark est généralement d’environ 0,68 chez les hommes et 0,55 chez "
        "les femmes. Si le tien s’en éloigne beaucoup, il vaut la peine de vérifier les "
        "valeurs ci-dessus.",
    "Elimination rate": "Vitesse d’élimination",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "À quelle vitesse ton foie élimine l’alcool une fois qu’il a été absorbé – la pente de "
        "la phase descendante de la courbe.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "L’alcool est éliminé à raison d’une quantité à peu près fixe par heure, et non d’un "
        "pourcentage, parce que l’enzyme qui le dégrade tourne déjà à pleine capacité à "
        "presque n’importe quel taux. C’est pour cela que des règles empiriques comme « un "
        "verre par heure » existent.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Avec ce réglage, %@ met environ %@ à redescendre à zéro. Presque tout le monde se "
        "situe entre %@ par heure.",
    "How to find yours": "Comment trouver la tienne",
    "With a breathalyser": "Avec un éthylotest",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Souffle deux fois, à au moins une heure d’intervalle, sur la phase descendante – deux "
        "heures ou plus après ton dernier verre, sans rien boire entre les deux. Soustrais la "
        "seconde mesure de la première et divise par le nombre d’heures qui les séparent.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Par exemple, %@ puis %@ deux heures plus tard donne %@ par heure.",
    "Without one": "Sans éthylotest",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "L’app t’indique quand elle prévoit ton retour à zéro. Si tu es systématiquement "
        "revenu à la normale bien avant, ta vitesse est plus élevée que le réglage – "
        "augmente-le d’un cran et observe pendant quelques sessions. Si cela prend plus de "
        "temps que prévu, baisse-le d’un cran.",
    "What moves it": "Ce qui la fait varier",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Une consommation régulière l’augmente : l’enzyme hépatique qui fait le travail est "
        "induite par l’usage. Elle est aussi légèrement plus élevée chez les femmes en "
        "moyenne, et plus basse à jeun ou en cas de problèmes de foie.",
    "Uncertainty": "Incertitude",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "À zéro, chaque valeur est un chiffre unique – la meilleure estimation de l’app. "
        "Au-dessus de zéro, les mêmes valeurs sont affichées sous forme de fourchettes, et la "
        "bande du graphique s’élargit en conséquence.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Un chiffre unique est plus facile à apprivoiser : avec le temps, tu découvres ce que "
        "représente ton propre 0,6. Une fourchette est la réponse la plus littérale, car la "
        "vitesse d’élimination est réellement incertaine. Les deux se défendent – à toi de "
        "choisir.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "L’écart suggéré par ta fréquence de consommation est de ± %@ par heure.",
    "Rate": "Vitesse",
    "Range": "Fourchette",
    "Advanced": "Avancé",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Plusieurs personnes",
    "History trends": "Tendances de l’historique",
    "Week": "Semaine",
    "Month": "Mois",
    "Year": "Année",
    "Sober days": "Jours sans alcool",
    "Change": "Évolution",
    "before records": "avant le début du suivi",
    "See further back": "Voir plus loin en arrière",
    "Weeks, months and years side by side — and every evening older than seven days.": "Semaines, mois et années côte à côte – et chaque soirée remontant à plus de sept jours.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Tout ce que tu as enregistré est déjà sauvegardé. Le déverrouillage ne fait que l’afficher.",
    "Coming soon": "Bientôt disponible",
    "Today": "Aujourd’hui",
    "Day": "Jour",
    "Yesterday": "Hier",
    "No drinks on this day": "Aucun verre ce jour-là",
    "Trend": "Tendance",
    "day": "jour",
    "Smoothing": "Lissage",
    "%@ sessions": "%@ sessions",
    "No data before %@": "Aucune donnée avant le %@",
    "vs.": "vs",
    "Grams": "Grammes",
    "Grams of alcohol": "Grammes d’alcool",
    "Standard units": "Unités standard",
    "Unit size": "Taille de l’unité",
    "Automatic": "Automatique",
    "UK": "Royaume-Uni",
    "Nordic countries": "Pays nordiques",
    "US standard drink": "Verre standard américain",
    "WHO, most of Europe": "OMS, la plupart de l’Europe",
    "Period": "Période",
    "Switch person": "Changer de personne",
    "Add person": "Ajouter une personne",
    "New person": "Nouvelle personne",
    "You": "Toi",
    "Name": "Nom",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Les quatre modifient la courbe, donc aucun ne peut être deviné pour quelqu’un "
        "d’autre.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Sa limite personnelle et les réglages plus fins pourront être modifiés plus tard dans "
        "l’onglet Profil, tant que c’est la personne sélectionnée.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Ajout rapide",
    "Choose a favourite drink": "Choisir une boisson favorite",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Choisis le verre que tu commandes d’habitude : un bouton sur l’écran Direct "
        "l’enregistrera d’un seul toucher.",
    "This is your quick-add drink": "C’est ton verre d’ajout rapide",
    "Set as my quick-add drink": "Définir comme mon verre d’ajout rapide",
    "This is now your usual": "C’est désormais ton verre habituel",
    "Remove favourite": "Retirer le favori",
    "Always add this one": "Toujours ajouter celui-ci",
    "Logs it straight away, without opening anything.":
        "L’enregistre immédiatement, sans rien ouvrir.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Un toucher sur l’écran Direct l’enregistre, avec le pic prévu affiché sur le bouton. Le "
        "remplissage de ton estomac est repris du verre précédent, et peut être corrigé juste "
        "après.",
    "Peak %@": "Pic %@",
    "%@ added": "Ajout de %@",
    "Save": "Enregistrer",
    "Undo": "Annuler",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Sauvegarde",
    "Export a backup": "Exporter une sauvegarde",
    "Import a backup": "Importer une sauvegarde",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Une sauvegarde contient toutes les personnes, toutes les sessions et tous les verres. "
        "L’importation ajoute ce qui manque – elle ne modifie ni ne supprime jamais ce qui est "
        "déjà là.",
    "Import this backup?": "Importer cette sauvegarde ?",
    "Import": "Importer",
    "Everything in this backup is already here.":
        "Tout ce que contient cette sauvegarde est déjà là.",
    "Import finished": "Importation terminée",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Langue",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Ouvre cette app dans Réglages, où « Langue préférée » définit la langue de l’app "
        "elle-même – celle du système reste inchangée. iOS redémarre l’app quand tu la "
        "changes.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Importation impossible",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Ce fichier n’est pas une sauvegarde LogMyDrink, ou il est endommagé.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Cette sauvegarde a été créée avec une version plus récente de LogMyDrink. Mets l’app "
        "à jour et réessaie.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        "Ajoute %@ sessions, %@ verres et %@ totaux mensuels. Rien de ce qui est déjà là n’est modifié ni supprimé.",
    'Added %@ occasions, %@ drinks and %@ monthly totals.': '%@ sessions, %@ verres et %@ totaux mensuels ajoutés.',
    'months as totals': 'mois en totaux seulement',
    'by month only': 'par mois seulement',
    'monthly total': 'total mensuel',
    'No daily records for this day': 'Aucun relevé quotidien pour ce jour',
    'Monthly total: %@': 'Total mensuel : %@',
    'A dry month': 'Un mois sans alcool',

    # --- RemovePersonSection ---
    'Remove %@?': 'Retirer %@ ?',
    'Remove': 'Retirer',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Supprime %@ sessions, %@ verres et %@ totaux mensuels. Cette action est irréversible.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Supprime %@ sessions et %@ verres. Cette action est irréversible.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Balaie vers la gauche sur un invité pour le retirer avec tout ce qui a été enregistré sous son nom. Tu ne peux pas être retiré.',
    'People': 'Personnes',
    'Owner': 'Propriétaire',
    'Everyone this app records. Switch, add, or remove someone.': "Toutes les personnes que cette app enregistre. Passe à une autre personne, ajoute ou retire quelqu’un.",
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Reporté de la veille au soir',
    # --- History, second card (5.24) ---
    'Calories': 'Calories',
    'Sessions': 'Sessions',
    'Per session': 'Par session',
    'Under the influence': 'Sous influence',
    '%@ of the time': '%@ du temps',
    'Days over limit': 'Jours au-dessus de la limite',
    'Longest sober run': 'Plus longue série sans alcool',
    'Favourite drink': 'Boisson favorite',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Affichage et langue",
    "Data": "Données",
    "Concentration": "Concentration",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Laisse la question sur la fréquence déterminer la vitesse, sauf si tu as une mesure à laquelle la comparer.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Estimation, pas une mesure. Ne te fie jamais à cette app pour décider si tu peux conduire.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Fourchette estimée, pas une mesure. Ne te fie jamais à cette app pour décider si tu peux conduire.',
    'How does the app calculate this?':
        'Comment l’app fait-elle ce calcul ?',
    'approximately %@ %@':
        'environ %@ %@',
    'How it works':
        'Fonctionnement',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Ne te fie jamais à cette app pour décider si tu peux conduire. Elle estime, elle ne mesure pas, et ton taux réel peut être très différent.',
    'Why this app exists':
        'Pourquoi cette app',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink t’aide à boire de façon plus consciente et à garder le contrôle. La décision se prend avant le verre suivant : l’app te montre donc à l’avance où un verre de plus mènerait ton taux, et quand il atteindrait son pic.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Mais il ne s’agit pas seulement de ce soir. Chaque verre enregistré s’ajoute à l’Historique : sur des mois et des années, tu vois combien, à quelle fréquence et jusqu’à quel taux tu bois. Tes habitudes s’en dégagent, ainsi que leur évolution – en mieux ou en moins bien.',
    'How it calculates':
        'Méthode de calcul',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'L’estimation repose sur la méthode de Widmark, utilisée depuis les années 1930 pour estimer l’alcoolémie ; l’app en utilise une version affinée.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'À partir de ton poids, ta taille, ton âge et ton sexe, elle calcule la quantité d’eau de ton corps, car c’est là que l’alcool se répartit. Elle suit chaque verre séparément : sa teneur en alcool, la vitesse à laquelle tu l’as bu et ce que tu avais mangé, car cela détermine la vitesse d’absorption.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Pendant ce temps, ton foie élimine une quantité à peu près constante chaque heure ; la tienne est estimée d’après la fréquence à laquelle tu bois. Il en résulte une courbe, minute par minute : où tu en es, où tu vas et quand tu seras revenu à zéro.',
    'Details':
        'Détails',
    'Body water':
        'Eau corporelle',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'La formule de Watson (1980), d’après le poids, la taille, l’âge et le sexe. La formule féminine ne tient pas compte de l’âge – c’est une propriété de la formule, pas un bug. Le volume de distribution est l’eau corporelle divisée par 0,85, la teneur en eau du sang.',
    'Absorption':
        'Absorption',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Chaque verre a son propre « estomac ». À jeun, la moitié de l’alcool est absorbée en 7 minutes environ ; l’estomac plein, en 21 environ. Un verre que tu sirotes arrive dans l’estomac de façon régulière pendant que tu le bois.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Donne un pic plus bas et un retour à zéro plus tôt. Surprenant, mais mesuré : avec de la nourriture, l’estomac dégrade une partie de l’alcool avant son absorption (l’app utilise 5, 10 et 15 pour cent), et ce qui n’est jamais entré n’a pas à être éliminé.',
    'Elimination':
        'Élimination',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Environ 0,15 ‰ par heure (fourchette publiée 0,10–0,25), davantage chez les buveurs réguliers, dont les enzymes du foie s’adaptent. Près de zéro, elle ralentit (cinétique de Michaelis-Menten) : la courbe s’adoucit au lieu de s’arrêter net.',
    'Computation':
        'Calcul',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'La courbe provient d’une simulation numérique à la minute près.',
    'Why it is only an estimate':
        'Pourquoi ce n’est qu’une estimation',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'L’app ne mesure rien. Ce qu’elle affiche est le résultat d’un modèle fondé sur des valeurs moyennes, et la réalité peut être différente. La plus grande inconnue est la vitesse à laquelle tu élimines l’alcool : dans la fourchette plausible, elle peut à elle seule déplacer le pic de 40 pour cent et le retour à zéro de quatre heures pour une même soirée.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'La génétique, l’état du foie, les médicaments, ce que tu as mangé, le sommeil et la fatigue comptent aussi – l’app n’en connaît rien. Seul un éthylomètre homologué ou une prise de sang donne une valeur exacte.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Le chiffre reste utile. Si l’app affiche systématiquement un peu trop haut ou un peu trop bas pour toi, elle se trompe dans le même sens chaque soir : avec le temps, tu apprends ce qu’une valeur signifie pour toi. Dans Profil, tu peux aussi afficher l’incertitude de la vitesse d’élimination : tu vois alors une fourchette au lieu d’un chiffre unique.',
    'Tips':
        'Astuces',
    'Favourite drink in one tap':
        'Boisson favorite en un toucher',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Choisis une favorite dans Profil, et le bouton de Direct l’enregistre d’un seul toucher.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Ajoute-le à l’écran verrouillé ou à l’écran d’accueil : un toucher enregistre ta favorite. Tant qu’il y a de l’alcool dans ton organisme, il affiche aussi ton taux et sa direction.',
    'How do I add it?':
        'Comment l’ajouter ?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Dis « Hey Siri, LogMyDrink now » : Siri enregistre ta favorite, puis t’indique vers quel pic tu vas. (La commande fonctionne en anglais.)',
    'Looking back':
        'Regarder en arrière',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '« Hier » en haut de l’écran Direct te mène à la veille d’un toucher ; l’onglet Historique montre tes habitudes sur des semaines, des mois et des années.',
    'Logging later':
        'Enregistrer après coup',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Si tu enregistres un verre après coup, recule l’heure avec les boutons − et + ; une journée oubliée peut être complétée depuis la vue Jour de l’Historique.',
    'One tap and done':
        'Un toucher et c’est fait',
    'Your favourite from the Lock Screen':
        'Ta favorite depuis l’écran verrouillé',
    'Say it, don’t type it':
        'Dis-le, ne le tape pas',
    'See your patterns':
        'Découvre tes habitudes',
    'Set what you drink most often and log it with a single tap.':
        'Indique ce que tu bois le plus souvent et enregistre-le d’un seul toucher.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Un toucher sur le widget enregistre ta favorite, sans chercher l’app. Le soir, il affiche aussi ton taux.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '« Hey Siri, LogMyDrink now » – Siri enregistre ta favorite et t’indique vers quel pic tu vas.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'L’Historique montre combien et jusqu’à quel taux tu bois sur des semaines, des mois et des années, et comment cela évolue.',
    'Set favourite':
        'Choisir une favorite',
    'Add widget':
        'Ajouter le widget',
    'Got it':
        'Compris',
    'Open History':
        'Ouvrir l’Historique',
    'Don’t show again':
        'Ne plus afficher',
    'Lock Screen':
        'Écran verrouillé',
    'Home Screen':
        'Écran d’accueil',
    'Where':
        'Où',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Verrouille ton iPhone, puis appuie de façon prolongée sur l’écran verrouillé.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Touche Personnaliser, puis Écran verrouillé, puis la rangée de widgets sous l’heure.',
    'Choose LogMyDrink, then tap Done.':
        'Choisis LogMyDrink, puis touche OK.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Touche de manière prolongée une zone vide de l’écran d’accueil jusqu’à ce que les icônes s’animent.',
    'Tap Edit, then Add Widget.':
        'Touche Modifier, puis Ajouter un widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Recherche LogMyDrink, choisis une taille et touche Ajouter le widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Un toucher sur le widget ouvre l’app et enregistre ta boisson favorite. Tant qu’il y a de l’alcool dans ton organisme, il affiche aussi ton taux et sa direction.',
    'Add the widget':
        'Ajouter le widget',
    'Show tips':
        'Afficher les astuces',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Une astuce par jour au maximum, à l’ouverture de l’app – jamais tant qu’il y a de l’alcool dans ton organisme.',
}
