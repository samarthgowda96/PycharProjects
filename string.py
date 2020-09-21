x = str(input("enter the input:"))

print(type(x))

altStr = ''

for i in range(len(x)):
    if (i % 2) == 0:
        altStr = altStr + x[i]

print(altStr)

