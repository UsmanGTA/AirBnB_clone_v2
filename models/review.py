#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60),
                      ForeignKey('places.id'),
                      nullable='False')
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)

    user = relationship(
            "User",
            back_populates="reviews",
            cascade="all, delete"
        )
    place = relationship(
            "Place",
            back_populates="reviews",
            cascade="all, delete"
        )
