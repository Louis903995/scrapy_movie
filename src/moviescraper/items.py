import scrapy
from scrapy.item import Item, Field

def duree_en_min(value):
    return  


class MovieItem(scrapy.Item):
    url = scrapy.Field()
    titre = scrapy.Field()
    titre_original = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    annee = scrapy.Field()
    duree = scrapy.Field()
    description = scrapy.Field()
    acteurs = scrapy.Field()
    pays = scrapy.Field()

class MoviescraperItem(scrapy.Item):
    name = scrapy.Field()
    pass 
    
