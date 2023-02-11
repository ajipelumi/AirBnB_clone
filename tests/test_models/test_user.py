#!/usr/bin/python3
""" User Class Test Module. """
from models.user import User
import unittest


class UserClass(unittest.TestCase):
    """ Tests the behaviour of User class. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.user = User()

    def test_class_attributes(self):
        """ Test the instance of every public attribute. """
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        

if __name__ == '__main__':
    unittest.main()
