# === All-in-One Bank Management System ===

def main_menu():
    while True:
        print("\n=== Welcome to Bank Management System ===")
        print("1. Banker Menu")
        print("2. Customer Menu")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            banker_menu()
        elif choice == '2':
            customer_menu()
        elif choice == '3':
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.")

def banker_menu():
    while True:
        print("\n--- Banker Menu ---")
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Search Customer")
        print("4. Total Bank Balance")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            add_customer()
        elif choice == '2':
            view_all_customers()
        elif choice == '3':
            search_customer()
        elif choice == '4':
            total_balance()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def add_customer():
    name = input("Enter customer name: ")
    acc_no = input("Enter account number: ")
    balance = input("Enter initial deposit: ")

    with open("customers.txt", "a") as file:
        file.write(f"{name},{acc_no},{balance}\n")

    with open("transactions.log", "a") as log:
        log.write(f"Added: {name}, Acc: {acc_no}, Balance: {balance}\n")

    print("Customer added successfully.")

def view_all_customers():
    print("\n--- All Customers ---")
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                name, acc, bal = line.strip().split(",")
                print(f"Name: {name}, Acc: {acc}, Balance: ₹{bal}")
    except FileNotFoundError:
        print("No customers found.")

def search_customer():
    acc_no = input("Enter account number to search: ")
    found = False
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                name, acc, bal = line.strip().split(",")
                if acc == acc_no:
                    print(f"Customer Found: {name}, Balance: ₹{bal}")
                    found = True
                    break
        if not found:
            print("Customer not found.")
    except FileNotFoundError:
        print("No data available.")

def total_balance():
    total = 0
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                _, _, bal = line.strip().split(",")
                total += float(bal)
        print(f"Total Bank Balance: ₹{total}")
    except FileNotFoundError:
        print("No data to calculate balance.")

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            view_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def view_balance():
    acc_no = input("Enter your account number: ")
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                name, acc, bal = line.strip().split(",")
                if acc == acc_no:
                    print(f"Hello {name}, Your Balance is ₹{bal}")
                    return
        print("Account not found.")
    except FileNotFoundError:
        print("Customer data not found.")

def deposit_money():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    lines = []
    updated = False

    try:
        with open("customers.txt", "r") as file:
            lines = file.readlines()

        with open("customers.txt", "w") as file:
            for line in lines:
                name, acc, bal = line.strip().split(",")
                if acc == acc_no:
                    new_bal = float(bal) + amount
                    file.write(f"{name},{acc},{new_bal}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            with open("transactions.log", "a") as log:
                log.write(f"Deposited ₹{amount} to Acc: {acc_no}\n")
            print("Deposit successful.")
        else:
            print("Account not found.")

    except FileNotFoundError:
        print("Customer data not found.")

def withdraw_money():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    lines = []
    updated = False

    try:
        with open("customers.txt", "r") as file:
            lines = file.readlines()

        with open("customers.txt", "w") as file:
            for line in lines:
                name, acc, bal = line.strip().split(",")
                if acc == acc_no:
                    bal = float(bal)
                    if bal >= amount:
                        new_bal = bal - amount
                        file.write(f"{name},{acc},{new_bal}\n")
                        updated = True
                    else:
                        file.write(line)
                        print("Insufficient balance.")
                        return
                else:
                    file.write(line)

        if updated:
            with open("transactions.log", "a") as log:
                log.write(f"Withdrew ₹{amount} from Acc: {acc_no}\n")
            print("Withdrawal successful.")
        else:
            print("Account not found.")

    except FileNotFoundError:
        print("Customer data not found.")

if __name__ == "__main__":
    main_menu()