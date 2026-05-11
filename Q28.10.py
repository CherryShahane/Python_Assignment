'''10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime'''

n=int(input("enter number:"))
count=0
sum=0
smallest=9
while n>0:
    t=n%10
    sum=sum+t
    if t==0:
        count=count+1

    if t<smallest:
        smallest=t
    n=n//10
    add = count + sum
    final=add*smallest
print("zero count",count)
print("sum",sum)
print("smallest",smallest)
print("final_result",final)
x=1
i=2
while final>0:
    if final%i==0:
        x=1
        break
    i+=1
if x==1:
    print("not prime")
else:
    print("prime")

