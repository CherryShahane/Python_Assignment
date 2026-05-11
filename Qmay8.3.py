'''3)	WAP to find out all the leap years between two entered years'''
a=int(input("enter first year"))
b=int(input("enter second year"))
for i in range (a,b+1):
    if (i%4==0 and i%100!=0 )or i%400==0:
        print(i)

