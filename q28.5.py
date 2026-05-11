'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3'''



a=int(input("enter no"))

n=a+1

while True:
    i=2
    x=0

    while i<n:
        if n%i==0:
            x=1
            break
        i+=1

    if x==0:
        print("next prime",n)
        gap = n - a
        print("gap", gap)
        break

    n+=1

