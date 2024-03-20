import scrapy
from moviescraper.items import MovieItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    custom_settings = {
        'FEEDS': { 'data.csv': { 'format': 'csv',}}
    }

    def start_request(self):
        url = 'https://www.imdb.com/chart/top/'
        yield scrapy.Request(url, callback=self.parse)

    
    def parse(self, response):
        product = response.css("")

        movie_item = MovieItem()
        movie_item["titre"] = product.css("").extract_first()
        movie_item["titre0riginal"] = response.xpath("")
        movie_item["score"] = response.xpath("")
        movie_item["genre"] = response.xpath("")
        movie_item["année"] = response.xpath("")
        movie_item['durée'] = response.xpath("")
        movie_item['description'] = response.xpath("")
        movie_item['acteurs'] = response.xpath("")
        movie_item['public'] = response.xpath("")
        movie_item['pays'] = response.xpath("")

        yield movie_item 


class MoviespiderSpider(scrapy, Spider):
    name = 'moviespider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        pass