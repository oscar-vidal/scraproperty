from ConfigParser import SafeConfigParser
import scrapy

class QuotesSpider(scrapy.Spider):

    name = "catastro"

    def start_requests(self):

        config = SafeConfigParser()
        config.read('properties/conf.cfg')

        url = config.get('site_info', 'url')

        print url

        urls = [
            url,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        EVENTVALIDATION = response.xpath("//*[@id='__EVENTVALIDATION']/@value").extract()
        VIEWSTATE = response.xpath("//*[@id='__VIEWSTATE']/@value").extract()
        VIEWSTATEGENERATOR = response.xpath("//*[@id='__VIEWSTATEGENERATOR']/@value").extract()

        #element_array = response.xpath("//select[@id='lcProvincias']/option")

        options = response.xpath("//*[@id='lcProvincias']/option[1]/text()")
        print options

        option_text = [option.text for option in options]

        print option_text

        print EVENTVALIDATION
        print VIEWSTATE
        print VIEWSTATEGENERATOR
        
