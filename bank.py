class BankAccount:
    """Creates a bank account with the information about the owner's name, 
    the balance within the account, and the account number."""

    def __init__(self, name, balance, account_number):

        self.name = name
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        """Takes money out of a bank account.
        
            If the amount attempting to be withdrawed exceeds the balance within 
            the account or the amount is negative, withdrawal doesn't go through."""
        if amount < 0 or self.balance - amount < 0:
            #raise(ValueError, "Insufficient balance.") #if we raise errors, must catch it
            return False
        self.balance -= amount
        return True
    
    def deposit(self, amount):
        """Adds money into a bank account.
        
            If the amount attempting to be deposited is negative, deposit 
            doesn't go through."""
        if amount < 0:
            return False
        self.balance += amount
        return True
    
    def print_current_balance(self):
        """Prints the balance in the bank account."""
        print(self.balance)
        return self.balance

    def __main__():
        BankAccount()

    if __name__ == "__main__":
        __main__()
