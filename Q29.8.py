

'''8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7'''

'''n=int(input("enter amount"))
count=0
while n>=100:
    n=n-100
    count+=1
print("notes", count)'''



n=int(input("enter amount"))
count=0
for i in range(100,n+100,100):
    n=n-i
    count+=1
print("notes", count)


