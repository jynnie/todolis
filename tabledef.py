from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String #importing different column types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tutorial.db', echo=True) #makes the database tutorial.db
Base = declarative_base()

class User(Base): #User() will be used to interact with this database
    __tablename__ = "users" #the name of the table is users

    #setting up columns for the table
    id          = Column(Integer, primary_key=True) #id is autogenerated
    username    = Column(String)
    email       = Column(String)
    password    = Column(String)
    todos       = relationship('Todo', backref='user', lazy='dynamic') #linked to values in todos; the first argument has to be the class

    def __init__(self, username, email, password): #defines what happens when User(x, y) is used
        self.username = username
        self.email = email
        self.password = password

class Todo(Base):
    __tablename__ = "todos"

    #setting up columns for the tables
    id          = Column(Integer, primary_key=True)
    user_id     = Column(Integer, ForeignKey('users.id')) #links to user
    content     = Column(String)

Base.metadata.create_all(engine) #creates all the above defined tables
