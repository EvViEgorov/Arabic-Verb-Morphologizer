import re

cons = 'bdfhklmnqrstwyzǮšṯḏḍṭṣẓˀġḫḥˁ'
vowels = 'aiuāīū'


def after_asterisk_form(word: str, root: str) -> str:

    # ОБЩИЕ ПЕРЕХОДЫ:
    # -awa| -> -ā|    -awi| -> -ā|    -aya| -> -ā|    -ayu| -> -ā|
    word = re.sub(rf'([{cons}])(awa|awi|aya|ayu)(\b|([{cons}][^{cons}]))', r'\1ā\3', word)

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
    word = re.sub(rf'([{cons}])(iyū|uwū)(\b|([{cons}][^{cons}]))', r'\ū\3', word)

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


def prothesis(word):
    word = re.sub(rf'^([{cons}]{{2}})(u|ū)', r'u\1\2', word)
    word = re.sub(rf'^([{cons}]{{2}})(a|i|ā|ī)', r'i\1\2', word)
    return word
