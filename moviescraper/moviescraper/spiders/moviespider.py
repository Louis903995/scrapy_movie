 import scrapy
from moviescraper.items import MovieItem

class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    custom_settings = {
        'FEEDS': {
            'data.csv': {
                'format': 'csv',
            }
        }
    }

    def parse(self, response):
      movies = response.xpath("//main//div[@data-testid='chart-layout-main-column']//ul[1]/li")
  
      for movie in movies:
          relative_url = movie.xpath(".//a[last()]/@href").get()
          if relative_url:
              movie_url = "https://www.imdb.com/" + relative_url
              yield scrapy.Request(movie_url, callback=self.parse_movie_page)
    
    
    
    def parse_movie_page(self, response):
        
        content = response.xpath("//main")
        movie_item = MovieItem()

        movie_item["url"] = response.url
        movie_item["titre"] = content.xpath(".//h1/span[@data-testid='hero__primary-text']/text()").get()
        movie_item["titre_original"] = content.xpath(".//h1/following-sibling::div/text()").get()
        movie_item["score"] = content.xpath(".//div[@data-testid='hero-rating-bar__aggregate-rating__score']/span[1]/text()").get()
        movie_item["genre"] = content.xpath(".//div[@data-testid='genres']//text()").getall()
        movie_item["année"] = content.xpath(".//h1/following-sibling::ul/li[1]//text()").get()
        movie_item['durée'] =  content.xpath(".//h1/following-sibling::ul/li[3]//text()").get()
        movie_item['description'] = content.xpath(".//p[@data-testid='plot']//text()").get()
        movie_item['acteurs'] = content.xpath(".//p[@data-testid='plot']/following-sibling::div//li[@data-testid='title-pc-principal-credit'][3]//li//text()").getall()
        movie_item['pays'] = content.xpath(".//li[@data-testid='title-details-origin']/div[last()]//text()").get()

        yield MovieItem
        