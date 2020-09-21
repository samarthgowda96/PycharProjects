string = str(input('enter the string'))

revString= ""

revString = string[::-1]
print(revString)

if(string == string[::-1]):
    print('it is a palindrome')
else:
    print("not a palindrome")

