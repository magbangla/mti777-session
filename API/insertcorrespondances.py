# -*- coding: utf-8 -*
import json
import pymongo
from pymongo import MongoClient
def insertdata():
    client = MongoClient('localhost', 27017)
    db = client.correspondances
    line=db.kangalou_items
    with open('all_items.json', 'r', encoding='utf-8') as f:
        items_dict = json.load(f)
    for item in items_dict:
        ville=item['nom_ville']
        enreg={
                "id":item['id'],
                "name":ville,
                "value":item['value']}
        post_id = line.insert_one(enreg).inserted_id
        print (post_id)

def findOne():
    client = MongoClient('localhost', 27017)
    db = client.correspondances
    line=db.kangalou_items
    items = line.find({"name": "Victoriaville"})
    for i in items:
        print(i)
if __name__=='__main__':
    findOne()
