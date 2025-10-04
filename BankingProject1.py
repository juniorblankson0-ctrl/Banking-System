balance = 0

def show_balance():
    print(f"Your bank account balance is $ {balance:.2f}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit into your account: "))
    if amount <= 0:
        print("Enter a valid amount to deposit.")
    else:
        balance += amount
        print(f"$ {amount:.2f} deposited successfully.")

def withdrawal():
    global balance
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds.")
    elif amount <= 0:
        print("Amount must be greater than 0.")
    else:
        balance -= amount
        print(f"$ {amount:.2f} withdrawn successfully.")

is_running = True

while is_running:
    print("\nBANKING PROJECT")
    print("CUSTOMER SERVICE")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = input("Enter a choice from the menu: ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdrawal()
    elif choice == '4':
        is_running = False
        print("Thank you for banking with us.")
    else:
        print("Make sure to enter a valid choice (1 - 4).")
