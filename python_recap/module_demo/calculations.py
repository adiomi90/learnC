if __name__ == "__main__":
    import calculate

a = 10
b = 5

print("{} + {} = {}".format(a,b,(calculate.add(a,b))))
print("{} + {} = {}".format(a,b,(calculate.div(a,b))))
print("{} + {} = {}".format(a,b,(calculate.mul(a,b))))
print("{} + {} = {}".format(a,b,(calculate.sub(a,b))))
