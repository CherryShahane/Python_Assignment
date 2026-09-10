s=input("enter string")
t=input("enter charactrt to check")
count=0
for i in s:
    if i ==t:
        count=count+1
print("character",t,"occurs",count,"times")
