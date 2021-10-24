class Bank:
    def __init__(self, full_name, acc_number,balance):
        self.Name = full_name 
        self.AccNumber = acc_number
        self.Balance = balance

    def deposit(self, amount):
        self.Balance = amount + self.Balance
        print(f'Amount Deposited: ${amount}')

    def withdraw(self, amount):
        if amount > self.Balance:
            self.Balance = self.Balance - amount
            print('Insufficient Funds')
            self.Balance = self.Balance - 10
            print(f'Amount Withdrawn ${amount}')
        else:
            self.Balance = self.Balance - amount
            print(f'Amount Withdrawn ${amount}')
    
    def get_balance(self):
        print(f'{self.Name}. Your account balance is ${self.Balance}')
    
    def add_interest(self):
        interest = self.Balance * 0.00083
        self.Balance = self.Balance + interest
        return self.Balance

    def statement(self):
        crypto = '****'
        print(self.Name)
        print(f'Account No:{crypto + self.AccNumber[4:9]}')
        print(f'Balance: ${self.Balance}')



#3 bank accounts
Nathan= Bank('Nathan Lua', '87654321', 400)
Alex = Bank('Alex Aguayo', '91254321', 60)
Jacob = Bank('Jacob Aguayo', '12344321', 34)

#6

Mitchell = Bank('Mitchell Hudson', '03141592', 400000)

Mitchell.statement()
Mitchell.add_interest()
Mitchell.statement()
Mitchell.add_interest()
Mitchell.statement()
Mitchell.withdraw(150)
Mitchell.statement()


    

    