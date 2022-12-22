# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()
class PostgresPipeline(object):
    def __init__(self):

        self.conn = psycopg2.connect(host= os.getenv("HOST"),
                            dbname= os.getenv("DBNAME"),
                            user =  os.getenv("USER"),
                            password = os.getenv("PASSWORD"),
                            port =os.getenv("PORT"))
        self.cur = self.conn.cursor()

    def open_spider(self, spider):
        self.cur.execute("CREATE TABLE IF NOT EXISTS items (id serial PRIMARY KEY, title text, image_url text)")

    def close_spider(self, spider):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO items (title, image_url) VALUES (%s, %s)",
                         (item['title'], item['image_url']))
        return item