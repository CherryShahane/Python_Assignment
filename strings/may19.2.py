'''
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST
'''

n=input("enter string")
word=n.split()
first=''
i=0
while i<len(word):
    words=word[i]
    if words[0]!=' ':
        first=first+words[0].upper()
    i+=1
print(first)


