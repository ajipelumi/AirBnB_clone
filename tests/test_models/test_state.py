#!/usr/bin/python3
""" State Class Test Module. """
from models.state import State
import unittest


class StateClass(unittest.TestCase):
    """ Tests the behaviour of State class. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.state = State()

    def test_class_attributes(self):
        """ Test the instance of every public attribute. """
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state.name, str)
        

if __name__ == '__main__':
    unittest.main()
