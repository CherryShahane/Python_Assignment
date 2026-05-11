'''2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''


n=int(input("enter no"))
sum=0
pro=1
while n>0:
    rem=n%10
    sum=sum+rem
    pro=pro*rem
    n=n//10
d=pro-sum
print("sum",sum)
print("product",pro)
print("difference",d)

digit=0
diff=d
while d>0:
    t=d%10
    digit=digit+1
    d=d//10
add=digit+diff
print("digit",digit)
print("final result",add)
i=2
x=0
add=add
while add>i:
    if add%i==0:
        x=1
        break
    i+=1
if x==1:
    print("not prime")
else:
    print("prime")