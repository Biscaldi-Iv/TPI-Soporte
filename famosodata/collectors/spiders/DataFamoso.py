from itemloaders import processors
import scrapy
from ..items import CollectorsItem
from scrapy.loader import ItemLoader
from ..lectorCSV import enumeradorURLS

next_url = enumeradorURLS(start=1300, cant=725)


class FamousSpider(scrapy.Spider):
    name = "DataFamous"

    start_urls = [
        next(next_url),
        next(next_url),
        next(next_url),
    ]

    def parse(self, response):
        pers = ItemLoader(item=CollectorsItem())
        pers.add_value(
            'nombre', response.xpath('//h3[contains(text(),"Full Name:")]/following-sibling::span/text()').get())
        pers.add_value('fortuna', response.css(
            'strong.net-profile_header_networth::text').get())
        pers.add_value(
            'altura', response.xpath('//h3[contains(text(),"Height:")]/following-sibling::span/text()').get())
        pers.add_value(
            'peso', response.xpath('//h3[contains(text(),"Weight:")]/following-sibling::span/text()').get())
        pers.add_value(
            'fnac', response.xpath('//h3[contains(text(),"Date of Birth:")]/following-sibling::span/text()').get())
        pers.add_value(
            'nacionalidad', response.xpath('//h3[contains(text(),"Nationality:")]/following-sibling::span/text()').get())

        yield pers.load_item()
        try:
            siguiente = next(next_url)
            if siguiente is not None:
                yield response.follow(siguiente, callback=self.parse)
        except:
            pass
