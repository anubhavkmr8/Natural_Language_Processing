import pandas as pd
from nltk.translate.bleu_score import corpus_bleu
import numpy as np
eng2hin_vowels = {
    "a": "अ",
    "A": "आ",
    "e": "ए",
    "E": "ऐ",
    "i": "इ",
    "I": "ई",
    "o": "ओ",
    "O": "औ",
    "u": "उ",
    "U": "ऊ"
}
eng2hin_vowels_half = {
    "A": "ा",
    "e": "े",
    "E": "ै",
    "i": "ि",
    "I": "ी",
    "o": "ो",
    "U": "ू",
    "u": "ु"
}
eng2hin_sonorants = {
    "q": "ऋ",
    "Q": "ॠ",
    "L": "ऌ"
}
eng2hin_anuswara = {"M": "अं"}
eng2hin_anuswara_half = {"M": "ं"}
eng2hin_consonants = {
    "k": "क",
    "K": "ख",
    "g": "ग",
    "G": "घ",
    "f": "ङ",
    "c": "च",
    "C": "छ",
    "j": "ज",
    "J": "झ",
    "F": "ञ",
    "t": "ट",
    "T": "ठ",
    "d": "ड",
    "D": "ढ",
    "N": "ण",
    "w": "त",
    "W": "थ",
    "x": "द",
    "X": "ध",
    "n": "न",
    "p": "प",
    "P": "फ",
    "b": "ब",
    "B": "भ",
    "m": "म",
    "y": "य",
    "r": "र",
    "l": "ल",
    "v": "व",
    "S": "श",
    "R": "ष",
    "s": "स",
    "h": "ह",
    "z": "ज"
}

eng2hin_all = {
    **eng2hin_sonorants,
    **eng2hin_consonants
}


def is_vowel_char(char):
    if char in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "M"}:
        return True
    return False


def eng2hin(english_string):
    """
    Converts the english_string to the Hindi string.

    This function goes through each character from the wx_string and
    maps it to a corresponding Devanagari character according to the
    Devanagari character mapping defined previously.
    """
    english_string += " "
    hindi_string = []
    for i, char in enumerate(english_string[:-1]):

        # If the current character is '“' or '”' the skip
        if char == "“" or char == "”":
            continue
        elif is_vowel_char(char):

            # If second last character of string is "a" then this makes aa sound.
            if char == "a" and i == len(english_string) - 2:
                hindi_string.append(eng2hin_vowels_half['A'])
            # If current character is "a" and not the first character
            # then skip
            if char == "a" and i != 0:
                continue

            if char == "M":
                hindi_string.append(eng2hin_anuswara_half[char])
            elif i == 0 or english_string[i - 1] == "a":
                hindi_string.append(eng2hin_vowels[char])
            else:
                hindi_string.append(eng2hin_vowels_half[char])
        else:
            hindi_string.append(eng2hin_all[char])

            # If char is not followed by vowel or space then it is treated as half character.
            if not is_vowel_char(english_string[i + 1]) and english_string[i + 1] != " ":
                hindi_string.append("्")
    return "".join(hindi_string)


dataset = pd.read_excel('English-Hindi.xlsx')
X = dataset.iloc[1:68922, 1].values
y = dataset["Hindi"]
y = y[0:68921]
y_pred = []
for english_string in X:
    y_pred.append(eng2hin(english_string))


score = corpus_bleu(y_pred[:68722], y[:68722], weights=(1, 0, 0, 0))
print(score)

