"""
Spanish (European).

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Por mil",
    "Percent": "Porcentaje",

    # --- DrinkCatalog: drink types ---
    "Beer": "Cerveza",
    "Wine": "Vino",
    "Champagne": "Espumoso",
    "Shot": "Chupito",
    "Cocktail": "Cóctel",
    "Custom": "Personalizado",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Estómago vacío",
    "Moderately full": "Moderadamente lleno",
    "Full stomach": "Estómago lleno",
    "Empty": "Vacío",
    "Moderate": "Moderado",
    "Full": "Lleno",
    "Fast absorption, higher and earlier peak.":
        "Absorción rápida, pico más alto y más temprano.",
    "Moderate absorption.": "Absorción moderada.",
    "Slow absorption, lower and later peak.": "Absorción lenta, pico más bajo y más tardío.",

    # --- DrinkingFrequency ---
    "Rarely": "Rara vez",
    "A few times a month": "Unas pocas veces al mes",
    "Several times a week": "Varias veces a la semana",
    "Almost daily": "Casi a diario",
    "A few occasions a year": "Algunas veces al año",
    "Social drinking": "Consumo social",
    "Weekly routine": "Rutina semanal",
    "Daily or nearly daily": "A diario o casi a diario",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Hora",
    "Level": "Nivel",
    "Lower": "Inferior",
    "Upper": "Superior",
    "Lower estimate": "Estimación inferior",
    "Upper estimate": "Estimación superior",
    "Personal limit": "Límite personal",
    "Drink": "Bebida",

    # --- BACChartView ---
    "Expected peak around %@": "Pico previsto en torno a %@",
    "Peaked around %@": "Pico alcanzado en torno a %@",
    "No active session": "Ninguna sesión activa",
    "Still rising": "Sigue subiendo",
    "YOUR LIMIT %@": "TU LÍMITE %@",
    "possible range": "rango posible",

    # --- Live screen: the day with nothing on it ---
    "Live": "En directo",
    "Nothing logged today": "Hoy no has registrado nada",
    "Add a drink when you have one.": "Añade una bebida cuando te la tomes.",

    # --- Tabs and history ---
    "History": "Historial",
    "No past sessions yet": "Aún no hay sesiones anteriores",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Una sesión aparece aquí cuando ha terminado: cuando tu nivel ha vuelto a cero y han "
        "pasado unas horas.",
    "%@ drinks": "%@ bebidas",
    "peak": "pico",
    "Started": "Inicio",
    "Lasted": "Duración",
    "Duration": "Duración",
    "Sober around": "Sobrio aprox.",
    "Sober at": "Sobrio",
    "Remaining": "Restante",
    "next day": "al día siguiente",
    "previous day": "el día anterior",
    "%@ days later": "%@ días después",
    "%@ days earlier": "%@ días antes",
    "Calculated with your profile at the time": "Calculado con tu perfil de ese momento",

    # --- TodayView ---
    "Profile": "Perfil",
    "Drinks": "Bebidas",
    "Units": "Unidades",
    "Drinks this session": "Bebidas de esta sesión",
    "Add drink": "Añadir bebida",

    # --- Editing an already logged drink ---
    "Edit drink": "Editar bebida",
    "Save changes": "Guardar cambios",
    "With this": "Con esta",
    "Delete": "Eliminar",
    "tap to edit · swipe to delete": "toca para editar · desliza para eliminar",

    # --- Drinking pace ---
    "How fast": "A qué velocidad",
    "In one go": "De un trago",
    "Counts as a single swallow — the steepest possible rise.":
        "Cuenta como un solo trago: la subida más rápida posible.",
    "A quick drink. The level climbs fast.": "Una bebida rápida. El nivel sube deprisa.",
    "A normal pace.": "Un ritmo normal.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Bebida despacio. Subida mucho más suave con el mismo alcohol.",

    # --- AddDrinkSheet ---
    "Cancel": "Cancelar",
    "Now": "Ahora",
    "Projected peak": "Pico previsto",
    "Peak at": "Pico a las",
    "Clears": "Vuelta a cero",
    "This would cross your limit": "Esto superaría tu límite",
    "Around %@, for up to %@.": "Alrededor de %@, durante %@ como máximo.",
    "This might cross your limit": "Esto podría superar tu límite",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Con un metabolismo más lento sí, con uno más rápido no. Esa es la incertidumbre de la "
        "estimación.",
    "Type": "Tipo",
    "Amount": "Cantidad",
    "Strength": "Graduación",
    "%@ units": "%@ unidades",
    "%@ g alcohol": "%@ g de alcohol",
    "Stomach": "Estómago",
    "When": "Cuándo",
    "Done": "OK",
    "Add": "Añadir",

    # --- ProfileSheet ---
    "Male": "Hombre",
    "Female": "Mujer",
    "Sex": "Sexo",
    "Weight": "Peso",
    "Height": "Altura",
    "Age": "Edad",
    "kg": "kg",
    "cm": "cm",
    "yrs": "años",
    "Body": "Cuerpo",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "El agua corporal total procede de las ecuaciones de Watson, que determinan el volumen "
        "en el que se distribuye el alcohol.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "El agua corporal total procede de las ecuaciones de Watson, que determinan el volumen "
        "en el que se distribuye el alcohol. La ecuación femenina no incluye la edad, así que "
        "cambiarla no afectará al resultado.",
    "Drinking frequency": "Frecuencia de consumo",
    "How often do you drink?": "¿Con qué frecuencia bebes?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Así estimamos tu tasa de eliminación. Beber con regularidad induce la vía CYP2E1 del hígado, por lo que quien bebe con frecuencia elimina el alcohol más rápido. Es el punto más débil del modelo, y por eso en Visualización e idioma puedes elegir cuánta de esa incertidumbre te muestra la app.",
    "Your limit": "Tu límite",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Tu propia cifra de referencia, no un límite legal. La app te avisa cuando una bebida "
        "prevista te haría superarlo y durante cuánto tiempo estarías por encima.",
    "Calculated values": "Valores calculados",
    "Total body water": "Agua corporal total",
    "Distribution volume": "Volumen de distribución",
    "Widmark factor": "Factor de Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "El factor de Widmark suele rondar 0,68 en hombres y 0,55 en mujeres. Si el tuyo se "
        "aleja mucho de eso, conviene revisar los valores de arriba.",
    "Elimination rate": "Tasa de eliminación",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "A qué velocidad elimina el alcohol tu hígado una vez absorbido: la pendiente de la "
        "parte descendente de la curva.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "El alcohol se elimina en una cantidad más o menos fija por hora, y no en un "
        "porcentaje, porque la enzima que lo descompone ya funciona a pleno rendimiento con "
        "casi cualquier nivel. Por eso existen reglas generales como «una bebida por hora».",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Con este ajuste, %@ tarda aproximadamente %@ en eliminarse. Casi todo el mundo está "
        "entre %@ por hora.",
    "How to find yours": "Cómo averiguar la tuya",
    "With a breathalyser": "Con un alcoholímetro",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Sopla dos veces, con al menos una hora de diferencia, en la parte descendente: dos "
        "horas o más después de tu última bebida, sin beber nada entretanto. Resta la segunda lectura "
        "de la primera y divide entre las horas transcurridas.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Por ejemplo, %@ y %@ dos horas después dan %@ por hora.",
    "Without one": "Sin alcoholímetro",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "La app te indica cuándo prevé que habrás eliminado el alcohol. Si vuelves a la "
        "normalidad de forma constante bastante antes, tu tasa es más alta que el ajuste: "
        "súbela un paso y observa durante unas cuantas sesiones. Si tarda más de lo previsto, "
        "bájala.",
    "What moves it": "Qué la modifica",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Beber con regularidad la aumenta: la enzima hepática que hace el trabajo se induce "
        "con el uso. También es algo más alta de media en las mujeres, y más baja con el "
        "estómago vacío o con problemas hepáticos.",
    "Uncertainty": "Incertidumbre",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "En cero, cada cifra es un solo número: la mejor estimación de la app. Por encima de "
        "cero, las mismas cifras se muestran como rangos, y la banda del gráfico se ensancha "
        "en consecuencia.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Con un solo número es más fácil aprender: con el tiempo descubres cómo te sientes con "
        "tu propio 0,6. Un rango es la respuesta más literal, porque la tasa es realmente "
        "incierta. Ambas opciones son defendibles; la decisión es tuya.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "El margen que sugiere tu frecuencia de consumo es de ± %@ por hora.",
    "Rate": "Tasa",
    "Range": "Rango",
    "Advanced": "Avanzado",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Varias personas",
    "History trends": "Tendencias del historial",
    "Week": "Semana",
    "Month": "Mes",
    "Year": "Año",
    "Sober days": "Días sin beber",
    "Change": "Cambio",
    "before records": "antes del registro",
    "See further back": "Ver más atrás",
    "Weeks, months and years side by side — and every evening older than seven days.": "Semanas, meses y años uno junto a otro, y cada noche de hace más de siete días.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Todo lo que has registrado ya está guardado. Desbloquear solo lo muestra.",
    "Coming soon": "Próximamente",
    "Today": "Hoy",
    "Day": "Día",
    "Yesterday": "Ayer",
    "No drinks on this day": "Sin bebidas este día",
    "Trend": "Tendencia",
    "day": "día",
    "Smoothing": "Suavizado",
    "%@ sessions": "%@ sesiones",
    "No data before %@": "Sin datos antes del %@",
    "vs.": "vs.",
    "Grams": "Gramos",
    "Grams of alcohol": "Gramos de alcohol",
    "Standard units": "Unidades estándar",
    "Unit size": "Tamaño de la unidad",
    "Automatic": "Automático",
    "UK": "Reino Unido",
    "Nordic countries": "Países nórdicos",
    "US standard drink": "Bebida estándar de EE. UU.",
    "WHO, most of Europe": "OMS, la mayor parte de Europa",
    "Period": "Periodo",
    "Switch person": "Cambiar de persona",
    "Add person": "Añadir persona",
    "New person": "Nueva persona",
    "You": "Tú",
    "Name": "Nombre",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Los cuatro cambian la curva, así que ninguno se puede suponer para otra persona.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Su propio límite y los ajustes más detallados se pueden cambiar después en la pestaña "
        "Perfil, mientras sea la persona seleccionada.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Registro rápido",
    "Choose a favourite drink": "Elige una bebida favorita",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Elige la bebida que sueles pedir y un botón en la pantalla En directo la registrará "
        "con un solo toque.",
    "This is your quick-add drink": "Esta es tu bebida de registro rápido",
    "Set as my quick-add drink": "Fijar como mi bebida de registro rápido",
    "This is now your usual": "Ahora es tu bebida habitual",
    "Remove favourite": "Quitar favorita",
    "Always add this one": "Añadir siempre esta",
    "Logs it straight away, without opening anything.":
        "La registra al instante, sin abrir nada.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Un toque en la pantalla En directo la registra, con el pico previsto en el botón. Lo "
        "lleno que está tu estómago se toma de la bebida anterior y se puede corregir justo "
        "después.",
    "Peak %@": "Pico %@",
    "%@ added": "Se ha añadido %@",
    "Save": "Guardar",
    "Undo": "Deshacer",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Copia de seguridad",
    "Export a backup": "Exportar una copia de seguridad",
    "Import a backup": "Importar una copia de seguridad",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Una copia de seguridad contiene todas las personas, sesiones y bebidas. Al importar "
        "se añade lo que falta; nunca se modifica ni se elimina nada de lo que ya hay aquí.",
    "Import this backup?": "¿Importar esta copia de seguridad?",
    "Import": "Importar",
    "Everything in this backup is already here.":
        "Todo lo que hay en esta copia de seguridad ya está aquí.",
    "Import finished": "Importación finalizada",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Idioma",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Abre esta app en Ajustes, donde «Idioma preferido» define el idioma de la propia app; "
        "el del sistema se mantiene igual. iOS reinicia la app cuando lo cambias.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "No se ha podido importar",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Este archivo no es una copia de seguridad de LogMyDrink o está dañado.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Esta copia de seguridad se creó con una versión más reciente de LogMyDrink. Actualiza "
        "la app e inténtalo de nuevo.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Añade %@ sesiones, %@ bebidas y %@ totales mensuales. No se modifica ni se elimina nada de lo que ya hay aquí.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Se han añadido %@ sesiones, %@ bebidas y %@ totales mensuales.',
    'months as totals': 'meses solo como totales',
    'by month only': 'solo por mes',
    'monthly total': 'total mensual',
    'No daily records for this day': 'No hay registros diarios de este día',
    'Monthly total: %@': 'Total mensual: %@',
    'A dry month': 'Un mes sin alcohol',

    # --- RemovePersonSection ---
    'Remove %@?': '¿Eliminar a %@?',
    'Remove': 'Eliminar',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Elimina %@ sesiones, %@ bebidas y %@ totales mensuales. No se puede deshacer.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Elimina %@ sesiones y %@ bebidas. No se puede deshacer.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Desliza a la izquierda sobre un invitado para eliminarlo con todo lo registrado bajo su nombre. A ti no se te puede eliminar.',
    'People': 'Personas',
    'Owner': 'Titular',
    'Everyone this app records. Switch, add, or remove someone.': 'Todas las personas que registra esta app. Cambia, añade o elimina a alguien.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Viene de la noche anterior',
    # --- History, second card (5.24) ---
    'Calories': 'Calorías',
    'Sessions': 'Sesiones',
    'Per session': 'Por sesión',
    'Under the influence': 'Bajo los efectos del alcohol',
    '%@ of the time': '%@ del tiempo',
    'Days over limit': 'Días por encima del límite',
    'Longest sober run': 'Racha más larga sin beber',
    'Favourite drink': 'Bebida favorita',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Visualización e idioma",
    "Data": "Datos",
    "Concentration": "Concentración",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Deja que la tasa la determine la pregunta sobre la frecuencia, salvo que tengas una medición con la que contrastarla.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Estimación, no medición. Nunca uses esto para decidir si puedes conducir.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Rango estimado, no medición. Nunca uses esto para decidir si puedes conducir.',
    'How does the app calculate this?':
        '¿Cómo lo calcula la app?',
    'approximately %@ %@':
        'aproximadamente %@ %@',
    'How it works':
        'Cómo funciona',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nunca uses esto para decidir si puedes conducir. La app estima, no mide, y tu nivel real puede ser muy distinto.',
    'Why this app exists':
        'Por qué existe esta app',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink te ayuda a beber de forma más consciente y a mantener el control. La decisión se toma antes de la siguiente copa, así que la app te muestra de antemano hasta dónde llevaría tu nivel otra bebida y cuándo alcanzaría el pico.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Pero no se trata solo de esta noche. Cada bebida que registras pasa a tu Historial, así que con los meses y los años ves cuánto, con qué frecuencia y hasta qué nivel bebes. De ahí surgen tus patrones, y también la dirección en la que cambian: si las cosas mejoran o empeoran.',
    'How it calculates':
        'Cómo calcula',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'La estimación se basa en el método de Widmark, que se usa desde los años treinta para estimar la alcoholemia; la app emplea una versión refinada.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'A partir de tu peso, altura, edad y sexo calcula cuánta agua contiene tu cuerpo, porque ahí se reparte el alcohol. Sigue cada bebida por separado: cuánto alcohol tenía, lo rápido que la bebiste y cuánto habías comido, porque eso determina la rapidez de la absorción.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Mientras tanto, tu hígado elimina una cantidad más o menos constante cada hora; la tuya se estima a partir de la frecuencia con que bebes. El resultado es una curva, minuto a minuto: dónde estás ahora, hacia dónde vas y cuándo volverás a cero.',
    'Details':
        'Detalles',
    'Body water':
        'Agua corporal',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'La fórmula de Watson (1980), a partir del peso, la altura, la edad y el sexo. La fórmula femenina no incluye la edad: es una propiedad de la fórmula, no un error. El volumen de distribución es el agua corporal dividida entre 0,85, el contenido de agua de la sangre.',
    'Absorption':
        'Absorción',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Cada bebida tiene su propio «estómago». En ayunas, la mitad del alcohol se absorbe en unos 7 minutos; con el estómago lleno, en unos 21. Una bebida que tomas a sorbos llega al estómago de forma uniforme mientras la bebes.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Da un pico más bajo y un regreso a cero más temprano. Sorprende, pero está medido: con comida, el estómago degrada parte del alcohol antes de absorberlo (la app usa un 5, 10 y 15 por ciento), y lo que nunca entra no hay que eliminarlo.',
    'Elimination':
        'Eliminación',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Unos 0,15 ‰ por hora (rango publicado 0,10–0,25), más en quienes beben con regularidad porque las enzimas del hígado se adaptan. Cerca de cero se ralentiza (cinética de Michaelis-Menten), así que la curva se suaviza en lugar de cortarse de golpe.',
    'Computation':
        'Cálculo',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'La curva procede de una simulación numérica con resolución de un minuto.',
    'Why it is only an estimate':
        'Por qué es solo una estimación',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'La app no mide nada. Lo que muestra es el resultado de un modelo con valores medios, y la realidad puede ser distinta. La mayor incógnita es lo rápido que eliminas el alcohol: dentro del rango plausible, eso por sí solo puede mover el pico un 40 por ciento y el regreso a cero cuatro horas en la misma noche.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'También influyen la genética, la salud del hígado, los medicamentos, lo que comiste, el sueño y el cansancio, y la app no conoce nada de eso. Solo un alcoholímetro homologado o un análisis de sangre dan un valor exacto.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Aun así, el número es útil. Si la app marca contigo siempre un poco de más o de menos, se equivoca en la misma dirección cada noche, así que con el tiempo aprendes qué significa un valor para ti. En Perfil también puedes mostrar la incertidumbre de la tasa de eliminación: verás un rango en lugar de un único número.',
    'Tips':
        'Consejos',
    'Favourite drink in one tap':
        'Bebida favorita con un toque',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Elige una favorita en Perfil y el botón de En directo la registra con un solo toque.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Añádelo a la pantalla de bloqueo o a la pantalla de inicio: un toque registra tu favorita. Mientras haya alcohol en tu cuerpo, muestra también tu nivel y hacia dónde va.',
    'How do I add it?':
        '¿Cómo lo añado?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Di «Hey Siri, LogMyDrink now» y Siri registrará tu favorita y te dirá hacia qué pico vas. (El comando funciona en inglés.)',
    'Looking back':
        'Mirar atrás',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '«Ayer», en la parte superior de En directo, te lleva al día anterior con un toque; la pestaña Historial muestra tus patrones a lo largo de semanas, meses y años.',
    'Logging later':
        'Registrar más tarde',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Si registras una bebida después, retrasa la hora con los botones − y +; un día olvidado se puede completar desde la vista Día de Historial.',
    'One tap and done':
        'Un toque y listo',
    'Your favourite from the Lock Screen':
        'Tu favorita desde la pantalla de bloqueo',
    'Say it, don’t type it':
        'Dilo, no lo escribas',
    'See your patterns':
        'Descubre tus patrones',
    'Set what you drink most often and log it with a single tap.':
        'Indica lo que bebes con más frecuencia y regístralo con un solo toque.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Un toque en el widget registra tu favorita, sin buscar la app. Por la noche muestra también tu nivel.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '«Hey Siri, LogMyDrink now»: Siri registra tu favorita y te dice hacia qué pico vas.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'En Historial ves cuánto y hasta qué nivel bebes a lo largo de semanas, meses y años, y hacia dónde cambia.',
    'Set favourite':
        'Elegir favorita',
    'Add widget':
        'Añadir widget',
    'Got it':
        'Entendido',
    'Open History':
        'Abrir Historial',
    'Don’t show again':
        'No volver a mostrar',
    'Lock Screen':
        'Pantalla de bloqueo',
    'Home Screen':
        'Pantalla de inicio',
    'Where':
        'Dónde',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Bloquea el iPhone y mantén pulsada la pantalla de bloqueo.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Toca Personalizar, luego Pantalla de bloqueo y después la fila de widgets bajo la hora.',
    'Choose LogMyDrink, then tap Done.':
        'Elige LogMyDrink y toca OK.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Mantén pulsada una zona vacía de la pantalla de inicio hasta que los iconos tiemblen.',
    'Tap Edit, then Add Widget.':
        'Toca Editar y luego Añadir widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Busca LogMyDrink, elige un tamaño y toca Añadir widget.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Un toque en el widget abre la app y registra tu bebida favorita. Mientras haya alcohol en tu cuerpo, muestra también tu nivel y hacia dónde va.',
    'Add the widget':
        'Añadir el widget',
    'Show tips':
        'Mostrar consejos',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Como mucho un consejo al día, al abrir la app; nunca mientras haya alcohol en tu cuerpo.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Qué muestra la cifra',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'La cifra es una estimación de tu alcoholemia (en inglés BAC, blood alcohol concentration): cuánto alcohol hay en tu sangre.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'En tanto por mil (‰) son gramos de alcohol por litro de sangre: 0,5 ‰ significa medio gramo en cada litro. En porcentaje son gramos por cada 100 mililitros, así que el mismo nivel da una cifra diez veces menor: 0,5 ‰ equivale a 0,05 por ciento. Puedes cambiar entre ambos en Perfil › Visualización e idioma.',
    'The curve shows the same level over time, minute by minute.':
        'La curva muestra ese mismo nivel a lo largo del tiempo, minuto a minuto.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'El tanto por mil (‰) son gramos de alcohol por litro de sangre; el porcentaje, gramos por cada 100 mililitros: 0,5 ‰ equivale a 0,05 por ciento.',
}
