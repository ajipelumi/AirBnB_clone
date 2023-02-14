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
        self.file = FileStorage()
        self.model = BaseModel()
        self.file_path = "test_file.json"
        self.file._FileStorage__file_path = self.file_path

    def tearDown(self):
        """ Clean up objects and variables. """
        file_exists = os.path.exists(self.file_path)
        if file_exists:
            os.remove(self.file_path)

    def test_file_path(self):
        """ Test that __file_path is not none. """
        self.assertNotEqual(self.file._FileStorage__file_path, None)

    def test_all_method(self):
        """
        Test that all() returns a dictionary.
        """
        file_dict = self.file.all()
        self.assertEqual(type(file_dict), dict)

    def test_new_method(self):
        """
        Test new() method in FileStorage class.
        """
        self.file.new(self.model)
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIn(key, self.file._FileStorage__objects)
        self.assertEqual(self.model, self.file._FileStorage__objects[key])

    def test_save_method(self):
        """
        Test that save() method serializes __objects to
        the JSON file (path: __file_path).
        """
        self.file.save()
        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, 'r', encoding='utf-8') as f:
            load_json = json.load(f)
        
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIn(key, load_json)
        self.assertEqual(self.model.to_dict(), load_json[key])

    def test_reload_method(self):
        """
        Test that reload() method deserializes the JSON file
        to __objects if the JSON file (__file_path) exists.
        """
        self.file.save()
        self.assertTrue(os.path.exists(self.file_path))
        self.file.reload()
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIn(key, self.file._FileStorage__objects)
        self.assertNotEqual(self.model, self.file._FileStorage__objects[key])
        self.assertEqual(type(self.file._FileStorage__objects[key]), BaseModel)



if __name__ == '__main__':
    unittest.main()
