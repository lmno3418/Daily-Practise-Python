# Swap two numbers (both ways).#
a = 1
b = 2
print("Before A is: ", a, "B is: ", b)

# method 1
a = a + b
b = a - b
a = a - b
print("After A is: ", a, "B is: ", b)

# method 2
(a, b) = (b, a)
print("After A is: ", a, "B is: ", b)

# method 3 (with additional variable)
c = a
a = b
b = c
print("After A is: ", a, "B is: ", b)
