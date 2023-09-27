from print_sorted_dictionary import print_sorted_dictionary

def multiply_by_2(a_dictionary):
    return { key: value *2 for key, value in a_dictionary.items()}


a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)