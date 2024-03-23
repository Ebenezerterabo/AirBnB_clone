#!/usr/bin/python3

""" This module contains the FileStorage class """


import json
import os
from json import JSONEncoder
import datetime


class FileStorage:
    """
    The FileStorage class is used for storing and managing files.
    """

    __file_path = "models/engine/instances.json"
    __objects = {}

    def all(self):
        """
        Returns all objects stored in a FileStorage object.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds an object to a dictionary with a key generated
        from the object's class name and id.

        Args:
          obj: Object to be added to the storage.
            It should have "__class__" and "id" attributes.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Saves the contents of the `__objects` dictionary to a file
        in JSON format.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file, cls=DateTimeEncoder)

    def reload(self):
        """
        Reads data from a file and loads it into the `FileStorage` object.
        """
        file_path = FileStorage.__file_path
        try:
            if os.path.exists(file_path):
                file = FileStorage.__file_path
                with open(f"{file}", "r", encoding="utf-8") as file:
                    data = file.read()
                    FileStorage.__objects = json.loads(data)
                file.close()
            else:
                FileStorage.__objects = {}
        except Exception:
            pass
