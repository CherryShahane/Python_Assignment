'''4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number'''

'''n=int(input("enter no"))
sum=0
pro=1
while n>0:
    rem=n%10
    sum=sum+rem
    pro=pro*rem
    n=n//10
if sum==pro:
    print("spy no")
else:
    print("not spy no")'''

n=input("enter no")
sum=0
pro=1
for i in n:
    sum=sum+int(i)
    pro=pro*int(i)
if sum==pro:
    print("spy no")
else:
    print("not spy no")