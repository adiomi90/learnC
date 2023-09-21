from sys import argv, exit
from calculate import  add, div, mul, sub

a = int(argv[1])
operator = argv[2]
b = int(argv[3])
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

if operator not in  ["+", "-", "/", "*"]:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

operation = {
    "+":add,
    "-":sub,
    "/":div,
    "*":mul
}

result = operation[operator](a, b)

print("{} {} {} = {} ".format(a, operator, b, result))

