'''4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID'''
n=input("Enter Employee ID: ")
ch=0
d=0
di=0
for i in n:
    if len(n)>=8:
        ch=1
    if i[0:2]=="EMP":
        d=1
    if (i[3: ].isdigit())  :
        di=1

if ch==1 and d==1 and di==1:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")
