from pprint import pprint

sentence = "I am the ink kila, i murder the ink before i write hte script like script"

char_sentence = {}
for char in sentence:
    if char in char_sentence:
        char_sentence[char] += 1
    else:
        char_sentence[char] = 1

x = sorted(char_sentence.items(),
           key=lambda kv: kv[1],
           reverse=True)
pprint(x)

print(x[1])
