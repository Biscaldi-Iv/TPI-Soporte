import scrapy
#from ..lectorCSV import enumeradorURLS

class FamousSpider(scrapy.Spider):
    name = "DataFamous"

    start_urls = [
        'https://www.therichest.com/celebnetworth/celeb/actors/mel-gibson-net-worth/',
        'https://www.therichest.com/celebnetworth/athletes/nba/michael-jordan-net-worth/',
        'https://www.therichest.com/celebnetworth/athletes/baseball/alex-rodriguez-net-worth/',
    ]

    def parse(self, response):
        return {'nombre': response.xpath('//h3[contains(text(),"Full Name:")]/following-sibling::span/text()').get(),
                'fortuna': response.css('strong.net-profile_header_networth::text').get(),
                'altura':response.xpath('//h3[contains(text(),"Height:")]/following-sibling::span/text()').get(),
                'peso':response.xpath('//h3[contains(text(),"Weight:")]/following-sibling::span/text()').get(),
                'fnac':response.xpath('//h3[contains(text(),"Date of Birth:")]/following-sibling::span/text()').get(),
                'nacionalidad':response.xpath('//h3[contains(text(),"Nationality:")]/following-sibling::span/text()').get(),}


