import scrapy
from moviescraper.items import MoviesItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    custom_settings = {
        'FEEDS': { 'data.csv': { 'format': 'csv',}}
    }

    def start_request(self):
        url = ''
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        product = response.css("")

        book_item =
        book_item
        book_item
        book_item
        book_item
        book_item 