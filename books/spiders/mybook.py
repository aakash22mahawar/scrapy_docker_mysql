import scrapy
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import time




class MybookSpider(scrapy.Spider):
    name = 'mybook'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']


    def parse(self, response):
        books=response.xpath('//article[@class="product_pod"]')
        for book in books:
          yield{
            'name':book.xpath('.//h3/a/text()').get(),
            'image':book.xpath('.//div/a/img/@src').get()
            }

def run_spider():
    configure_logging()
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(MybookSpider)
    print('<<<< Crawler is running >>>>')
    process.start()


if __name__ == '__main__':
    start = time.time()
    run_spider()
    print('<<<<<<<<<<<<<<<<<<<<<Entire Data has been Scraped>>>>>>>>>>>>>>>>>>>>')
    end = time.time()
    print(round((end - start), 4), '****Time in Seconds****')