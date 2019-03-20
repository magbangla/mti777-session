# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from models import annonces, db

class Mti777Pipeline(object):

    def process_item(self, item, spider):
        # create a new SQL Alchemy object and add to the db session
        record = annonces(id_annonces=item['id_annonces'].decode('unicode_escape'),
                         adresse=item['adresse'],
                         prix_mini=None,
                         prix_maxi=None,
                         details=None,
                         url_annonce=item['url'])
        db.add(record)
        db.commit()
        return item
