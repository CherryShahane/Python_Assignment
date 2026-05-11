'''2.
Digit Order Break Analyzer

A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

Write a program to:

Traverse the digits from left to right
Check whether each digit is greater than the previous digit
If the pattern breaks at any point, stop checking further using break
Display the position where the order breaks (1-based index)
If no break occurs, print Strictly Increasing Number

Use loops and break wherever required.

Input:
12357

Output:
Strictly Increasing Number

Input:
12342

Output:
Break at position = 4
Not Increasing Number


num = input("Enter Number = ")

prev = int(num[0])
break_pos = -1

for i in range(1, len(num)):
    curr = int(num[i])

    if curr <= prev:
        break_pos = i + 1
        break

    prev = curr

if break_pos == -1:
    print("Strictly Increasing Number")
else:
    print("Break at position =", break_pos)
    print("Not Increasing Number")'''

n=int(input("Enter Number = "))
rev=0
temp=n
count=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10

prev = rev % 10
rev = rev // 10
found = 0
while rev > 0:
    digit = rev%10
    if digit < prev:
        found = 1
        break
    prev = digit
    rev = rev // 10

if found == 0:
    print("Strictly Increasing Number")
else:
    print("Not Increasing Number")

'''curr = (rev // 10) % 10
    rev=rev//10

if curr<pre:
    count+=1
    print("not increasing")

else:
    print("Strictly Increasing Number")'''




