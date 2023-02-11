#!/usr/bin/python3
""" City Class Test Module. """
from models.city import City
import unittest


class CityClass(unittest.TestCase):
    """ Tests the behaviour of City class. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.city = City()

    def test_class_attributes(self):
        """ Test the instance of every public attribute. """
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
        

if __name__ == '__main__':
    unittest.main()
