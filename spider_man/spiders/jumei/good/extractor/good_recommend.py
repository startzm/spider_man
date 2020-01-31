import re

from spider_man.crawler.extractors import JsonExtractor
from spider_man.crawler.fields import JsonField
from spider_man.spiders.jumei.good.items import GoodRecommendItem

__all__ = ['GoodRecommendPageExtractor']


class GoodRecommendPageExtractor():
    @classmethod
    def get_item(cls, response):
        return cls._extract(response)

    @classmethod
    def _extract(cls, response):
        item = GoodRecommendExtractor.get_item(response)
        comment_item = GoodRecommendItem()
        comment_item['item_id'] = re.findall('item_id=(.*?)&', response.url)[0]
        comment_item['item_list'] = item.item_list
        return comment_item


class GoodRecommendExtractor(JsonExtractor):
    item_list = JsonField(json_selector='$.item_list')