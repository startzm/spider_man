import scrapy

from sqlalchemy import Table, Column, Integer, String, MetaData

__all__ = ['CategoryItem']


class CategoryItem(scrapy.Item):
    _id = scrapy.Field()
    type = scrapy.Field()
    # 种类ID
    category_id = scrapy.Field()
    # 种类名
    name = scrapy.Field()
    # 子分类
    sub_categories = scrapy.Field()


# metadata = MetaData()
# table = Table('type', metadata,
#               Column('id', Integer, primary_key=True),
#               Column('category_id', String),
#               Column('name', String)
#               )
