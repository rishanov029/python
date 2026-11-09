class Bank:
    def __init__(self, acc_no, name, account_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.account_type = account_type
        self.bal = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        else:
            self.bal += amount
            print("Your current balance is", self.bal)

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > self.bal:
            print("Insufficient balance.")
        else:
            self.bal -= amount
            print("Your current balance is", self.bal)

    def display(self):
        print(f"Account number: {self.acc_no}")
        print(f"Account holder: {self.name}")
        print(f"Account type: {self.account_type}")
        print(f"Current balance: {self.bal}")


def main():
    acc_no = int(input("Enter the account number: "))
    name = input("Enter your name: ")
    account_type = input("Enter the account type: ")
    balance = int(input("Enter your balance: "))
    account = Bank(acc_no, name, account_type, balance)

    while True:
        print("\n1) Deposit\n2) Withdraw\n3) Account information\n4) Exit")
        option = int(input("Enter the option: "))

        if option == 1:
            amount = int(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif option == 2:
            amount = int(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif option == 3:
            account.display()
        elif option == 4:
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
