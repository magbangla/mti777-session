from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, String, Integer
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

class annonces(Base):
    __tablename__ = 'annonces'

    id = Column(Integer, primary_key=True)
    id_annonces=Column(String(20))
    adresse=Column(String(100))
    prix_mini=Column(Integer)
    prix_maxi=Column(Integer)
    details=Column(String(1000))
    url_annonce=Column(String(500))

    def __init__(self, id=None, id_annonces=None, adresse=None, prix_mini=None,prix_maxi=None,details=None,url_annonce=None):

        self.id = id
        self.id_annonces=id_annonces
        self.adresse=adresse
        self.prix_mini=prix_mini
        self.prix_maxi=prix_maxi
        self.details=details
        self.url_annonce=url_annonce
    def __repr__(self):
        return "<AllData: id='%d', title='%s', url='%s', desc='%s'>" % (self.id, self.title, self.url, self.desc)
