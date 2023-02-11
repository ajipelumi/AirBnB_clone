#!/usr/bin/python3
""" Place Class. """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class inherits from BaseModel. """

    # City ID attribute. It will be the City.id
    city_id = ""

    # User ID attribute. It will be the User.id
    user_id = ""

    # Name attribute
    name = ""

    # Description attribute
    description = ""

    # Room Number attribute
    number_rooms = 0

    # Bathroom Number attribute
    number_bathrooms = 0

    # Maximum Guest attribute
    max_guest = 0

    # Price by Night attribute
    price_by_night = 0

    # Latitude attribute
    latitude = 0.0

    # Longitude attribute
    longitude = 0.0

    # Amenity attribute. It will be the list of Amenity.id
    amenity_ids = []
