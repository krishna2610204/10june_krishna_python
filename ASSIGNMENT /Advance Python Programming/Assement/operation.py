from db import get_connection
from customer import Customer
import getpass

def register_customer():
    name = input("Enter Customer Name: ").strip()
    email = input("Enter Email: ").strip()
    password = getpass.getpass("Enter Password: ").strip()

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO customers (name, email, password, balance) VALUES (%s, %s, %s, %s)",
                    (name, email, password, 0.0))
        conn.commit()
        print("✅ Customer Registered Successfully!")
    except Exception as e:
        print("❌ Registration Failed:", e)
    finally:
        cur.close()
        conn.close()

def login_customer():
    email = input("Enter Email: ").strip()
    password = getpass.getpass("Enter Password: ").strip()

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM customers WHERE email=%s AND password=%s", (email, password))
        row = cur.fetchone()
        if row:
            customer = Customer(row[0], row[1], row[2], row[3], row[4])
            print(f"✅ Welcome {customer.name}!")
            return customer
        else:
            print("❌ Invalid email or password.")
            return None
    except Exception as e:
        print("❌ Login error:", e)
        return None
    finally:
        cur.close()
        conn.close()

def deposit_amount(customer):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("❌ Please enter a positive amount.")
            return

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE customers SET balance = balance + %s WHERE id = %s", (amount, customer.user_id))
        conn.commit()
        print(f"✅ ₹{amount} deposited successfully.")
    except Exception as e:
        print("❌ Deposit failed:", e)
    finally:
        cur.close()
        conn.close()

def withdraw_amount(customer):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("❌ Please enter a positive amount.")
            return

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customers WHERE id = %s", (customer.user_id,))
        balance = cur.fetchone()[0]

        if amount > balance:
            print("❌ Insufficient funds.")
        else:
            cur.execute("UPDATE customers SET balance = balance - %s WHERE id = %s", (amount, customer.user_id))
            conn.commit()
            print(f"✅ ₹{amount} withdrawn successfully.")
    except Exception as e:
        print("❌ Withdrawal failed:", e)
    finally:
        cur.close()
        conn.close()

def view_balance(customer):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customers WHERE id = %s", (customer.user_id,))
        balance = cur.fetchone()[0]
        print(f"💰 Your current balance is: ₹{balance}")
    except Exception as e:
        print("❌ Failed to fetch balance:", e)
    finally:
        cur.close()
        conn.close()
