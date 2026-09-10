'''
1
12
1 3
1  4
12345


'''

n = int(input("enter the number"))

for i in range(1, n + 1):
    print()
    print("1", end="")
    for j in range(2, i + 1):

        if i == j:
            print(j, end="")
        elif i == n:
            print(j, end="")
        else:
            print(" ", end="")