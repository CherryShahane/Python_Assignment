'''9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime'''

n=int(input("enter no"))
even=0
odd=0
while n>0:
    t=n%10
    if t%2==0:
        even+=1
    if t%2!=0:
        odd+=1
    n=n//10
difference=even-odd
print(even)
print(odd)
print("difference=",difference)
i=2
while difference%i==0:
      x=1
      break
      i+=1
if x==1:
    print("not prime")
else:
    print("prime")

