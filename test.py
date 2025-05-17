from after_asterisk_form import after_asterisk_form
from build_form import build_wordform, build_paradigm


def print_paradigm(paradigm: dict) -> str: # тестовая функция чтобы красиво запринтить словарь
    dstem, form = 0, ''
    COUNTER = 0
    output = ''
    for gram, wordform in paradigm.items():
        if gram[0] != dstem:
            dstem = gram[0]
            output += '\n\n' + str(dstem) + '\n\n'
        if gram[1] != form:
            form = gram[1]
            output += '\n' + str(form) + '\n\n'
        output += wordform
        COUNTER += 1
        if COUNTER >= 3:
            output += '\n'
            COUNTER = 0
        else:
            output += '\t'
    return output


'''wordform = build_wordform('ktb', (2, 'impf', '3fsg'))
print(wordform)'''

paradigm = build_paradigm('fˁl')
print(paradigm)

with open('test_output.txt', 'w', encoding='UTF-8') as f:
    f.write(print_paradigm(paradigm))
