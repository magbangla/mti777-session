# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import decimal
class logisquebecSpider(scrapy.Spider):
    name = 'logisquebecSpider'
    allowed_domains = ['www.logisquebec.com']
    start_urls = ['https://www.logisquebec.com/a-louer/']
    page_number=2
    def parse(self, response):
        #ouvrir la page avec phantomJS
        browser = webdriver.PhantomJS()
        #browser.get(logisquebecSpider.start_urls[0])
        annonces=response.css('.box-result-unit-louer')
        for annonce in annonces:
            url_annonce=annonce.css('#box-result-unit-title a').xpath("@href").extract_first()
            url_annonce1="https://www.logisquebec.com"+str(url_annonce)
            titre=annonce.css('#box-result-unit-title a').css('a::text').extract()
            prix=str(annonce.css('.box-result-unit-price::text').extract()).split('$')
            img_small=str(annonce.css('.box-result-unit-photo img').css('img').xpath("@src").extract_first())
            adresse_complete=str(annonce.css('.box-result-unit-11A::text').extract())
            print(len(adresse_complete))
            if len(titre)>0:
                titre=titre[0]
            if len(url_annonce)!=0:
                #browser.get('https://www.logisquebec.com/a-louer/')
                browser.get(url_annonce1)
                html = browser.page_source
                soup = BeautifulSoup(html,'html.parser')
                #print(soup)
                ref_annonce=soup.select('.content-annonce-reference')
                id_="LGQ_"+ref_annonce[0].text.split(":")[1].strip()
                id_=u' '.join(id_).encode('utf-8').strip()
                cout=str(prix[0].encode('utf-8').strip())
                spl=str(cout[3:len(cout)]).split(' ')
                if len(str(cout[3:len(cout)]).split(' ')) >1:
                    prix_stg=str(spl[0])+str(spl[1])
                    #cout=float(prix_stg.encode('utf-8'))
                    try:
                        cout=float(str(prix_stg).strip())
                    except:
                        print(type(prix_stg))
                        print('erreur de conversion')
                else:
                    #cout=float(cout.encode('utf-8'))
                    cout=float(spl[0])
                det1=[]
                images=[]
                description=None
                dimension=None
                data={
                        #"loyer":loyer,
                        "titre":str(titre.strip().encode('utf8')),
                        "url":str(url_annonce1.encode('utf8')).strip(),
                        "cost":cout,
                        "adresse":adresse_complete.encode('utf-8').strip(),
                        "disponibilité":"",
                        "annonce":"",
                        "images":"",
                        "id_annonces":id_,
                        "petite_img":img_small
                        }
                yield data
#        browser.close()
        next_page='https://www.logisquebec.com/a-louer/'+str(logisquebecSpider.page_number)
        if logisquebecSpider.page_number<=496:
            logisquebecSpider.page_number+=1
            #browser.close()
            yield response.follow(next_page,callback=self.parse)
