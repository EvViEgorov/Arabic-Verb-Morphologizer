import re
from pyscript import document
from itertools import product


cons = 'bdfhklmnqrstwyzǮšṯḏḍṭṣẓˀġḫḥˁ'
vowels = 'aiuāīū'

weak_origin = {
    'u': ['w'],
    'i': ['w', 'y'],
    'a': ['w', 'y'],
    'ū': ['w', 'y', 'ˀ'],
    'ī': ['w', 'y', 'ˀ'],
    'ā': ['w', 'y', 'ˀ'],
    'w': ['y']
}

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
    'i': 'a',
    'u': 'u'
}


def mandatory_asterisk(word: str) -> str:
    # ОБЩИЕ ПЕРЕХОДЫ:
    # -awa| -> -ā|    -awi| -> -ā|    -aya| -> -ā|    -ayu| -> -ā|
    word = re.sub(rf'([{cons}])(awa|awi|aya|ayu)(\b|([{cons}][{vowels}]))', r'\1ā\3', word)

    # -awaC| -> -uC|
    word = re.sub(rf'([{cons}])(awa)([{cons}]\b|[{cons}]{{2}})', r'\1u\3', word)

    # -awiC| -> -iC|    -iyiC| -> iC|    -iyuC| -> iC|
    word = re.sub(rf'([{cons}])(awi|iyi|iyu)([{cons}]\b|[{cons}]{{2}})', r'\1i\3', word)

    # -ayī| -> -ay|
    word = re.sub(rf'([{cons}])(ayī)(\b|([{cons}][^{cons}]))', r'\1ay\3', word)

    # -ayū| -> aw|
    word = re.sub(rf'([{cons}])(ayū)(\b|([{cons}][^{cons}]))', r'\1aw\3', word)

    # -iyi| -> ī|    -iyī| -> ī|    -iyu| -> ī|    -uwi| -> ī|
    word = re.sub(rf'([{cons}])(iyi|iyī|iyu|uwi|uwī)(\b|([{cons}][^{cons}]))', r'\1ī\3', word)

    # -iyū| -> ū|    -uwū| -> ū|
    word = re.sub(rf'([{cons}])(iyū|uwū)(\b|([{cons}][^{cons}]))', r'\1ū\3', word)

    # -iwV- -> -iyV    -iw[^V]- -> -ī-
    word = re.sub(rf'([{cons}])(iw)([{vowels}])', r'\1iy\3', word)
    word = re.sub(rf'([{cons}])(iw)(\b|([{cons}]))', r'\1ī\3', word)

    # -C|wa- -> Cā-
    word = re.sub(rf'([{vowels}][{cons}])(wa)(\b|([{cons}][^{cons}]))', r'\1ā\3', word)

    # -C|wu- -> Cū-
    word = re.sub(rf'([{vowels}][{cons}])(wu)(\b|([{cons}][^{cons}]))', r'\1ū\3', word)

    # -C|wuC|- -> C|uC|-
    word = re.sub(rf'([{vowels}][{cons}])(wu)([{cons}]\b|[{cons}]{{2}})', r'\1u\3', word)

    # -C|yi- -> Cī-
    word = re.sub(rf'([{vowels}][{cons}])(yi)(\b|([{cons}][^{cons}]))', r'\1ī\3', word)

    # 'v'|C -> 'vv|C
    word = re.sub(rf'ˀuˀ([{cons}])', r'ˀū\1', word)
    word = re.sub(rf'ˀiˀ([{cons}])', r'ˀī\1', word)
    word = re.sub(rf'ˀaˀ([{cons}])', r'ˀā\1', word)

    return word


