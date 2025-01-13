# Find the sum of digits of a number using a loop.
n = input("Enter a number: ")
l = len(n)
sum = 0
for i in range(0, l, 1):
    sum += int(n[i])
print(sum)
