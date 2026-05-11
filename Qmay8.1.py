'''1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9'''
sum=0
for i in range(100,200+1):
    if i%9==0:
        sum=sum+i
print(sum)