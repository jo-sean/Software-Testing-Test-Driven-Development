# Name: Sean Perez
# CS 362: A2
# Date: 4.29.22

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    """TDD implementation"""

    def test1(self):
        test_pwd = ''
        self.assertFalse(check_pwd(test_pwd),
                         msg=''.format(check_pwd(test_pwd)))

