from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, String, Integer, Text
import pymysql
# db settings
dbuser = 'magbangla' #DB username
dbpass = 'password' #DB password
dbhost = 'db4free.net' #DB host
dbname = 'mti777' #DB database name
engine = create_engine("mysql+pymysql://%s:%s@%s/%s?charset=utf8&use_unicode=0"
                       %(dbuser, dbpass, dbhost, dbname),
                       echo=False,
                       pool_recycle=1800)
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))

Base = declarative_base()

def create_table(engine):
    Base.metadata.create_all(engine)

class annonces(Base):
    __tablename__ = 'annonces'

    id = Column(Integer, primary_key=True)
    id_annonces=Column(String(20))
    titre_annonce=Column(String(100))
    adresse=Column(String(100))
    loyer=Column(Integer)
    details=Column(Text())
    url_annonce=Column(String(500))



    def __init__(self, id=None, id_annonces=None, titre_annonce=None, adresse=None, loyer=None,details=None,url_annonce=None):

        self.id = id
        self.id_annonces=id_annonces
        self.titre_annonce=titre_annonce
        self.adresse=adresse
        self.loyer=loyer
        self.details=details
        self.url_annonce=url_annonce
    def __repr__(self):
        return "<Annonce: id='%d', title='%s', url='%s', adresse='%s', loyer='%s', detail='%s'>" % (self.id, self.titre_annonce, self.url_annonce, self.adresse, self.loyer, self.details)
