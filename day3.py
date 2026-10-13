correct = "2020"
attempts = 0

while attempts < 3:
    pin = input("Enter pin: ")
    if pin == correct:
        print("Access granted")
        break
    else:
        print("Wrong pin, try again")
        attempts = attempts + 1

if attempts == 3:
    print("Card blocked!")
else:
    balance = 10000
    withdraw = int(input(f"Balance is {balance}. How much to withdraw? "))
    if withdraw > balance:
        print("Insufficient funds!")
    else:
        print(f"Done! New balance is {balance - withdraw}")