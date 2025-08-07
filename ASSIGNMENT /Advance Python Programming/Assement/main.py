from operation import (
    register_customer,
    login_customer,
    deposit_amount,
    withdraw_amount,
    view_balance
)

def customer_actions(customer):
    while True:
        print("\n👤 Customer Dashboard")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            deposit_amount(customer)
        elif choice == '2':
            withdraw_amount(customer)
        elif choice == '3':
            view_balance(customer)
        elif choice == '4':
            print("👋 Logged out successfully.")
            break
        else:
            print("❌ Invalid option. Please try again.")

def customer_menu():
    while True:
        print("\n📋 Customer Menu")
        print("1. Register")
        print("2. Login")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_customer()
        elif choice == '2':
            customer = login_customer()
            if customer:
                customer_actions(customer)
        elif choice == '3':
            break
        else:
            print("❌ Invalid input. Try again.")

def main_menu():
    while True:
        print("\n🏦 Welcome to Python Bank")
        print("1. Customer Section")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_menu()
        elif choice == '2':
            print("👋 Thank you for using Python Bank!")
            break
        else:
            print("❌ Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()
