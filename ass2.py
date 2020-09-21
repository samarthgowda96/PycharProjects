from math import *
string = input("Enter the input")
string = string.split()
print(string)

def add(*args):
    total = 0
    for i in string:
        if i.isdigit():
            print("Is Valid Number")
            print(i)
            total = total + int(i)

    return total

print(add(string))







