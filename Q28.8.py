'''8'. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime'''

n=int(input("enter no"))
largest=0
smallest = 9

while n>0:
    t=n%10
    if t>largest:
        largest=t
    if t<smallest:
        smallest=t
    n=n//10
sum=largest+smallest
print("largest", largest)
print("smallest", smallest)
print("sum", sum)
x=0
i=2
while i <= sum//2:
    if sum%i==0:
        x=1
        break
    i+=1

if x==0:
    print("prime")
else:
    print("not prime")