class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
        self.card_number = float(int(input("Pls Provide Your Card Number : ")))
        self.pin_number = float(int(input("Pls Provide Your Pin Number : ")))

    def deposit(self):
        amount = float(int(input("Enter The Amount To Be Deposited : ")))
        self.balance += amount
        print("\n Amount Deposited:",amount)
    
    def withdrawal(self):
        amount = float(int(input("Enter The Amount To Be Withdrawn : ")))
        if(self.balance >= amount):
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ") 

    def display(self):
        print("\n Net Available Balance=",self.balance) 


MyBankAccount = Bank_Account()

MyBankAccount.deposit()
MyBankAccount.withdrawal()
MyBankAccount.display()
