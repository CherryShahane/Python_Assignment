
'''24/4/26
1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9

---------------------------------------------------
#while loop
n = int(input("enter no: "))

largest = 0

while n > 0:
    rem = n % 10
    rem1 = (n // 10) % 10

    if rem > largest:
        largest = rem

    if rem1 > largest:
        largest = rem1

    n = n // 10

print("largest is", largest)


#for loop
n=input("enter no: ")
largest=0
for i in (n):
    rem=int(i)%10
    if rem>largest:
        largest=rem
    i=int(i)//10
print("largest is", largest)

-----------------------------------------'''

'''2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
-------------------------------

#while loop
n = int(input("enter no: "))

smallest = n % 10

while n > 0:
    rem = n % 10

    if rem < smallest:
        smallest = rem

    n = n // 10

print("smallest is", smallest)

#for loop
n=input("enter no: ")
smallest=9
for i in (n):
    rem=int(i)%10
    if rem<smallest:
        smallest=rem
    i=int(i)//10
print("smallest",smallest)'''

'''----------------------------------------------
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5
--------------------------------------------
n = int(input("enter no: "))
r=0
while n >0:
   rem=n%10
   r=r*10+rem
   n=n//10
   rem=r%10
print("first digit=",rem)

#for loop
n=input("enter no: ")
for i in (n):
    print(int(i))
    break
    
--------------------------------------------------'''
'''4. Numbers Divisible by 3 Between Two Numbers
A school is organizing a quiz competition. Only students whose roll numbers are divisible by 3 are selected for the first round. The teacher enters a roll number range and wants the system to display eligible roll numbers.
Write a program to display numbers divisible by 3 between two given numbers using loops.

Input:
10 25

Output:
12 15 18 21 24


------------------------------------------------------
#for loop
a=int(input("enter no"))
b=int(input("enter no"))
for i in range(a,b+1,1):
    if i%3==0:
       print(i)


#while loop
a,b=map(int,input("enter no: ").split())
while a<=b:
    if a%3==0:
        print(a)
    a+=1
--------------------------------------  '''
'''5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6

----------------------------------------------
#for loop
a=int(input("enter no"))
count=0
for i in range (1,a+1):
   if a%i==0:
      count=count+1
print("total factors",count)

#while loop
n=int(input("enter no: "))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
print("total factors",count)'''
'''------------------------------------------
6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12
-------------------------------------------
#for loop
a=int(input("enter no"))

sum=0
for i in range (1,a+1):
   if a%i==0:
      sum=sum+i
print("total sum",sum)

#while loop
n=int(input("enter no: "))
sum=0
i=1
while i<=n:
    if n%i==0:
        sum=sum+i
    i+=1
print("sum",sum)'''

'''-----------------------------------
7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
------------------------------------------------------

a,b=map(int,input("enter no").split())
while a<=b:
    p= a**b
    break
print("power",p)


a=int(input("enter no: "))
b=int(input("enter no: "))
for i in range(a,b+1):
    p=a**b
    break
print("power",p)'''
''''---------------------------------
8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4
--------------------------------------
a,b=map(int,input("enter no").split())
count=0
for i in range (a,b+1):
    if i%5==0:
       count=count+1
print("count",count)

a,b=map(int,input("enter no: ").split())
count=0
while a<=b:
    if a%5==0:
        count=count+1
    a+=1
print("count",count)'''
'''----------------------------------
9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number!

.......................................................

n=int(input("enter number"))
rem=0
sum=0
temp=n
seq=n*n
while seq>0:
    rem=seq%10
    sum=sum+rem
    seq=seq//10



if sum==temp:
   print("Glowing Success! You've found the Neon Number!")
else:
   print("Try again! Not quite glowing yet")

#for loop
n=input("enter number")
s=int(n)*int(n)
sum=0
for i in range(s):
    s=s%10
    sum=sum+s
    s=s//10
print(sum)'''
'''-----------------------------------
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 4
-------------------------------------

n=int(input("enter number"))
count=0
while n>0:
   rem=n%10
   if rem%2!=0:
      count=count+1
   n=n//10
print("odd digits are",count)


n=input("enter number")
count=0
for i in (n):
    if int(i)%2!=0:
       count=count+1
print("odd digits are",count)'''













