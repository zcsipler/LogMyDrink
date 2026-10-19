"""
Bulgarian.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Промил",
    "Percent": "Процент",

    # --- DrinkCatalog: drink types ---
    "Beer": "Бира",
    "Wine": "Вино",
    "Champagne": "Пенливо",
    "Shot": "Шот",
    "Cocktail": "Коктейл",
    "Custom": "По избор",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Празен стомах",
    "Moderately full": "Умерено пълен",
    "Full stomach": "Пълен стомах",
    "Empty": "Празен",
    "Moderate": "Умерен",
    "Full": "Пълен",
    "Fast absorption, higher and earlier peak.": "Бързо усвояване, по-висок и по-ранен пик.",
    "Moderate absorption.": "Умерено усвояване.",
    "Slow absorption, lower and later peak.": "Бавно усвояване, по-нисък и по-късен пик.",

    # --- DrinkingFrequency ---
    "Rarely": "Рядко",
    "A few times a month": "Няколко пъти в месеца",
    "Several times a week": "Няколко пъти седмично",
    "Almost daily": "Почти всеки ден",
    "A few occasions a year": "Няколко пъти в годината",
    "Social drinking": "Социално пиене",
    "Weekly routine": "Седмична рутина",
    "Daily or nearly daily": "Всеки ден или почти всеки ден",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Час",
    "Level": "Ниво",
    "Lower": "Долна",
    "Upper": "Горна",
    "Lower estimate": "Долна оценка",
    "Upper estimate": "Горна оценка",
    "Personal limit": "Личен лимит",
    "Drink": "Напитка",

    # --- BACChartView ---
    "Expected peak around %@": "Очакван пик около %@",
    "Peaked around %@": "Достигна пик около %@",
    "No active session": "Няма активна сесия",
    "Still rising": "Все още се покачва",
    "YOUR LIMIT %@": "ТВОЯТ ЛИМИТ %@",
    "possible range": "възможен диапазон",

    # --- Live screen: the day with nothing on it ---
    "Live": "На живо",
    "Nothing logged today": "Днес няма нищо записано",
    "Add a drink when you have one.": "Добавяй напитка, когато изпиеш такава.",

    # --- Tabs and history ---
    "History": "История",
    "No past sessions yet": "Все още няма минали сесии",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Сесията се появява тук, след като приключи — когато нивото ти се изчисти и минат "
        "няколко часа.",
    "%@ drinks": "Напитки: %@",
    "peak": "пик",
    "Started": "Започна",
    "Lasted": "Продължи",
    "Duration": "Продължителност",
    "Sober around": "Трезв прибл.",
    "Sober at": "Трезв",
    "Remaining": "Остават",
    "next day": "следващия ден",
    "previous day": "предишния ден",
    "%@ days later": "%@ дни по-късно",
    "%@ days earlier": "%@ дни по-рано",
    "Calculated with your profile at the time": "Изчислено с профила ти от онзи момент",

    # --- TodayView ---
    "Profile": "Профил",
    "Drinks": "Напитки",
    "Units": "Единици",
    "Drinks this session": "Напитки в тази сесия",
    "Add drink": "Добави напитка",

    # --- Editing an already logged drink ---
    "Edit drink": "Редактирай напитката",
    "Save changes": "Запази промените",
    "With this": "С тази напитка",
    "Delete": "Изтрий",
    "tap to edit · swipe to delete": "докосни за редакция · плъзни за изтриване",

    # --- Drinking pace ---
    "How fast": "Колко бързо",
    "In one go": "Наведнъж",
    "Counts as a single swallow — the steepest possible rise.":
        "Брои се като една глътка — възможно най-стръмното покачване.",
    "A quick drink. The level climbs fast.": "Бързо изпита напитка. Нивото се покачва бързо.",
    "A normal pace.": "Нормално темпо.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Изпита бавно. Много по-плавно покачване при същия алкохол.",

    # --- AddDrinkSheet ---
    "Cancel": "Отказ",
    "Now": "Сега",
    "Projected peak": "Прогнозен пик",
    "Peak at": "Пик в",
    "Clears": "Изчиства се",
    "This would cross your limit": "Това би преминало лимита ти",
    "Around %@, for up to %@.": "Около %@, в продължение на до %@.",
    "This might cross your limit": "Това може да премине лимита ти",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "При по-бавен метаболизъм — да, при по-бърз — не. Това е несигурността на оценката.",
    "Type": "Вид",
    "Amount": "Количество",
    "Strength": "Градус",
    "%@ units": "Единици: %@",
    "%@ g alcohol": "%@ г алкохол",
    "Stomach": "Стомах",
    "When": "Кога",
    "Done": "Готово",
    "Add": "Добави",

    # --- ProfileSheet ---
    "Male": "Мъж",
    "Female": "Жена",
    "Sex": "Пол",
    "Weight": "Тегло",
    "Height": "Височина",
    "Age": "Възраст",
    "kg": "кг",
    "cm": "см",
    "yrs": "год.",
    "Body": "Тяло",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Общата телесна вода идва от уравненията на Watson, които определят обема, в който се "
        "разпределя алкохолът.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Общата телесна вода идва от уравненията на Watson, които определят обема, в който се "
        "разпределя алкохолът. Женското уравнение не включва възрастта, затова промяната ѝ "
        "няма да повлияе на резултата.",
    "Drinking frequency": "Честота на пиене",
    "How often do you drink?": "Колко често пиеш?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Така оценяваме скоростта ти на елиминиране. Редовното пиене индуцира чернодробния път CYP2E1, затова честите консуматори изчистват алкохола по-бързо. Това е най-слабото място на модела и затова в „Показване и език“ можеш да зададеш колко от тази несигурност да ти показва приложението.",
    "Your limit": "Твоят лимит",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Твоя собствена отправна стойност, а не законова граница. Приложението ти казва кога "
        "планирана напитка би те извела над нея и колко време ще останеш отгоре.",
    "Calculated values": "Изчислени стойности",
    "Total body water": "Обща телесна вода",
    "Distribution volume": "Обем на разпределение",
    "Widmark factor": "Фактор на Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Факторът на Widmark обикновено е около 0,68 при мъжете и 0,55 при жените. Ако твоят е "
        "далеч от това, си струва да провериш стойностите по-горе.",
    "Elimination rate": "Скорост на елиминиране",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Колко бързо черният ти дроб изчиства алкохола, след като той е усвоен — наклонът на "
        "спадащата част от кривата.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Алкохолът се изчиства с приблизително постоянно количество на час, а не с процент от "
        "наличното, защото ензимът, който го разгражда, вече работи с пълен капацитет при "
        "почти всяко ниво. Затова изобщо съществуват правила като „една напитка на час“.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "При тази настройка %@ се изчиства за около %@. Почти всички попадат между %@ на час.",
    "How to find yours": "Как да откриеш своята",
    "With a breathalyser": "С алкотестер",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Духни два пъти, с поне час разлика, в спадащата част — два или повече часа след "
        "последната напитка и без нищо междувременно. Извади второто отчитане от първото и "
        "раздели на часовете между тях.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Например %@ и %@ два часа по-късно дават %@ на час.",
    "Without one": "Без алкотестер",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Приложението ти казва кога очаква нивото ти да се изчисти. Ако редовно се връщаш към "
        "нормалното доста преди това, скоростта ти е по-висока от настройката — вдигни я с "
        "една стъпка и наблюдавай няколко сесии. Ако отнема повече от предвиденото, свали я с "
        "една стъпка.",
    "What moves it": "Какво я променя",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Редовното пиене я повишава: чернодробният ензим, който върши работата, се индуцира от "
        "употреба. Средно тя е и малко по-висока при жените, а по-ниска на празен стомах или "
        "при чернодробни проблеми.",
    "Uncertainty": "Несигурност",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "При нула всяка стойност е едно число — най-добрата преценка на приложението. Над нула "
        "същите стойности се показват като диапазони, а лентата на графиката се разширява "
        "съответно.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "С едно число се учиш по-лесно: с времето разбираш как се усещат твоите собствени 0,6. "
        "Диапазонът е по-буквалният отговор, защото скоростта наистина е несигурна. И двете са "
        "защитими — решението е твое.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Разсейването, което честотата ти на пиене подсказва, е ± %@ на час.",
    "Rate": "Скорост",
    "Range": "Диапазон",
    "Advanced": "Разширени",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Multiple people": "Няколко души",
    "History trends": "Тенденции в историята",
    "Week": "Седмица",
    "Month": "Месец",
    "Year": "Година",
    "Sober days": "Дни без алкохол",
    "Change": "Промяна",
    "before records": "преди началото на записите",
    "See further back": "Виж по-назад",
    "Weeks, months and years side by side — and every evening older than seven days.": "Седмици, месеци и години една до друга – и всяка вечер, по-стара от седем дни.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Всичко, което си записал, вече е запазено. Отключването само го показва.",
    "Coming soon": "Очаквайте скоро",
    "Today": "Днес",
    "Day": "Ден",
    "Yesterday": "Вчера",
    "No drinks on this day": "Няма напитки на този ден",
    "Trend": "Тенденция",
    "day": "ден",
    "Smoothing": "Изглаждане",
    "%@ sessions": "%@ случая",
    "No data before %@": "Няма данни преди %@",
    "vs.": "спрямо",
    "Grams": "Грамове",
    "Grams of alcohol": "Грамове алкохол",
    "Standard units": "Стандартни единици",
    "Unit size": "Размер на единицата",
    "Automatic": "Автоматично",
    "UK": "Великобритания",
    "Nordic countries": "Северните страни",
    "US standard drink": "Стандартна напитка в САЩ",
    "WHO, most of Europe": "СЗО, по-голямата част от Европа",
    "Period": "Период",
    "Switch person": "Смени човека",
    "Add person": "Добави човек",
    "New person": "Нов човек",
    "You": "Ти",
    "Name": "Име",
    "All four change the curve, so none of them can be guessed for someone else.":
        "И четирите променят кривата, затова нито едно от тях не може да се гадае за друг "
        "човек.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Собственият им лимит и по-фините настройки могат да се променят по-късно в раздела "
        "„Профил“, докато този човек е избран.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Бързо добавяне",
    "Choose a favourite drink": "Избери любима напитка",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Избери напитката, която обикновено поръчваш, и бутон на екрана „На живо“ ще я записва "
        "с едно докосване.",
    "This is your quick-add drink": "Това е напитката ти за бързо добавяне",
    "Set as my quick-add drink": "Задай като напитка за бързо добавяне",
    "This is now your usual": "Това вече е обичайната ти напитка",
    "Remove favourite": "Премахни любимата",
    "Always add this one": "Винаги добавяй тази напитка",
    "Logs it straight away, without opening anything.":
        "Записва я веднага, без да отваря нищо.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Едно докосване на екрана „На живо“ я записва, а прогнозният пик стои на бутона. Колко "
        "пълен е стомахът ти се взема от предишната напитка и може да се коригира веднага след "
        "това.",
    "Peak %@": "Пик %@",
    "%@ added": "Добавено: %@",
    "Save": "Запази",
    "Undo": "Отмени",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Резервно копие",
    "Export a backup": "Експортирай резервно копие",
    "Import a backup": "Импортирай резервно копие",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Резервното копие съдържа всеки човек, всяка сесия и всяка напитка. Импортирането "
        "добавя липсващото — то никога не променя и не премахва нищо от вече наличното.",
    "Import this backup?": "Да се импортира ли това резервно копие?",
    "Import": "Импортирай",
    "Everything in this backup is already here.": "Всичко от това резервно копие вече е тук.",
    "Import finished": "Импортирането завърши",
    "OK": "Добре",

    # --- LanguageSection: the app's language ---
    "Language": "Език",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Отваря това приложение в Настройки, където „Предпочитан език“ задава езика на самото "
        "приложение — системният остава непроменен. iOS рестартира приложението, когато го "
        "смениш.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Импортирането е неуспешно",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Този файл не е резервно копие на LogMyDrink или е повреден.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Това резервно копие е направено с по-нова версия на LogMyDrink. Обнови приложението и "
        "опитай отново.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Ще добави сесии: %@, напитки: %@ и месечни суми: %@. Нищо, което вече е тук, не се променя и не се премахва.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Добавени: %@ сесии, %@ напитки и %@ месечни суми.',
    'months as totals': 'месеца само като суми',
    'by month only': 'само по месеци',
    'monthly total': 'месечна сума',
    'No daily records for this day': 'Няма дневни записи за този ден',
    'Monthly total: %@': 'Месечна сума: %@',
    'A dry month': 'Сух месец',

    # --- RemovePersonSection ---
    'Remove %@?': 'Да се премахне ли %@?',
    'Remove': 'Премахване',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Изтрива сесии: %@, напитки: %@ и месечни суми: %@. Това не може да бъде отменено.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Изтрива сесии: %@ и напитки: %@. Това не може да бъде отменено.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Плъзни наляво върху гост, за да го премахнеш с всичко, записано за него. Ти не можеш да бъдеш премахнат.',
    'People': 'Хора',
    'Owner': 'Собственик',
    'Everyone this app records. Switch, add, or remove someone.': 'Всички, които това приложение записва. Превключи, добави или премахни някого.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Пренесено от предната вечер',
    # --- History, second card (5.24) ---
    'Calories': 'Калории',
    'Sessions': 'Поводи',
    'Per session': 'На повод',
    'Under the influence': 'Под влияние',
    '%@ of the time': '%@ от времето',
    'Days over limit': 'Дни над лимита',
    'Longest sober run': 'Най-дълга трезва серия',
    'Favourite drink': 'Любима напитка',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Показване и език",
    "Data": "Данни",
    "Concentration": "Концентрация",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Остави скоростта на въпроса за честотата, освен ако нямаш измерване, с което да я сравниш.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Оценка, не измерване. Никога не решавай по това дали можеш да шофираш.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Оценен диапазон, не измерване. Никога не решавай по това дали можеш да шофираш.',
    'How does the app calculate this?':
        'Как изчислява приложението?',
    'approximately %@ %@':
        'приблизително %@ %@',
    'How it works':
        'Как работи',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Никога не решавай по това дали можеш да шофираш. Приложението оценява, а не измерва, и действителното ти ниво може да се различава значително.',
    'Why this app exists':
        'Защо съществува това приложение',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink ти помага да пиеш по-осъзнато и да запазиш контрола. Решението се взема преди следващата чаша, затова приложението ти показва предварително докъде би стигнало нивото ти с още една напитка и кога би достигнало върха си.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Но не става дума само за тази вечер. Всяка въведена напитка отива в историята, така че с месеци и години виждаш колко, колко често и колко високо пиеш. От това изпъкват навиците ти, а също и посоката, в която се променят – дали нещата се подобряват или влошават.',
    'How it calculates':
        'Как изчислява',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Оценката се основава на метода на Видмарк, с който алкохолът в кръвта се оценява от 30-те години на XX век; приложението използва негова усъвършенствана версия.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'От теглото, ръста, възрастта и пола ти изчислява колко вода има в тялото ти, защото именно в нея се разпределя алкохолът. Следи всяка напитка поотделно: колко алкохол е съдържала, колко бързо си я изпил и колко си ял преди това, защото от това зависи скоростта на усвояване.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Междувременно черният дроб разгражда всеки час приблизително постоянно количество; твоето се оценява според това колко често пиеш. Резултатът е крива минута по минута: къде си сега, накъде вървиш и кога отново ще си на нула.',
    'Details':
        'Подробности',
    'Body water':
        'Телесна вода',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Формулата на Уотсън (1980) по тегло, ръст, възраст и пол. Във формулата за жени няма възраст – това е особеност на формулата, а не грешка. Обемът на разпределение е телесната вода, разделена на 0,85 – водното съдържание на кръвта.',
    'Absorption':
        'Усвояване',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Всяка напитка има свой „стомах“. На празен стомах половината алкохол се усвоява за около 7 минути, на пълен – за около 21. Напитка, която отпиваш, постъпва в стомаха равномерно през цялото време на пиене.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Дава по-нисък връх и по-ранна нула. Изненадващо, но измерено: с храна стомахът разгражда част от алкохола още преди усвояването (приложението използва 5, 10 и 15 процента), а онова, което изобщо не е влязло, не е нужно да се разгражда.',
    'Elimination':
        'Разграждане',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Около 0,15 ‰ на час (публикуван диапазон 0,10–0,25), повече при редовно пиещите, защото чернодробните ензими се адаптират. Близо до нулата се забавя (кинетика на Михаелис–Ментен), затова кривата плавно затихва, вместо да прекъсне рязко.',
    'Computation':
        'Изчисление',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Кривата е резултат от числена симулация с резолюция от една минута.',
    'Why it is only an estimate':
        'Защо е само оценка',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Приложението не измерва нищо. Показва резултата от модел със средни стойности, а реалността може да е различна. Най-голямото неизвестно е колко бързо разграждаш алкохола: в правдоподобния диапазон само то може да измести върха с 40 процента, а нулата – с четири часа в рамките на една вечер.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Значение имат и гените, здравето на черния дроб, лекарствата, храната, сънят и умората – приложението не знае нищо от това. Точна стойност дава само сертифициран дрегер или кръвен тест.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Числото все пак е полезно. Ако приложението при теб постоянно показва малко повече или по-малко, то греши в една и съща посока всяка вечер, така че с времето научаваш какво означава дадена стойност за теб. В Профил можеш да покажеш и несигурността на скоростта на разграждане: тогава ще виждаш диапазон вместо едно число.',
    'Tips':
        'Съвети',
    'Favourite drink in one tap':
        'Любима напитка с едно докосване',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Задай любима напитка в Профил и бутонът на екрана На живо ще я въвежда с едно докосване.',
    'Widget':
        'Уиджет',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Добави го на заключения или началния екран: едно докосване въвежда любимата ти напитка. Докато имаш алкохол в тялото, показва и нивото ти и посоката му.',
    'How do I add it?':
        'Как да го добавя?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Кажи „Hey Siri, LogMyDrink now“ и Siri ще въведе любимата ти напитка и ще ти каже накъде отива върхът ти.',
    'Looking back':
        'Поглед назад',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Вчера“ в горната част на На живо те отвежда към предишния ден с едно докосване; разделът История показва навиците ти за седмици, месеци и години.',
    'Logging later':
        'Въвеждане по-късно',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Ако въвеждаш напитка по-късно, върни часа назад с бутоните − и +; пропуснат ден може да се допълни от изгледа Ден в Историята.',
    'One tap and done':
        'Едно докосване и готово',
    'Your favourite from the Lock Screen':
        'Любимата ти напитка от заключения екран',
    'Say it, don’t type it':
        'Кажи го, не го пиши',
    'See your patterns':
        'Виж навиците си',
    'Set what you drink most often and log it with a single tap.':
        'Задай какво пиеш най-често и го въвеждай с едно докосване.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Едно докосване на уиджета въвежда любимата ти напитка, без да търсиш приложението. Вечер показва и нивото ти.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now“ – Siri въвежда любимата ти напитка и ти казва накъде отива върхът ти.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Историята показва колко и колко високо пиеш за седмици, месеци и години и в каква посока се променя това.',
    'Set favourite':
        'Задай любима',
    'Add widget':
        'Добави уиджет',
    'Got it':
        'Ясно',
    'Open History':
        'Отвори историята',
    'Later':
        'По-късно',
    'Don’t show again':
        'Не показвай повече',
    'Lock Screen':
        'Заключен екран',
    'Home Screen':
        'Начален екран',
    'Where':
        'Къде',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Заключи iPhone и след това задръж пръст върху заключения екран.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Докосни „Персонализиране“, после „Заключен екран“ и накрая реда с уиджети под часовника.',
    'Choose LogMyDrink, then tap Done.':
        'Избери LogMyDrink и докосни „Готово“.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Задръж пръст върху празно място на началния екран, докато иконките започнат да се клатят.',
    'Tap Edit, then Add Widget.':
        'Докосни „Редактиране“, после „Добавяне на уиджет“.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Потърси LogMyDrink, избери размер и докосни „Добавяне на уиджет“.',
    'A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.':
        'Докосване на уиджета отваря приложението и въвежда любимата ти напитка. Докато имаш алкохол в тялото, показва и нивото ти и посоката му.',
    'Add the widget':
        'Добави уиджета',
    'Show tips':
        'Показвай съвети',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Най-много един съвет на ден при отваряне на приложението – никога, докато имаш алкохол в тялото.',
}
