def roman_to_interger(roman_string):
    roman_numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    result = 0
    pre_value = 0

    reversed_roman_string  = roman_string[::-1]
    for character in reversed_roman_string:
        current_value = roman_numerals[character]
        if current_value < pre_value:
            result -= current_value
        else:
            result += current_value
        pre_value = current_value
    return result

print(roman_to_interger("MIX"))

