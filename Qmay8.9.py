'''9.
    1
   10
  101
 1010
10101
n=int(input("enter no"))
for i in range(1,n+1):
    print()
    space=n
    while space>i:
        print(" ",end="")
        space-=1
    j=1
    while j<=i:
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j+=1'''

n=int(input("enter no"))
for i in range(1,n+1):
    print()
    space=1
    while space<=n-i:
        print(" ",end="")
        space+=1
    j=1
    while j<=i:
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j+=1