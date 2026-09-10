'''
*
* *
*   *
*     *
* * * * *

'''

n = int(input("enter the number"))
print("*")
for i in range(2, n):
    for j in range(2, i + 1):
        if j == 2:
            print("*", end="")
        else:
            print("  ", end="")
    print(" *", end="")
    print()
print("* " * n)

