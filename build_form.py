'''
def create_affixes_dict():
    affixes = dict()
    affixes['perf'] = dict()
    affixes['perf']['3msg'] = '-a'
    affixes['perf']['3fsg'] = '-at'
    affixes['perf']['2msg'] = '-ta'
    affixes['perf']['2fsg'] = '-ti'
    affixes['perf']['1csg'] = '-tu'
    affixes['perf']['3mdu'] = '-ā'
    affixes['perf']['3fdu'] = '-atā'
    affixes['perf']['2mdu'] = '-tumā'
    affixes['perf']['2fdu'] = '-tumā'
    affixes['perf']['1cdu'] = '-nā'
    affixes['perf']['3mpl'] = '-ū'
    affixes['perf']['3fpl'] = '-a'
    affixes['perf']['2mpl'] = '-tum'
    affixes['perf']['2fpl'] = '-tunna'
    affixes['perf']['1cpl'] = '-nā'
    affixes['juss'] = dict()
    affixes['juss']['3msg'] = 'yD-'
    affixes['juss']['3fsg'] = 'tD-'
    affixes['juss']['2msg'] = 'tD-'
    affixes['juss']['2fsg'] = 'tD-ī'
    affixes['juss']['1csg'] = 'ˀD-'
    affixes['juss']['3mdu'] = 'yD-ā'
    affixes['juss']['3fdu'] = 'tD-ā'
    affixes['juss']['2mdu'] = 'tD-ā'
    affixes['juss']['2fdu'] = 'tD-ā'
    affixes['juss']['1cdu'] = 'nD-'
    affixes['juss']['3mpl'] = 'yD-ū'
    affixes['juss']['3fpl'] = 'yD-na'
    affixes['juss']['2mpl'] = 'tD-ū'
    affixes['juss']['2fpl'] = 'tD-na'
    affixes['juss']['1cpl'] = 'nD-'

    return affixes
'''

affixes = \
    {
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
            '3fpl': '-a',
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
        }
    }

stems = \
    {
        1: {
            'perf': '1a2T3',
            'juss': '12T3'
        },
        2: {
            'perf': '1a22a3',
            'juss': '1a22i3'
        },
        3: {
            'perf': '1ā2a3',
            'juss': '1ā2i3'
        },
        4: {
            'perf': '12a3',
            'juss': '12i3'
        },
        5: {
            'perf': 'ta1a22a3',
            'juss': 'ta1a22a3'
        },
        6: {
            'perf': 'ta1ā2a3',
            'juss': 'ta1ā2a3'
        },
        7: {
            'perf': '1a2a3',
            'juss': '1a2i3'
        },
        8: {
            'perf': '1ta2a3',
            'juss': '1ta2i3'
        },
        10: {
            'perf': 'sta12a3',
            'juss': 'sta12i3'
        },
    }

poss_grams = \
    ['3msg', '3mdu', '3mpl', '3fsg', '3fdu', '3fpl', '2msg', '2mdu', '2mpl', '2fsg', '2fdu', '2fpl', '1csg', '1cdu', '1cpl']

poss_forms = \
    ['perf', 'juss']

# Словарь грамматики: {'dstem': 1, 'form': 'perf', 'gram': '3msg'}

def build_wordform(root: str, gram_cat: dict) -> str:
    stem = stems[gram_cat['dstem']][gram_cat['form']]
    stem = stem.replace('1', root[0]).replace('2', root[1]).replace('3', root[2])
    wordform = affixes[gram_cat['form']][gram_cat['gram']]
    wordform = wordform.replace('-', stem)
    return wordform

def build_paradigm(root: str) -> str:
    counter = 0
    for dstem in {1, 2, 3, 4, 5, 6, 7, 8, 10}:
        print(dstem)
        for form in poss_forms:
            print(form)
            paradigm = []
            for gram in poss_grams:
                paradigm.append(build_wordform(root, {'dstem': dstem, 'form': form, 'gram': gram}))
            for i in {0, 3, 6, 9, 12}:
                print('\t'.join(paradigm[i:i+3]))

build_paradigm('fˁl')