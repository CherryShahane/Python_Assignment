# 23/4/26

'''1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the *total points earned after n days* by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55
---------------------------------------------------------
n=int(input("enter n"))
sum=0
for i in range (n,n+1):

    sum=sum+i
print("total points",sum)
print("out of loop")

#while loop
n=int(input("enter no"))
sum=0
i=1
while n>=i:
    sum=sum+i
    i+=1
print("total points",sum)'''

'''2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the *factorial of a given number using loops*.

Input: n = 5
Output: Total Ways = 120
-----------------------------------------
n=int(input("enter n"))
f=1
for i in range(1,n+1):
    f=f*i
print("total ways",f)


n=int(input("enter no"))
f=1
i=1
while i<=n:
     f=f*i
     i=i+1
print("factorial is ",f)'''

'''3. Multiplication Table
A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
Write a program to print the *multiplication table of a given number up to 10 using loops*.

Input: n = 6
Output:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
-------------------------------------------------------------------
n=int(input("enter n"))
for i in range (1,11):
    print(n*1)
print(i)'''

'''n=int(input("enter n"))
i=1
while i<=10:
    print(,n*i)
    i=i+1'''

'''.............................................................'''
'''4. Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.

Input: 1234
Output: 4321'''

'''n = int(input("enter n: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("reverse =", rev)

n=int(input("enter n"))
rev=0
for i in range(n):
    if n==0:
        break
    rem=n%10
    rev=rev*10+rem
    n=n//10

print("reverse =", rev)

n=int(input("enter n"))
rev=0
for i in range(len(str(n))):
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

print("reverse =", rev)'''

'''------------------------------------------------------------'''

'''5 Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops'''

'''n=int(input("enter no")
for i in range(n,n+1,-1)
   if n==i:
      print ("palindream",n) 

n=int(input("enter no"))
temp=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if temp==rev:
    print ("palindrome")
else:
    print("not palindrome")

------------------------------------------------'''
'''6 In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

x = int(input("enter number: "))

temp = x
sum = 0

while x > 0:
    rem = x % 10
    sum = sum + rem**3
    x = x // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not Armstrong number")


n=int(input("enter no"))
temp=n
sum=0
for i in range(n):

   rem=n%10
   cube=rem*rem*rem
   sum=sum+cube
   n=n//10
if sum==temp:
    print("armstorm no")
else:
    print("not armstorm no")
-----------------------------------------------------------------------------'''

'''*7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3
--------------------------------------------------------

x = int(input("enter number: "))
i=2
count=0
while i<=x:
   print(i)
   count=count+i
   i+=2
   count=count+i
print("even digits are ",count)'''


'''n=int(input("enter no"))
count=0
for i in range (len(str(n))):
    rem=i%10
    if rem%2==0:
        count+=1
    n=n//10
print("even digits are ",count)'''

''' *8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3
-------------------------------------------

n=int(input("enter n"))
i=1
count=0
while i<=n:
   print(i)
   count=count+i
   i=+2
print("odd digit are",count)'''

n=input("enter no")
count=0
for i in n :
    if int(i)%2!=0:
        count=count+1
print("odd digits are ",count)

# 9. Check All Digits Are Even*
# A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
# Write a program to *check whether all digits of a number are even using loops

# Input: 2468
# Output: All Even

# Input: 2456
# Output: Not All Even

'''n = int(input("enter no: "))
temp = n

while n > 0:
    rem = n % 10

    if rem % 2 != 0:
        print("Rejected: contains odd digit")
        break

    n = n // 10

else:
    print("Accepted: all digits are even", temp)

n=input("enter no")
for i in n:

    if int(i)%2!=0:
        print(" not all even")
        break
else:
    print("  all even")'''









