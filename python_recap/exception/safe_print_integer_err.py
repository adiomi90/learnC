import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except (TypeError, ValueError) as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))