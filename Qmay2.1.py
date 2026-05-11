'''1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern'''

n = int(input("Enter Number : "))

prev = n % 10
n = n // 10
count = 0
largest = 0
check = None
uniform = 1
print("Differences",end = " ")
while n > 0:
    curr = n % 10
    diff = abs(prev - curr)
    print(diff, end = " ")
    if diff%2 == 0:
        count+=1
    if diff > largest:
        largest = diff
    if check == None:
        check = diff
    elif check!= diff:
        uniform = 0
    prev = curr
    n = n // 10

print("\nEven Count = ",count)
print("Maximum Difference = ",largest)
if uniform == 1:
    print("Uniform Pattern")
else:
    print("Non-Uniform Pattern")
