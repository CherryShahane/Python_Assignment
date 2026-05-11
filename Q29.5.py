'''5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number'''

n=int(input("Enter Number:"))
big=0
while n>0:
    rem=n%10
    if rem>big:
       big=rem
    n=n//10
if big>rem:
    print("stabel no")

   
else:
    print("unstable no")

