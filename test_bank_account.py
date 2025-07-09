import unittest
from bank import BankAccount


class TestBankAccount(unittest.TestCase):
    
    def test_withdraw(self):
        """Tests the withdraw method in the BankAccount class.
        
            Checks if withdrawing a valid amount results in expected balance. Attempts 
            to withdraw an amount larger than current balance and checks if balance 
            remains the same. Attempts to withdraw a negative value and checks if balance
            remains the same."""
        account1 = BankAccount("Alicia", 100, 123456)
        account1.withdraw(17)
        self.assertEqual(account1.balance, 83)
        account1.withdraw(200) #attempting to withdraw more than amount in account
        self.assertEqual(account1.balance, 83)
        account1.withdraw(-10) #attempting to withdraw negative account
        self.assertEqual(account1.balance, 83) 
        account1.withdraw(20)
        self.assertNotEqual(account1.balance, 20) #balance should be 63 not 20

    def test_deposit(self):
        """Tests the deposit method in the BankAccount class.
        
            Checks if depositing a valid amount results in expected balance. Attempts 
            to withdraw an amount larger than current balance and checks if balance 
            remains the same."""
        account1 = BankAccount("Alicia", 100, 123456)
        account1.deposit(50)
        self.assertEqual(account1.balance, 150)
        account1.deposit(100)
        self.assertEqual(account1.balance, 250)
        account1.deposit(-90) #attempting to deposit negative amount
        self.assertEqual(account1.balance, 250)
        account1.deposit(40)
        self.assertNotEqual(account1.balance, 200) #should be 290

    
    def test_print_current_balance(self):
        """Tests the print_current_balance method in the BankAccount class."""
        account1 = BankAccount("Alicia", 100, 123456)
        self.assertEqual(account1.print_current_balance(), 100)
        self.assertNotEqual(account1.print_current_balance(), 478)


if __name__ == "__main__":
    unittest.main()
