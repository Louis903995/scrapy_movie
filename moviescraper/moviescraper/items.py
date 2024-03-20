import scrapy
from scrapy.item import Item, Field

class MovieItem(Item):
    Titre = Field()
    Titre0riginal = Field()
    Score = Field()
    Genre = Field()
    Année = Field()
    Durée = Field()
    Descriptions = Field()
    Acteurs = Field()
    Public = Field()
    Pays = Field()
    
