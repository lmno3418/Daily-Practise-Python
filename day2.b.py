#Build a basic calculator for addition, subtraction, multiplication, and division.
n1=int(input("Enter your number 1: "))
n2=int(input("Enter your number 2: "))
print("Enter +\nEnter -\nEnter *\nEnter /\nEnter ^\nEnter %\nEnter //")
o=input("Enter any Operation: ")

if(o=="+"):
    print(n1+n2)
elif(o=="-"):
    print(n1 - n2)
elif(o=="*"):
    print(n1 * n2)
elif(o=="/"):
    print(n1 / n2)
elif(o=="^"):
    print(n1 ** n2)
elif(o=="%"):
    print(n1 % n2)
elif(o=="//"):
    print(n1 // n2)    
else:
    print("Error")    