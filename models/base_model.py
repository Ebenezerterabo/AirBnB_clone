#!/usr/bin/python3
""" This module contains the BaseModel class """

import uuid
import datetime


class BaseModel:
    """
    The BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ initializes the BaseModel objects """
        from models.engine.file_storage import FileStorage
        if kwargs:
            """ Instantiates all the objects of the BaseModel class """
            storage.new(self)
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value1 = datetime.datetime.fromisoformat(value)
                        setattr(self, key, value1)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime
        """
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        return {
                "__dict__": self.__dict__,
                "__class__": self.__class__.__name__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "id": self.id
            }

    def __str__(self):
        """ print the string representation of the instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
