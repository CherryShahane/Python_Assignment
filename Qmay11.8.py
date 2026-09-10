'''8) Border Number Pattern
    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5'''

n=int(input("enter no"))
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            if j==i:
                print(i,end="")
            else:
                print(j,end="")
        else:
            print("  ",end="")
