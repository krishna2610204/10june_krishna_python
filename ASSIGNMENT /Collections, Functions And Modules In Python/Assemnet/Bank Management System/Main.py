from banker import banker_menu
from customer import customer_menu

def main_menu():
    while True:
        print("\n==== Bank Management Console ====")
        print("1. Banker")
        print("2. Customer")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            banker_menu()
        elif choice == '2':
            customer_menu()
        elif choice == '3':
            print("Thank you for using Bank Management System!")
            break
        else:
            print("Invalid input! Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main_menu()
