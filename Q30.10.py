'''10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit
        Next 100 units      → ₹7 per unit
        Above 200 units     → ₹10 per unit

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge
        - If units < 50 → give ₹100 subsidy

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700'''

n=int(input("no of houses"))
bill=0
for i in range(1,n+1):
    units=int(input("Enter units"))
    if units<50:
        bill=units*5
        s=100
        bill=abs(bill-s)


    elif units >50 and units<=100:
        bill=5*units


    elif units >100 and units<=200:
        bill=(100*5)+((units-100)*7)

    else:
        bill=(100*5)+(100*7)+((units-200)*10)


    print(bill)
while bill>0:
    if bill>2000:
       s=(bill*10/100)
       bill=s+bill

