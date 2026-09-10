n=int(input())
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
        if j<=i and i%2==0:
           print("0",end='')
        else:
            if j<=i:
               print("1",end='')
