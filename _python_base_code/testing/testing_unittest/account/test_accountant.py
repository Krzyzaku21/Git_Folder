import  unittest
from accountant import Accountant

class TestAccountant(unittest.TestCase):

# a == b or a !=b
# assertEqual(a, b) or assertNotEqual(a, b)
# x is True or x is False
# assertTrue(x) or assertFalse(x)
# veryfity an item is in list or not in list
#assertIn(item, list) or assertNotIn(item, list)

    def setUp(self):
        self.acc = Accountant()

    #default balance shood be 0
    def test_initial_balance(self):
        self.assertEqual(self.acc.balance, 0)
    #non-default balance
        acc = Accountant(100)
        self.assertEqual(acc.balance, 100)
    #test depsit
    def  test_deposit(self):
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 100)
    #test multiple deposit
        self.acc.deposit(100)
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 300)

    def test_withdrawal(self):
        self.acc.deposit(1000)
        self.acc.withdraw(100)
        self.assertEqual(self.acc.balance, 900) #if you change 900 to 800 -> AssertionError: 900 != 800

if __name__ == '__main__':
    unittest.main()