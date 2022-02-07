'''
given a dictionary and 2 strings find if both strings can be made from the
characters in dictionary : retrun 2
one string can be made out of dictionary: return 1
none: return 0
'''


def create_strings_from_characters(frequencies, string1, string2):
    can_create_string1 = can_create_string(frequencies, string1)
    can_create_string2 = can_create_string(frequencies, string2)
    if (not can_create_string1) or (not can_create_string2):
        if can_create_string1 or can_create_string2:
            return 1
        return 0

    for character in string1+string2:
        if character not in frequencies or frequencies[character] == 0:
            return 1
        frequencies[character] -= 1      
    return 2


def can_create_string(frequencies, string):
    for character in set(string):
        if string.count(character) > frequencies.get(character, 0):
            return False
    return True


freq = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
st1='hello'
st2 ='world'
print(create_strings_from_characters(freq, st1,st2))