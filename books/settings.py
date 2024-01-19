# Scrapy settings for books project


BOT_NAME = 'books'

SPIDER_MODULES = ['books.spiders']
NEWSPIDER_MODULE = 'books.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_ENABLED = True
LOG_LEVEL = 'INFO'

# download settings
DOWNLOAD_DELAY = 0
DOWNLOAD_TIMEOUT = 5
AUTOTHROTTLE_ENABLED = True
CONCURRENT_REQUESTS = 16 # Increase the number of concurrent request
CONCURRENT_ITEMS = 50

AUTOTHROTTLE_TARGET_CONCURRENCY = 8



#other settings
COOKIES_ENABLED = False
RETRY_ENABLED = True
REDIRECT_ENABLED = False
AJAXCRAWL_ENABLED = False
REACTOR_THREADPOOL_MAXSIZE = 8
DNS_RESOLVER = "scrapy.resolver.CachingHostnameResolver"
HTTPCACHE_ENABLED = False
RETRY_HTTP_CODES = [429]
RETRY_TIMES = 3

DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'books.useragent_middleware.MyUserAgentsMiddleware': 400,
  }


# MySQL Database Settings
MYSQL_HOST = 'mysql'    #pls use service name of docker corresponding to mysql
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'confident22'
MYSQL_PORT = 3306
MYSQL_DATABASE = 'books'
MYSQL_AUTOCOMMIT = True  # Set to True to enable autocommit

# Enable and configure the MySQL pipeline
ITEM_PIPELINES = {
    'books.pipelines.MysqlPipeline': 300,
}