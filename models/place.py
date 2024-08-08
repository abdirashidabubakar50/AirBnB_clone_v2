#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
import os

# Define Place_amenity association table
place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True,
        nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True,
        nullable=False)
    )
class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(String(1024), nullable=True)
        longitude = Column(String(1024), nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            back_populates="place_amenities"
        )
    else:
        @property
        def reviews(self):
            from models.review import Review
            from models import storage
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]
        
        @property
        def amenities(self):
            """Getter that returns the list of Amenity instances"""
            return [amenity for amenity in models.storage.all(Amenity).values()
            if amenity.id in self.amenity_ids]
        
        @amenities.setter
        def amenities(self, obj):
            """setter that adds an Amenity.id to amenity_ids"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
