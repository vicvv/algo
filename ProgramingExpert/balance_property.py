class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    # Write your code here
    @property
    def balance(self):
        return round(self._balance)
    
    @balance.setter
    def balance(self, balance):
        if isinstance (balance, float) and 100000 >  balance > 0 :
            self._balance = balance
        else:
            self._balance = 0


import unittest

class TestProgram(unittest.TestCase):
    # def test_case_1(self):
    #     self.assertTrue(inspect.isclass(BankAccount), "BankAccount should be a class.")

    def test_case_2(self):
        account = BankAccount("Tim")
        self.assertTrue(hasattr(account, "balance"), "A BankAccount should have a `balance` attribute.")

    def test_case_3(self):
        account = BankAccount("Tim")
        self.assertEqual(0, account.balance)

    def test_case_4(self):
        account = BankAccount("Clement")
        account.balance = -1
        self.assertEqual(0, account.balance)
        account.balance = "1.0"
        self.assertEqual(0, account.balance)
        account.balance = 100001
        self.assertEqual(0, account.balance)

    def test_case_5(self):
        account = BankAccount("Antoine")
        account.balance = 56.2
        self.assertEqual(56, account.balance)
        account.balance = 56.6
        self.assertEqual(57, account.balance)



if __name__ == "__main__":
    unittest.main()