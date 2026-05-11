'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31'''

'''n=int(input("enter no"))

i=2
x=0

if n<1:
    print("not prime")

else:
    while i<n:
        if n%i==0:
            x=1
            break
        i+=1
    if x==1:
       print("not prime")
    i=2
    x=0
    pre=n-1

    while pre>1:
        i = 2
        x = 0
        if pre%i==0:
            x=1
            break
        i+=1
    if pre==0:
        print("previous prime", pre)

    pre-=1
    else:
        print("prime")

    next = n + 1

    while True:
        i = 2
        x = 0

        while i < next:
            if next % i == 0:
                x = 1
                break
            i += 1

        if x == 0:
            print("next prime", next)
            break

        next += 1'''

n=int(input("enter no") )
prime=1
i=2
next = n+1
pre = n-1

while i<n:
    if n%i==0:
        prime=0
        break
    i+=1

if prime==1:
    print("prime")
    while True:
        i = 2
        x = 0
        while i<next:
            if next%i==0:
                x=1
                break
            i+=1
        if x==0:
           print("next prime", next)
           break
        next+=1
else:
    print(" not prime")
    while True:
        i = 2
        x = 0
        while i<pre:
            if pre%i==0:
                x=1
                break
            i+=1
        if x==0:
            print("previous prime is",pre)
        pre-=1


