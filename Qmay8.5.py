'''5)
A
AB
ABC
ABCD
ABCDE'''
'''n=int(input("enter no"))
i=1
while i<=n:
    print()
    j=1
    ch=65
    while j<=i:
        print(chr(ch),end="")
        ch=ch+1
        j+=1
    i+=1'''

'''6)
a
ab
abc
abcd
abcde'''

n=int(input("enter no"))
i=1
while i<=n:
    print()
    j=1
    ch=65
    while j<=i:
        print(chr(ch).lower(),end="")
        ch=ch+1
        j+=1
    i+=1