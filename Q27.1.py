'''27/4/26
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15'''


#while loop
'''num = int(input("Enter number = "))
product = 1
i = 0

while i <= num:
    if i%2 != 0:
        product = product * i
    i+=1
print(product)'''



#for loop
n=int(input("Enter number = "))
pro=1
for i in range(1,n+1,2):
    if i%2 != 0:
        pro=pro*i
    i+=1
print("product is ",pro)

      
    
    

