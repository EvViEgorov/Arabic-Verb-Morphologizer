from after_asterisk_form import prothesis

affixes = {
        'perf': {
            '3msg': '-a',
            '3fsg': '-at',
            '2msg': '-ta',
            '2fsg': '-ti',
            '1csg': '-tu',
            '3mdu': '-ā',
            '3fdu': '-atā',
            '2mdu': '-tumā',
            '2fdu': '-tumā',
            '1cdu': '-nā',
            '3mpl': '-ū',
            '3fpl': '-na',
            '2mpl': '-tum',
            '2fpl': '-tunna',
            '1cpl': '-nā'
        },
        'juss': {
            '3msg': 'yD-',
            '3fsg': 'tD-',
            '2msg': 'tD-',
            '2fsg': 'tD-ī',
            '1csg': 'ˀD-',
            '3mdu': 'yD-ā',
            '3fdu': 'tD-ā',
            '2mdu': 'tD-ā',
            '2fdu': 'tD-ā',
            '1cdu': 'nD-',
            '3mpl': 'yD-ū',
            '3fpl': 'yD-na',
            '2mpl': 'tD-ū',
            '2fpl': 'tD-na',
            '1cpl': 'nD-'
        },
        'impv': {
            '2msg': '-',
            '2fsg': '-ī',
            '2mdu': '-ā',
            '2fdu': '-ā',
            '2mpl': '-ū',
            '2fpl': '-na',
        }
    }

stems = {
        '1aa': {
            'perf': '1a2a3',
            'juss': '12a3',
            'impv': '12a3',
            'actp': '1ā2i3',
            'pasp': 'ma12ū3',
            'masd': 'DICTIONARY FORM'
        },
        '1ai': {
            'perf': '1a2a3',
            'juss': '12i3',
            'impv': '12i3',
            'actp': '1ā2i3',
            'pasp': 'ma12ū3',
            'masd': 'DICTIONARY FORM'
        },
        '1au': {
            'perf': '1a2a3',
            'juss': '12u3',
            'impv': '12u3',
            'actp': '1ā2i3',
            'pasp': 'ma12ū3',
            'masd': 'DICTIONARY FORM'
        },
        '1ia': {
            'perf': '1a2i3',
            'juss': '12a3',
            'impv': '12a3',
            'actp': '1ā2i3',
            'pasp': 'ma12ū3',
            'masd': 'DICTIONARY FORM'
        },
        '1uu': {
            'perf': '1a2u3',
            'juss': '12u3',
            'impv': '12u3',
            'actp': '1ā2i3',
            'pasp': 'ma12ū3',
            'masd': 'DICTIONARY FORM'
        },
        '2': {
            'perf': '1a22a3',
            'juss': '1a22i3',
            'impv': '1a22i3',
            'actp': 'mu1a22i3',
            'pasp': 'mu1a22a3',
            'masd': 'ta12ī3'
        },
        '3': {
            'perf': '1ā2a3',
            'juss': '1ā2i3',
            'impv': '1ā2i3',
            'actp': 'mu1ā2i3',
            'pasp': 'mu1ā2a3',
            'masd': '1i2ā3 / mu1ā2a3at'
        },
        '4': {
            'perf': 'ˀa12a3',
            'juss': '12i3',
            'impv': 'ˀa12i3',
            'actp': 'mu12i3',
            'pasp': 'mu12al',
            'masd': 'ˀi12ā3'
        },
        '5': {
            'perf': 'ta1a22a3',
            'juss': 'ta1a22a3',
            'impv': 'ta1a22a3',
            'actp': 'muta1a22i3',
            'pasp': 'muta1a22a3',
            'masd': 'ta1a22u3'
        },
        '6': {
            'perf': 'ta1ā2a3',
            'juss': 'ta1ā2a3',
            'impv': 'ta1ā2a3',
            'actp': 'muta1ā2i3',
            'pasp': 'muta1ā2a3',
            'masd': 'ta1ā2u3'
        },
        '7': {
            'perf': 'n1a2a3',
            'juss': 'n1a2i3',
            'impv': 'n1a2i3',
            'actp': 'mun1a2i3',
            'pasp': 'mun1a2a3',
            'masd': 'in1i2ā3'
        },
        '8': {
            'perf': '1ta2a3',
            'juss': '1ta2i3',
            'impv': '1ta2i3',
            'actp': 'mu1ta2i3',
            'pasp': 'mu1ta2a3',
            'masd': 'i1ti2ā3'
        },
        '10': {
            'perf': 'sta12a3',
            'juss': 'sta12i3',
            'impv': 'sta12i3',
            'actp': 'musta12i3',
            'pasp': 'musta12a3',
            'masd': 'ˀisti12ā3'
        },
    }

