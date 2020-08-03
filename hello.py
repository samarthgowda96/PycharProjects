import re
data = open("regex_sum_703482.txt")
x = list()
for i in data:
    num = re.findall('[0-9]+', i)
    x = x+num
sum = 0
for i in x:
    sum = sum + int(i)

print(sum)

