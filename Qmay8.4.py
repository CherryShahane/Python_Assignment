'''4)
1
00
111
0000
11111
n=int(input("enter no"))
i=1
k=1
b=0
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print(b,end="")
        else:
            print(k,end="")
        j+=1
    i+=1'''
n=int(input("enter no"))
i=1
k=0
b=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print(k,end="")
        else:
            print(b,end="")
        j+=1
    i+=1
