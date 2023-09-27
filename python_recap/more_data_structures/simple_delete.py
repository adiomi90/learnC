def simple_delete(a_dictionary, key):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'tracking')
print(new_dict)