from datetime import datetime

class BankAccount:
    def __init__(self,username,password):
        self.__transaction=[]
        self.username=username
        self.__password=password
        self.__balance=0
        print(f'Your account has been created successfully,{self.username} ')

    def check_password(self,password):
        return self.__password==password

    def deposit(self,amount):
        if amount <=0:
            print('Amount must be positive. ')
        else:
            self.__balance+=amount
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.__transaction.append(f'[{timestamp}] Deposit: {amount}$')
            print(f'Dear {self.username},An amount of {amount}$ has been deposited successfully. ')
    def withdraw(self,amount):
        if amount <=0:
            print('Amount must be positive. ')
        elif amount > self.__balance:
            print("Insufficient funds!! ")
        else:
            self.__balance-=amount
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.__transaction.append(f'[{timestamp}] Withdraw: {amount}$')
            print(f'Dear {self.username}, An amount of {amount}$ has been withdrawn from your account. ')

    def check_balance(self):
        print(f'Your balance is {self.__balance}$')

    def transaction_history(self):
        print(f'Transaction history for {self.username}.')
        if not self.__transaction:
            print("No transaction yet.")
        else:
            for i,t in enumerate(self.__transaction,start=1):
                print(f'{i}. {t}')

class BankSystem:
    def __init__(self):
        self.accounts={}

    def create_account(self,username,password):
        if username in self.accounts:
            print('Username already exist,try some other. ')
        else:
            self.accounts[username]=BankAccount(username, password)

    def login(self,username,password):
        account=self.accounts.get(username)
        if account and account.check_password(password):
            print(f'Welcome, {username}')
            self.account_menu(account)
        else:
            print('Invalid Username and password! ')

    def account_menu(self,account):
        while True:
            print('--- Account Menu --- ')
            print('1. Check Balance ')
            print('2. Deposit ')
            print('3. Withdraw ')
            print('4. Transaction History')
            print('5. Exit ')
            choice=input('Enter your choice: ')

            if choice == '1':
                account.check_balance()
            elif choice== '2':
                amount=float(input("Enter the amount: "))
                account.deposit(amount)
            elif choice == '3':
                amount=float(input('Enter the amount: '))
                account.withdraw(amount)
            elif choice == '4':
                account.transaction_history()
            elif choice == '5':
                print('Logging Out....')
                break
            else:
                print('Invalid Choice ')


def main():
    bank = BankSystem()
    while True:
         print('--- Bank System Menu ---')
         print('1. Create Account')
         print('2. Login')
         print('3. Exit')
         choice= input('Enter the choice: ')
         if choice == '1':
            username=input('Choose the Username: ')
            password=input('Choose the password: ')
            bank.create_account(username, password)

         elif choice == '2':
            username= input('Enter the Username: ')
            password= input('Enter password: ')
            bank.login(username, password)

         elif choice == '3':
            print('Exiting from System...')
            break
         else:
             print("Invalid Choice---Try Again.")



if __name__ == '__main__':
    main()

