'''2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number'''

n=int(input("enter no"))
temp=n
count=0
while temp>0:
    if temp>0:
        count=count+1
        temp=temp//10
print(count)

s=count//2
i=0
first_sum=0
second_sum=0
temp=n
while temp>0:
    rem=temp%10
    if i<s:
        first_sum=first_sum+rem
    else:
        second_sum=second_sum+rem
    temp=temp//10
    i=i+1
print("first sum",first_sum)
print("second sum",second_sum)
if first_sum==second_sum:
    print("Balanced Number")
else:
    print("Unbalanced Number")

