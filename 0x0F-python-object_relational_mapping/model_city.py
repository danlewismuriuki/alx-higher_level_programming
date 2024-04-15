#!/usr/bin/python3

"""
Module that connects a python script to the database
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State  # Importing Base and State from model_state

class City(Base):
    """
    City class that links to MySQL table `cities`
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship with State
    state = relationship("State", back_populates="cities")

State.cities = relationship("City", order_by=City.id, back_populates="state")
