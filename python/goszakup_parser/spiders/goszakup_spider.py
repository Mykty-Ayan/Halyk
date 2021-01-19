import scrapy

from ..items import TenderLot


class GoszakupSpider(scrapy.Spider):

    name = 'goszakup'

    page_number = 2

    start_urls = ['https://www.goszakup.gov.kz/ru/search/lots?count_record=25&page=1']

    def parse(self, response, **kwargs):
        last_page = 3


