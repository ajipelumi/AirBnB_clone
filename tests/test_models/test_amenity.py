#!/usr/bin/python3
""" Amenity Class Test Module. """
from models.amenity import Amenity
import unittest


class AmenityClass(unittest.TestCase):
    """ Tests the behaviour of Amenity class. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.amenity = Amenity()

    def test_class_attributes(self):
        """ Test the instance of every public attribute. """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity.name, str)
        

if __name__ == '__main__':
    unittest.main()
