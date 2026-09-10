"""
1
10
101
1010
10101
"""

n=int(input())
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
        if j<=i and j%2!=0:
            print("1",end="")
        else:
            if j<=i and j%2==0:
                print("0",end="")
