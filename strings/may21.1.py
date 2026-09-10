'''
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the
longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc



str = input("Enter String = ")

check = ""

i = 0
while i < len(str):
    if str[i] in check:
        break
    else:
        check = check + str[i]
    i+=1

print(check)'''

a=input("enter number")
r=''
h=''
i=0
while i<len(a):
    if a[i] not in r:
        r=r+a[i]
    else:
        if len(r)>len(h):
            h=r

            e=(i-len(r))+r.index(a[i])
            i=e+1
            r=''
            continue
    i=i+1
if len(r)>len(h):
    print(r)
else:
    print(h)
