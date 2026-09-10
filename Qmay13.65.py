'''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''
n = int(input("enter the number"))

for i in range(1, n + 1):
    print()
    for k in range(1, n - i + 1):
        print(" ", end="")
    print("1", end=" ")
    for j in range(2, i + 1):
        if i == j:
            print("1", end=" ")
        elif n == i:
            if j % 2 != 0:
                print(n + 1, end=" ")
            else:
                print(n - 1, end=" ")

        else:
            print(i - 1, end=" ")