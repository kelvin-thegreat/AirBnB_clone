#!/usr/bin/python3
""" Review Module for HBNB project """

from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from models import storage_type

class Review(BaseModel, Base):
    """ Review instance for storing review infor. """
    __tablename__ = 'reviews'
    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
