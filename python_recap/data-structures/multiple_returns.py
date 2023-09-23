def multiple_returns(sentence):
    if not sentence:
        return None
    else:
        first = sentence[0]
        length = len(sentence)
        return "Length:{:d} - First character: {}".format(length, first)
    

print(multiple_returns("Particles Molecular"))
print(multiple_returns("me"))