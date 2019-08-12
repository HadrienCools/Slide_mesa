
from sqlalchemy import create_engine

DATABASE_URI = 'postgres+psycopg2://postgres:usagisan@localhost:5432/tuto'
        #engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(DATABASE_URI, echo=False)#True