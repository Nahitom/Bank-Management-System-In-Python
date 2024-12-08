import sys

class BankSystem:
    def __init__(self):
        self.id = 0
        self.balance = 0
        self.customers_list = []
        self.customer = {}

    
    def create_account(self):
        self.id += 1
        self.first_name, self.last_name = self.get_name()
        self.initial_deposit = self.get_initial_deposit()
        self.balance += self.initial_deposit
        self.customer["Id"] = self.id
        self.customer["First Name"] = self.first_name
        self.customer["Last Name"] = self.last_name
        self.customer["Balance"] = self.balance
        self.customers_list.append(self.customer)


    def get_name(self):
        first_name = input("Enter Your first name: ")
        last_name = input("Enter your last name: ")
        return first_name, last_name
    
    def get_initial_deposit(self):
        initial_deposit = float(input("What is the initial deposit? "))
        return initial_deposit
    
    def get_deposit_amount(self):
        self.deposit_amount = float(input("Enter money to be deposited: "))
        return self.deposit_amount

    def get_withdraw_amount(self):
        self.withdraw_amount = float(input("Enter amount to be withdrawn: "))
        return self.withdraw_amount

    def withdraw(self):
        self.balance -= self.get_withdraw_amount()

    def deposit(self):
        deposit_amount = self.get_deposit_amount()
        self.balance += deposit_amount

        
    def display_balance(self):
        self.customer["Balance"] = self.balance
        return self.balance


    def main(self):
        print("Hello, this is a simple banking system, please read the following instructions to continue to our system...\n")
        create_account = input("Enter any key to create account or '0' to quit: ")

        if create_account == "0":
            sys.exit()
        else:
            self.create_account()
            print("\nYou have successfully created an account.")

        while True:

            print("\n1: To create account")
            print("2: To deposit money")
            print("3: To withdraw money")
            print("4: To transfer money")
            print("5: To check balance")
            print("0 to quit\n")


            choice = int(input("Enter your choice: "))
            if choice == 0:
                break

            match(choice):
                case 1:
                    self.create_account()
                    print("You have successfully created an account.")
                case 2:
                    self.deposit()
                    print(f"You have successfully deposited {str(self.deposit_amount)} to your account. Your new balance is {str(self.display_balance())}.")

                case 3:
                    self.withdraw()
                    print(f"You have successfully withdrawn {str(self.withdraw_amount)} from your account. Your new balance is {str(self.display_balance())}")

                case 4:
                    self.transfer()
                    break
                case 5:
                    print(f"Your balance is {self.display_balance()}")
                case _:
                    print("Invalid input. Please try again! ")

    
bank_system = BankSystem()
bank_system.main()
# print(bank_system.id)
# print(bank_system.first_name)
# print(bank_system.last_name)
# print(bank_system.initial_deposit)
# print(bank_system.customers_list[0])


    
