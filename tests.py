# Name: Sean Perez
# CS 362: A2
# Date: 4.29.22

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    """TDD implementation"""

    # Empty string
    def test1(self):
        test_pwd = ''
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))

    # Character length equals 7
    def test2(self):
        test_pwd = 'aj7fg45'
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))

    # Character length equals 21
    def test3(self):
        test_pwd = 'aj7fg57fhe7trf74jds92'
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))

    # Character length less than 8
    def test4(self):
        test_pwd = 'aj7f'
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))

    # Character length more than 20
    def test5(self):
        test_pwd = 'aj7fg57fhe7trf74jds92aj7f'
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))

    # Capital letters and numbers only
    def test6(self):
        test_pwd = 'AD2FGH9H8976'
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))

    # Lowercase letters and numbers only
    def test7(self):
        test_pwd = 'as7dfg7639g'
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))

    # Capital and lowercase letters only
    def test8(self):
        test_pwd = 'asdYYfgFGjhDF'
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
