#!/usr/bin/python3
"""Module for HBNB project """

from models import storage_type
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
