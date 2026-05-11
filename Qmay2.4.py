'''4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number'''
n=int(input("enter no"))
rev=0
temp=n
count=0
max=0
print("Differences", end=" ")
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10

while rev>10:
    curr=rev%10
    next=(rev//10)%10
    diff=abs(curr-next)

    print( diff,end=" ")
    rev = rev // 10
    if diff>2:
       count=count+1
    if max<diff:
       max=diff



print("\ncount",count)
print("max",max)

if max<=2:
    print("Smooth Number")
else:
    print("Irregular Pattern")
