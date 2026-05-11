'''2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4'''

'''a,b = map(int,input("Enter 2 numbers : ").split())
count = 0

for i in range(a,b):
    if i%7 == 0:
       count+=1
print("Count = ",count)'''


n=int(input("Enter the number: "))
a=int(input("Enter the  number: "))
sum=0
while n<a:
    if n%7==0:
        sum=sum+1
    n+=1
print("count",sum)




