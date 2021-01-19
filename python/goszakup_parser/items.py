# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TenderLot(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    company_manager = scrapy.Field()
    iin = scrapy.Field()


