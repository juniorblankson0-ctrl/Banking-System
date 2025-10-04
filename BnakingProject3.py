balance = 0
transaction_history = []
correct_pin = "1234"



# ---------------------- PIN SECURITY ----------------------
attempts = 0
while attempts < 3:
    pin = input("Enter your 4-digit PIN: ").strip()
    if pin == correct_pin:
        print("Access granted.\n")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. Attempts left: {3 - attempts}")
else:
    print("Too many attempts. Exiting...")
    exit()




# ------------------ BANK FUNCTIONS -----------------------
def show_balance():
    print(f"Your bank account balance is $ {balance:.2f}")
    transaction_history.append("Checked balance")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit into your account: "))
    if amount <= 0:
        print("Enter a valid amount to deposit.")
    else:
        balance += amount
        print(f"$ {amount:.2f} deposited successfully.")
        transaction_history.append(f"Deposited $ {amount:.2f}")

def withdrawal():
    global balance
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds.")
        transaction_history.append(f"Attempted withdrawal of $ {amount:.2f} — Failed (Insufficient funds)")
    elif amount <= 0:
        print("Amount must be greater than 0.")
    else:
        balance -= amount
        print(f"$ {amount:.2f} withdrawn successfully.")
        transaction_history.append(f"Withdrew $ {amount:.2f}")

def show_transaction_history():
    print("\n--- TRANSACTION HISTORY ---")
    if transaction_history:
        for i, entry in enumerate(transaction_history, 1):
            print(f"{i}. {entry}")
    else:
        print("No transactions yet.")



# ---------------------- MAIN MENU ------------------------
is_running = True

while is_running:
    print("\nBANKING PROJECT")
    print("CUSTOMER SERVICE")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter a choice from the menu: ").strip()

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdrawal()
    elif choice == '4':
        show_transaction_history()
    elif choice == '5':
        is_running = False
        print("Thank you for banking with us.")
    else:
        print("Make sure to enter a valid choice (1 - 5).")
