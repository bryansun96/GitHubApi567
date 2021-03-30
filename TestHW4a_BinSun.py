""" author: Bin Sun
These are the test cases
"""
import unittest
from HW4a_BinSun import *
from unittest.mock import MagicMock, patch


class TestHW4a(unittest.TestCase):
    """ Test cases for HW4a """
    @patch('HW4a_BinSun.get_repo')
    @patch('HW4a_BinSun.get_commits')

    def test_correct_result(self,repos, Mocktest):
        """ test case for checking results of valid user name """
        Mocktest.return_value.json.return_value = ('richkempinski')
        
        repos = get_repo("richkempinski")
        self.assertEqual(len(repos), 9)
        self.assertEqual(repos[0], "csp")
        self.assertEqual(repos[1], "hellogitworld")
        self.assertEqual(repos[2], "helloworld")
        self.assertEqual(repos[3], "Mocks")
        self.assertEqual(repos[4], "Project1")


    def test_special_cases(self):
        """ Test cases for invalid input """
    pass
    """self.assertEqual(get_repo("kkk"), [])"""


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
