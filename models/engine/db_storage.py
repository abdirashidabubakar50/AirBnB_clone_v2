#!/usr/bin/python3
from models.city import City
from models.state import State
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ initialize the DBStorage instance"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD  = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')

        print(f"HBNB_MYSQL_USER={HBNB_MYSQL_USER}")
        self.__engine = create_engine(f"mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}",
        pool_pre_ping = True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

        # Base.metadata.create_all(self.__engine)
        # Session = sessionmaker(bind=self.__engine)
        # self.__session =  Session()
    
    def all(self, cls=None):
        """Query all objects  from the current database session
        (self.__session), if cls is None, query all types of objects
        Return a dictionary: key = <class-name>.<object-id>"""
        objects = {}
        if cls is None:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review

            for class_name in [User, State, City, Amenity, Place, Review]:
                query_result = self.__session.query(class_name).all()
                for obj in query_result:
                    key = f"{class_name.__name__}.{obj.id}"
                    objects[key] = obj
        else:
            query_result = self.__session.query(class_name).all()
            for  obj in query_result:
                key = f"{class_name.__name__}.{obj.id}"
                objects[key] = obj
        
        return objects

    def new(self, obj):
        """Add the object to the current database sessoin"""
        self.__session.add(obj)
    
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """create all tables  in the database and intialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
