#!/usr/bin/python3
""" This module contains the Review class which inherits from BaseModel class """
from models import BaseModel


class Review(BaseModel):
    """ This represents the Review class """

    place_id = ""
    user_id = ""
    text = ""
