"""
Portuguese (European).

Drafted in one pass and not yet read by a speaker of the language, so every
string lands in the catalog as `needs_review`. Moving the code into REVIEWED
in make_catalog.py is the act of vouching for it.
"""

TRANSLATIONS = {
    # --- BACUnit ---
    "Per mille": "Por mil",
    "Percent": "Percentagem",

    # --- DrinkCatalog: drink types ---
    "Beer": "Cerveja",
    "Wine": "Vinho",
    "Champagne": "Espumante",
    "Shot": "Shot",
    "Cocktail": "Cocktail",
    "Custom": "Personalizado",

    # --- DrinkCatalog: stomach state ---
    "Empty stomach": "Estômago vazio",
    "Moderately full": "Moderadamente cheio",
    "Full stomach": "Estômago cheio",
    "Empty": "Vazio",
    "Moderate": "Moderado",
    "Full": "Cheio",
    "Fast absorption, higher and earlier peak.": "Absorção rápida, pico mais alto e mais cedo.",
    "Moderate absorption.": "Absorção moderada.",
    "Slow absorption, lower and later peak.": "Absorção lenta, pico mais baixo e mais tarde.",

    # --- DrinkingFrequency ---
    "Rarely": "Raramente",
    "A few times a month": "Algumas vezes por mês",
    "Several times a week": "Várias vezes por semana",
    "Almost daily": "Quase todos os dias",
    "A few occasions a year": "Algumas ocasiões por ano",
    "Social drinking": "Consumo social",
    "Weekly routine": "Rotina semanal",
    "Daily or nearly daily": "Todos os dias ou quase",

    # --- BACChartView: chart axis and series labels (VoiceOver reads these) ---
    "Time": "Hora",
    "Level": "Nível",
    "Lower": "Inferior",
    "Upper": "Superior",
    "Lower estimate": "Estimativa inferior",
    "Upper estimate": "Estimativa superior",
    "Personal limit": "Limite pessoal",
    "Drink": "Bebida",

    # --- BACChartView ---
    "Expected peak around %@": "Pico previsto por volta de %@",
    "Peaked around %@": "Pico por volta de %@",
    "No active session": "Nenhuma sessão ativa",
    "Still rising": "Ainda a subir",
    "YOUR LIMIT %@": "O TEU LIMITE %@",
    "possible range": "intervalo possível",

    # --- Live screen: the day with nothing on it ---
    "Live": "Em direto",
    "Nothing logged today": "Nada registado hoje",
    "Add a drink when you have one.": "Adiciona uma bebida sempre que beberes uma.",

    # --- Tabs and history ---
    "History": "Histórico",
    "No past sessions yet": "Ainda não há sessões anteriores",
    "A session appears here once it has ended — when your level has cleared and a few hours "
    "have passed.":
        "Uma sessão aparece aqui depois de terminar — quando o teu nível tiver voltado a zero e "
        "tiverem passado algumas horas.",
    "%@ drinks": "%@ bebidas",
    "peak": "pico",
    "Started": "Começou",
    "Lasted": "Durou",
    "Duration": "Duração",
    "Sober around": "Sóbrio aprox.",
    "Sober at": "Sóbrio",
    "Remaining": "Restante",
    "next day": "no dia seguinte",
    "previous day": "no dia anterior",
    "%@ days later": "%@ dias depois",
    "%@ days earlier": "%@ dias antes",
    "Calculated with your profile at the time": "Calculado com o teu perfil da altura",

    # --- TodayView ---
    "Profile": "Perfil",
    "Drinks": "Bebidas",
    "Units": "Unidades",
    "Drinks this session": "Bebidas nesta sessão",
    "Add drink": "Adicionar bebida",

    # --- Editing an already logged drink ---
    "Edit drink": "Editar bebida",
    "Save changes": "Guardar alterações",
    "With this": "Com esta",
    "Delete": "Eliminar",
    "tap to edit · swipe to delete": "toca para editar · desliza para eliminar",

    # --- Drinking pace ---
    "How fast": "Com que rapidez",
    "In one go": "De uma vez",
    "Counts as a single swallow — the steepest possible rise.":
        "Conta como um único gole — a subida mais acentuada possível.",
    "A quick drink. The level climbs fast.": "Uma bebida rápida. O nível sobe depressa.",
    "A normal pace.": "Um ritmo normal.",
    "Nursed slowly. Much gentler climb for the same alcohol.":
        "Bebida devagar. Subida muito mais suave para o mesmo álcool.",

    # --- AddDrinkSheet ---
    "Cancel": "Cancelar",
    "Now": "Agora",
    "Projected peak": "Pico previsto",
    "Peak at": "Pico às",
    "Clears": "Volta a zero",
    "This would cross your limit": "Isto ultrapassaria o teu limite",
    "Around %@, for up to %@.": "Por volta de %@, durante no máximo %@.",
    "This might cross your limit": "Isto pode ultrapassar o teu limite",
    "With slower metabolism yes, with faster no. That's the uncertainty of the estimate.":
        "Com um metabolismo mais lento sim, com um mais rápido não. É essa a incerteza da "
        "estimativa.",
    "Type": "Tipo",
    "Amount": "Quantidade",
    "Strength": "Teor alcoólico",
    "%@ units": "%@ unidades",
    "%@ g alcohol": "%@ g de álcool",
    "Stomach": "Estômago",
    "When": "Quando",
    "Done": "OK",
    "Add": "Adicionar",

    # --- ProfileSheet ---
    "Male": "Masculino",
    "Female": "Feminino",
    "Sex": "Sexo",
    "Weight": "Peso",
    "Height": "Altura",
    "Age": "Idade",
    "kg": "kg",
    "cm": "cm",
    "yrs": "anos",
    "Body": "Corpo",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into.":
        "A água corporal total vem das equações de Watson, que definem o volume no qual o "
        "álcool se distribui.",
    "Total body water comes from the Watson equations, which set the volume alcohol "
    "distributes into. The female equation does not include age, so changing it will not "
    "affect the result.":
        "A água corporal total vem das equações de Watson, que definem o volume no qual o "
        "álcool se distribui. A equação feminina não inclui a idade, por isso alterá-la não "
        "afeta o resultado.",
    "Drinking frequency": "Frequência de consumo",
    "How often do you drink?": "Com que frequência bebes?",
    "This is how we estimate your elimination rate. Regular drinking induces the liver's CYP2E1 pathway, so frequent drinkers clear alcohol faster. It is the weakest point of the model, which is why you can set under Display & language how much of that uncertainty the app shows you.":
        "É assim que estimamos a tua taxa de eliminação. Beber com regularidade induz a via do CYP2E1 no fígado, por isso quem bebe com frequência elimina o álcool mais depressa. É o ponto mais fraco do modelo, e é por isso que podes definir em Apresentação e idioma quanto dessa incerteza a app te mostra.",
    "Your limit": "O teu limite",
    "Your own reference number, not a legal limit. The app tells you when a planned drink "
    "would take you past it, and for how long you would stay above.":
        "Um número de referência teu, não um limite legal. A app avisa-te quando uma bebida "
        "planeada te faria ultrapassá-lo, e durante quanto tempo ficarias acima.",
    "Calculated values": "Valores calculados",
    "Total body water": "Água corporal total",
    "Distribution volume": "Volume de distribuição",
    "Widmark factor": "Fator de Widmark",
    "The Widmark factor is typically around 0.68 for men and 0.55 for women. If yours is far "
    "from that, it is worth checking the values above.":
        "O fator de Widmark ronda normalmente 0,68 nos homens e 0,55 nas mulheres. Se o teu "
        "estiver longe disso, vale a pena verificar os valores acima.",
    "Elimination rate": "Taxa de eliminação",
    "How fast your liver clears alcohol once it has been absorbed — the slope of the falling "
    "side of the curve.":
        "Com que rapidez o teu fígado elimina o álcool depois de absorvido — o declive da "
        "parte descendente da curva.",
    "Alcohol leaves at a roughly fixed amount per hour rather than a percentage, because the "
    "enzyme that breaks it down already runs at full capacity at almost any level. That is why "
    "rules of thumb like “one drink an hour” exist at all.":
        "O álcool sai a um ritmo aproximadamente fixo por hora, e não a uma percentagem, "
        "porque a enzima que o decompõe já trabalha no máximo em quase qualquer nível. É por "
        "isso que existem regras práticas como «uma bebida por hora».",
    "At this setting, %@ takes about %@ to clear. Almost everyone falls between %@ per hour.":
        "Com esta definição, %@ demora cerca de %@ a voltar a zero. Quase toda a gente fica "
        "entre %@ por hora.",
    "How to find yours": "Como descobrir a tua",
    "With a breathalyser": "Com um alcoolímetro",
    "Blow twice, at least an hour apart, on the falling side — two hours or more after your "
    "last drink, with nothing in between. Subtract the second reading from the first and "
    "divide by the hours between them.":
        "Sopra duas vezes, com pelo menos uma hora de intervalo, na parte descendente — duas "
        "horas ou mais depois da última bebida, sem beber nada pelo meio. Subtrai a segunda "
        "leitura à primeira e divide pelas horas entre elas.",
    "For example %@ and %@ two hours later works out to %@ per hour.":
        "Por exemplo, %@ e %@ duas horas depois dão %@ por hora.",
    "Without one": "Sem alcoolímetro",
    "The app tells you when it expects you to clear. If you are reliably back to normal well "
    "before that, your rate is higher than the setting — nudge it up a step and watch for a "
    "few sessions. If it takes longer than predicted, nudge it down.":
        "A app diz-te quando espera que voltes a zero. Se estiveres consistentemente de volta ao "
        "normal bem antes disso, a tua taxa é mais alta do que a definida — aumenta-a um nível e "
        "observa durante algumas sessões. Se demorar mais do que o previsto, diminui-a.",
    "What moves it": "O que a altera",
    "Regular drinking raises it: the liver enzyme that does the work is induced by use. It "
    "also runs slightly higher in women on average, and lower on an empty stomach or with "
    "liver trouble.":
        "Beber com regularidade aumenta-a: a enzima hepática que faz o trabalho é induzida "
        "pelo uso. Em média, também é ligeiramente mais alta nas mulheres, e mais baixa com o "
        "estômago vazio ou com problemas de fígado.",
    "Uncertainty": "Incerteza",
    "At zero every figure is a single number — the app's best estimate. Above zero the same "
    "figures are shown as ranges, and the band on the chart widens to match.":
        "A zero, cada valor é um número único — a melhor estimativa da app. Acima de zero, os "
        "mesmos valores são apresentados como intervalos, e a banda no gráfico alarga em "
        "conformidade.",
    "A single number is easier to learn against: over time you find out what your own 0.6 "
    "feels like. A range is the more literal answer, because the rate really is uncertain. "
    "Both are defensible — this is your call.":
        "Um número único é mais fácil de interiorizar: com o tempo, descobres o que o teu "
        "próprio 0,6 significa para ti. Um intervalo é a resposta mais literal, porque a taxa "
        "é mesmo incerta. Ambos se defendem — a escolha é tua.",
    "The spread suggested by your drinking frequency is ± %@ per hour.":
        "A dispersão sugerida pela tua frequência de consumo é de ± %@ por hora.",
    "Rate": "Taxa",
    "Range": "Intervalo",
    "Advanced": "Avançado",

    # --- PersonSwitcher / FeatureFlags: more than one person (11.5) ---
    "Week": "Semana",
    "Month": "Mês",
    "Year": "Ano",
    "Sober days": "Dias sem beber",
    "Change": "Variação",
    "before records": "antes do registo",
    "See further back": "Ver mais para trás",
    "Weeks, months and years side by side — and every evening older than seven days.": "Semanas, meses e anos lado a lado — e todas as noites com mais de sete dias.",
    "Everything you have logged is already saved. Unlocking only shows it.": "Tudo o que registaste já está guardado. Desbloquear apenas o torna visível.",
    "Back up and restore": "Cópia de segurança e restauro",
    "Log for friends too": "Regista também para amigos",
    "Switch to someone else in one tap and log their drinks with their own body and limit — each person gets their own curve and history.": "Muda para outra pessoa com um toque e regista as bebidas dela com o corpo e o limite dela – cada pessoa tem a sua curva e o seu histórico.",
    "Save everything to a file, and read a backup back in — on this phone or on a new one.": "Guarda tudo num ficheiro e volta a carregar uma cópia de segurança, neste telemóvel ou num novo.",
    "Backup and restore are part of Pro.": "A cópia de segurança e o restauro fazem parte do Pro.",
    "Today": "Hoje",
    "Day": "Dia",
    "Yesterday": "Ontem",
    "No drinks on this day": "Sem bebidas neste dia",
    "Trend": "Tendência",
    "day": "dia",
    "Smoothing": "Suavização",
    "%@ sessions": "%@ sessões",
    "No data before %@": "Sem dados antes de %@",
    "vs.": "vs.",
    "Grams": "Gramas",
    "Grams of alcohol": "Gramas de álcool",
    "Standard units": "Unidades padrão",
    "Unit size": "Tamanho da unidade",
    "Automatic": "Automático",
    "UK": "Reino Unido",
    "Nordic countries": "Países nórdicos",
    "US standard drink": "Bebida padrão dos EUA",
    "WHO, most of Europe": "OMS, a maior parte da Europa",
    "Period": "Período",
    "Switch person": "Mudar de pessoa",
    "Add person": "Adicionar pessoa",
    "New person": "Nova pessoa",
    "You": "Tu",
    "Name": "Nome",
    "All four change the curve, so none of them can be guessed for someone else.":
        "Os quatro alteram a curva, por isso nenhum deles pode ser adivinhado para outra "
        "pessoa.",
    "Their own limit and the finer settings can be changed later on the Profile tab, while "
    "they are the selected person.":
        "O limite próprio e as definições mais detalhadas podem ser alterados depois no "
        "separador Perfil, enquanto esta for a pessoa selecionada.",

    # --- FavouriteDrinkSection and QuickAddBar: the one-tap usual ---
    "Quick add": "Registo rápido",
    "Choose a favourite drink": "Escolhe uma bebida favorita",
    "Pick the drink you usually order, and a button on the Live screen will log it in one tap.":
        "Escolhe a bebida que costumas pedir e um botão no ecrã Em direto regista-a com um "
        "toque.",
    "This is your quick-add drink": "Esta é a tua bebida de registo rápido",
    "Set as my quick-add drink": "Definir como a minha bebida de registo rápido",
    "This is now your usual": "Esta é agora a tua habitual",
    "Remove favourite": "Remover favorita",
    "Always add this one": "Adicionar sempre esta",
    "Logs it straight away, without opening anything.":
        "Regista-a de imediato, sem abrir nada.",
    "One tap on the Live screen logs this, with the projected peak on the button. How full "
    "your stomach is comes from the drink before it, and can be corrected straight after.":
        "Um toque no ecrã Em direto regista-a, com o pico previsto no botão. O quão cheio está "
        "o teu estômago vem da bebida anterior e pode ser corrigido logo a seguir.",
    "Peak %@": "Pico %@",
    "%@ added": "Adicionaste %@",
    "Save": "Guardar",
    "Undo": "Anular",

    # --- DataTransferSection: backup and restore ---
    "Backup": "Cópia de segurança",
    "Export a backup": "Exportar uma cópia de segurança",
    "Import a backup": "Importar uma cópia de segurança",
    "A backup holds every person, occasion and drink. Importing adds what is missing — it "
    "never changes or removes anything already here.":
        "Uma cópia de segurança contém todas as pessoas, ocasiões e bebidas. Importar "
        "acrescenta o que falta — nunca altera nem remove nada do que já está aqui.",
    "Import this backup?": "Importar esta cópia de segurança?",
    "Import": "Importar",
    "Everything in this backup is already here.":
        "Tudo o que está nesta cópia de segurança já está aqui.",
    "Import finished": "Importação concluída",
    "OK": "OK",

    # --- LanguageSection: the app's language ---
    "Language": "Idioma",
    "Opens this app in Settings, where “Preferred Language” sets the app's own language — the "
    "system's stays as it is. iOS restarts the app when you change it.":
        "Abre esta app nas Definições, onde «Idioma preferido» define o idioma da própria app "
        "— o do sistema mantém-se como está. O iOS reinicia a app quando o alteras.",

    # --- DataArchive: why a file could not be read ---
    "Could not import": "Não foi possível importar",
    "This file is not a LogMyDrink backup, or it is damaged.":
        "Este ficheiro não é uma cópia de segurança do LogMyDrink, ou está danificado.",
    "This backup was made by a newer version of LogMyDrink. Update the app and try again.":
        "Esta cópia de segurança foi feita por uma versão mais recente do LogMyDrink. Atualiza "
        "a app e tenta novamente.",

    # --- History: months known only by total (MonthlyTotal) ---
    'Adds %@ occasions, %@ drinks and %@ monthly totals. Nothing already here is changed or removed.':
        'Adiciona %@ ocasiões, %@ bebidas e %@ totais mensais. Nada do que já está aqui é alterado ou removido.',
    'Added %@ occasions, %@ drinks and %@ monthly totals.': 'Adicionadas %@ ocasiões, %@ bebidas e %@ totais mensais.',
    'months as totals': 'meses só como totais',
    'by month only': 'só por mês',
    'monthly total': 'total mensal',
    'No daily records for this day': 'Sem registos diários para este dia',
    'Monthly total: %@': 'Total mensal: %@',
    'A dry month': 'Um mês sem álcool',

    # --- RemovePersonSection ---
    'Remove %@?': 'Remover %@?',
    'Remove': 'Remover',
    'Deletes %@ occasions, %@ drinks and %@ monthly totals. This cannot be undone.':
        'Apaga %@ ocasiões, %@ bebidas e %@ totais mensais. Isto não pode ser anulado.',
    'Deletes %@ occasions and %@ drinks. This cannot be undone.': 'Apaga %@ ocasiões e %@ bebidas. Isto não pode ser anulado.',

    # --- PeopleView ---
    'Swipe left on a guest to remove them with everything recorded under them. You cannot be removed.':
        'Desliza para a esquerda sobre um convidado para o remover com tudo o que foi registado em seu nome. Tu não podes ser removido.',
    'People': 'Pessoas',
    'Owner': 'Titular',
    'Everyone this app records. Switch, add, or remove someone.': 'Todas as pessoas que esta app regista. Muda, adiciona ou remove alguém.',
    # --- Day window (5.22) ---
    "Carried over from the night before": 'Transportado da noite anterior',
    # --- History, second card (5.24) ---
    'Calories': 'Calorias',
    'Sessions': 'Sessões',
    'Per session': 'Por sessão',
    'Under the influence': 'Sob o efeito do álcool',
    '%@ of the time': '%@ do tempo',
    'Days over limit': 'Dias acima do limite',
    'Longest sober run': 'Maior série sem beber',
    'Favourite drink': 'Bebida favorita',

    # --- Profile sub-pages (5.26) ---
    "Display & language": "Apresentação e idioma",
    "Data": "Dados",
    "Concentration": "Concentração",
    "Leave the rate to the frequency question unless you have a measurement to match it against.":
        "Deixa a taxa a cargo da pergunta sobre a frequência, a menos que tenhas uma medição com que a comparar.",

    # --- How it works, estimate badge, launch tips ---
    'Estimate, not a measurement. Never use this to decide whether you can drive.':
        'Estimativa, não medição. Nunca uses isto para decidir se podes conduzir.',
    'Estimated range, not a measurement. Never use this to decide whether you can drive.':
        'Intervalo estimado, não medição. Nunca uses isto para decidir se podes conduzir.',
    'How does the app calculate this?':
        'Como é que a app calcula isto?',
    'approximately %@ %@':
        'aproximadamente %@ %@',
    'How it works':
        'Como funciona',
    'Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.':
        'Nunca uses isto para decidir se podes conduzir. A app estima, não mede, e o teu nível real pode ser muito diferente.',
    'Why this app exists':
        'Porque existe esta app',
    'LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak.':
        'O LogMyDrink ajuda-te a beber de forma mais consciente e a manter o controlo. A decisão é tomada antes do copo seguinte, por isso a app mostra-te antecipadamente até onde outra bebida levaria o teu nível e quando atingiria o pico.',
    'But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse.':
        'Mas não se trata só desta noite. Cada bebida registada vai para o Histórico, por isso ao longo de meses e anos vês quanto, com que frequência e até que nível bebes. Daí surgem os teus padrões, e também a direção em que mudam: se as coisas estão a melhorar ou a piorar.',
    'How it calculates':
        'Como calcula',
    'The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it.':
        'A estimativa baseia-se no método de Widmark, usado desde a década de 1930 para estimar a taxa de alcoolemia; a app usa uma versão aperfeiçoada.',
    'From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed.':
        'A partir do teu peso, altura, idade e sexo, calcula quanta água o teu corpo contém, porque é aí que o álcool se distribui. Acompanha cada bebida separadamente: quanto álcool tinha, a rapidez com que a bebeste e quanto tinhas comido, porque isso determina a rapidez da absorção.',
    'Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear.':
        'Entretanto, o fígado elimina uma quantidade aproximadamente constante por hora; a tua é estimada a partir da frequência com que bebes. O resultado é uma curva, minuto a minuto: onde estás agora, para onde vais e quando voltarás a zero.',
    'Details':
        'Detalhes',
    'Body water':
        'Água corporal',
    'The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood.':
        'A fórmula de Watson (1980), a partir do peso, altura, idade e sexo. A fórmula feminina não inclui a idade — é uma característica da fórmula, não um erro. O volume de distribuição é a água corporal dividida por 0,85, o teor de água do sangue.',
    'Absorption':
        'Absorção',
    'Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it.':
        'Cada bebida tem o seu próprio «estômago». Em jejum, metade do álcool é absorvida em cerca de 7 minutos; com o estômago cheio, em cerca de 21. Uma bebida tomada aos golinhos chega ao estômago de forma uniforme enquanto a bebes.',
    'Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down.':
        'Dá um pico mais baixo e um regresso a zero mais cedo. Surpreendente, mas comprovado por medições: com comida, o estômago decompõe parte do álcool antes da absorção (a app usa 5, 10 e 15 por cento), e o que nunca entrou não precisa de ser eliminado.',
    'Elimination':
        'Eliminação',
    'About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly.':
        'Cerca de 0,15 ‰ por hora (intervalo publicado 0,10–0,25), mais em quem bebe regularmente, porque as enzimas do fígado se adaptam. Perto de zero abranda (cinética de Michaelis-Menten), pelo que a curva vai suavizando em vez de parar de repente.',
    'Computation':
        'Cálculo',
    'The curve comes from a numerical simulation at one-minute resolution.':
        'A curva resulta de uma simulação numérica com resolução de um minuto.',
    'Why it is only an estimate':
        'Porque é só uma estimativa',
    'The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening.':
        'A app não mede nada. O que mostra é o resultado de um modelo com valores médios, e a realidade pode ser diferente. A maior incógnita é a rapidez com que eliminas o álcool: dentro do intervalo plausível, só isso pode alterar, na mesma noite, o pico em 40 por cento e o regresso a zero em quatro horas.',
    'Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value.':
        'A genética, a saúde do fígado, os medicamentos, o que comeste, o sono e o cansaço também contam — a app não sabe nada disso. Só um alcoolímetro homologado ou uma análise ao sangue dão um valor exato.',
    'The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number.':
        'Mesmo assim, o número é útil. Se a app indicar sempre um pouco a mais ou a menos no teu caso, erra na mesma direção todas as noites, por isso com o tempo aprendes o que um valor significa para ti. Em Perfil podes também mostrar a incerteza da taxa de eliminação: verás um intervalo em vez de um único número.',
    'Tips':
        'Dicas',
    'Favourite drink in one tap':
        'Bebida favorita com um toque',
    'Set a favourite in Profile and the Live button logs it with a single tap.':
        'Define uma favorita em Perfil e o botão do ecrã Em direto regista-a com um único toque.',
    'Widget':
        'Widget',
    'Add it to your Lock Screen or Home Screen: one tap logs your favourite. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Adiciona-o ao ecrã bloqueado ou ao Ecrã principal: um toque regista a tua favorita. Com o Pro, enquanto houver álcool no organismo, mostra também o teu nível e se está a subir ou a descer.',
    'How do I add it?':
        'Como o adiciono?',
    'Siri':
        'Siri',
    'Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading.':
        'Diz «Hey Siri, LogMyDrink now» e a Siri regista a tua favorita e depois diz-te até onde deverá chegar o teu pico. (O comando funciona em inglês.)',
    'Looking back':
        'Olhar para trás',
    '“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years.':
        '«Ontem», no topo de Em direto, leva-te ao dia anterior com um toque; o separador Histórico mostra os teus padrões ao longo de semanas, meses e anos.',
    'Logging later':
        'Registar mais tarde',
    'If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History.':
        'Se registares uma bebida mais tarde, recua a hora com os botões − e +; um dia esquecido pode ser preenchido a partir da vista Dia do Histórico.',
    'One tap and done':
        'Um toque e pronto',
    'Your favourite from the Lock Screen':
        'A tua favorita a partir do ecrã bloqueado',
    'Say it, don’t type it':
        'Diz, não escrevas',
    'See your patterns':
        'Vê os teus padrões',
    'Set what you drink most often and log it with a single tap.':
        'Define o que bebes com mais frequência e regista-o com um único toque.',
    'One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too.':
        'Um toque no widget regista a tua favorita, sem teres de procurar a app. À noite mostra também o teu nível.',
    '“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading.':
        '«Hey Siri, LogMyDrink now» — a Siri regista a tua favorita e diz-te até onde deverá chegar o teu pico.',
    'History shows how much and how high you drink over weeks, months and years, and which way it is changing.':
        'O Histórico mostra quanto e até que nível bebes ao longo de semanas, meses e anos, e em que sentido está a mudar.',
    'Set favourite':
        'Definir favorita',
    'Add widget':
        'Adicionar widget',
    'Got it':
        'Percebi',
    'Open History':
        'Abrir Histórico',
    'Don’t show again':
        'Não mostrar novamente',
    'Lock Screen':
        'Ecrã bloqueado',
    'Home Screen':
        'Ecrã principal',
    'Where':
        'Onde',
    'Lock your phone, then touch and hold the Lock Screen.':
        'Bloqueia o iPhone e mantém premido o ecrã bloqueado.',
    'Tap Customize, then Lock Screen, then the widget row under the clock.':
        'Toca em Personalizar, depois em Ecrã bloqueado e, por fim, na fila de widgets por baixo da hora.',
    'Choose LogMyDrink, then tap Done.':
        'Escolhe LogMyDrink e toca em OK.',
    'Touch and hold an empty area of the Home Screen until the icons jiggle.':
        'Mantém premida uma zona vazia do Ecrã principal até os ícones começarem a agitar-se.',
    'Tap Edit, then Add Widget.':
        'Toca em Editar e depois em Adicionar widget.',
    'Search for LogMyDrink, pick a size and tap Add Widget.':
        'Procura LogMyDrink, escolhe um tamanho e toca em Adicionar widget.',
    'A tap on the widget opens the app and logs your favourite drink. With Pro, it also shows your level and which way it is going while there is alcohol in your system.':
        'Um toque no widget abre a app e regista a tua bebida favorita. Com o Pro, enquanto houver álcool no organismo, mostra também o teu nível e se está a subir ou a descer.',
    'Add the widget':
        'Adicionar o widget',
    'Show tips':
        'Mostrar dicas',
    'One tip a day at most, when you open the app — never while there is alcohol in your system.':
        'No máximo uma dica por dia, ao abrir a app — nunca enquanto houver álcool no organismo.',

    # --- Blood alcohol: label, axis unit, explanation (5.28) ---
    'What the number shows':
        'O que o número mostra',
    'The number is an estimate of your blood alcohol concentration, BAC for short: how much alcohol there is in your blood.':
        'O número é uma estimativa da tua taxa de alcoolemia (em inglês BAC, blood alcohol concentration): quanto álcool tens no sangue.',
    'In per mille (‰) it is grams of alcohol per litre of blood: 0.5 ‰ means half a gram in every litre. In percent it is grams per 100 millilitres, so the same level is a tenth of the number: 0.5 ‰ is 0.05 percent. You can switch between the two in Profile, under Display & language.':
        'Em por mil (‰) são gramas de álcool por litro de sangue: 0,5 ‰ significa meio grama em cada litro. Em percentagem são gramas por 100 mililitros, por isso o mesmo nível dá um número dez vezes menor: 0,5 ‰ equivale a 0,05 por cento. Podes alternar entre os dois em Perfil › Apresentação e idioma.',
    'The curve shows the same level over time, minute by minute.':
        'A curva mostra esse mesmo nível ao longo do tempo, minuto a minuto.',
    'Per mille (‰) is grams of alcohol per litre of blood, percent is grams per 100 millilitres: 0.5 ‰ is 0.05 percent.':
        'O por mil (‰) indica gramas de álcool por litro de sangue, a percentagem gramas por 100 mililitros: 0,5 ‰ equivale a 0,05 por cento.',

    # --- ProPaywallSheet: plans and buying ---
    "Prices could not be loaded.": "Não foi possível carregar os preços.",
    "Try again": "Tentar novamente",
    "Save %@": "Poupa %@",
    "About %@ a month": "Cerca de %@ por mês",
    "Yearly": "Anual",
    "Monthly": "Mensal",
    "%@ / year": "%@ / ano",
    "%@ / month": "%@ / mês",
    "Start my free month": "Começar o meu mês grátis",
    "Subscribe": "Subscrever",
    "Free for one month, then %@ a year.": "Grátis durante um mês, depois %@ por ano.",
    "Free for one month, then %@ a month.": "Grátis durante um mês, depois %@ por mês.",
    "%@ a year.": "%@ por ano.",
    "%@ a month.": "%@ por mês.",
    "Renews automatically until you cancel. Cancel anytime in Settings.": "Renova automaticamente até cancelares. Cancela quando quiseres nas Definições.",
    "Restore purchases": "Restaurar compras",
    "Redeem code": "Resgatar código",
    "Terms of Use": "Termos de utilização",
    "Privacy Policy": "Privacidade",
    "Waiting for approval. Pro opens as soon as the purchase goes through.": "A aguardar aprovação. O Pro abre assim que a compra for concluída.",
    "The purchase did not go through. Please try again.": "A compra não foi concluída. Tenta novamente.",
    "No active subscription was found for this Apple ID.": "Não foi encontrada nenhuma subscrição ativa para este ID Apple.",
}
