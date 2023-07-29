def fizz_buzz():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        message = "Invalid input. Please enter a valid integer."
        return message

    if num % 3 == 0 and num % 5 == 0:
        message = "FizzBuzz"
    elif num % 3 == 0:
        message = "Fizz"
    elif num % 5 == 0:
        message = "Buzz"
    else:
        message = str(num)

    return message


result = fizz_buzz()
print(result)
