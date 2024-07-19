# Author: Jacob Deaton
# GitHub username: jd-58
# Date: 7-19-24
# Description: Convert roman numerals to integers


one = "I"
five = "V"
ten = "X"
fifty = "L"
one_hundred = "C"
five_hundred = "D"
one_thousand = "M"

test = "MMMCDXC"


"""def roman_to_int(string):
    total = 0
    i = 0
    length = len(string)
    while i < length:
        character = string[i]
        character.upper()
        if character == "I":
            group_string = character + string[i + 1]
            if group_string == "IV":
                total += 4
                i += 2
            elif group_string == "IX":
                total += 9
                i += 2
            else:
                total += 1
                i += 1
        elif character == "V":
            total += 5
            i += 1
        elif character == "X":
            group_string = character + string[i + 1]
            if group_string == "XL":
                total += 40
                i += 2
            elif group_string == "XC":
                total += 90
                i += 2
            else:
                total += 10
                i += 1
        elif character == "L":
            total += 50
            i += 1
        elif character == "C":
            group_string = character + string[i + 1]
            if group_string == "CD":
                total += 400
                i += 2
            elif group_string == "CM":
                total += 900
                i += 2
            else:
                total += 100
                i += 1
        elif character == "D":
            total += 500
            i += 1
        elif character == "M":
            total += 1000
            i += 1
    return total"""


def romanToInt(s):
    total = 0
    i = len(s) - 1
    s = s.upper()
    while i >= 0:
        character = s[i]
        if character == "I":
            total += 1
            i -= 1
        elif character == "X":
            if i == 0:
                total += 10
                return total
            group_character = character + s[i - 1]
            if group_character == "XI":
                total += 9
                i -= 2
            else:
                total += 10
                i -= 1
        elif character == "V":
            if i == 0:
                total += 5
                return total
            group_character = character + s[i - 1]
            if group_character == "VI":
                total += 4
                i -= 2
            else:
                total += 5
                i -= 1
        elif character == "L":
            if i == 0:
                total += 50
                return total
            group_character = character + s[i - 1]
            if group_character == "LX":
                total += 40
                i -= 2
            else:
                total += 50
                i -= 1
        elif character == "C":
            if i == 0:
                total += 100
                return total
            group_character = character + s[i - 1]
            if group_character == "CX":
                total += 90
                i -= 2
            else:
                total += 100
                i -= 1
        elif character == "D":
            if i == 0:
                total += 500
                return total
            group_character = character + s[i - 1]
            if group_character == "DC":
                total += 400
                i -= 2
            else:
                total += 500
                i -= 1
        elif character == "M":
            if i == 0:
                total += 1000
                return total
            group_character = character + s[i - 1]
            if group_character == "MC":
                total += 900
                i -= 2
            else:
                total += 1000
                i -= 1
    return total


total2 = romanToInt(test)
print(total2)




