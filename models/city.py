#!/usr/bin/python3
""" City Class. """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class inherits from BaseModel. """

    # State ID attribute. It will be the State.id
    state_id = ""

    # Name attribute
    name = ""
