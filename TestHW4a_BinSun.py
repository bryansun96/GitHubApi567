""" author: Bin Sun
These are the test cases
"""
import unittest
from HW4a_BinSun import get_repo, get_commits
from unittest.mock import MagicMock as Mock, patch

class TestHW4a(unittest.TestCase):
    """ Test cases for HW4a """
    @patch('HW4a_BinSun.get_repo')

    def test_correct_result(self,repos,get_commits):
        """ test case for checking results of valid user name """

        repos = get_repo("richkempinski")
        self.assertEqual(len(repos), 9)
        self.assertEqual(repos[0], "csp")
        self.assertEqual(repos[1], "hellogitworld")
        self.assertEqual(repos[2], "helloworld")
        self.assertEqual(repos[3], "Mocks")
        self.assertEqual(repos[4], "Project1")

        """self.assertEqual(get_commits("richkempinski", repos[0]), 2)
        self.assertEqual(get_commits("richkempinski", repos[1]), 30)
        self.assertEqual(get_commits("richkempinski", repos[2]), 6)
        self.assertEqual(get_commits("richkempinski", repos[3]), 10)
        self.assertEqual(get_commits("richkempinski", repos[4]), 2)
        """

    def test_special_cases(self):
        """ Test cases for invalid input """

        self.assertEqual(get_repo("kkk"), [])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
