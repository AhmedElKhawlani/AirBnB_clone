#!/usr/bin/python3

"""
This module defines the class User.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that defines A user.
    Ineherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
