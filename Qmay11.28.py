'''28) Hollow Square
    *****
    *   *
    *   *
    *   *
    *****'''
n=int(input("enter no"))
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            if j==i:
                print("*",end="")
            else:
                print("*",end="")
        else:
            print(" ",end="")