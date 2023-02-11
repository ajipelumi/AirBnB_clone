#!/usr/bin/python3
""" Review Class Test Module. """
from models.review import Review
import unittest


class ReviewClass(unittest.TestCase):
    """ Tests the behaviour of Review class. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.review = Review()

    def test_class_attributes(self):
        """ Test the instance of every public attribute. """
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        

if __name__ == '__main__':
    unittest.main()
