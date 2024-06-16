#!/usr/bin/python3

"""
The __init__.py file for this package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
