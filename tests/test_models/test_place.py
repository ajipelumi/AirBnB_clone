#!/usr/bin/python3
""" Place Class Test Module. """
from models.place import Place
import unittest


class PlaceClass(unittest.TestCase):
    """ Tests the behaviour of Place class. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.place = Place()

    def test_class_attributes(self):
        """ Test the instance of every public attribute. """
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)
        

if __name__ == '__main__':
    unittest.main()
