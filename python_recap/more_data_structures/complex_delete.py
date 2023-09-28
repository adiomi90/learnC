from print_sorted_dictionary import print_sorted_dictionary
"""The script delete the value associated with a key in the dictionary"""

def complex_delete(a_dictionary, value):
    
    for keys in list(a_dictionary.keys()):
        if a_dictionary[keys] == value:
            del a_dictionary[keys]
    return a_dictionary


a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
