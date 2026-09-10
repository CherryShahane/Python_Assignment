'''
# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8

'''

n=input("enter string")
i=0

while i<len(n):
    count = 0
    j=0
    if n[i].isdigit():
        while j<len(n):
            if n[i] == n[j]:
                count+=1
            j+=1
    if count == 1:
        break
    i+=1
print(n[i])