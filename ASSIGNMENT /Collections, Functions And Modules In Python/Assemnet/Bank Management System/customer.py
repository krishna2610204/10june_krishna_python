import os
from datetime import datetime

customers_file = "customers.txt"
log_file = "log.txt"

def log_action(action):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {action}\n")

def find_customer(account_number):
    if not os.path.exists(customers_file):
        return None
    with open(customers_file, "r") as f:
        for line in f:
            name, acc, bal = line.strip().split(",")
            if acc == account_number:
                return name, acc, float(bal)
    return None

def view_balance():
    acc = input("Enter your account number: ").strip()
    data = find_customer(acc)
    if data:
        name, acc, bal = data
        print(f"👤 Name: {name}, 💰 Balance: ₹{bal}")
        log_action(f"{name} viewed balance")
    else:
        print("❌ Account not found.")

def deposit_money():
    acc = input("Enter your account number: ").strip()
    data = find_customer(acc)
    if data:
        name, account, balance = data
        amount = float(input("Enter amount to deposit: "))
        new_balance = balance + amount
        lines = []
        with open(customers_file, "r") as f:
            for line in f:
                n, a, b = line.strip().split(",")
                if a == acc:
                    lines.append(f"{n},{a},{new_balance}\n")
                else:
                    lines.append(line)
        with open(customers_file, "w") as f:
            f.writelines(lines)
        print("✅ Deposit successful.")
        log_action(f"{name} deposited ₹{amount}")
    else:
        print("❌ Account not found.")

def withdraw_money():
    acc = input("Enter your account number: ").strip()
    data = find_customer(acc)
    if data:
        name, account, balance = data
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("❌ Insufficient funds.")
            return
        new_balance = balance - amount
        lines = []
        with open(customers_file, "r") as f:
            for line in f:
                n, a, b = line.strip().split(",")
                if a == acc:
                    lines.append(f"{n},{a},{new_balance}\n")
                else:
                    lines.append(line)
        with open(customers_file, "w") as f:
            f.writelines(lines)
        print("✅ Withdrawal successful.")
        log_action(f"{name} withdrew ₹{amount}")
    else:
        print("❌ Account not found.")

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Back to Main Menu")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            view_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            break
        else:
            print("❌ Invalid input. Please choose between 1 to 4.")
