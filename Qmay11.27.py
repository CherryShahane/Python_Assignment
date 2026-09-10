'''27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10'''
n=int(input("enter no"))

num=1
for i in range(1,n+1):
    print()
    spa=1
    while spa<=n-i:
        print(" ",end="")
        spa=spa+1
    k = i
    while k>=i and k<=i+(i-1):
        print(num,end=" ")
        k=k+1
        num=num+1
