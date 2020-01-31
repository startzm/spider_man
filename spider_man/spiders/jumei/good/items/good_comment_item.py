import scrapy

__all__ = ['GoodCommentItem']


class GoodCommentItem(scrapy.Item):
    # 商品评价
    _id = scrapy.Field()
    product_id = scrapy.Field()
    filterList = scrapy.Field()
    page_count = scrapy.Field()
    row_count = scrapy.Field()
    rows_per_page = scrapy.Field()
    page_number = scrapy.Field()
    is_show_checkall = scrapy.Field()
    rate_high = scrapy.Field()
    tag = scrapy.Field()
