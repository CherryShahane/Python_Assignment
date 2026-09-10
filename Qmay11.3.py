'''3) X Star Pattern
    *   *
     * *
      *
     * *
    *   *'''

n=int(input("enter no"))
for i in range(1,n+1):
    print()
    j=1
    for j in range(1,n+3):
        if j==n-i+1 or j==i:
            print("*",end="")
        else:
            print(" ",end="")

