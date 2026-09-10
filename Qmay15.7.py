num=input("enter number")
dig=0
n=0
d=0
for i in num:
    if len(num)==10:
        dig=1
    if num[0:1].isalpha():
        n=1
    if num[2:3].isdigit():
        d=1
if dig==1 and n==1 and d==1:
    print("valid vehicle number")
else:
    print("invalid vehicle numner")

