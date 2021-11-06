# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import itemloaders, ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def fortune(w: str):
    try:
        w = w.replace('$', '')
        if 'Billion' in w:
            f = 1000000000
            x, _ = w.split(' ')
            f = f*float(x)
            return f
        elif 'Million' in w:
            f = 1000000
            x, _ = w.split(' ')
            f = f*float(x)
            return f
        else:
            return None
    except:
        return None


def to_metro_float(a: str):
    try:
        a.replace('\\', '')
        if ('(' in a) and ('m' in a) and (')' in a):
            """Contiene altura en metros"""
            _, a = a.split('(')
            a = a.replace(')', '')
            a = a.replace('m', '')
            return float(a)
        elif "'" in a:
            """Se procesan pies"""
            pies, res = a.split("'")
            pies = pies.replace("'", '')
            pies = pies.replace(" ", '')
            pies = int(pies)
            metros = pies/3.2808399
            if '"' in res:
                """Se procesan pulgadas"""
                pulgadas = res.replace('"', '')
                pulgadas = pulgadas.replace(' ', '')
                pulgadas = int(pulgadas)/39.3700787
                metros += pulgadas
            return metros
        return None
    except:
        return None


def toKgFloat(peso: str):
    try:
        peso = peso.replace(',', '.').replace(' ', '')
        if ('(' in peso) and ('kg' in peso) and (')' in peso):
            _, peso = peso.split('(')
            peso = peso.replace(')', '').replace('kg', '')
            return float(peso)
        peso = peso.replace('lbs', '')
        peso = float(peso)/2.20462262
        return float(peso)
    except:
        return None

# Falta procesar y convertir a date la fecha de nacimiento


class CollectorsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nombre = scrapy.Field()
    fortuna = scrapy.Field(input_processor=MapCompose(fortune))
    altura = scrapy.Field(input_processor=MapCompose(
        to_metro_float))
    peso = scrapy.Field(input_processor=MapCompose(toKgFloat))
    fnac = scrapy.Field()
    nacionalidad = scrapy.Field()
