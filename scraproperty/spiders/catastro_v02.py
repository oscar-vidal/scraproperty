import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class QuotesSpider(scrapy.Spider):

    name = "catastro2"

    def __init__(self):
        #self.driver = webdriver.Chrome('/Users/oscar/code/scrape_catastro/drivers/chromedriver') 
        #self.driver = webdriver.Firefox('/Users/oscar/code/scrape_catastro/drivers/geckodriver') 
        self.driver = webdriver.Firefox() 

    def __del__(self):
        self.driver.close()

    def start_requests(self):
        urls = [
            'https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        self.driver.get(response.url)

        element_array = self.driver.findElement(By.xpath("//select[@id='lcProvincias']/option"))
        print element_array        

        EVENTVALIDATION = response.xpath("//*[@id='__EVENTVALIDATION']/@value").extract()
        VIEWSTATE = response.xpath("//*[@id='__VIEWSTATE']/@value").extract()
        VIEWSTATEGENERATOR = response.xpath("//*[@id='__VIEWSTATEGENERATOR']/@value").extract()
        

        #element_array = response.xpath("//select[@id='lcProvincias']/option")

        #options = response.xpath("//*[@id='lcProvincias']/option").extract()
        #print options

        #option_text = [option.text for option in options]

        #print option_text

        #print EVENTVALIDATION
        #print VIEWSTATE
        #print VIEWSTATEGENERATOR
        
