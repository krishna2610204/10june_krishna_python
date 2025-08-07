from user import User

class Customer(User):
    def __init__(self, user_id, name, email, password, balance=0.0):
        super().__init__(user_id, name, email, password)
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return False
        self.__balance -= amount
        return True
