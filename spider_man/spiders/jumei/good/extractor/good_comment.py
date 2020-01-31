import re

from spider_man.spiders.jumei.good.extractor import GoodDetailCommentExtractor
from spider_man.spiders.jumei.good.items import GoodCommentItem

__all__ = ['GoodCommentPageExtractor']


class GoodCommentPageExtractor():
    @classmethod
    def get_item(cls, response):
        return cls._extract(response)

    @classmethod
    def _extract(cls, response):
        item = GoodDetailCommentExtractor.get_item(response)

        comment_item = GoodCommentItem()
        comment_item['product_id'] = re.findall('product_id=(.*?)&', response.url)[0]
        comment_item['filterList'] = item.filterList
        comment_item['page_count'] = item.page_count
        comment_item['row_count'] = item.row_count
        comment_item['rows_per_page'] = item.rows_per_page
        comment_item['page_number'] = item.page_number
        comment_item['is_show_checkall'] = item.is_show_checkall
        comment_item['rate_high'] = item.rate_high
        comment_item['tag'] = item.tag

        if comment_item['product_id']:
            return comment_item
