'''2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12'''

n=input("Enter contact number: ")
dig=0
for i in n:
    if i>="0" and i<="9":
        dig=dig+1
print("total digit ",dig)