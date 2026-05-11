'''5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1'''

n=int(input("enter no"))
i=n
while i>1:
    print()
    dec=1
    while dec<i:
        print(dec,end="")
        dec=dec+1
    for k in range(n,i,-1):
        print("**",end="")
    for m in range(i-1,0,-1):
        print(m,end="")
    i=i-1







