def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzBuzz",end=" ")
        if num % 3 == 0:
            print("Fizz",end=" ")
        elif num % 5 == 0:
            print("buzz",end=" ")
        else:
            print(num, end=" ")

fizzbuzz()