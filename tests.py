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
