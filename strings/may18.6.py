'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''

first=input("enter first code")
second=input("enter second code")
c=0

for i in first:
    if   first.count(first)==1 and second.count(second):
          c=1
if c==1:
    print("matching")
else:
    print("not matching")
            


