# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


# useful for handling different item types with a single interface


class TenderParserPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect('./companies.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS companies;""")

        self.cursor.execute("""CREATE TABLE companies (
            company_name text,
            company_manager text,
            iin text
            ); 
        """)

    def store_db(self, item):
        self.cursor.execute("""
            INSERT INTO companies (company_name, company_manager, iin) VALUES(?, ?, ?);""",
                            (item['company_name'], item['company_manager'], item['iin'],))
        self.connection.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
