import json
# Load your actual format
try:
    with open("bank_data.json", "r") as f:
        accounts = json.load(f)
except:
    accounts = {"2020": {"name": "Kelly", "balance": 6000}}
# Make sure 2020 exists
if "2020" not in accounts:
    accounts["2020"] = {"name": "Kelly", "balance": 6000}
print("=== DAY 6 - TRANSFER ===")
print(f"Your account 2020 ({accounts['2020']['name']}): ${accounts['2020']['balance']}")
print("")
transfer_to = input("Transfer to account: ")
amount = int(input("Amount: $"))
if amount > accounts["2020"]["balance"]:
    print("❌ Insufficient funds!")
else:
    # Deduct from you
    accounts["2020"]["balance"] -= amount
    
    # Add to other account
    if transfer_to in accounts:
        # if it's dict format
        if isinstance(accounts[transfer_to], dict):
            accounts[transfer_to]["balance"] += amount
        else:
            accounts[transfer_to] += amount
    else:
        accounts[transfer_to] = {"name": "User", "balance": amount}
    # Save
    with open("bank_data.json", "w") as f:
        json.dump(accounts, f, indent=2)
    print(f" Transferred ${amount} to {transfer_to}")
    print(f"Your new balance: ${accounts['2020']['balance']}")