'''7.

     *
    **
   ***
  ****
 *****
******
n=int(input("enter no"))
i=1
while i<=n:
    print()
    space=1
    while space<=n-i:
        print(" ",end="")
        space+=1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i+1'''
n=int(input("enter no"))
for i in range(1,n+1):
    print()
    space=1
    while space<=n-i:
        print(" ",end="")
        space+=1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1