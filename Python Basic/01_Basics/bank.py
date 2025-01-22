class BankAccount:
    def __init__(self):
        self.accnum = ''
        self.name = ''
        self.balance = 0
        self.menu()
    
    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to give account information
        2. Press 2 to deposit amount
        3. Press 3 to withdraw amount
        4. Press 4 to display balance
        5. Anything else to exit
        """)
    
        if user_input == '1':
            self.setval()
        elif user_input == '2':
            self.Deposit()
        elif user_input == '3':
            self.Withdraw()
        elif user_input == '4':
            self.display()
        else:
            exit()
      
    def setval(self):
        self.accnum = input("Enter your account number: ")
        self.name = input("Enter your name: ")
        self.balance = float(input("Enter your balance: "))
        print("\nAccount information added successfully!")
        self.menu()
        
    def Deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)
        print("Balance available:", self.balance)
        self.menu()
        
    def Withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
            print("Balance available:", self.balance)
        else:
            print("\nInsufficient balance")
        
        self.menu()
            
    def display(self):
        print("\nAccount Number:", self.accnum)
        print("Account Holder Name:", self.name)
        print("Net Available Balance:", self.balance)
        self.menu()
        
newAcc = BankAccount()
