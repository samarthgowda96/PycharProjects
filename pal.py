string= input("enter the input"+" ")

def isPalindrome(str):
    length = len(str)
    first = 0
    last = length - 1
    palindrome = 1
    while first < last:
        if(str[first] == str[last]):
            first = first + 1
            last = last - 1
            continue
        else:
            palindrome= 0
            break

    return palindrome

palindrome= isPalindrome(string)

if(palindrome):
    print(string+" "+"it is a palindrome")
else:
    print("Please try again :)")

