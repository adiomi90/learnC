from timeit import timeit

code1 = """
def cal(age):
    if age <= 0:
        raise ValueError("Age cant be zero: ")
    return 10 / age


try:
    cal(5)
except ValueError as error:
    pass
"""

print("first code ", timeit(code1, number=10000))