stem_types = {
        'perf': 'perf',
        'juss': 'juss',
        'subj': 'juss',
        'impf': 'juss',
        'impv': 'impv',
        'actp': 'actp',
        'pasp': 'pasp',
        'masd': 'masd'
    }

poss_grams = ['3msg', '3mdu', '3mpl', '3fsg', '3fdu', '3fpl', '2msg', '2mdu', '2mpl', '2fsg', '2fdu', '2fpl', '1csg', '1cdu', '1cpl']

pers_forms = ['perf', 'juss', 'impf', 'subj', 'impv']

pers_forms_no_impv = ['perf', 'juss', 'impf', 'subj']

non_pers_forms = ['actp', 'pasp', 'masd']

perf_second_vowel = {
    'a': ('u', 'i', 'a'),
    'i': ('a'),
    'u': ('u')
}

vowels = 'aiuāīū'
consonants = 'bdfhklmnqrstwyzǮšṯḏḍṭṣẓˀġḫḥˁ'

# Кортеж грамматики: (1, 'perf', '3msg') либо (1, 'masd') -
# [0] - порода
# [1] - форма
# [2] - личные грам.категории
# 3 элемента если личная форма, 2 элемента если не личная


def build_wordform(root: str, gram_cat: tuple) -> str: # строим словоформу по корню и грамматическому описанию

    # делаем основу
    stem = stems[gram_cat[0]][stem_types[gram_cat[1]]]
    stem = stem.replace('1', root[0]).replace('2', root[1]).replace('3', root[2])

    # добавляем аффиксы для личных форм глагола
    if len(gram_cat) > 2:
        wordform = affixes[stem_types[gram_cat[1]]][gram_cat[2]]
        wordform = wordform.replace('-', stem)
        if gram_cat[1] == 'subj': # добавляем доп. суффиксы для субъюнктива и имперфекта
            if wordform[-1] not in vowels:
                wordform += 'a'
        if gram_cat[1] == 'impf':
            if wordform[-1] not in vowels:
                wordform += 'u'
            elif wordform[-1] == 'ā':
                wordform += 'ni'
            elif wordform[-1] == 'ū':
                wordform += 'na'
        if wordform.find('D'): # определяем гласный в префиксе
            if gram_cat[0] in {'2', '3', '4'}:
                wordform = wordform.replace('D', 'u')
            else:
                wordform = wordform.replace('D', 'a')

    # нефинитные формы просто выводим
    else:
        wordform = stem

    # вставляем протезу
    wordform = prothesis(wordform)

    return wordform


def build_paradigm(root: str) -> dict:
    paradigm = dict()
    for dstem in stems.keys():

        # личные формы кроме императива
        for form in pers_forms_no_impv:
            for gram in poss_grams:
                paradigm[(dstem, form, gram)] = build_wordform(root, (dstem, form, gram))

        # императив отдельно
        for gram in ['2msg', '2mdu', '2mpl', '2fsg', '2fdu', '2fpl']:
            paradigm[(dstem, 'impv', gram)] = build_wordform(root, (dstem, 'impv', gram))

        # нефинитные формы
        for form in non_pers_forms:
            paradigm[(dstem, form)] = build_wordform(root, (dstem, form))

    return paradigm

def weak_verb_process(root: str, wordform: str) -> str:
    print(0)