import re

cons = 'bdfhklmnqrstwyzǮšṯḏḍṭṣẓˀġḫḥˁ'
vowels = 'aiuāīū'


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
            word = re.sub(rf'({root[0]}t?)(u|i)({root[2]})', r'\1a\3', word)

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
            word = re.sub(rf'({root[0]}t?)(u|i)({root[2]})', r'\1a\3', word)

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
    word = re.sub(rf'^([{cons}]{{2}})(u|ū)', r'u\1\2', word)
    word = re.sub(rf'^([{cons}]{{2}})(a|i|ā|ī)', r'i\1\2', word)
    return word
