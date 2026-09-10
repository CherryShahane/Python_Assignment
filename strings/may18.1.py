'''1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username'''

n=input("enter string")
d=0
dig=0
digit=0
under=0
space=0
for i in n:
    if len(n)>=5 and len(n)<=12:
        d=1
    if i[0]>="a" and i[0]<="z":
        dig=1
    #if int(i)>= 0 and int(i)<=9:
     #   digit=1
    if i=="_":
        under=1
    if i==" ":
        space=1
    else:
        digit=1
if d==1 and dig==1 and digit==1 and under==1 and space==0:
    print("Valid Username")
else:
    print("Invalid Username")



