class Account_Opening:
    no : int
    name : str
    Acc_Type : str

    def Account_Open(self):
        self.no = input("Enter your Account NUmber:")
        self.name = input("Enter your Name:")
        self.Acc_Type = input("Enter your Account type Savings / Current:")

class deposite(Account_Opening):
    bal:int = 0

    def Amount(self):
        self.bal = int(input("Enter your Balance: "))
        if self.bal < 2000:
            print("Insufficient Balance")
        else:
            print("Sufficient Balance")

class withdrwal(deposite):
    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.bal:
            print("Insufficient funds for withdrawal")
        else:
            self.bal -= amount
            print(f"Withdrawal successful! Remaining balance: {self.bal}")

class statement(withdrwal):
   def show(self):
       print("Account Number:",self.no)
       print("Account Holder Name:",self.name)
       print("Account Type:",self.Acc_Type)
       print("Total Balance:",self.bal)

w = statement()
w.Account_Open()
w.Amount()      
w.withdraw()    
w.show() 