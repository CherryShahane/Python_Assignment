'''8.
enter n6
 654321
  65432
   6543
    654
     65
n=int(input("enter no"))
i=1
while i<n:
    print()
    space=1
    while space<i:
        print(" ",end="")
        space=space+1
    j=n
    while j>=i:
        print(j,end="")
        j-=1
    i+=1'''


n=int(input("enter no"))
for i in range(1,n):
    print()
    space=1
    while space<i:
        print(" ",end="")
        space+=1
    j=n
    while j>=i:
        print(j,end="")
        j-=1
