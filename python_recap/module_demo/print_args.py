if __name__ == "__main__":
    
    from sys import argv
    counter =len(argv) - 1 
    if counter  == 0:
        print("0 arguments")
    elif counter == 1:
        print("1 arguments")
    else:
        print("{} arguments".format(counter))
    for i in range(counter):
        print("{}: {}".format(i + 1, argv[i]))