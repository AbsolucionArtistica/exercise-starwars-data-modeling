import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    favorite = relationship("User", back_populates="favorite")
    suscription_date = Column(DateTime, nullable=True)
    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = relationship("User", back_populates="favorite")
    user_id = Column(Integer, ForeignKey('user.id'))
    character = relationship("Character", back_populates="character")
    character_id = Column(Integer, ForeignKey('character.id'))
    planet = relationship("Planet", back_populates="planet")
    planet_id = Column(Integer, ForeignKey('planet.id'))


class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    properties = Column(String(500), nullable=True)
    favorite = relationship("Favorite", back_populates="planet")

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    properties = Column(String(500), nullable=True)
    favorite = relationship("Favorite", back_populates="character")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
