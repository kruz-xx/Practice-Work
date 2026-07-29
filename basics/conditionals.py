class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
            
    def show_balance(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance}")
        
if __name__ == "__main__":
    acc = BankAccount("123456789", "John Doe", 1000)
    acc.show_balance()
    acc.deposit(500)
    acc.withdraw(200)
    
        
