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

op_function = {
    "+":add,
    "-":sub,
    "/":div,
    "*":mul
}

result = op_function[operator](a, b)

print(f"{a} {operator} {b}  = {result}")