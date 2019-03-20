# see https://kirankoduru.github.io/python/running-scrapy-programmatically.html
from . import routes

import os, sys, json
from src.services.crawlService import CrawlService

from flask import Flask
from flask import request, jsonify


'''
Since we use CrawlerRunner with twistd reactor, and reactor is not restartable.
We need to follow below process when we start a crawler:
a. Call /crawl/start
b. Call /crawl/dddddkasjdfksd
c. Call /crawl/stop
'''

## start the reactor service in order to starting spider
@routes.route('/crawl/start', methods=['POST'])
def start():
    service = CrawlService()
    service.start_reactor()
    return 'Started Successful.', 200

## stop the reactor service in order to stopping spider
@routes.route('/crawl/stop', methods=['POST'])
def stop():
    service = CrawlService()
    service.stop_reactor()
    return 'Stop Successful.', 200

## start a crawl for a website with spider instance
@routes.route('/crawl/<siteuuid>', methods=['POST'], defaults={'crawluuid':''})
@routes.route('/crawl/<siteuuid>/<crawluuid>', methods=['POST'])
def crawl(siteuuid, crawluuid):
    if request.is_json:
        # json format: {url:'https://google.com'}
        service = CrawlService()
        website = request.get_json()
        website['UUID'] = siteuuid
        service.crawl(website, crawluuid) # won't return any result since it is executed by CrawlerRunner.
        return 'Executing crawling', 200
    return "Bad Request", 500

## start a crawl for a website with crawl process
@routes.route('/crawlp/<siteuuid>', methods=['POST'], defaults={'crawluuid':''})
@routes.route('/crawlp/<siteuuid>/<crawluuid>', methods=['POST'])
def crawl_by_process(siteuuid, crawluuid):
    if request.is_json:
        # json format: {url:'https://google.com'}
        service = CrawlService()
        website = request.get_json()
        website['UUID'] = siteuuid
        result = service.crawl_by_process(website, crawluuid)
        return jsonify(result), 200
    return "Bad Request", 500
