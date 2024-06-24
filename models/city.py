#!/usr/bin/python3

"""
This module defines the class User.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that defines a City.
    Ineherits from BaseModel
    """

    state_id = ""
    name = ""
