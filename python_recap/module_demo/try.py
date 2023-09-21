for n in range(122, 96, -1):
    if n % 2 != 0:
        n -= 32
    print(chr(n), end="")