# Calculate compound interest.#
"""Write a Python program to calculate compound interest using the formula:
A = P \times (1 + \frac{R}{100})^T
Where:
        •	 P : Principal amount (initial investment)
        •	 R : Annual interest rate (in percentage)
        •	 T : Time (in years)
        •	 A : Final amount after interest is compounded

Also, compute the compound interest ( CI ) as:

CI = A - P

Input:
        1.	Principal amount ( P )
        2.	Annual interest rate ( R )
        3.	Time in years ( T )

Output:
        1.	Final amount ( A )
        2.	Compound interest ( CI )"""

P=float(input("Enter P"))
R=float(input("Enter R"))
T=float(input("Enter T"))
A=P*(1+(R/100))**T
print("A:",A)