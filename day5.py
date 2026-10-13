import os
import json

BASE_DIR = os.path.dirname(__file__)
FILE = os.path.join(BASE_DIR, "bank_data.json")

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        accounts = json.load(f)
else:
    accounts = {
        "2020": {"name": "Kelly", "balance": 10000},
        "1234": {"name": "David", "balance": 50000}
    }
    with open(FILE, "w") as f:
        json.dump(accounts, f)

def save_data():
    with open(FILE, "w") as f:
        json.dump(accounts, f)
    print(">> Saved to file!")

pin = input("Enter PIN: ").strip()
if pin not in accounts:
    print("Invalid PIN!")
    exit()

user = accounts[pin]
print(f"Welcome {user['name']}!")

while True:
    print("\n1.Check 2.Withdraw 3.Deposit 4.Exit")
    choice = input("> ").strip()
    if choice == "1":
        print(f"Balance: {user['balance']}")
    elif choice == "2":
        amt = int(input("Amount: "))
        if amt > user['balance']:
            print("Insufficient!")
        else:
            user['balance'] -= amt
            save_data()
            print(f"New balance: {user['balance']}")
    elif choice == "3":
        amt = int(input("Amount: "))
        user['balance'] += amt
        save_data()
        print(f"New balance: {user['balance']}")
    elif choice == "4":
        print("Bye!")
        break