import re

cons = 'bdfhklmnqrstwyzǮšṯḏḍṭṣẓˀġḫḥˁ'
vowels = 'aiuāīū'
def after_asterisk_form(word):
    word = re.sub(rf'([{cons}])(awa|wu)([{cons}]{{2}})', r'\1u\3', word)
    
    word = re.sub(rf'([{cons}])(awi|iyi|iyu)([{cons}]{{2}})', r'\1i\3', word)

    word = re.sub(rf'([{cons}])(awa|awi|aya)(\b|([{cons}]))', r'\1ā\3', word)

    word = re.sub(rf'([{cons}])(iyi|iyī|iyu|iw|uwi|uwī|yi)(\b|([{cons}]))', r'\1ī\3', word)

    word = re.sub(rf'([{cons}])(iyū|uwū|wu)(\b|([{cons}]))', r'\1ū\3', word)

    word = re.sub(rf'([{cons}])ayī(\b|([{cons}]))', r'\1ay\2', word)

    word = re.sub(rf'([{cons}])ayū(\b|([{cons}]))', r'\1aw\2', word)

    word = re.sub(rf'([{cons}])iw([{vowels}])', r'\1iy\2', word)

    word = re.sub(rf'ˀuˀ([{cons}])', r'ˀū\1', word)

    word = re.sub(rf'ˀiˀ([{cons}])', r'ˀī\1', word)

    word = re.sub(rf'ˀaˀ([{cons}])', r'ˀā\1', word)

    return word

print(after_asterisk_form("tawala"))