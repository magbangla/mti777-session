import os, sys, json, datetime, uuid
sys.path.append(os.getcwd() + '/src/scrapyweb')

# scrapy api
from threading import Thread
from flask import Flask
from flask import request, jsonify
from flask import Blueprint
from twisted.internet import reactor
from scrapy import signals
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import inspect
import subprocess

from src.scrapyweb.webscrapy.spiders import hintCrawl
from src.scrapyweb.webscrapy import settings
from src.scrapyweb import webscrapy

# how to run Scrapy from Python script: https://scrapy.readthedocs.io/en/latest/topics/practices.html#run-scrapy-from-a-script
class CrawlService():
    def spider_closing(self):
        """Activates on spider closed signal"""
        print("Closing reactor")
        reactor.stop()
        pass

    def start_reactor(self):
        if not reactor.running:
            try:
                reactor.run()
            except:
                pass

    def stop_reactor(self):
        if reactor.running:
            reactor.stop()

    # how to pass parameters: https://stackoverflow.com/questions/15611605/how-to-pass-a-user-defined-argument-in-scrapy-spider
    def crawl_by_process(self, website, crawluuid= ''):
        websiteuuid = website['UUID']
        crawluuid = crawluuid

        crawlSettings = self.toCrawlSettings(website, crawluuid)

        subprocess.check_output(['scrapy', 'crawl', "hintCrawl", '-a', 'cs='+json.dumps(crawlSettings)])


    # async, will return immediately and won't wait crawl finished
    def crawl(self, website, crawluuid = ''):
        needUpdateWebsite = not crawluuid
        websiteuuid = website['UUID']
        crawluuid =  crawluuid

        crawlSettings = self.toCrawlSettings(website, crawluuid)

        configure_logging()

        s = get_project_settings()
        for a in inspect.getmembers(settings):
            if not a[0].startswith('_'):
                # Ignores methods
                if not inspect.ismethod(a[1]):
                    s.update({a[0]:a[1]})

        # if you want to use CrawlerRunner, when you want to integrate Scrapy to existing Twisted Application
        runner = CrawlerRunner(s)
        d = runner.crawl(hintCrawl.HintCrawlSpider, crawlSettings)
        d.addCallback(return_spider_output)
        return d

def return_spider_output(output):
    """
    :param output: items scraped by CrawlerRunner
    :return: json with list of items
    """
    # this just turns items into dictionaries
    # you may want to use Scrapy JSON serializer here
    return json.dumps([dict(item) for item in output])
