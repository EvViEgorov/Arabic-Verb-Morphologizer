import re

cons = 'bcdfghjklmnpqrstvwxyzǯšṯḏkqḍṭṣḏˀġḫḥˁ'
vowels = 'aiuāīū'

def prothesis(word):
    word = re.sub(rf'^([{cons}]{{2}})(u|ū)', r'u\1\2', word)

    word = re.sub(rf'^([{cons}]{{2}})(a|i|ā|ī)', r'i\1\2', word)
    return word