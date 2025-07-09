import unittest
from bank import BankAccount

account1 = BankAccount("Alicia", 100, 123456)

class TestBankAccount(unittest.TestCase):

    def test_withdraw(self):
        self.assertEqual(account1.withdraw(50), 50)
        self.assertEqual(account1.withdraw(100), 0)
        self.assertEqual(account1.withdraw(200), 100) #attempting to withdraw more than the available amount
        self.assertNotEqual(account1.withdraw(20), 20) #should be 80

    def test_deposit(self):
        self.assertEqual(account1.deposit(50), 150)
        self.assertEqual(account1.deposit(100), 200)
        self.assertEqual(account1.deposit(-50), 100) #attempting to deposit negative amount
        self.assertNotEqual(account1.deposit(40), 200) #should be 140

    
    def test_print_current_balance(self):
        self.assertEqual(account1.print_current_balance(), "The current balance in Alicia's account is 100 dollars.")
        self.assertNotEqual(account1.print_current_balance(), "The current balance in Alicia's account is 50 dollars.")


if __name__ == "__main__":
    unittest.main()
