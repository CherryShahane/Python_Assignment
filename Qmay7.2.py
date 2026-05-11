'''2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496'''

x=int(input("Enter starting number: "))
y=int(input("Enter ending number: "))

for i in range(x,y+1):
    n=1
    temp=i
    sum=0
    while n>0 and n<i:
        if i%n==0:
           sum=sum+n
        n+=1
    if sum==temp:
       print(temp)







