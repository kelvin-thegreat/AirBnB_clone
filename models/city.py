#!/usr/bin/python3
""" City Module for AirBnB clone project """

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage_type

class City(BaseModel, Base):
    """ The city class with stateID & Name """
    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
