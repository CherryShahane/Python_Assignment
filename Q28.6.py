'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2''''''
n=int(input("enter no"))
if n<=1:
    print(" neither prime not composite")
x=0
i=2
smallest=0
while i<n:
    if n%i==0:
        x=1
        break
    i+=1
if x==1:
    print("composite")
    count=0
    for i in range(1,n+1):

        if n%i==0:
            count+=1
            if i!=1 and smallest=0
               smallest=i

    print("total factors",count)
    print("smallest",smallest)
    if count>1:
        print(i)
        

else:
    print("not composite")'''

num = int(input("Enter Number = "))
count = 0
smallest = 0

i = 1
while i<=num:
    if num%i==0:
        count+=1
        if i != 1 and smallest == 0:
            smallest=i
    i+=1

if count > 2:
    print("composite")
    print("count",count)
    print("smallest",smallest)
else:
    print("not composite")