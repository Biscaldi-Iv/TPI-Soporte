import scrapy


class FamousSpider(scrapy.Spider):
    name = "nameFamous"

    start_urls = [
        'https://www.therichest.com/celebnetworth/celeb/actors/shahrukh-khan-net-worth/',
    ]

    def parse(self, response):
        return {'nombre': response.css('h1.net-profile_header_title::text').get(),}