def after_asterisk_form(word: str, root: str, gram: tuple) -> str:

    if root[0] == 'w':
        if gram[0] in {'1aa', '1ai', '1au', '1ia', '1uu'}:
            # -awC2 -> -aC2
            word = re.sub(rf'([{cons}])(aw)([{root[1]}])', r'\1a\3', word)
        elif gram[0] == '8':
            # -wt- -> -tt-
            word = re.sub(rf'^wt', r'tt', word)

    if root[1] == 'w':

        if gram[0] in {'1au'}:
            word = mandatory_asterisk(word)
            # -CwuC| -> -CuC|
            word = re.sub(rf'([{cons}])(wu)([{cons}]\b|[{cons}]{{2}})', r'\1u\3', word)
            # -Cwu| -> -Cū|
            word = re.sub(rf'([{cons}])(wu)(\b|([{cons}][^{cons}]))', r'\1ū\3', word)

        if gram[0] in {'4', '10'}:
            word = mandatory_asterisk(word)
            # -CwaC| -> -CaC|
            word = re.sub(rf'([{cons}])(wa)([{cons}]\b|[{cons}]{{2}})', r'\1a\3', word)
            # -CwiC| -> -CiC|
            word = re.sub(rf'([{cons}])(wi)([{cons}]\b|[{cons}]{{2}})', r'\1i\3', word)
            # -Cwi| -> -Cī|
            word = re.sub(rf'([{cons}])(wi)(\b|([{cons}][^{cons}]))', r'\1ī\3', word)

        if gram[0] in {'7', '8'}:
            word = mandatory_asterisk(word)
            # -C1uC3 -> C1aC3    -C1iC3 -> C1aC3
            word = re.sub(rf'({root[0]}t?)([ui])({root[2]})', r'\1a\3', word)

    if root[1] == 'y':

        if gram[0] in {'1ai'}:
            word = mandatory_asterisk(word)
            # -CayaC| -> -CiC|
            word = re.sub(rf'([{cons}])(aya|yi)([{cons}]\b|[{cons}]{{2}})', r'\1i\3', word)
            # -Cyi| -> -Cī|
            word = re.sub(rf'([{cons}])(yi)(\b|([{cons}][^{cons}]))', r'\1ī\3', word)

        if gram[0] in {'4', '10'}:
            word = mandatory_asterisk(word)
            # Cya| > Ca|
            word = re.sub(rf'([{cons}])(ya)(\b|([{cons}][^{cons}]))', r'\1ā\3', word)
            # -CyaC| -> -CaC|
            word = re.sub(rf'([{cons}])(ya)([{cons}]\b|[{cons}]{{2}})', r'\1a\3', word)
            # -CyiC| -> -CiC|
            word = re.sub(rf'([{cons}])(yi)([{cons}]\b|[{cons}]{{2}})', r'\1i\3', word)
            # -Cyi| -> -Cī|
            word = re.sub(rf'([{cons}])(yi)(\b|([{cons}][^{cons}]))', r'\1ī\3', word)

        if gram[0] in {'7', '8'}:
            word = mandatory_asterisk(word)
            #Caya/ayi|C > Ca|C
            word = re.sub(rf'([{cons}])(aya|ayi)([{cons}]\b|[{cons}]{{2}})', r'\1a\3', word)
            # Cayi| > Caa|
            word = re.sub(rf'([{cons}])(ayi)(\b|([{cons}][^{cons}]))', r'\1ā\3', word)
            # -C1uC3 -> C1aC3    -C1iC3 -> C1aC3
            word = re.sub(rf'({root[0]}t?)([ui])({root[2]})', r'\1a\3', word)

    if root[2] in {'w', 'y'}:
        if gram[0] in {'1aa', '1ai', '1au', '1ia', '1uu'}:
            if root[2] == 'y' and gram[0] == '1ia':
                # -iyC -> -īC
                word = re.sub(rf'([{cons}])(iy)([{cons}])', r'\1ī\3', word)
                # -iyū -> -ū
                word = re.sub(rf'([{cons}])(iyū)\b', r'\1ū', word)
                # -ay -> -a
                word = re.sub(rf'([{cons}])(ay)\b', r'\1a', word)
                # -ayī -> -ay
                word = re.sub(rf'([{cons}])(ayī)(\b|([{cons}][^{cons}]))', r'\1ay\3', word)
                # -ayū -> -aw
                word = re.sub(rf'([{cons}])(ayū)(\b|([{cons}][^{cons}]))', r'\1aw\3', word)
                # -ayu -> -ā
                word = re.sub(rf'([{cons}])(ayu|aya)\b', r'\1ā', word)

            elif root[2] == 'y':
                # -CayaC -> -CaC
                word = re.sub(rf'([{cons}])(aya)([{cons}])', r'\1a\3', word)
                word = mandatory_asterisk(word)
                # -Ciy -> -Ci
                word = re.sub(rf'([{cons}])(iy)\b', r'\1i', word)
                # -CiyC -> -CīC
                word = re.sub(rf'([{cons}])(iy)(\b|([{cons}][{vowels}]))', r'\1ī\3', word)

            if root[2] == 'w':
                # -CawaC -> -CaC
                word = re.sub(rf'([{cons}])(awa)([{cons}])', r'\1a\3', word)
                word = mandatory_asterisk(word)
                # -Cawuu -> Caw
                word = re.sub(rf'([{cons}])(awū)\b', r'\1aw', word)
                # -Cuw -> -Cu
                word = re.sub(rf'([{cons}])(uw)\b', r'\1u', word)
                # -CuwC -> -CūC
                word = re.sub(rf'([{cons}])(uw)(\b|([{cons}][{vowels}]))', r'\1ū\3', word)
                # -Cuwu -> -Cū
                word = re.sub(rf'([{cons}])(uwu)(\b)', r'\1ū\3', word)
        elif gram[0] in {'2', '3', '4', '7', '8', '10'}:
            # -CayaC -> -CaC
            word = re.sub(rf'([{cons}])(aya)([{cons}])', r'\1a\3', word)
            word = mandatory_asterisk(word)
            # -Ciy -> -Ci
            word = re.sub(rf'([{cons}])(iy)\b', r'\1i', word)
            # -CiyC -> -CīC
            word = re.sub(rf'([{cons}])(iy)(\b|([{cons}][{vowels}]))', r'\1ī\3', word)
        elif gram[0] in {'5', '6'}:
            if gram[1] == 'perf':
                # -CayaC -> -CaC
                word = re.sub(rf'([{cons}])(aya)([{cons}])', r'\1a\3', word)
                word = mandatory_asterisk(word)
                # -Ciy -> -Ci
                word = re.sub(rf'([{cons}])(iy)\b', r'\1i', word)
                # -CiyC -> -CīC
                word = re.sub(rf'([{cons}])(iy)(\b|([{cons}][{vowels}]))', r'\1ī\3', word)
            elif gram[1] in {'juss', 'impf', 'subj', 'impv'}:
                # -iyC -> -īC
                word = re.sub(rf'([{cons}])(iy)([{cons}])', r'\1ī\3', word)
                # -iyū -> -ū
                word = re.sub(rf'([{cons}])(iyū)\b', r'\1ū', word)
                # -ay -> -a
                word = re.sub(rf'([{cons}])(ay)\b', r'\1a', word)
                # -ayī -> -ay
                word = re.sub(rf'([{cons}])(ayī)(\b|([{cons}][^{cons}]))', r'\1ay\3', word)
                # -ayū -> -aw
                word = re.sub(rf'([{cons}])(ayū)(\b|([{cons}][^{cons}]))', r'\1aw\3', word)
                # -ayu -> -ā
                word = re.sub(rf'([{cons}])(ayu|aya)\b', r'\1ā', word)


    if root[1] == root[2]:
        # metathesis for vowels
        word = re.sub(rf'([iau])([{cons}])([aiu])([{cons}])([{vowels}])', r'\1\2\4\5', word)
        # metath for cons
        word = re.sub(rf'([{cons}])([{cons}])([aiu])([{cons}])([{vowels}])', r'\1\3\2\4\5', word)
    return word


