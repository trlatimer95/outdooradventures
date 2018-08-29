# Database Setup file for Catalog project
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    name = Column(String(80), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    id = Column(Integer, primary_key=True)


class Category(Base):
    __tablename__ = 'category'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        # Returns category data
        return {
            'name': self.name,
            'id': self.id,
        }


class Item(Base):
    __tablename__ = 'item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Return item data
        return {
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'id': self.id,
        }

engine = create_engine('postgres://itoebvbeobxksl:d75445491f0f66b9b2360a19094658ad1119509b52c3e82144f6fb179228f3b8@ec2-54-221-237-246.compute-1.amazonaws.com:5432/d43ksk0d1rnbdj')
Base.metadata.create_all(engine) 
#Base.metadata.drop_all(engine)
