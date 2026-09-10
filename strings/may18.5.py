'''5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code'''
n=input("Enter product code: ")
for ch in n:
    if n[0: ]==n[-1: ]:
        print("palindrome")
    else:
        print("not a palindrome")