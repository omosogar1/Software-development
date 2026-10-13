correct = "2020"
attempts = 0
balance = 10000

# Step 1: PIN Check with 3 tries
while attempts < 3:
    pin = input("Enter pin: ")
    if pin == correct:
        print("Access granted\n")
        break
    else:
        print("Wrong pin, try again")
        attempts += 1

if attempts == 3:
    print("Card blocked! Contact your bank.")
else:
    # Step 2: ATM Menu Loop
    while True:
        print("\n--- KELLY BANK ATM ---")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        
        choice = input("Choose 1-4: ")

        if choice == "1":
            print(f"Your balance is: {balance}")

        elif choice == "2":
            amount = int(input("How much to withdraw? "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance = balance - amount
                print(f"Success! New balance is {balance}")

        elif choice == "3":
            amount = int(input("How much to deposit? "))
            balance = balance + amount
            print(f"Deposited! New balance is {balance}")

        elif choice == "4":
            print("Thank you for using KELLY BANK. Goodbye!")
            break

        else:
            print("Invalid choice, try 1-4")