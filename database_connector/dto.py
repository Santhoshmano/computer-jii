import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from db_connector import connector

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250),nullable=False)
    password = Column(String(250),nullable=False)
    mobile = Column(String(250),nullable=False)
    location = Column(String(250),nullable=False)
    designation = Column(String(250),nullable=False)

    def __init__(self,name,email,password,mobile,location,designation):
        self.name = name
        self.email = email
        self.password = password
        self.mobile = mobile
        self.location = location
        self.designation = designation

class ModelUserCount(Base):
    __tablename__='model_user_count'
    id = Column(Integer,primary_key=True)
    email = Column(String(250),nullable=False)
    model_type = Column(String(250),nullable=False)
    count = Column(Integer,nullable=False)

    def __init__(self,email,model_type,count):
        self.email = email
        self.model_type = model_type
        self.count = count
    
class ModelCount(Base):
    __tablename__='model_count'
    id = Column(Integer,primary_key=True)
    model_type = Column(String(250),nullable=False)
    count = Column(Integer,nullable=False)

    def __init__(self,model_type,count):
        self.model_type = model_type
        self.count = count

class ModelRequest(Base):
    __tablename__='model_request'
    id = Column(Integer,primary_key=True)
    email = Column(String(250),nullable=False)
    model_type = Column(String(250),nullable=False)
    model_name = Column(String(250),nullable=False)
    request = Column(Integer,nullable=False)

    def __init__(self,email,model_type,model_name,request):
        self.email = email
        self.model_name = model_name
        self.model_type = model_type
        self.request = request

class ModelApi(Base):
    __tablename__='model_api'
    id = Column(Integer,primary_key=True)
    email = Column(String(250),nullable=False)
    model_type = Column(String(250),nullable=False)
    model_name = Column(String(250),nullable=False)
    api = Column(Integer,nullable=False)

    def __init__(self,email,model_type,model_name,api):
        self.email = email
        self.model_name = model_name
        self.model_type = model_type
        self.api = api

class TrainableModels(Base):
    __tablename__='trainable_models'
    id = Column(Integer,primary_key=True)
    model_type = Column(String(250),nullable=False)
    model_description = Column(String(250),nullable=False)
    input_format = Column(String(250),nullable=False)
    output_format = Column(String(250),nullable=False)
    
    def __init__(self,model_type,model_description,input_format,output_format):
        self.model_type = model_type
        self.model_description = model_description
        self.input_format = input_format
        self.output_format = output_format

class NonTrainableModels(Base):
    __tablename__='non_trainable_models'
    id = Column(Integer,primary_key=True)
    model_type = Column(String(250),nullable=False)
    model_description = Column(String(250),nullable=False)
    input_format = Column(String(250),nullable=False)
    output_format = Column(String(250),nullable=False)
    
    def __init__(self,model_type,model_description,input_format,output_format):
        self.model_type = model_type
        self.model_description = model_description
        self.input_format = input_format
        self.output_format = output_format

class Model(Base):
    __tablename__='model'
    id = Column(Integer,primary_key=True)
    email = Column(String(250),nullable=False)
    model_type = Column(String(250),nullable=False)
    model_name = Column(String(250),nullable=False)


    def __init__(self,email,model_name,model_type):
        self.email = email
        self.model_type = model_type
        self.model_name = model_name


engine = create_engine(connector)
#'sqlite:///computer_jii.db'
Base.metadata.create_all(engine)