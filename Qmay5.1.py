'''1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.'''

t=input("enter type")
a=int(input("enter amount"))

discount = (20/100 if t == "premium" and a > 5000 else 10/100 if t == "premium" else 10/100 if t == "regular" and a > 3000 else 5/100 )

total = a - (a * discount)
print("Final payable amount",total)