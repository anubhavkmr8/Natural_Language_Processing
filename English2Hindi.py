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
        if is_vowel_char(char):

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


print(eng2hin(input()))
