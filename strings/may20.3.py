'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:


e

'''
n=input("enter string")
f=0
i=0
while i<len(n):
    count=0
    j=0
    while j<len(n):
        if n[i]==n[j]:
            count=count+1
            j=j+1
    if count==1:
        print("first character not repeated",n[i])
        f=1
        break
if f==0:
    print("no non repeated character found")