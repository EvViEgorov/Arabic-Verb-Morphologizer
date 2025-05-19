from build_form import consonants, build_paradigm
from itertools import product

weak_origin = {
    'u': ['w'],
    'i': ['w', 'y'],
    'a': ['w', 'y'],
    'ū': ['w', 'y', 'ˀ'],
    'ī': ['w', 'y', 'ˀ'],
    'ā': ['w', 'y', 'ˀ'],
    'w': ['y']
}


def get_roots(wordform: str) -> list: # получаем все возможные варианты корня слова

    # делаем список возможных согласных
    cons_list = [['w']]
    for letter in wordform:
        if letter not in weak_origin.keys() and letter in consonants:
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


def get_forms(wordform) -> dict:
    poss_forms = dict()
    for root in get_roots(wordform):
        paradigm = build_paradigm(root)
        for k, v in paradigm.items():
            if v == wordform:
                poss_forms[k] = v

    return poss_forms