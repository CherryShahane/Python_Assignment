'''5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number'''

n=int(input("enter no"))
count=0
while n>0:
    if n>0:
       count+=1
       n=n//10
print(count)
s=count//2
print(s)
first_half=0
second_half=0
i=0
temp=n
while temp>0:
    rem=temp%10
    if i<s:
        first_half=first_half+rem
    else:
        second_half=second_half+rem
print(first_half)
print(second_half)
