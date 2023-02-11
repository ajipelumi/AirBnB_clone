#!/usr/bin/python3
""" BaseModel Class Test Module. """
from models.base_model import BaseModel
import unittest
import datetime


class TestBaseModelClass(unittest.TestCase):
    """ Tests all methods in BaseModel class. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.obj = BaseModel()

    def test_create_instance(self):
        """ Test that BaseModel instance is created. """
        self.assertTrue(self.obj)

    def test_instance_attributes(self):
        """ Test that instance attributes are created. """
        self.obj.name = "My First Model"
        self.obj.number = 89
        self.assertEqual(self.obj.name, 'My First Model')
        self.assertEqual(self.obj.number, 89)

    def test_basemodel_instance(self):
        """ Test instance of BaseModel. """
        self.assertIsInstance(self.obj, BaseModel)
        self.assertNotIsInstance(self.obj, int)
        self.assertNotIsInstance(self.obj, float)

    def test_basemodel_id(self):
        """ Test BaseModel id. """
        self.assertTrue(self.obj.id)

    def test_basemodel_datetime(self):
        """ Test the datetime an instance is created. """
        self.assertEqual(type(self.obj.created_at), datetime.datetime)
        self.assertEqual(type(self.obj.updated_at), datetime.datetime)

    def test_save(self):
        """ Test the save method. """
        old_time = self.obj.updated_at
        self.assertNotEqual(self.obj.save(), old_time)

    def test_str(self):
        """ Test string representation. """
        cls_name = self.obj.__class__.__name__
        obj_id = self.obj.id
        obj_dict = self.obj.__dict__
        exp_string = f"[{cls_name}] ({obj_id}) {obj_dict}"
        self.assertEqual(self.obj.__str__(), exp_string)

    def test_to_dict(self):
        """ Test that to_dict returns all keys/values of __dict__. """
        self.obj.name = "My First Model"
        self.obj.number = 89
        json_dict = self.obj.to_dict()
        self.assertIsInstance(json_dict["name"], str)
        self.assertIsInstance(json_dict["number"], int)
        self.assertIsInstance(json_dict["id"], str)
        self.assertIsInstance(json_dict["__class__"], str)
        self.assertIsInstance(json_dict["updated_at"], str)
        self.assertIsInstance(json_dict["created_at"], str)
        self.assertIsInstance(json_dict, dict)

        self.assertEqual(json_dict["name"], "My First Model")
        self.assertEqual(json_dict["number"], 89)
        self.assertEqual(json_dict["id"], self.obj.id)
        self.assertEqual(json_dict["__class__"], "BaseModel")
        self.assertEqual(json_dict["updated_at"], str(self.obj.updated_at))
        self.assertEqual(json_dict["created_at"], str(self.obj.created_at))

    def test_kwargs(self):
        """ Test instance recreated with dictionary representation. """
        self.obj.name = "My First Model"
        self.obj.number = 89
        json_dict = self.obj.to_dict()
        new_model = BaseModel(**json_dict)
        self.assertEqual(new_model.id, self.obj.id)
        self.assertEqual(new_model.name, self.obj.name)
        self.assertEqual(new_model.number, self.obj.number)
        self.assertEqual(new_model.created_at, self.obj.created_at)
        self.assertEqual(new_model.updated_at, self.obj.updated_at)
        self.assertIsInstance(new_model.created_at, datetime.datetime)
        self.assertIsNot(self.obj, new_model)


if __name__ == '__main__':
    unittest.main()
