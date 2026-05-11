'''3.
Digit Neighbor Sum Analyzer

A system analyzes the relationship between a digit and its immediate neighbors.

Write a program to:

Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
121314
413121

Output:
Matching Digits: 2
Count = 2
Neighbor Sum Pattern Found'''
n=int(input("enter no"))
temp = n
rev = 0
count = 0
found = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Matcing Digits = ",end = " ")
while rev >= 100:
    left = rev % 10
    rev = rev // 10
    curr = rev % 10
    rev = rev // 10
    right = rev % 10

    if curr == left + right:
        print(curr, end = " ")
        count+=1
        found = 1
print("\ncount = ",count)
if found:
    print("Neighbor Sum Pattern Found")
else:
    print("No Matching Digit")