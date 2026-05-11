'''3.

 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

---'''
amount=0
withdrawl=0
current_balance=0
intrest=0
update_balance=0
while True:
    print("menu")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            amount=int(input("enter amount to deposit: "))
            print("amount deposited successfully")

        case 2:
            if amount==0:
                print(" no balance available. Plase deposite amount")
            else:
                withdrawl=int(input("enter amount to withdrawl: "))
                if withdrawl>amount:
                    print("insufficient balance")
                else:
                    amount=abs(withdrawl-amount)
                    print("withdrawal successful")


        case 3:
            if amount==0:
                print(" no balance available. Plase deposite amount")
            else:
                current_balance=amount-withdrawl
                print("current balance",current_balance)

        case 4:
            if amount==0:
                print(" no balance available. Plase deposite amount")
            else:
                if current_balance>50000:
                    intrest=current_balance*5/100
                    print("entrest added",intrest)
                    update_balance=current_balance+intrest
                    print("updated balance",update_balance)

                else:
                    intrest=current_balance*3/100
                    print("entrest added", intrest)
                    update_balance = current_balance + intrest
                    print("updated balance", update_balance)
        case 5:
            print("Exiting loop. Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")

