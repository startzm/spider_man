import scrapy

__all__ = ['MerchantItem']


class MerchantItem(scrapy.Item):
    _id = scrapy.Field()
    store_id = scrapy.Field()
    name = scrapy.Field()
    logo = scrapy.Field()
    backgroundImg = scrapy.Field()
    certification = scrapy.Field()
    collection = scrapy.Field()
