p=input("enter password")
rn=0
num=0
dig=0
for i in p:
    if p[0:3]=="PNR" :
        rn=1
    if len(p)==12:
        num=1
    if p[3:12].isdigit():
        dig=1
if rn==1 and num==1 and dig==1:
    print("valid password")
else:
    print("invalid password")



