#!/usr/bin/python3
""" This file contains the FileStorage class """
import json
import os


class FileStorage:
    """ This class represents the FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Instanciates the objects of this class """
        pass

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets the obj with key  id in the dictionary __objects """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as __file:
            json.dump(FileStorage.__objects, __file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            if os.path.exists(FileStorage.__file_path):
                _file = FileStorage.__file_path
                with open(f"{_file}", "r", encoding="utf-8") as _file:
                    data = _file.read()
                    FileStorage.__objects = json.loads(data)
            else:
                FileStorage.__objects = {}
        except Exception:
            pass
