'''2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17'''
'''
n=int(input("Enter a number: "))

i=2
x=0
while i<n:
    if n%i==0:
        x=1
        break
    i+=1
if x==1:
    print("Next Prime",i)'''


num = int(input("Enter Number : "))

next = num + 1

while True:
    i = 2
    prime = 1
    while i<next:
        if next%i==0:
            prime = 0
            break
        i+=1
    if prime==1:
        print("Next Prime",next)
        break
    next+=1



