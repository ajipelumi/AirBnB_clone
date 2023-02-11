#!/usr/bin/python3
""" Review Class. """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class inherits from BaseModel. """

    # Place ID attribute. It will be the Place.id
    place_id = ""

    # User ID attribute. It will be the User.id
    user_id = ""

    # Text attribute
    text = ""
