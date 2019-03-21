# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from models import annonces, db

class Mti777Pipeline(object):

    def process_item(self, item, spider):
        # create a new SQL Alchemy object and add to the db session
        record = annonces(id_annonces='KGL_'+item['id_annonces'].decode('unicode_escape'),titre_annonce=item['titre'].decode('unicode_escape'),
                         adresse=item['adresse'].decode('unicode_escape'),
                         loyer=None,
                         details=None,
                         url_annonce=item['url'].decode('unicode_escape'))
        val=record.id_annonces
        nb=db.query(annonces).filter(annonces.id_annonces == val).first()
        if nb==None:
            db.add(record)
            db.commit()
            return item


class AddTablePipeline(object):

    def process_item(self, item, spider):
        return item
