import scrapy
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver

class logisquebecSpider(scrapy.Spider):
    name = 'logisquebecSpider'
    allowed_domains = ['www.logisquebec.com']
    start_urls = ['https://www.logisquebec.com/a-louer/']
    page_number=2
    def parse(self, response):
        #ouvrir la page avec phantomJS
        #browser = webdriver.PhantomJS()
        #browser.get(logisquebecSpider.start_urls[0])
        annonces=response.css('.box-result-unit-louer')
        for annonce in annonces:
            url_annonce=annonce.css('#box-result-unit-title a').xpath("@href").extract_first()
            url_annonce1="https://www.logisquebec.com"+str(url_annonce)
            titre=annonce.css('#box-result-unit-title a').css('a::text').extract()
            prix=str(annonce.css('.box-result-unit-price::text').extract()).split('$')

            if len(url_annonce)!=0:
                browser.get('https://www.logisquebec.com/a-louer/')
                browser.get(url_annonce)
                #html = browser.page_source
                #soup = BeautifulSoup(html,'html.parser')
                cout=prix[0]
                det1=[]
                images=[]
                description=None
                dimension=None
                data={
                        #"loyer":loyer,
                        "titre":str(titre.encode('utf8')).strip(),
                        "url":str(url_annonce1.encode('utf8')).strip(),
                        "cost":str(cout.encode('utf8')).strip()
                        }
                yield data
#        browser.close()
        next_page='https://www.logisquebec.com/a-louer/'+str(logisquebecSpider.page_number)
        if logisquebecSpider.page_number<=496:
            logisquebecSpider.page_number+=1
            browser.close()
            yield response.follow(next_page,callback=self.parse)
