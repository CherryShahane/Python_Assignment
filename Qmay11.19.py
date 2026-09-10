'''19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5'''
n=int(input("Enter a number = "))
for i in range(1, n+1):
    print()
    for j in range(1, n+3):
        if j==n-i+1 or j==i:
            if j%2!=0:
                if j==n or j==1:
                    print(n,end="")
                else:
                    print(n-2,end="")
            else:
                print(n-1,end="")
        else:
            print(" ",end="")