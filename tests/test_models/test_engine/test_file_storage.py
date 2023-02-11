#!/usr/bin/python3
""" FileStorage Class Test Module. """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import json
import os


class FileStorageClass(unittest.TestCase):
    """ Tests the behaviour of FileStorage class. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.model = BaseModel()
        self.model.name = "Pelumi"
        self.model.number = 89

    def test_file_storage_(self):
        """
        Test that FileStorage serializes instances to a JSON file
        and deserializes JSON file to instances.
        """
        


if __name__ == '__main__':
    unittest.main()
