'''7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number'''
n=int(input("enter the number"))
sum = 0
while n>0:
    t=n%10
    sum = sum + t
    n=n//10
print(sum)

i = 2
x = 0
while i<=sum//2:
    if sum%i==0:
      x=1
      break
    i+=1

if x==0:
    print("lucky number")

else:
    print("not lucky number")





