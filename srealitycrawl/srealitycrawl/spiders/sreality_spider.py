import scrapy
import json
import re
from srealitycrawl.items import SrealityItem

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']

    def parse(self, response, **kwargs):
        response_json = json.loads(response.body)
        sreality_item = SrealityItem()

        for flat in response_json.get('_embedded').get('estates'):
            title =  re.sub(r'\s', ' ', flat.get('name'))
            image_url = flat.get('_links').get('images')[0].get('href')
            sreality_item['title'] = title
            sreality_item['image_url'] = image_url
            yield sreality_item