def prothesis(word):
    word = re.sub(rf'^([{cons}]{{2}}[uū])', r'u\1', word)
    word = re.sub(rf'^([{cons}]{{2}}[aiāī])', r'i\1', word)
    return word


# Кортеж грамматики: ('3', 'perf', '3msg') либо (1, 'masd') -
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
            elif wordform[-1] in {'ū', 'ī'}:
                wordform += 'na'
        if wordform.find('D'): # определяем гласный в префиксе
            if gram_cat[0] in {'2', '3', '4'}:
                wordform = wordform.replace('D', 'u')
            else:
                wordform = wordform.replace('D', 'a')

    # нефинитные формы просто выводим
    else:
        wordform = stem

    # переходы со слабыми
    if 'w' in root or 'y' in root or root[1] == root[2]:
        wordform = after_asterisk_form(wordform, root, gram_cat)

    # вставляем протезу
    wordform = prothesis(wordform)

    return wordform


def build_paradigm(root: str) -> dict:
    paradigm = dict()

    if root[1] == 'w':
        gen_forms = ['1au', '2', '3', '4', '5', '6', '7', '8', '10']
    else:
        gen_forms = stems.keys()

    for dstem in gen_forms:

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


def get_roots(wordform: str) -> list: # получаем все возможные варианты корня слова

    # делаем список возможных согласных
    cons_list = [['w']]
    for letter in wordform:
        if letter not in weak_origin.keys() and letter in cons:
            cons_list.append([letter])
        elif letter in weak_origin.keys():
            cons_list.append(weak_origin[letter])

    # создаем множество корней
    roots = set()
    n = len(wordform)

    # берем по три согласных
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for root in product(cons_list[i], cons_list[j], cons_list[k]):

                    roots.add(''.join(root))

    return roots


def get_dict_form(root: str, gram: tuple) -> list:
    dict_forms = []
    if gram[0][0] == '1':
        dict_forms.append(build_wordform(root, (gram[0], 'perf', '3msg')))
    else:
        for form in {'1aa', '1ai', '1au', '1ia', '1uu'}:
            dict_forms.append(build_wordform(root, (form, 'perf', '3msg')))

    return dict_forms


def get_forms(wordform) -> dict:
    poss_forms = dict()
    for root in get_roots(wordform):
        paradigm = build_paradigm(root)
        for k, v in paradigm.items():
            if v == wordform:
                for dict_form in get_dict_form(root, k):
                    poss_forms[k] = dict_form
    return poss_forms
    
def forms(text):
    input_text = document.querySelector("#user_input")
    became = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = get_forms(became)
def paradigms(text):
    input_text = document.querySelector("#user_input")
    became = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = build_paradigm(became)    
