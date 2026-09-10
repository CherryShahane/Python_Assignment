'''7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5'''

n=int(input("enter no"))
for i in range(1,n+1):
    print()
    spa=2
    while spa<=i :
        print(spa, end="")
        while spa==i:
          print(i+1,end="")
        spa=spa+1



        