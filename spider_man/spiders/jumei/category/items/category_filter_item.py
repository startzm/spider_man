import scrapy

__all__ = ['CategoryFilterItem']


class CategoryFilterItem(scrapy.Item):
    _id = scrapy.Field()
    # 父分类ID
    category_id = scrapy.Field()
    # 子分类
    category = scrapy.Field()
    # 功效
    function = scrapy.Field()
    # 品牌
    brand = scrapy.Field()
