import scrapy

from w3lib.html import remove_tags

from ..items import Company


class CompanySpider(scrapy.Spider):
    name = 'tender'

    page_number = 2
    last_page = 15

    start_urls = ['https://tenderplus.kz/organization?page=1']

    def parse(self, response, **kwargs):
        items = Company()

        companies = response.css('div.company-teaser')
        for company in companies:
            company_name = company.css('a.link::text').get()
            company_manager = company.css('div.detail-value::text').get()
            iin = company.css('span.search-attribute::text').get()
            items['company_name'] = company_name
            items['company_manager'] = company_manager
            items['iin'] = iin
            yield items

        next_page = f'https://tenderplus.kz/organization?page={self.page_number}'
        if self.page_number <= self.last_page:
            self.page_number += 1
            yield scrapy.Request(next_page, callback=self.parse)




