class BankSystem:
    def __init__(self):
        id = 0
        self.customers_list = []
        self.customer = {}
        self.id = id

    
    def create_account(self):
        self.id += 1
        self.first_name, self.last_name = self.get_name()
        self.initial_deposit = BankSystem.get_initial_deposit()
        self.customer[id] = id
        self.customer["First Name"] = self.first_name
        self.customer["Last Name"] = self.last_name
        self.customer["Balance"] = self.balance()
        self.customers_list.append(self.customer)



    def get_name(self):
        first_name = input("Enter Your first name: ")
        last_name = input("Enter your last name: ")
        return first_name, last_name
    
    def get_initial_deposit():
        initial_deposit = eval(input("What is the initial deposit? "))
        return initial_deposit
    
    def balance(self):
        return self.balance


    
bank_system = BankSystem()
bank_system.create_account()
print(bank_system.id)
print(bank_system.first_name)
print(bank_system.last_name)
print(bank_system.initial_deposit)


    
