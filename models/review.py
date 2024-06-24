#!/usr/bin/python3

"""
This module defines the class User.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Class that defines a Review.
    Ineherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
