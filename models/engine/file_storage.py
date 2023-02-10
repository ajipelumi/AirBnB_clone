#!/usr/bin/python3
""" File Storage Class Module. """
import json
import os.path


class FileStorage():
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    # Define path to JSON file
    __file_path = "file.json"

    # Define dictionary to store objects
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id. """
        # Set key
        key = obj.__class__.__name__ + "." + obj.id

        # Set in __objects
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path). """
        # Call to_dict
        obj_json = {}

        # Iterate through items
        for key, value in self.__objects.items():

            # value is a BaseModel object as seen in new().
            # a call to to_dict will return a dict object
            # which makes it serializable
            obj_json.update({key: value.to_dict()})

        # Open JSON file with write access
        with open(self.__file_path, 'w', encoding='utf-8') as f:

            # Write to JSON file with json.dump
            json.dump(obj_json, f, sort_keys=True)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists.
        """
        # import BaseModel for eval() call
        from models.base_model import BaseModel

        # Check if file exists
        file_exists = os.path.exists(self.__file_path)

        # File does not exist
        if file_exists is False:
            pass

        # File exists
        else:

            # Open file with read access
            with open(self.__file_path, 'r', encoding='utf-8') as f:

                # Read into memory
                from_json = json.load(f)

                # Iterate through items
                for key, value in from_json.items():

                    # Get the class name because we want
                    # to recreate the instance of that class
                    class_name = value["__class__"]

                    # Call eval() to treat string as Python expression
                    # and recreate the instance of the class.
                    python_obj = eval("{}({})".format(class_name, "**value"))

                    # Call new() to set class and id as key
                    self.new(python_obj)
