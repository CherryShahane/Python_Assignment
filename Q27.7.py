'''
7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers.
Coupon numbers containing at least one zero in between digits are considered special duck numbers.
However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number

num = input("Enter Number = ")
zero = False

if  num[0] == '0':
    print("Not a duck number")
else:
    num = int(num)
    while num > 0:
        digit = num % 10
        if digit == 0:
            zero = True
            break
        num = num // 10
    if zero:
        print("Duck number")
    else:
        print("Not a duck number")'''

n = input("Enter number: ")


if n[0] == '0':
    print("Not a Duck number")
else:
    has_zero = 0

    for i in n:
        if i == '0':
            has_zero = 1
            break

    if has_zero == 1:
        print("Duck number")
    else:
        print("Not a Duck number")



