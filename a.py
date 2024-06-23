#!/usr/bin/python3

import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

m = BaseModel()

print(type(m.created_at))
print(type(m.updated_at))

d = m.to_dict()

print(type(m.created_at))
print(type(m.updated_at))

m = BaseModel(**d)

print(type(m.created_at))
print(type(m.updated_at))
