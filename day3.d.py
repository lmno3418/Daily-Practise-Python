#Check if a number is prime.
n=int(input("Check if prime :"))
for i in range(n):
    if(n<=1):
        print("Not a prime")
    else:
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count=count+1
        if count==2:
            print(n," is prime no: ")
            break
        else:
            print(n," is not a prime no: ")
            break
    