import scrapy
from moviescraper.items import MoviesItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    all
    custom_settings = {
        'FEEDS': { 'data.csv': { 'format': 'csv',}}
    }

    def start_request(self):
        url = ''
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        product = response.css("")

        movie_item = MoviesItem
        movie_item =
        movie_item =
        movie_item =
        movie_item =
        movie_item =

        yield movie_item 

class MoviespiderSpider(scrapy, Spider):
    name = 'moviespider'
    allowed_domains = ['']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        pass