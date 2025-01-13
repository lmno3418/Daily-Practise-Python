#Print numbers from 1 to N using while and for loops.
n=int(input("Enter any number N: "))

i=1
while i<=n:
    print(i)
    i+=1
    
for i in range(1,n+1,1):
    print(i)