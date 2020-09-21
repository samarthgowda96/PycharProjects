string = str(input("enter the input:"))
char= str(input("to check  "))
freq = [None] * len(string);
count = 0


for i in range(0,len(string)):
    if ord(string[i]) == ord(char):
        # print(string[i])
        count = count + 1
    else:
        continue

print(count)


