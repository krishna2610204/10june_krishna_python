import os
from datetime import datetime

customers_file = "customers.txt"
log_file = "log.txt"

def log_action(action):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {action}\n")

def add_customer():
    try:
        name = input("Enter customer name: ").strip()
        account = input("Enter account number: ").strip()
        balance = float(input("Enter initial balance: ").strip())
        with open(customers_file, "a") as f:
            f.write(f"{name},{account},{balance}\n")
        log_action(f"Added customer {name} with account {account}")
        print("✅ Customer added successfully.")
    except:
        print("❌ Error in input! Please try again.")
        add_customer()

def view_customers():
    try:
        if not os.path.exists(customers_file):
            print("❌ No customer records found.")
            return
        print("\n📋 Customer List:")
        with open(customers_file, "r") as f:
            for line in f:
                name, acc, bal = line.strip().split(",")
                print(f"Name: {name}, Account: {acc}, Balance: ₹{bal}")
        log_action("Viewed all customers")
    except:
        print("❌ Error displaying customers.")

def search_customer():
    try:
        acc = input("Enter account number to search: ").strip()
        found = False
        with open(customers_file, "r") as f:
            for line in f:
                name, a, bal = line.strip().split(",")
                if a == acc:
                    print(f"✅ Found: Name: {name}, Balance: ₹{bal}")
                    found = True
                    log_action(f"Searched and found account {acc}")
                    break
        if not found:
            print("❌ Customer not found.")
            log_action(f"Searched account {acc} - Not found")
    except:
        print("❌ Error in search.")

def total_amount():
    try:
        total = 0
        with open(customers_file, "r") as f:
            for line in f:
                _, _, bal = line.strip().split(",")
                total += float(bal)
        print(f"💰 Total bank balance: ₹{total}")
        log_action("Checked total bank amount")
    except:
        print("❌ Could not calculate total amount.")

def banker_menu():
    while True:
        print("\n--- Banker Menu ---")
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Search Customer")
        print("4. Total Amount in Bank")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            search_customer()
        elif choice == '4':
            total_amount()
        elif choice == '5':
            break
        else:
            print("Invalid input! Please enter 1 to 5.")
