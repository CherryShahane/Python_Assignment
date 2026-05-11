'''3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.'''

s=int(input("enter salalry"))
e=int(input("enter experience"))
bonus=((30/100*s) if e>10  else (20/100*s) if e>5  else (10/100*s))
total=s+bonus
print(total)


