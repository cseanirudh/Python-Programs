#Getting Input from user i 1D Array input

from numpy import *
n = int(input("Enter Number of elements"))
a = zeros(n, dtype=int)
for i in range(len(a)):
    x = int(input("Enter Element"))
    a[i] = x
for i in range(len(a)):
    print(a[i])


# Getting Input from user in 1D Array using While Loop Numpy
from numpy import *
n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype=int)
u = len(a)
i = 0
j = 0
while(i<u):
	x = int(input("Enter Element: "))
	a[i] = x
	i+=1
	
while(j<(len(a))):
	print(a[j])
	j+=1

print(type(a))
