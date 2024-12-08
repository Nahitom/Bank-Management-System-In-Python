import sys

class BankSystem:
    def __init__(self):
        self.id = 0
        self.balance = 0
        self.customers_list = {}
        self.customer = {}
        self.user_id = 0

    
    def create_account(self):
        self.balance = 0
        self.id += 1
        self.first_name, self.last_name = self.get_name()
        self.initial_deposit = self.get_initial_deposit()
        self.balance += self.initial_deposit

        customer = {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Balance": self.balance }
        self.customers_list[self.id] = customer

    def get_id(self):
        self.id = int(input("What's your ID? "))
        return self.id

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

    def withdraw(self, user_id):
        user_id = self.get_id()
        if user_id in self.customers_list:
            withdraw_amount = self.get_withdraw_amount()
            self.customers_list[user_id]["Balance"] -= withdraw_amount
            print(f"You have successfully withdrawn {str(self.withdraw_amount)} from your account. Your new balance is {str(self.customers_list[user_id]['Balance'])}.")


    def deposit(self, user_id):
        user_id = self.get_id()
        if user_id in self.customers_list:
            deposit_amount = self.get_deposit_amount()
            self.customers_list[user_id]["Balance"] += deposit_amount
            print(f"You have successfully deposited {str(self.deposit_amount)} to your account. Your new balance is {str(self.customers_list[user_id]['Balance'])}.")

        
    def display_balance(self, user_id):
        user_id = self.get_id()
        if user_id in self.customers_list:
            return self.customers_list[user_id]["Balance"]


    def main(self):
        print("Hello, this is a simple banking system, please read the following instructions to continue to our system...\n")
        create_account = input("Enter any key to create account or '0' to quit: ")

        if create_account == "0":
            print("\nExiting...\n")
            sys.exit()
        else:
            self.create_account()
            print(f"\nYou have successfully created an account. And your ID is {self.id}.")

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
                    print(f"You have successfully created an account.Your ID is {self.id}")
                case 2:
                    self.deposit(self.id)

                case 3:
                    self.withdraw(self.id)

                case 4:
                    self.transfer()
                    break
                case 5:
                    print(f"Your balance is {self.display_balance(self.id)}")
                case _:
                    print("Invalid input. Please try again! ")

    
bank_system = BankSystem()
bank_system.main()
# print(bank_system.id)
# print(bank_system.first_name)
# print(bank_system.last_name)
# print(bank_system.initial_deposit)
print(bank_system.customers_list[1])
print(bank_system.customers_list[2])



    
