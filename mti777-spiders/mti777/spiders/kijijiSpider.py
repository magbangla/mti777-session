import scrapy
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver

class kijijispider(scrapy.Spider):
    name = 'kijijispider'
    allowed_domains = ['www.kangalou.com/fr']
    start_urls = ['https://www.kangalou.com/fr/recherche/']
    def parse(self, response):
        qcs=response.css('.city-child label')
        # class item
        for qc in qcs:
            nom_ville=qc.css("span::text").extract()
            id=qc.css('input').xpath("@id").get()
            value=qc.css('input').xpath("@value").get()
    #    html=BeautifulSoup(page,'html.parser')
            yield {
            "nom_ville":nom_ville,
            "id":id,
            "value":value
            }
