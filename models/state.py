#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from models.city import City
from os import getenv

class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128),
                      nullable=False)
        cities = relationship(
                "City",
                backref="state",
                cascade="all, delete"
            )

    else:
        @property
        def cities(self):
            """Getter for the cities"""
            from models.engine.file_storage import FileStorage

            objects = FileStorage.all(City)

            buffer = []
            for keys, cities in objects.items():
                if 'City' in keys and cities.state_id == self.id:
                    buffer.append(cities)

            return buffer
