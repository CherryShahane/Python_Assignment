'''4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''
x=int(input("Enter starting number: "))
y=int(input("Enter ending number: "))
for i in range(x,y+1):
    temp=i
    total=0
    power=len(str(i))
    while i>0:
        digit=i%10
        total=total+digit**power
        i=i//10

    if total==temp:
        print(temp)

