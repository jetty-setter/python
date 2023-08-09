import unittest
from account import *


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = Account('Checking')
        self.account2 = Account('Savings')

    def tearDown(self):
        del self.account1
        del self.account2

    def test_init(self):
        self.assertEqual(self.account1.get_name(), 'Checking')
        self.assertEqual(self.account1.get_balance(), 0)
        self.assertEqual(self.account2.get_name(), 'Savings')
        self.assertEqual(self.account2.get_balance(), 0)

    def test_deposit(self):
        assert self.account1.deposit(100.0) is True
        self.assertEqual(self.account1.get_balance(), 100.0)
        assert self.account2.deposit(0) is False
        self.assertEqual(self.account2.get_balance(), 0)
        assert self.account1.deposit(-25.0) is False
        self.assertEqual(self.account1.get_balance(), 100.0)

    def test_withdraw(self):
        assert self.account1.deposit(100.0) is True
        assert self.account1.withdraw(25.0) is True
        self.assertEqual(self.account1.get_balance(), 75.0)
        assert self.account1.withdraw(100.0) is False
        self.assertEqual(self.account1.get_balance(), 75.0)
        assert self.account2.withdraw(-100) is False
        self.assertEqual(self.account2.get_balance(), 0)


if __name__ == '__main__':
    unittest.main()
