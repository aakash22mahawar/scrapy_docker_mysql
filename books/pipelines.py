import mysql.connector
from scrapy.exceptions import DropItem
import logging
import traceback

class MysqlPipeline:
    def __init__(self, mysql_config):
        self.mysql_config = mysql_config

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_config={
                'host': crawler.settings.get('MYSQL_HOST'),
                'user': crawler.settings.get('MYSQL_USER'),
                'password': crawler.settings.get('MYSQL_PASSWORD'),
                'database': crawler.settings.get('MYSQL_DATABASE'),
                'autocommit': crawler.settings.get('MYSQL_AUTOCOMMIT'),
            }
        )

    def open_spider(self, spider):
        self.connection = mysql.connector.connect(**self.mysql_config)
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            query = """INSERT INTO books (
                title, price, availability
            ) VALUES (%s, %s, %s)"""

            values = (
                item["title"],
                item["price"],
                item["availability"]
            )

            self.cursor.execute(query, values)
            spider.log("++++ Item has been pushed into MySQL ++++", level=logging.INFO)

        except Exception as e:
            # Log the exception to help with debugging
            spider.log(f"Error processing item: {e}", level=logging.INFO)
            spider.log(traceback.format_exc(), level=logging.INFO)  # Add this line to print the traceback
            raise DropItem("Item processing failed")

        return item


