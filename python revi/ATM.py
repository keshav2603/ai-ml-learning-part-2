import os
import random
class ATM:
    def __init__(self):
        self.current_account = None
        self.authenticated = False
        if not os.path.exists("data.txt"):
        # Create the file if it does not exist
            with open("data.txt", 'w') as file:
                file.write('')

    def generate_pin(self):
        return random.randint(1000, 9999)

    def create_account(self):
        firstName = input("Enter your first Name:\n")
        lastName = input("enter your last Name:\n")
        initial_balance= int(input("enter your initial balance:\n"))
        pin = self.generate_pin()
        self.current_account = Account(firstName, lastName, initial_balance, pin)
        self.authenticated = True
        with open("data.txt", "a") as data:
            data.write(f"{self.current_account.get_account_number()[1]},{firstName} {lastName},{self.current_account.get_balance()[1]},{pin}\n")
        print("your account has been created successfully:")
        print(f"your account number:  {self.current_account.get_account_number()[1]}")
        print(f"your initial balance: ${self.current_account.get_balance()[1]}")
        print(f"your pin is : {pin}")

    def deposit_money(self, amount):
        if not self.authenticated:
            return (False, None, "You are not authenticated")
    
        success, new_balance, message = self.current_account.deposit(amount)

        if success:
            self.update_data(new_balance)

            print("Deposit successful! New balance:", new_balance)
        else:
            print("Deposit failed:", message)
    
    
    def withdraw_money(self, amount):
        if not self.authenticated:
            return (False, None, "You are not authenticated")

        success, new_balance, message = self.current_account.withdraw(amount)

        if success:
            self.update_data(new_balance)

            print("withDraw successful! New balance:", new_balance)
        else:
            print("withdraw failed:", message) 

    def update_data(self, new_balance):
        with open("data.txt", "r") as data:
                lines = data.readlines()
        
        modified_lines = []
        account_number_str = str(self.current_account.get_account_number()[1])  # Ensure this is a string
        for line in lines:
            accountNumber = line[0:4].strip()  # Strip any extra spaces/newlines
            if accountNumber == account_number_str:  # Compare as strings                 
                splitedLine = line.strip().split(",")
                modified_line = f"{accountNumber},{splitedLine[1]},{new_balance},{splitedLine[3]}\n"  # Add newline
                modified_lines.append(modified_line)
            else:
                modified_lines.append(line)  # Keep the original line if no match
            # Write the modified lines back to the file
        with open("data.txt", "w") as data:
            data.writelines(modified_lines)

    #incase already have an account
    def verify_pin(self, pin, account_number):
        with open("data.txt", "r") as data:
            lines = data.readlines()

        for line in lines:
            account_number_db = line[0:4].strip() 
            if account_number_db:  # Ensure it's not empty
                if account_number == int(account_number_db):  # Ensure the account number is matched
                    split_line = line.split(",")
                    pin_db = int(split_line[3].strip())  # Convert pin_db to int and strip whitespace
                
                    print(f"Comparing PIN: user={pin}, db={pin_db}")  # Debugging line

                    if pin == pin_db:  # Compare as integers
                    # Create the Account object and assign it to current_account
                        self.current_account = Account(
                            split_line[1].split()[0],  # First name
                            split_line[1].split()[1],  # Last name
                            int(split_line[2]),        # Balance
                            pin                        # Pin
                        )
                        self.authenticated = True
                        print("You have access to your account.")
                        return (True, self.current_account, "Authentication successful")

        print("Invalid PIN or account number not found.")
        return (False, None, "Invalid PIN or account number not found")

class Account:
    accountNumberCounter =1000
    def __init__(self, firstName, lastName, balance, pin):
        self.firstName = firstName
        self.lastName = lastName
        self.__balance = balance
        self.__pin = pin
        self.__accountNumber = Account.accountNumberCounter
        Account.accountNumberCounter +=1

    def get_balance(self):
        return (True, self.__balance, "")
    
    def get_account_number(self):
        return (True, self.__accountNumber, "")

    def deposit(self, amount):
        if(amount<=0):
            return (False, self.__balance, "Invalid amount")
        else:
            self.__balance +=amount
            return (True, self.__balance, "amount deposit successful")

    def withdraw(self,amount):
        if(amount<=0):
            return (False, self.__balance, "Invalid amount")
        
        elif(amount>self.__balance):
            return (False, self.__balance, "Insufficient balance")
        else:
            self.__balance -=amount
            return (True, self.__balance, "amount withdraw successful")




