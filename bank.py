class BankAccount:
    """Creates a bank account with the information about the owner's name, 
    the balance within the account, and the account number."""

    def __init__(self, name, balance, account_number):

        self.name = name
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        """Takes money out of a bank account and returns the new balance.
        
            If the amount attempted to be withdrawed exceeds the balance within 
            the account, withdrawal doesn't go through."""
        
        if self.balance - amount < 0:
            print("Not enough money in account")
            return self.balance
        else:
            return self.balance - amount
    
    def deposit(self, money):
        if money < 0:
            print("Trying to deposit negative value")
            return self.balance
        else:
            return self.balance + money
    
    def print_current_balance(self):
        current_balance = "The current balance in " + self.name + "'s account is " + self.balance + " dollars."
        print(current_balance)
        return current_balance

    
    def __main__():
        BankAccount()

    if __name__ == "__main__":
        __main__()
