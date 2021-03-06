from itemloaders import processors
import scrapy
from ..items import CollectorsItem
from scrapy.loader import ItemLoader
from ..lectorCSV import enumeradorURLS
from bs4 import BeautifulSoup
import requests
import os
import time

start_n = 1801
next_url = enumeradorURLS(start=start_n, cant=224)


class FamousSpider(scrapy.Spider):
    name = "DataFamous"

    start_urls = [
        next(next_url),
    ]

    def parse(self, response):
        """Carga datos"""
        pers = ItemLoader(item=CollectorsItem())
        pers.add_value(
            'nombre', response.xpath('//h3[contains(text(),"Full Name:")]/following-sibling::span/text()').get())
        img_name = 'anonimo.jpg'
        try:
            img_name = (response.xpath(
                '//h3[contains(text(),"Full Name:")]/following-sibling::span/text()').get()).replace(' ', '-').replace('"', '')+'.jpg'
        except:
            pass

        pers.add_value('img_name', img_name)

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
        global start_n
        start_n += 1
        yield pers.load_item()
        print(
            f"###############################    ITEM CARGADO   {start_n=}   #############################################")
        """Carga de imagen"""
        if img_name != 'anonimo.jpg':

            image_link = response.xpath(
                '/html/body/div[2]/div[4]/article/header/div/meta/@content').get()

            try:
                os.mkdir(os.path.join(os.getcwd(), 'famousimg'))
            except:
                pass

            os.chdir(os.path.join(os.getcwd(), 'famousimg'))
            try:
                time.sleep(2)
                with open(img_name, 'wb') as f:
                    im = requests.get(image_link)
                    f.write(im.content)

                print(
                    f"###############################    IMAGEN CARGADA   {start_n=}   #############################################")

            except:
                print(
                    f"###############################    IMAGEN NO CARGADA   {start_n=}   #############################################")
            os.chdir('..')

        try:
            siguiente = next(next_url)
            if siguiente is not None:
                yield response.follow(siguiente, callback=self.parse)
        except:
            pass
