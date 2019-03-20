# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from models import AllData, db

class Mti777Pipeline(object):

    def process_item(self, item, spider):
        # create a new SQL Alchemy object and add to the db session
        record = AllData(title=item['title'][0].decode('unicode_escape'),
                         url=item['url'][0],
                         desc=desc)
        db.add(record)
        db.commit()
        return item
