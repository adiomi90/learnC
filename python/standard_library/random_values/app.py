from random import random,randint,choice,choices,shuffle
import string
print(random())
print(randint(1, 10))
print(choice([1,2,8,4,3,5,3]))
#pick random numbers
print(choices([1, 2, 3, 4, 5, 7, 8, 9],k=4))
#pick individual characters fromt the string
print(choices("particles molecular",k=7))
print(choices("particles molecular",k=7))
print("".join(choices("particles molecular", k=8)))
password = ("".join(choices(string.ascii_letters + string.digits,k=10)))
print(password)
number = [1, 2 , 3, 4]
shuffle(number)
print(number)
