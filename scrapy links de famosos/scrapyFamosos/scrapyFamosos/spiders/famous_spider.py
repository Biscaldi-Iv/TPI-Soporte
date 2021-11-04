import scrapy


class FamousSpider(scrapy.Spider):
    name = "famous"

    start_urls = [
        'https://www.therichest.com/top-lists/top-100-richest-actors/',
        'https://www.therichest.com/top-lists/top-100-richest-actresses/',
        'https://www.therichest.com/top-lists/top-100-richest-athletes/',
        'https://www.therichest.com/top-lists/top-100-richest-businessmen/',
        'https://www.therichest.com/top-lists/top-100-richest-models/',
        'https://www.therichest.com/top-lists/top-100-richest-baseball-players/',
        'https://www.therichest.com/top-lists/top-100-richest-basketball-players/',
        'https://www.therichest.com/top-lists/top-100-richest-businesswomen/',
        'https://www.therichest.com/top-lists/top-100-richest-ceos/',
        'https://www.therichest.com/top-lists/top-100-richest-celebrities/',
        'https://www.therichest.com/top-lists/top-100-richest-comedians/',
        'https://www.therichest.com/top-lists/top-100-richest-directors/',
        'https://www.therichest.com/top-lists/top-100-richest-entrepreneurs/',
        'https://www.therichest.com/top-lists/top-100-richest-hockey-players/',
        'https://www.therichest.com/top-lists/top-100-richest-musicians/',
        'https://www.therichest.com/top-lists/top-100-richest-nfl-players/',
        'https://www.therichest.com/top-lists/top-100-richest-producers/',
        'https://www.therichest.com/top-lists/top-100-richest-rappers/',
        'https://www.therichest.com/top-lists/top-100-richest-singers/',
        'https://www.therichest.com/top-lists/top-100-richest-soccer-players/',
        'https://www.therichest.com/top-lists/top-100-richest-tv-personalities/'

    ]

    def parse(self, response):
        for fila in response.css('tr'):
            yield {
                'link': fila.css('td.name a::attr(href)').get(),
            }

        siguiente = response.css('a.next').attrib['href']
        if siguiente is not None:
            yield response.follow(siguiente, callback=self._parse)