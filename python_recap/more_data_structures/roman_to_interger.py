def roman_to_int(roman_string):
    roman_numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    result = 0
    prev_value = 0
    for char in roman_string[::-1]:
        current_value = roman_numerals[char]
        if current_value < prev_value:
            result -=current_value
        else:
            result +=current_value
        prev_value = current_value
    return result




roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
print(roman_to_int("MIX"))

