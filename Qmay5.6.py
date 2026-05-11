'''6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.'''
n=input("enter number")
for ch in n:
   display=("alphabets " if ch.isalpha()  else "digits " if ch.isdigit() else "special character ")
   print(display)

