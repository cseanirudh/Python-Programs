x=5
y=10

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)


x = 5
y = 10
x = x + y
y = x - y
x = x - y
print("x =", x)
print("y =", y)

x = 5
y = 10
x = x * y
y = x / y
x = x / y
print("x =", x)
print("y =", y)


x = 5
y = 10
x = x ^ y
y = x ^ y
x = x ^ y
print("x =", x)
print("y =", y)

