import re


# get uniq elements of string and convert upper-case letters to lower-case , returns set
def filter_string(userStr):
    return set(userStr.lower())   #set of unique characters from input string

#checks if string has all a-z letters, then it returns True
def check_is_alphabet(userStr):
    letters_count=0
    for char in filter_string(userStr):
        if re.findall("[a-z]+",char):  #matching regular expression
            letters_count += 1            #counter increase by 1 until it reach 26 alphabets
    if letters_count >= 26:
        return True
    else:
        return False