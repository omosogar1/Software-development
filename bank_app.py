import json
from datetime import datetime

DATA_FILE = "bank_data.json"
HISTORY_FILE = "transactions.json"

try:
    with open(DATA_FILE, "r") as f:
        accounts = json.load(f)
except:
    accounts = {"2020": {"name": "Kelly", "balance": 5500}}

try:
    with open(HISTORY_FILE, "r") as f:
        transactions = json.load(f)
except:
    transactions = []

def save_all():
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=2)
    with open(HISTORY_FILE, "w") as f:
        json.dump(transactions, f, indent=2)

def add_transaction(type_, amount, to_acc=""):
    transactions.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "type": type_,
        "amount": amount,
        "to": to_acc,
        "balance": accounts["2020"]["balance"]
    })
    save_all()

if "2020" not in accounts:
    accounts["2020"] = {"name": "Kelly", "balance": 5500}

while True:
    print("\n=== KELLY BANK APP ===")
    print(f"Account: 2020 ({accounts['2020']['name']}) | Balance: ${accounts['2020']['balance']}")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Transaction History")
    print("6. Exit")
    
    choice = input("Choose (1-6): ")

    if choice == "1":
        print(f"Your balance: ${accounts['2020']['balance']}")

    elif choice == "2":
        amt = int(input("Deposit amount: $"))
        accounts["2020"]["balance"] += amt
        add_transaction("Deposit", amt)
        print(f"Deposited ${amt}. New balance: ${accounts['2020']['balance']}")

    elif choice == "3":
        amt = int(input("Withdraw amount: $"))
        if amt > accounts["2020"]["balance"]:
            print("Insufficient funds!")
        else:
            accounts["2020"]["balance"] -= amt
            add_transaction("Withdraw", amt)
            print(f"Withdrew ${amt}. New balance: ${accounts['2020']['balance']}")

    elif choice == "4":
        to_acc = input("Transfer to account: ")
        amt = int(input("Amount: $"))
        if amt > accounts["2020"]["balance"]:
            print("Insufficient funds!")
        else:
            accounts["2020"]["balance"] -= amt
            if to_acc not in accounts:
                accounts[to_acc] = {"name": "User", "balance": 0}
            if isinstance(accounts[to_acc], dict):
                accounts[to_acc]["balance"] += amt
            else:
                accounts[to_acc] += amt
            add_transaction("Transfer", amt, to_acc)
            print(f"Transferred ${amt} to {to_acc}. Your balance: ${accounts['2020']['balance']}")

    elif choice == "5":
        print("\n--- Transaction History ---")
        if not transactions:
            print("No transactions yet.")
        else:
            for t in transactions[-10:]:
                print(f"{t['time']} | {t['type']} ${t['amount']} {t['to']} | Balance: ${t['balance']}")

    elif choice == "6":
        print("Thank you for banking with Kelly Bank!")
        break
    else:
        print("Invalid choice. Try 1-6.")