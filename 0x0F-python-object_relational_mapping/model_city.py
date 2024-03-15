#!/usr/bin/python3
"""
script that defines city class
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    class City
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, Foreignkey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
