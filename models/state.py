#!/usr/bin/python3
""" State Module """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type
from models.city import City
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """ State/table model"""
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            '''returns City instances state id
                equals the current State.id
                FileStorage Rship btn State and City
            '''
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
