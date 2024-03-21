import scrapy
from scrapy.item import Item, Field

class MovieItem(scrapy.Item):
    Titre = scrapy.Field()
    Titre0riginal = scrapy.Field()
    Score = scrapy.Field()
    Genre = scrapy.Field()
    Année = scrapy.Field()
    Durée = scrapy.Field()
    Descriptions = scrapy.Field()
    Acteurs = scrapy.Field()
    Public = scrapy.Field()
    Pays = scrapy.Field()
    
