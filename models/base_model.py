#!/usr/bin/python3

"""
This module defines the class BaseModel.
"""

import uuid
import datetime


class BaseModel:
    """
    Class BaseModel that defines all common
    attributes/methods for other classes.
    """

    def __init__(self):
        """
        Instance Initialization.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Defines a string representation for an instance.
        """
        name = __class__.__name__
        sid = self.id
        d = str(self.__dict__)
        return "[" + name + "] " + "(" + sid + ") " + d

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of the instance.
        """
        d = self.__dict__
        d['__class__'] = __class__.__name__
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        return d
