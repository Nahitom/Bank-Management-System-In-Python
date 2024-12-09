import sys

class BankSystem:
    def __init__(self):
        self.id = 0
        self.balance = 0
        self.customers_list = {}
        self.customer = {}
        self.user_id = 0
        self.from_id = 0
        self.target_id = 0
        self.transfer_amount = 0

    
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

    def get_id(self, prompt="What's your ID? "):
        while True:
            try:
                self.user_id = int(input(prompt))
                return self.user_id
            except ValueError:
                print("Invalid Input! Please try again.")
            except KeyboardInterrupt:
                print("\nClosing...", flush=True)
                sys.exit()

    def get_name(self):
        try:
            while True:
                first_name = input("Enter Your first name: ").strip()
                if first_name:
                    break
                else:
                    print("Invalid input! Please enter your first name correctly.")
            while True:
                last_name = input("Enter your last name: ").strip()
                if last_name:
                    break
                else:
                    print("Invalid input! Please enter your last name correctly.")
            return first_name, last_name
        except KeyboardInterrupt:
                print("\nClosing...", flush=True)
                sys.exit()
    
    def get_initial_deposit(self):
        while True:
            try:
                initial_deposit = float(input("What is the initial deposit? "))
                return initial_deposit
            except ValueError:
                print("Invalid Input! Please try again.")
            except KeyboardInterrupt:
                print("\nClosing...", flush=True)
                sys.exit()
    
    def get_deposit_amount(self):
        while True:
            try:
                self.deposit_amount = float(input("Enter money to be deposited: "))
                return self.deposit_amount
            except ValueError:
                print("Invalid Input! Please try again.")
            except KeyboardInterrupt:
                print("\nClosing...", flush=True)
                sys.exit()

    def get_withdraw_amount(self):
        while True:
            try:
                self.withdraw_amount = float(input("Enter amount to be withdrawn: "))
                return self.withdraw_amount
            except ValueError:
                print("Invalid Input! Please try again.")
            except KeyboardInterrupt:
                print("\nClosing...", flush=True)
                sys.exit()

    def get_transfer_amount(self):
        while True:
            try:
                self.transfer_amount = float(input("Enter the amount you wish to transfer: "))
                return self.transfer_amount
            except ValueError:
                print("Invalid Input! Please try again.")
            except KeyboardInterrupt:
                print("\nClosing...", flush=True)
                sys.exit()

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
        else:
            print("ID not found.")

    def transfer(self, from_id, target_id):
        from_id = self.get_id()
        target_id = self.get_id("Enter the ID you wish to transfer: ")

        if from_id in self.customers_list and target_id in self.customers_list:
            transfer_amount = self.get_transfer_amount()
            self.customers_list[from_id]["Balance"] -= transfer_amount
            self.customers_list[target_id]["Balance"] += transfer_amount
        print(f"You have successfully transferred {str(self.transfer_amount)} to {self.customers_list[target_id]['First Name']}.")

        
    def display_balance(self, user_id):
        user_id = self.get_id()
        if user_id in self.customers_list:
            return self.customers_list[user_id]["Balance"]


def main():
    print("Hello, this is a simple banking system, please read the following instructions to continue to our system...\n")
    try:
        create_account = input("Enter any key to create account or '0' to quit: ")

        if create_account == "0":
            print("\nExiting...\n", flush=True)
            sys.exit()
        else:
            bank_system.create_account()
            print(f"\nYou have successfully created an account. And your ID is {bank_system.id}.")
    except KeyboardInterrupt:
        print("\nClosing...", flush=True)
        sys.exit()


    while True:

        print("\n1: To create account")
        print("2: To deposit money")
        print("3: To withdraw money")
        print("4: To transfer money")
        print("5: To check balance")
        print("6: To display all custumers' informations")
        print("0 to quit\n")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                break

            match(choice):
                case 1:
                    bank_system.create_account()
                    print(f"You have successfully created an account.Your ID is {bank_system.id}")
                case 2:
                    bank_system.deposit(bank_system.id)
                case 3:
                    bank_system.withdraw(bank_system.id)
                case 4:
                    bank_system.transfer(bank_system.from_id, bank_system.target_id)
                    print("Success!")
                case 5:
                    print(f"Your balance is {bank_system.display_balance(bank_system.id)}")
                case 6:
                    for id in bank_system.customers_list:
                        print(f'ID: {id}\nFirst Name: {bank_system.customers_list[id]["First Name"]}\nLast Name: {bank_system.customers_list[id]["Last Name"]}\nBalance: {bank_system.customers_list[id]["Balance"]}')
                case _:
                    print("Please chose one from the above alternatives: ")
        except ValueError:
            print("Invalid input. Please try again! ")
        except KeyboardInterrupt:
                print("\nClosing...", flush=True)
                sys.exit()
    
bank_system = BankSystem()

if __name__ == "__main__":
    main()



    
