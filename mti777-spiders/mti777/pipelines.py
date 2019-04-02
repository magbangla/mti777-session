# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from models import annonces,photos, db

class Mti777Pipeline(object):

    def process_item(self, item, spider):
        # create a new SQL Alchemy object and add to the db session
        record = annonces(id_annonces='KGL_'+item['id_annonces'].decode('unicode_escape'),titre_annonce=item['titre'].decode('utf8'),
                         adresse=item['adresse'].decode('utf8'),
                         loyer=item['cost'],
                         details=None,
                         disponibilite=item['disponibilité'].decode('utf8'),
                         url_annonce=item['url'].decode('unicode_escape'),
                         thumbnail=item['petite_img'].decode('unicode_escape'))
        val=record.id_annonces
        nb=db.query(annonces).filter(annonces.id_annonces == val).first()
        if nb==None:
            db.add(record)
            db.commit()
            for i in range(0,len(item['images'])):
                #print(len(item['images']))
                enreg=photos(id_annonce_='KGL_'+item['id_annonces'] ,url_img=str(item['images'][i]))
                db.add(enreg)
                db.commit()
            return item

class Mti777LGQPipeline(object):

    def process_item(self, item, spider):
        # create a new SQL Alchemy object and add to the db session
        record = annonces(id_annonces=item['id_annonces'].decode('unicode_escape'),titre_annonce=item['titre'].decode('utf8'),
                         adresse=item['adresse'].decode('utf8'),
                         loyer=item['cost'],
                         details=None,
                         disponibilite=item['disponibilité'].decode('utf8'),
                         url_annonce=item['url'].decode('unicode_escape'),
                         thumbnail=item['petite_img'].decode('unicode_escape'))
        val=record.id_annonces
        nb=db.query(annonces).filter(annonces.id_annonces == val).first()
        if nb==None:
            db.add(record)
            db.commit()
            for i in range(0,len(item['images'])):
                #print(len(item['images']))
                enreg=photos(id_annonce_='LGQ_'+item['id_annonces'] ,url_img=str(item['images'][i]))
                db.add(enreg)
                db.commit()
            return item


class AddTablePipeline(object):

    def process_item(self, item, spider):
        return item
