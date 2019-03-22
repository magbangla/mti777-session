# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from bs4 import BeautifulSoup
import webbrowser
import json
from selenium import webdriver
#from items import KangalouResultItem
import pymysql.cursors
class KangalouSpider(scrapy.Spider):
    name = 'KangalouSpider'
    page_number=2
    allowed_domains = ['www.kangalou.com']
    start_urls = ['https://www.kangalou.com/fr/recherche/?page=1']
    def parse(self, response):
        #ouvrir la page avec phantomJS
        browser = webdriver.PhantomJS()
        browser.get(KangalouSpider.start_urls[0])
        #recuperer le contenu de la page
        #html = browser.page_source
        #soup = BeautifulSoup(html,'html.parser')
        #resp=HtmlResponse(browser.current_url, body=html, encoding='utf-8', request=request)
        #annonces = soup.find_all('div', {'class':'property__inner'})
        annonces=response.css('.js-propertyTitle')
        #webbrowser.open(response.url)
        for annonce in annonces:
            #loyer=annonce.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "js-cost", " " ))]').extract_first()
            url_annonce=annonce.css('.js-propertyTitle a').xpath("@href").extract_first()
            url_reel=str(url_annonce).split('?')
            titre=annonce.css('.js-propertyTitle a').css('a::text').extract()
            #titre=titre_h3.css('a')
            #detail_url=titre_h3.find('a', href=True)['href']
            if len(url_reel[0])!=0:
                browser.get(url_reel[0])
                html = browser.page_source
                soup = BeautifulSoup(html,'html.parser')
                cout=None
                det1=[]
                images=[]
                description=None
                dimension=None
                for desc in soup.select('.ui-nt+p'):
                    description=desc
                for dim in soup.select('.details-header .property__dimension'):
                    dimension=dim

                for slide in soup.select("div.slick-slide"):
                    for a in slide.select("a.js-LightobxTrigger"):
                        for img in a.select("img"):
                            images.append("https://www.kangalou.com"+str(img['src'])[0:(len(str(img['src']))-1)])
                for item in soup.select("p.details-title-meta"):
                    det1.append(item.get_text())
                for cost in soup.find_all('span', {'class':'cost'}):
                    cout=cost.text
                    stg1=str(cout.encode('utf8')).strip()
                    cout1=stg1[0:len(stg1)-1]
                    if len(cout1.split(" "))>1:
                        stg2=cout1.split(' ')
                        stg3=stg2[0]+stg2[1]
                        try:
                            cout=float(stg3)
                        except:
                            cout=0
                    else:
                        try:
                            cout=float(stg1[0:len(stg1)-1])
                        except:
                            cout=0
                if len(det1)!=0:
                    liste_detail=str(det1[0].encode('utf8')).split('\n')
                    print str(url_reel[0].encode('utf8')).strip().split('/')
                    if len(str(url_reel[0].encode('utf8')).strip().split('/'))>4:
                        data={
                        #"loyer":loyer,
                        "titre":str(titre[0].encode('utf8')).strip(),
                        "url":str(url_reel[0].encode('utf8')).strip(),
                        "cost":cout,
                        "adresse":liste_detail[1],
                        "disponibilité":liste_detail[4].strip(),
                        "annonce":str(liste_detail[5].encode('utf8')).strip(),
                        "images":images,
                        "id_annonces":str(url_reel[0].encode('utf8')).strip().split('/')[5]
                        }
                        yield data
                    else:
                        pass

        next_page='https://www.kangalou.com/fr/recherche/?page='+str(KangalouSpider.page_number)
        if KangalouSpider.page_number<=141:
            KangalouSpider.page_number+=1
            browser.close()
            yield response.follow(next_page,callback=self.parse)
