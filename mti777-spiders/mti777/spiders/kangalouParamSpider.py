# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from bs4 import BeautifulSoup
import webbrowser
import json
from selenium import webdriver



class KangalouParamSpider(scrapy.Spider):
    name = 'KangalouParamSpider'
    allowed_domains = ['www.kangalou.com']
    start_urls = ['https://www.kangalou.com/fr/recherche/']
    def parse(self, response):
        data={
            'c[]':"400",
            'pmin':"900",
            'pmax':"5000",
            's':"pasc"
        }
        head={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control':' max-age=0',
            'referrer':'https://www.kangalou.com/fr/recherche/',
            'Connection': 'keep-alive',
            'Host': 'www.kangalou.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        yield scrapy.FormRequest(url=self.start_urls[0], callback=self.parse_result,headers=head, dont_filter=True)

    def parse_result(self, response):
        webbrowser.open(response.url)
        #browser = webdriver.PhantomJS()Firefox()
        browser = webdriver.PhantomJS()
        browser.get(response.url)
        html = browser.page_source
        #location=browser.find_elements_by_xpath('"//*[contains(concat( " ", @class, " " ), concat( " ", "js-propertyTitle", " " ))]//a')
        #print(html)
        #soup = BeautifulSoup(html, 'lxml')
        #a = soup.find('h3.property__title', 'wrapper')
        soup = BeautifulSoup(html, "lxml")
        div = soup.find_all('span', {'class':'js-cost'})
        for l in div:
            print l
