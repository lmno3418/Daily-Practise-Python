#Implement basic age category checks (child, teenager, adult).
age=int(input("Enter your age:"))
if age<=12:
    print("CHILD")
elif age<=18 and age>12:
    print("TEEN")
else:
    print("ADULT")