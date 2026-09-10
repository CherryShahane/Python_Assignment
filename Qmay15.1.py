s=input("enter  string")
count=0
for i in s:
    if i in "aeiou":
        count=count+1
print("Total Vowels",count)