#!/usr/bin/python3

"""
This module defines the class FileStorage.
"""

import json
from ..base_model import BaseModel
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State 
from ..user import User


class FileStorage:
    """
    - Serializes instances to a JSON file ;
    - Deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """

        return self.__class__.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """

        key = obj.__class__.__name__ + "." + obj.id
        self.__class__.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """

        dict_json = {}
        for key, value in self.__class__.__objects.items():
            dict_json[key] = value.to_dict()
        with open(self.__class__.__file_path, "w") as f:
            json.dump(dict_json, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        try:
            with open(self.__class__.__file_path, "r") as f:
                dict_json = json.load(f)
            for key, value in dict_json.items():
                obj = eval(key.split('.')[0])(**value)
                self.new(obj)
        except Exception:
            pass
