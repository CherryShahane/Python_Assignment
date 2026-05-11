'''*10. Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20

-------------------------
#for loop
a, b = map(int, input("enter two numbers a,b: ").split())
for i in range(a,b+1):
    if i%2==0:
       print(i,end=" ")
else:
   pass

#while loop
a,b=map(int,input("enter no").split())
while a<=b:
    if a%2==0:
       print(a)
    a+=1

...........................................................
*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3
----------------------------------------------------
#while loop
n = int(input("enter no: "))
c=int(input("enter no to count"))
count=0
while n>0:
     rem=n%10
     if rem==c:
        count=count+1
     n=n//10
print(count)
----------------------------
#for loop
n=input("enter no: ")
d=input("enter no")
count=0
for i in (n):
    if i==d:
        count=count+1
print(count)

-------------------------------------------------
12. Multiplication of Digits*
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.

Input: 1234
Output: 24
Even

---------------------------------------------
#while loop
n = int(input("enter no: "))
mul=1

while n>0:
     rem=n%10
     mul=mul*rem
     n=n//10
print(mul)
if mul%2==0:
   print("even")
else:
   print("odd ")


#for loop

#for loop
n=input("enter no: ")
pro=1
for i in (n):
    pro=pro*int(i)
print(pro)
if pro%2==0:
    print("even no")
else:
    print("odd no")

------------------------------


*13. Number Range Display System (if-elif with loops)*
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using *if-elif-else and loops* to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same

--------------------------------------------

#while loop
n = int(input("enter no: "))
n = int(input("enter no: "))
n1 = int(input("enter no: "))
if n<n1:
    for i in range(n,n1+1,1):
       print(i)
elif n>n1:
     for i in range(n,n1-1,-1):
        print(i)
else:
   print("both no are same")


#for loop
a,b=map(int,input("enter no: ").split())
if b>a:
    while b>=a:
       print(a)
       a+=1
elif a>b:
    while a>=b:
        print(a)
        a=a-1

elif a==b:
       print("both no are same")

----------------------------------------------------
14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor
--------------------------------------------
n = int(input("enter no: "))
f=int (input("enter no"))

if n<f:
   for i in range(n,f+1,1):
       print(i)
elif n>f:
    for i in range(n,f-1,-1):
       print(i)
else:
   print("on the same floor")


#while loop

c=int(input("current floor"))
d=int(input("destination floor"))
if c<d:
    while c<=d:
        print(c,end=" ")
        c+=1
elif c>d:
    while c>=d:
        print(c,end=" ")
        c-=1
elif c==d:
    print("already on the same floor")
'''









