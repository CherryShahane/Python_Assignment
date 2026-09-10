'''13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5'''

n=int(input("enter no"))
for i in range(1,n+1):
    print()
    for j in range(1,n+3):
        if j==n-i+1 or j==i:
            print(j,end="")
        else:
            print(" ",end="")