#!/usr/bin/python3
""" This module contains the User class which inherits from BaseModel class """
from models import BaseModel


class User(BaseModel):
    """ This represents the User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
