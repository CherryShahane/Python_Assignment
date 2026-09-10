''''
*
 *
  *
   *
    *'''
n=int(input("enter no"))
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
       if j==i:
           print("*",end="")
       else:
           print(" ",end="")
