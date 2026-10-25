"""
Polish.

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Promile",
    "Percent": "Procent",

    # --- DrinkCatalog: drink types ---
    "Beer": "Piwo",
    "Wine": "Wino",
    "Champagne": "Wino musujące",
    "Shot": "Shot",
    "Cocktail": "Koktajl",
    "Custom": "Własny",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Pusty żołądek",
    "Moderately full": "Średnio pełny",
    "Full stomach": "Pełny żołądek",
    "Empty": "Pusty",
    "Moderate": "Średni",
    "Full": "Pełny",
    "Fast absorption, higher and earlier peak.":
        "Szybkie wchłanianie, wyższy i wcześniejszy szczyt.",
    "Moderate absorption.": "Umiarkowane wchłanianie.",
    "Slow absorption, lower and later peak.":
        "Powolne wchłanianie, niższy i późniejszy szczyt.",

    # --- DrinkingFrequency ---
    "Rarely": "Rzadko",
    "A few times a month": "Kilka razy w miesiącu",
    "Several times a week": "Kilka razy w tygodniu",
    "Almost daily": "Prawie codziennie",
    "A few occasions a year": "Kilka razy w roku",
    "Social drinking": "Picie towarzyskie",
    "Weekly routine": "Cotygodniowy zwyczaj",
    "Daily or nearly daily": "Codziennie lub prawie codziennie",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Czas",
    "Level": "Poziom",
    "Lower": "Dolne",
    "Upper": "Górne",
    "Lower estimate": "Dolne oszacowanie",
    "Upper estimate": "Górne oszacowanie",
    "Personal limit": "Osobisty limit",
    "Drink": "Napój",

    # --- BACChartView ---
    "Expected peak around %@": "Szczyt spodziewany około %@",
    "Peaked around %@": "Szczyt był około %@",
    "No active session": "Brak aktywnej sesji",
    "Still rising": "Nadal rośnie",
    "YOUR LIMIT %@": "TWÓJ LIMIT %@",
    "possible range": "możliwy zakres",

    # --- Live screen: the day with nothing on it ---
    "Live": "Na żywo",
    "Nothing logged today": "Nic dziś nie zapisano",
    "Add a drink when you have one.": "Dodaj napój, gdy coś wypijesz.",

    # --- Tabs and history ---
    "History": "Historia",
    "No past sessions yet": "Brak wcześniejszych sesji",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Sesja pojawia się tutaj po zakończeniu – gdy twój poziom zejdzie do zera i minie "
        "kilka godzin.",
    "%@ drinks": "Napoje: %@",
    "peak": "szczyt",
    "Started": "Początek",
    "Lasted": "Trwała",
    "Duration": "Czas trwania",
    "Sober around": "Trzeźwy ok.",
    "Sober at": "Trzeźwy",
    "Remaining": "Pozostało",
    "next day": "następnego dnia",
    "previous day": "poprzedniego dnia",
    "%@ days later": "%@ dni później",
    "%@ days earlier": "%@ dni wcześniej",
    "Calculated with your profile at the time":
        "Obliczone na podstawie twojego ówczesnego profilu",

    # --- TodayView ---
    "Profile": "Profil",
    "Drinks": "Napoje",
    "Units": "Jednostki",
    "Drinks this session": "Napoje w tej sesji",
    "Add drink": "Dodaj napój",

    # --- Editing an already logged drink ---
    "Edit drink": "Edytuj napój",
    "Save changes": "Zapisz zmiany",
    "With this": "Z nim",
    "Delete": "Usuń",
    "tap to edit · swipe to delete": "stuknij, aby edytować · przesuń, aby usunąć",

    # --- Drinking pace ---
    "How fast": "Jak szybko",
    "In one go": "Duszkiem",
    "Counts as a single swallow — the steepest possible rise.":
        "Liczy się jako jeden łyk – najbardziej stromy możliwy wzrost.",
    "A quick drink. The level climbs fast.": "Wypity szybko. Poziom szybko rośnie.",
    "A normal pace.": "Normalne tempo.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Pity powoli. Dużo łagodniejszy wzrost przy tej samej ilości alkoholu.",

    # --- AddDrinkSheet ---
    "Cancel": "Anuluj",
    "Now": "Teraz",
    "Projected peak": "Przewidywany szczyt",
    "Peak at": "Szczyt o",
    "Clears": "Zejście do zera",
    "This would cross your limit": "To przekroczyłoby twój limit",
    "Around %@, for up to %@.": "Około %@, przez maksymalnie %@.",
    "This might cross your limit": "To może przekroczyć twój limit",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Przy wolniejszym metabolizmie tak, przy szybszym nie. Na tym polega niepewność tego "
        "oszacowania.",
    "Type": "Rodzaj",
    "Amount": "Ilość",
    "Strength": "Moc",
    "%@ units": "Jednostki: %@",
    "%@ g alcohol": "%@ g alkoholu",
    "Stomach": "Żołądek",
    "When": "Kiedy",
    "Done": "Gotowe",
    "Add": "Dodaj",

    # --- ProfileSheet ---
    "Male": "Mężczyzna",
    "Female": "Kobieta",
    "Sex": "Płeć",
    "Weight": "Waga",
    "Height": "Wzrost",
    "Age": "Wiek",
    "kg": "kg",
    "cm": "cm",
    "yrs": "lat",
    "Body": "Ciało",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "Całkowita woda ustrojowa jest wyliczana z równań Watsona i wyznacza objętość, w "
        "której rozprowadza się alkohol.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "Całkowita woda ustrojowa jest wyliczana z równań Watsona i wyznacza objętość, w "
        "której rozprowadza się alkohol. Równanie dla kobiet nie uwzględnia wieku, więc jego "
        "zmiana nie wpłynie na wynik.",
    "Drinking frequency": "Częstotliwość picia",
    "How often do you drink?": "Jak często pijesz?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "Tak szacujemy twoje tempo eliminacji. Regularne picie indukuje wątrobowy szlak CYP2E1, więc osoby pijące często usuwają alkohol szybciej. To najsłabszy punkt modelu i dlatego w sekcji Wyświetlanie i język możesz określić, jak dużo tej niepewności aplikacja ci pokazuje.",
    "Your limit": "Twój limit",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Twoja własna wartość odniesienia, a nie limit prawny. Aplikacja informuje, gdy "
        "planowany napój sprawiłby, że ją przekroczysz, i jak długo pozostaniesz powyżej.",
    "Calculated values": "Obliczone wartości",
    "Total body water": "Całkowita woda ustrojowa",
    "Distribution volume": "Objętość dystrybucji",
    "Widmark factor": "Współczynnik Widmarka",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "Współczynnik Widmarka wynosi zwykle około 0,68 u mężczyzn i 0,55 u kobiet. Jeśli twój "
        "jest daleki od tych wartości, warto sprawdzić dane powyżej.",
    "Elimination rate": "Tempo eliminacji",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Jak szybko twoja wątroba usuwa alkohol po jego wchłonięciu – nachylenie opadającej "
        "strony krzywej.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "Alkohol znika w mniej więcej stałej ilości na godzinę, a nie jako procent poziomu, "
        "ponieważ enzym, który go rozkłada, przy niemal każdym poziomie pracuje już na pełnych "
        "obrotach. Dlatego w ogóle istnieją reguły w rodzaju „jedna porcja na godzinę”.",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Przy tym ustawieniu %@ schodzi do zera w około %@. Prawie wszyscy mieszczą się w "
        "przedziale %@ na godzinę.",
    "How to find yours": "Jak poznać swoje tempo",
    "With a breathalyser": "Z alkomatem",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Dmuchnij dwa razy, w odstępie co najmniej godziny, w fazie spadku – dwie "
        "godziny lub więcej po ostatnim napoju, nic w międzyczasie nie pijąc. Odejmij drugi "
        "odczyt od pierwszego i podziel przez liczbę godzin między nimi.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Na przykład %@ i %@ dwie godziny później daje %@ na godzinę.",
    "Without one": "Bez niego",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "Aplikacja podaje, kiedy spodziewa się twojego zejścia do zera. Jeśli regularnie "
        "wracasz do normy wyraźnie wcześniej, twoje tempo jest wyższe niż ustawione – podnieś "
        "je o jeden stopień i obserwuj przez kilka sesji. Jeśli trwa to dłużej, niż "
        "przewidywano, obniż je.",
    "What moves it": "Co na to wpływa",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Regularne picie je podnosi: enzym wątrobowy, który wykonuje tę pracę, ulega indukcji "
        "przy częstym używaniu. Średnio jest też nieco wyższe u kobiet, a niższe na czczo lub "
        "przy problemach z wątrobą.",
    "Uncertainty": "Niepewność",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "Przy zerze każda wartość to pojedyncza liczba – najlepsze oszacowanie aplikacji. "
        "Powyżej zera te same wartości pokazywane są jako zakresy, a pasmo na wykresie "
        "odpowiednio się poszerza.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Pojedyncza liczba jest łatwiejszym punktem odniesienia: z czasem dowiesz się, jak się "
        "czujesz przy swoim własnym 0,6. Zakres to odpowiedź bardziej dosłowna, bo tempo "
        "naprawdę jest niepewne. Oba podejścia da się obronić – to twoja decyzja.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "Rozrzut wynikający z twojej częstotliwości picia to ± %@ na godzinę.",
    "Rate": "Tempo",
    "Range": "Zakres",
    "Advanced": "Zaawansowane",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Week": "Tydzień",
    "Month": "Miesiąc",
    "Year": "Rok",
    "Sober days": "Dni bez alkoholu",
    "Change": "Zmiana",
    "before records": "przed rozpoczęciem zapisów",
    "See further back": "Sięgnij dalej wstecz",
    "Weeks, months and years side by side — and every evening older than seven days.": "Tygodnie, miesiące i lata obok siebie – oraz każdy wieczór starszy niż siedem dni.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Wszystko, co zapisałeś, jest już zachowane. Odblokowanie tylko to pokazuje.",
    "Back up and restore": "Kopia zapasowa i przywracanie",
    "Log for friends too": "Zapisuj też za znajomych",
    "Switch to someone else in one tap and log their drinks with their own body and limit — each person gets their own curve and history.": "Jednym stuknięciem przełącz się na kogoś innego i zapisuj jego napoje z jego własnym ciałem i limitem – każdy ma swoją krzywą i historię.",
    "Save everything to a file, and read a backup back in — on this phone or on a new one.": "Zapisz wszystko w pliku i wczytaj kopię zapasową z powrotem – na tym telefonie albo na nowym.",
    "Backup and restore are part of Pro.": "Kopia zapasowa i przywracanie są częścią Pro.",
    "Today": "Dziś",
    "Day": "Dzień",
    "Yesterday": "Wczoraj",
    "No drinks on this day": "Brak napojów tego dnia",
    "Trend": "Trend",
    "day": "dzień",
    "Smoothing": "Wygładzanie",
    "%@ sessions": "Sesje: %@",
    "No data before %@": "Brak danych przed %@",
    "vs.": "wobec",
    "Grams": "Gramy",
    "Grams of alcohol": "Gramy alkoholu",
    "Standard units": "Jednostki standardowe",
    "Unit size": "Wielkość jednostki",
    "Automatic": "Automatycznie",
    "UK": "Wielka Brytania",
    "Nordic countries": "Kraje nordyckie",
    "US standard drink": "Standardowa porcja w USA",
    "WHO, most of Europe": "WHO, większość Europy",
    "Period": "Okres",
    "Switch person": "Zmień osobę",
    "Add person": "Dodaj osobę",
    "New person": "Nowa osoba",
    "You": "Ty",
    "Name": "Imię",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Wszystkie cztery zmieniają przebieg krzywej, więc żadnej z nich nie da się zgadnąć za "
        "kogoś innego.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "Własny limit tej osoby i dokładniejsze ustawienia można zmienić później na karcie "
        "Profil, gdy ta osoba jest wybrana.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Szybkie dodawanie",
    "Choose a favourite drink": "Wybierz ulubiony napój",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Wybierz napój, który zwykle zamawiasz, a przycisk na ekranie Na żywo zapisze go "
        "jednym stuknięciem.",
    "This is your quick-add drink": "To twój napój do szybkiego dodawania",
    "Set as my quick-add drink": "Ustaw jako mój napój do szybkiego dodawania",
    "This is now your usual": "To teraz twój stały napój",
    "Remove favourite": "Usuń z ulubionych",
    "Always add this one": "Zawsze dodawaj ten napój",
    "Logs it straight away, without opening anything.":
        "Zapisuje go od razu, bez otwierania czegokolwiek.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Jedno stuknięcie na ekranie Na żywo zapisuje ten napój, a na przycisku widać "
        "przewidywany szczyt. Stopień wypełnienia żołądka jest przejmowany z poprzedniego "
        "napoju i można go poprawić zaraz po zapisaniu.",
    "Peak %@": "Szczyt %@",
    "%@ added": "Dodano: %@",
    "Save": "Zapisz",
    "Undo": "Cofnij",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Kopia zapasowa",
    "Export a backup": "Eksportuj kopię zapasową",
    "Import a backup": "Importuj kopię zapasową",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Kopia zapasowa zawiera wszystkie osoby, sesje i napoje. Import dodaje tylko to, czego "
        "brakuje – nigdy nie zmienia ani nie usuwa niczego, co już tu jest.",
    "Import this backup?": "Zaimportować tę kopię zapasową?",
    "Import": "Importuj",
    "Everything in this backup is already here.": "Wszystko z tej kopii zapasowej już tu jest.",
    "Import finished": "Import zakończony",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Język",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Otwiera tę aplikację w Ustawieniach, gdzie „Preferowany język” ustawia język samej "
        "aplikacji – język systemu pozostaje bez zmian. iOS uruchamia aplikację ponownie po "
        "zmianie.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Nie udało się zaimportować",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Ten plik nie jest kopią zapasową LogMyDrink albo jest uszkodzony.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Ta kopia zapasowa została utworzona w nowszej wersji aplikacji LogMyDrink. "
        "Zaktualizuj aplikację i spróbuj ponownie.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Dodaje sesji: %@, napojów: %@ i sum miesięcznych: %@. Nic z tego, co już tu jest, nie zostanie zmienione ani usunięte.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Dodano sesji: %@, napojów: %@ i sum miesięcznych: %@.',
    'months as totals': 'mies. tylko jako sumy',
    'by month only': 'tylko w skali miesiąca',
    'monthly total': 'suma miesięczna',
    'No daily records for this day': 'Brak dziennych zapisów dla tego dnia',
    'Monthly total: %@': 'Suma miesięczna: %@',
    'A dry month': 'Miesiąc bez alkoholu',

    # --- RemovePersonSection ---
    'Remove %@?': 'Usunąć %@?',
    'Remove': 'Usuń',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Usuwa sesji: %@, napojów: %@ i sum miesięcznych: %@. Tego nie można cofnąć.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Usuwa sesji: %@ i napojów: %@. Tego nie można cofnąć.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Przesuń gościa w lewo, aby usunąć go wraz ze wszystkim, co pod nim zapisano. Ciebie nie można usunąć.',
    'People': 'Osoby',
    'Owner': 'Właściciel',
    'Everyone this app records. Switch, add, or remove someone.': 'Wszyscy, których dane zapisuje ta aplikacja. Przełącz, dodaj lub usuń osobę.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Przeniesione z poprzedniego wieczoru',
    # --- History, second card (5.24) ---
    'Calories': 'Kalorie',
    'Sessions': 'Sesje',
    'Per session': 'Na sesję',
    'Under the influence': 'Pod wpływem',
    '%@ of the time': '%@ czasu',
    'Days over limit': 'Dni powyżej limitu',
    'Longest sober run': 'Najdłuższa seria bez alkoholu',
    'Favourite drink': 'Ulubiony napój',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Wyświetlanie i język",
    "Data": "Dane",
    "Concentration": "Stężenie",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Jeśli nie masz pomiaru do porównania, zostaw tempo wyznaczone na podstawie pytania o częstotliwość.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Szacunek, nie pomiar. Nigdy nie decyduj na tej podstawie, czy możesz prowadzić.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Szacowany zakres, nie pomiar. Nigdy nie decyduj na tej podstawie, czy możesz prowadzić.',
    'How does the app calculate this?':
        'Jak aplikacja to oblicza?',
    'approximately %@ %@':
        'około %@ %@',
    'How it works':
        'Jak to działa',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nigdy nie decyduj na tej podstawie, czy możesz prowadzić. Aplikacja szacuje, a nie mierzy, a twój rzeczywisty poziom może się znacznie różnić.',
    'Why this app exists':
        'Po co ta aplikacja',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'LogMyDrink pomaga pić bardziej świadomie i zachować kontrolę. Decyzja zapada przed kolejnym kieliszkiem, więc aplikacja z wyprzedzeniem pokazuje, jak wysoko kolejny napój podniesie twój poziom i kiedy nastąpi szczyt.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Ale nie chodzi tylko o dzisiejszy wieczór. Każdy zapisany napój trafia do Historii, więc na przestrzeni miesięcy i lat widzisz, ile, jak często i do jakiego poziomu pijesz. Wyłaniają się z tego twoje wzorce oraz kierunek, w którym się zmieniają – na lepsze czy na gorsze.',
    'How it calculates':
        'Jak liczy aplikacja',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'Szacunek opiera się na metodzie Widmarka, stosowanej od lat 30. XX wieku do szacowania stężenia alkoholu we krwi; aplikacja używa jej udoskonalonej wersji.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'Na podstawie wagi, wzrostu, wieku i płci oblicza, ile wody zawiera twój organizm, bo w niej rozprowadza się alkohol. Śledzi każdy napój osobno: ile zawierał alkoholu, jak szybko go wypiłeś i ile wcześniej zjadłeś, bo od tego zależy tempo wchłaniania.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'W tym czasie wątroba rozkłada co godzinę mniej więcej stałą ilość; ile w twoim przypadku, szacuje się na podstawie tego, jak często pijesz. Wynikiem jest krzywa, minuta po minucie: gdzie jesteś teraz, dokąd zmierzasz i kiedy wrócisz do zera.',
    'Details':
        'Szczegóły',
    'Body water':
        'Woda w organizmie',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'Wzór Watsona (1980) na podstawie wagi, wzrostu, wieku i płci. Wzór dla kobiet nie uwzględnia wieku – to cecha wzoru, nie błąd. Objętość dystrybucji to woda w organizmie podzielona przez 0,85, czyli zawartość wody we krwi.',
    'Absorption':
        'Wchłanianie',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Każdy napój ma swój własny „żołądek”. Na pusty żołądek połowa alkoholu wchłania się w około 7 minut, na pełny w około 21. Napój pity małymi łykami trafia do żołądka równomiernie przez cały czas picia.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Daje niższy szczyt i wcześniejszy powrót do zera. Zaskakujące, ale zmierzone: przy jedzeniu żołądek rozkłada część alkoholu przed wchłonięciem (aplikacja przyjmuje 5, 10 i 15 procent), a tego, co nigdy nie trafiło do krwi, nie trzeba rozkładać.',
    'Elimination':
        'Eliminacja',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Około 0,15 ‰ na godzinę (zakres w literaturze 0,10–0,25), więcej u osób pijących regularnie, bo enzymy wątroby się dostosowują. Blisko zera zwalnia (kinetyka Michaelisa-Menten), więc krzywa łagodnie wygasa zamiast urywać się nagle.',
    'Computation':
        'Obliczenia',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'Krzywa pochodzi z symulacji numerycznej o rozdzielczości jednej minuty.',
    'Why it is only an estimate':
        'Dlaczego to tylko szacunek',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'Aplikacja niczego nie mierzy. To, co pokazuje, jest wynikiem modelu opartego na wartościach średnich, a rzeczywistość może być inna. Największą niewiadomą jest tempo rozkładu alkoholu: w wiarygodnym zakresie samo ono może przesunąć szczyt o 40 procent, a powrót do zera o cztery godziny tego samego wieczoru.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'Znaczenie mają też genetyka, stan wątroby, leki, to, co zjadłeś, sen i zmęczenie – aplikacja nic o tym nie wie. Dokładną wartość daje tylko legalizowany alkomat lub badanie krwi.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Liczba i tak jest przydatna. Jeśli w twoim przypadku aplikacja stale pokazuje trochę za dużo lub za mało, myli się każdego wieczoru w tę samą stronę, więc z czasem uczysz się, co dana wartość oznacza dla ciebie. W Profilu możesz też pokazać niepewność tempa eliminacji: zobaczysz wtedy zakres zamiast jednej liczby.',
    'Tips':
        'Wskazówki',
    'Favourite drink in one tap':
        'Ulubiony napój jednym stuknięciem',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Ustaw ulubiony napój w Profilu, a przycisk na ekranie Na żywo zapisze go jednym stuknięciem.',
    'Widget':
        'Widżet',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Dodaj go do ekranu blokady lub ekranu początkowego: jedno stuknięcie zapisuje ulubiony napój. Z Pro, dopóki masz alkohol w organizmie, pokazuje też twój poziom i jego kierunek.',
    'How do I add it?':
        'Jak go dodać?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Powiedz „Hey Siri, LogMyDrink now”, a Siri zapisze ulubiony napój i powie, dokąd zmierza twój szczyt. (Polecenie działa po angielsku.)',
    'Looking back':
        'Spojrzenie wstecz',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '„Wczoraj” u góry ekranu Na żywo przenosi jednym stuknięciem do poprzedniego dnia; karta Historia pokazuje twoje wzorce na przestrzeni tygodni, miesięcy i lat.',
    'Logging later':
        'Zapis po fakcie',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Jeśli zapisujesz napój później, cofnij godzinę przyciskami − i +; pominięty dzień możesz uzupełnić w widoku Dzień w Historii.',
    'One tap and done':
        'Jedno stuknięcie i gotowe',
    'Your favourite from the Lock Screen':
        'Ulubiony napój z ekranu blokady',
    'Say it, don’t type it':
        'Powiedz, zamiast pisać',
    'See your patterns':
        'Zobacz swoje wzorce',
    'Set what you drink most often and log it with a single tap.':
        'Ustaw, co pijesz najczęściej, i zapisuj to jednym stuknięciem.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Jedno stuknięcie w widżet zapisuje ulubiony napój, bez szukania aplikacji. Wieczorem pokazuje też twój poziom.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '„Hey Siri, LogMyDrink now” – Siri zapisze ulubiony napój i powie, dokąd zmierza twój szczyt.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'Historia pokazuje, ile i do jakiego poziomu pijesz na przestrzeni tygodni, miesięcy i lat, oraz w którą stronę to się zmienia.',
    'Set favourite':
        'Ustaw ulubiony',
    'Add widget':
        'Dodaj widżet',
    'Got it':
        'Rozumiem',
    'Open History':
        'Otwórz Historię',
    'Don’t show again':
        'Nie pokazuj więcej',
    'Lock Screen':
        'Ekran blokady',
    'Home Screen':
        'Ekran początkowy',
    'Where':
        'Gdzie',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Zablokuj iPhone’a, a następnie dotknij i przytrzymaj ekran blokady.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Stuknij przycisk Dostosuj, potem Ekran blokady, a następnie rząd widżetów pod zegarem.',
    'Choose LogMyDrink, then tap Done.':
        'Wybierz LogMyDrink i stuknij przycisk Gotowe.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Dotknij i przytrzymaj puste miejsce na ekranie początkowym, aż ikony zaczną drżeć.',
    'Tap Edit, then Add Widget.':
        'Stuknij przycisk Edytuj, a następnie Dodaj widżet.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Wyszukaj LogMyDrink, wybierz rozmiar i stuknij Dodaj widżet.',
    'A tap on the widget opens the app and logs your favourite drink. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Stuknięcie w widżet otwiera aplikację i zapisuje ulubiony napój. Z Pro, dopóki masz alkohol w organizmie, pokazuje też twój poziom i jego kierunek.',
    'Add the widget':
        'Dodaj widżet',
    'Show tips':
        'Pokazuj wskazówki',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'Najwyżej jedna wskazówka dziennie, przy otwarciu aplikacji – nigdy, gdy masz alkohol w organizmie.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'Co pokazuje liczba',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'Liczba to szacowane stężenie alkoholu we krwi (po angielsku BAC, blood alcohol concentration): ile alkoholu masz we krwi.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'W promilach (‰) to gramy alkoholu na litr krwi: 0,5 ‰ oznacza pół grama w każdym litrze. W procentach to gramy na 100 mililitrów, więc ten sam poziom daje dziesięć razy mniejszą liczbę: 0,5 ‰ to 0,05 procent. Przełączysz je w Profil › Wyświetlanie i język.',
    'The curve shows the same level over time, minute by minute.':
        'Krzywa pokazuje ten sam poziom w czasie, minuta po minucie.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'Promil (‰) to gramy alkoholu na litr krwi, procent – gramy na 100 mililitrów: 0,5 ‰ to 0,05 procent.',

    # --- ProPaywallSheet: plans and buying ---
    "Prices could not be loaded.": "Nie udało się wczytać cen.",
    "Try again": "Spróbuj ponownie",
    "Save %@": "Oszczędzasz %@",
    "About %@ a month": "Około %@ miesięcznie",
    "Yearly": "Rocznie",
    "Monthly": "Miesięcznie",
    "%@ / year": "%@ / rok",
    "%@ / month": "%@ / mies.",
    "Start my free month": "Zacznij darmowy miesiąc",
    "Subscribe": "Subskrybuj",
    "Free for one month, then %@ a year.": "Miesiąc za darmo, potem %@ rocznie.",
    "Free for one month, then %@ a month.": "Miesiąc za darmo, potem %@ miesięcznie.",
    "%@ a year.": "%@ rocznie.",
    "%@ a month.": "%@ miesięcznie.",
    "Renews automatically until you cancel. Cancel anytime in Settings.": "Odnawia się automatycznie, dopóki nie anulujesz. Anuluj w dowolnej chwili w Ustawieniach.",
    "Restore purchases": "Przywróć zakupy",
    "Redeem code": "Zrealizuj kod",
    "Terms of Use": "Warunki użytkowania",
    "Privacy Policy": "Prywatność",
    "Waiting for approval. Pro opens as soon as the purchase goes through.": "Czeka na zatwierdzenie. Pro odblokuje się, gdy tylko zakup zostanie zrealizowany.",
    "The purchase did not go through. Please try again.": "Zakup się nie udał. Spróbuj ponownie.",
    "No active subscription was found for this Apple ID.": "Nie znaleziono aktywnej subskrypcji dla tego Apple ID.",
}
