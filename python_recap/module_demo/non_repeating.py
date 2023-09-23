for n in range(10):
    for j in range(n+1,10):
        if n != 8:
            print(f"{n}{j}", end=",")
        else:
            print(f"{n}{j}")
        