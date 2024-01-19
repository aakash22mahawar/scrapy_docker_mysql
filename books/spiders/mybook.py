from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import logging




class MybookSpider(CrawlSpider):
    name = 'mybook'
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    book_details = LinkExtractor(restrict_css='article.product_pod')
    rule_book_details = Rule(book_details, callback='parse_item', follow=False)
    # next_page = LinkExtractor(restrict_css='li.next>a')
    # next_page_details = Rule(next_page, follow=True)
    # rules = (rule_book_details, next_page_details)
    rules = (rule_book_details,)

    def parse_item(self, response):
        try:
            if response.status == 200:
                logging.info(
                    f"url: {response.url}, status: {response.status}, 'user_agent': {response.request.headers['User-Agent']}")
                main = response.xpath('//div[@class="col-sm-6 product_main"]')

                title = main.css('h1::text').get()
                price = main.css('p.price_color::text').get() if main.css('p.price_color') else '#NA'
                avail = main.css('p.instock.availability::text').getall()[-1].strip() if main.css(
                    'p.instock.availability') else '#NA'
                item = {'title': title, 'price': price, 'availability': avail}
                logging.info(f"Scraped item: {item}")

                yield item

            else:
                logging.error(f"Failed URL: {response.url}, Failed Status: {response.status}")
        except Exception as e:
            logging.error(f"Script halted prematurely for URL: {response.url}")
            logging.exception(e)


if __name__ == '__main__':
    configure_logging(install_root_handler=False)
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(MybookSpider)
    logging.info('<<<< Crawler is running >>>>')
    process.start()