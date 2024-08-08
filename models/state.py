#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref="state",
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """returns list of City instances with state_id equals to
            the current  State.id"""
            from models.city import City
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
