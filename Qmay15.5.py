p=input("enter password :")
upper=0
digit=0
count=0
special=0
num=0
for i in p:
    if  len(p)>=8 and len(p)<=15:
        num=1

    if( p[-1].isdigit()):
            digit=1
    if (i[0].isupper()) :
        upper=1
    if i.isdigit():
        count=count+1
    if i==" ":
        special=0
    else:
        special=1
if digit==1 and upper==1 and special==1 and count==2 and num==1:
    print("valid password")
else:
    print("invalid password")
