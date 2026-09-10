s=input("enter string").lower()
count=0
for i in s:
    if i not in "aeiou" and i!=" ":
         count=count+1
print("total consonent are=",count)