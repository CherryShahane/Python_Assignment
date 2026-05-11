'''7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144'''
'''n=int(input("enter no"))
rem=0
temp=n
while n>0:
    s=n*n
    rev=n%10
    rem=rem*10+rev
    n=n//10
print(rem)
if rem>temp:
    ab = 0
    while rem>temp:

       rev=rem%10
       ab=ab*10+rev
       rem=rem//10
    if rem==ab:
       print("yes")'''
n=int(input("enter no"))
sq=n*n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
rs=rev*rev
rev1=0
while rs>0:
    rem=rs%10
    rev1=rev1*10+rem
    rs=rs//10
if   sq==rev1:
    print("adoms number")
else:
    print("not adoms number")





