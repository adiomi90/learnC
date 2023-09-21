def is_lower(character):
    for n in range(97, 123):
        if character == chr(n):
            return True
        else:
            return False
           
result = is_lower("H")
print(result)