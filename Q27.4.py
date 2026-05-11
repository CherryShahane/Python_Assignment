'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''

n=int(input("enter the number"))
sum=0
f=1
i=1
t=n
while i<=n:
    n=n%10
    f=f*i
    sum=sum+f
    i += 1
if sum==t:
    print("Strong Number")
else:
    print("Not Strong Number")









