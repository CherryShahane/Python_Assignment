'''4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code'''

n=int(input("Enter Number:"))
while n>0:
    rem=n%10
    rem1=(n//10)%10
    n=n//10
    if rem==rem1:
        print("rejected")
        break
    n=n//10
else:
    print("accept")