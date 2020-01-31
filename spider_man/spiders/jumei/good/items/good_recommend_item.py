import scrapy

__all__ = ['GoodRecommendItem']


class GoodRecommendItem(scrapy.Item):
    # 相关推荐
    _id = scrapy.Field()
    item_id = scrapy.Field()
    item_list = scrapy.Field()
