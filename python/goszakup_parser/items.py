# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TenderLot(scrapy.Item):
    # define the fields for your item here like:
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    lot_name = scrapy.Field()
    sponsor = scrapy.Field()
    iin = scrapy.Field()
    document = scrapy.Field()
    id_number = scrapy.Field()


