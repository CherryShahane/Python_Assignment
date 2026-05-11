'''1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime'''

n=int(input("enter no"))
sum=0
rev=0
temp=n
while n>0:
    t=n%10
    rev=rev*10+t
    sum=sum+t
    n=n//10
difference=abs(temp-rev)
add=sum+difference
print("sum",sum)
print("reverse",rev)
print("difference",difference)
print("add",add)
i=2
x=0
while add>0:
    if add%i==0:
        x=1
        break
    i+=1
if x==1:
    print("not prime")
else:
    print("prime")
