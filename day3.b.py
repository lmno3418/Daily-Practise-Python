# Find the sum of digits of a number using a loop.
n = input("Enter a number: ")
sum=0
for i in range(len(n)):
    sum+=int(n[i])
print(sum)