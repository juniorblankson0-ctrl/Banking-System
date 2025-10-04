import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# ----------------- INITIAL VALUES -----------------
balance = 0.0
transaction_history = []
correct_pin = "1234"


# ----------------- FUNCTIONS -----------------
def verify_pin():
    pin = pin_entry.get()
    if pin == correct_pin:
        pin_window.destroy()
        open_main_window()
    else:
        messagebox.showerror("Access Denied", "Incorrect PIN")


def show_balance():
    messagebox.showinfo("Balance", f"Your balance is $ {balance:.2f}")
    transaction_history.append("Checked balance")


def deposit():
    global balance
    try:
        amount = float(simpledialog.askstring("Deposit", "Enter amount to deposit:"))
        if amount <= 0:
            messagebox.showerror("Invalid", "Amount must be greater than 0.")
        else:
            balance += amount
            messagebox.showinfo("Success", f"Deposited $ {amount:.2f}")
            transaction_history.append(f"Deposited $ {amount:.2f}")
    except:
        messagebox.showerror("Error", "Invalid amount entered.")


def withdrawal():
    global balance
    try:
        amount = float(simpledialog.askstring("Withdrawal", "Enter amount to withdraw:"))
        if amount > balance:
            messagebox.showwarning("Insufficient", "Not enough balance.")
            transaction_history.append(f"Attempted withdrawal of $ {amount:.2f} — Failed (Insufficient funds)")
        elif amount <= 0:
            messagebox.showerror("Invalid", "Amount must be greater than 0.")
        else:
            balance -= amount
            messagebox.showinfo("Success", f"Withdrew $ {amount:.2f}")
            transaction_history.append(f"Withdrew $ {amount:.2f}")
    except:
        messagebox.showerror("Error", "Invalid amount entered.")


def show_history():
    if not transaction_history:
        messagebox.showinfo("History", "No transactions yet.")
    else:
        history = "\n".join([f"{i+1}. {item}" for i, item in enumerate(transaction_history)])
        messagebox.showinfo("Transaction History", history)


# ----------------- WINDOWS -----------------
def open_main_window():
    main_window = tk.Tk()
    main_window.title("Banking System")
    main_window.geometry("400x400")
    main_window.resizable(False, False)

    ttk.Label(main_window, text="Welcome to Our Bank", font=("Arial", 16, "bold")).pack(pady=10)

    ttk.Button(main_window, text="Show Balance", command=show_balance).pack(pady=10, ipadx=10, ipady=5)
    ttk.Button(main_window, text="Deposit", command=deposit).pack(pady=10, ipadx=20, ipady=5)
    ttk.Button(main_window, text="Withdraw", command=withdrawal).pack(pady=10, ipadx=20, ipady=5)
    ttk.Button(main_window, text="Transaction History", command=show_history).pack(pady=10, ipadx=5, ipady=5)
    ttk.Button(main_window, text="Exit", command=main_window.destroy).pack(pady=10, ipadx=40, ipady=5)

    main_window.mainloop()


# ----------------- PIN LOGIN WINDOW -----------------
pin_window = tk.Tk()
pin_window.title("Login")
pin_window.geometry("300x180")
pin_window.resizable(False, False)

ttk.Label(pin_window, text="Enter 4-digit PIN", font=("Arial", 12)).pack(pady=20)
pin_entry = ttk.Entry(pin_window, show="*", font=("Arial", 14), justify="center")
pin_entry.pack(pady=5)
ttk.Button(pin_window, text="Login", command=verify_pin).pack(pady=10)

pin_window.mainloop()
