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
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path). """
        # Open JSON file with write access
        with open(self.__file_path, 'w', encoding='utf-8') as f:

            # Write to JSON file with json.dump
            json.dump(self.__objects, f, sort_keys=True)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists.
        """
        # Check if file exists
        file_exists = os.path.exists(self.__file_path)

        # File does not exist
        if file_exists is False:
            pass

        # File exists
        else:

            # Open file with read access
            with open(self.__file_path, 'r', encoding='utf-8') as f:

                # Read into __objects
                self.__objects = json.load(f)
