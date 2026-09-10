'''
    *
   *_*
  *___*
 *_____*
*********
'''

n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i*2):
        if j==1:
            print("*",end="")
        elif i==n:
            print("*",end="")
        elif j==i*2-1:
            print("*",end="")
        else:
            print("_",end="")