import scrapy

class GovItem(scrapy.Item):
    domain_collection = scrapy.Field() #站点urlmd5编码
    html   = scrapy.Field() #html的urlmd5编码
    images = scrapy.Field()
    pdf    = scrapy.Field()
    xls    = scrapy.Field()
    others = scrapy.Field()

