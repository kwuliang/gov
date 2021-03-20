BOT_NAME = 'gov'

SPIDER_MODULES = ['gov.spiders']
NEWSPIDER_MODULE = 'gov.spiders'


MONGO_URI = '127.0.0.1:27017'
MONGO_DB = 'scrapy_gov'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# for example DATA_DIR = '/home/user/data/'
DATA_DIR = ''

# for example DOMAINS_LIST = '/home/user/sites.xls'
DOMAINS_LIST = ''

SPLASH_URL = 'http://localhost:8050'

# Use redis to duplicate repeated data
REDIS_DUPLICATE = True

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}

ITEM_PIPELINES = {
   'gov.pipelines.MongoPipeline':300,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
