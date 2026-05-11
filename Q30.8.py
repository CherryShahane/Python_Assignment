'''8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number'''
n=int(input("enter no"))
temp=n
c=n
while n>0:
    rem=n%10
    n=n//10
    temp=temp*temp*temp
    rem1=temp%10
    temp=temp//10
    if c%10==rem1:
        print("trimorphic number")
        break
    else:
        print("not trim number")
        break
