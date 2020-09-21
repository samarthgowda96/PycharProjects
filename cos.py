from numpy import dot
from numpy.linalg import norm


x = input("enter the values for list 1: ")
y = input("enter the value for list 2: ")
list1= [float(i) for i in x.split(' ')]
list2= [float(s) for s in y.split(' ')]

co_sine = dot(list1, list2)/(norm(list1)*norm(list2))
print(co_sine)