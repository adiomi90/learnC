import sys

if(len(sys.argv) == 1):
    print("Usage: python expect a password")
else:
    password = sys.argv[1]
    print("Password", password)