import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData 
    
#
from app.database import engine
from app.database.models import User
        

class manager:
    Base = declarative_base()
    Base.metadata.create_all(engine)
    
    #on ouvre la session
    Session = sessionmaker(bind=engine)
    session = Session()
    print( User.__table__ )
    print("into obj")
    
    def __init__(self):
        print("su15454ce")
        self.name ="ok"

    @classmethod
    def add_user(cls):
        ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
        manager.session.add(ed_user)
        our_user = manager.session.query(User).filter_by(name='ed').first() 
        #on commit la session
        manager.session.commit()
        #les operation de recherche dans la sb
        manager.querry()
        manager.querry2()
        #pour l instant a delete
        manager.commit()
        
    @classmethod
    def add_users(cls):
        
        ed_user = User(name='ssssssssssssss', fullname='Ed sssss', nickname='ssssssss')
        manager.session.add(ed_user)
        #pour l instant a delete
        manager.commit()
        
    @classmethod
    def commit(cls):
        manager.session.commit()
    #querries fuinctions 
    
    @classmethod
    def querry(cls):
        for instance in manager.session.query(User).order_by(User.id):
            print(instance.name, instance.fullname)
            
    @classmethod
    def querry2(cls):
        for name, fullname in manager.session.query(User.name, User.fullname):
            print(name, fullname)



##################################poubelle################################
# a mettre dans l'init
#DATABASE_URI = 'postgres+psycopg2://postgres:usagisan@localhost:5432/tuto'
        #engine = create_engine('sqlite:///:memory:', echo=True)
#engine = create_engine(DATABASE_URI, echo=True)

#database.manager.add_user