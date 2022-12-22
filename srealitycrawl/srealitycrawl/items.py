# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SrealityItem(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()

    # def __repr__(self):
    #     return repr({"title": self.title, "image_urls":self.image_url})

