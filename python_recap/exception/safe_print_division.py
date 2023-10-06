def safe_print_division(num1, num2):
    """
    Safely divides two numbers and prints the result.
    If division by zero occurs, returns None.

    Args:
    num1 (int or float): The numerator.
    num2 (int or float): The denominator.

    Returns:
    float or None: The result of the division, or None if division by zero occurs.
    """
    try:
        div = num1 / num2
    except (ZeroDivisionError, ArithmeticError):
        div = None
    finally:
        print(f"Inside result {div}")
    return div

    
a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))