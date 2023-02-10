#!/usr/bin/python3
""" User Class. """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class inherits from BaseModel. """

    # Email attribute
    email = ""

    # Password attribute
    password = ""

    # First name attribute
    first_name = ""

    # Last name attribute
    last_name = ""
