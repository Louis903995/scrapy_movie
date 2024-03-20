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
        movie_item["titre"] = product.css("")
        movie_item["titre0riginal"] = product.css("")
        movie_item["score"] = product.css("")
        movie_item["genre"] = product.css("")
        movie_item["année"] = product.css("")
        movie_item['durée'] = product.css("")
        movie_item['description'] = product.css("")
        movie_item['acteurs'] = product.css("")
        movie_item['public'] = product.css("")
        movie_item['pays'] = product.css("")

        yield movie_item 


class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        movies = response.css('')
        for movie in movies:
            relative_url = response.css('').get()

            if 'catalogue/' in relative_url:
                next_page_url = '' + relative_url
            else:
                next_page_url = '' + relative_url
            yield response.follow(movie_url, callback=self.parse_movie_page)
    
        next_page = response.css('').get()
        if next_page is None:
            if 'catalogue/' in next_page:
                next_page_url = '' + next_page
            else:
                next_page_url = '' + relative_url
            yield response.follow(next_page_url, callback=self.parse)

    def parse_movie_page(self, response):

        table_rows = response.css("")

