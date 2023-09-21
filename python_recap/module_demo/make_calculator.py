from calculate import add, div, mul, sub
from sys import argv,exit

a = int(argv[1])
operator = argv[2]
b = int(argv[3]) 


if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
elif operator not in ["+","-","/","*"]:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
else:
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a,b)))
        exit(0)
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a,b)))
        exit(0)
    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(a,b)))
        exit(0)
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a,b)))
        exit(0)
        






