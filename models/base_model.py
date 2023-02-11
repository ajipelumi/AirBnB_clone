#!/usr/bin/python3
""" Base of all other classes. """
import uuid
import datetime
from models import storage


class BaseModel():
    """ Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """ Initialize data. """
        # If kwargs is not empty
        if kwargs:
            for key, value in kwargs.items():

                # __class__ should not be added as attribute
                if key == "__class__":
                    continue

                # Check for created_at and updated_at
                if key == "created_at":
                    # Convert to datetime object
                    value = datetime.datetime.fromisoformat(value)

                if key == "updated_at":
                    # Convert to datetime object
                    value = datetime.datetime.fromisoformat(value)

                # Set attribute
                setattr(self, key, value)

        else:
            # Generates unique id when an instance is created
            self.id = str(uuid.uuid4())

            # The current datetime when an instance is created
            self.created_at = datetime.datetime.now()

            # The current datetime when an instance is updated
            self.updated_at = self.created_at

            # Call method new() on storage
            storage.new(self)

    def __str__(self):
        """ Returns a string representation to print to STDOUT. """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        # Call save method of storage
        storage.save()

        # Update updated_at
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__. """

        # Create dictionary
        base_dict = {}

        # Add class key whose value is class name
        base_dict['__class__'] = f'{self.__class__.__name__}'

        # Iterate through self.__dict__ and update dictionary
        for key, value in self.__dict__.items():
            # If created_at is met
            if key == 'created_at':
                value = str(self.created_at)

            # If updated_at is met
            if key == 'updated_at':
                value = str(self.updated_at)

            # Append keys/values
            base_dict[key] = value

        return base_dict  # return dictionary
