#!/usr/bin/python3
"""
script defines state class and base class
"""
from sqlalchemy import Column, Interger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

clas State(Base):
    """
    state class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
