a=4
b=5
c=6

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) **0.5
print("the area of the triangle is %0.2f" %area)
##BY User Input
a=int(input("Enter firsst side of triangle"))
b=int(input("Enter second side of triangle"))
c=int(input("Enter third side of triangle"))

s=(a+b+c) / 2
area=(s*(s-a)*(s-b)*(s-c)) **0.5
print("The area of triangle is %0.2f"%area)
