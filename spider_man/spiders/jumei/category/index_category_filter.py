import json

import scrapy
from scrapy import Request

from spider_man.crawler.extractors import JsonExtractor
from spider_man.crawler.fields import ContainerField, JsonField
from spider_man.custom_settings import MONGO_SETTINGS
from spider_man.database import MongoDB
from spider_man.spiders.jumei.category.items.category_filter_item import CategoryFilterItem


class CategoryFilterExtractor(JsonExtractor):
    container = ContainerField(json_selector='$.data.filter.[*]')
    category = JsonField(json_selector='$.category')
    function = JsonField(json_selector='$.function')
    brand = JsonField(json_selector='$.brand')


class CategoryFilterSpider(scrapy.Spider):
    # 商品分类筛选，包括子分类、品牌、功效
    name = 'categoryFilter_spider'

    # 商品分类集合名
    collect = 'category'

    default_category_url = 'http://m.jumei.com/search/index?category_id=%(category_id)s&ajax=get'

    custom_settings = MONGO_SETTINGS

    def start_requests(self):
        ids = self.get_category_id(self.collect)
        for id in ids:
            yield Request(
                url=self.default_category_url % {
                    'category_id': id
                },
                callback=self.parse
            )

    def get_category_id(self, collect):
        category_ids = []
        for category in MongoDB[collect].find():
            if 'sub_categories' in category:
                for sub_category in category['sub_categories']:
                    category_ids.append(sub_category['category_id'])
        return category_ids

    def parse(self, response):
        self.logger.info('Requested url: %s', response.url)

        item = json.loads(response.text)
        if item:
            category_filter_item = CategoryFilterItem()
            category_filter_item['category_id'] = item['category_id']
            category_filter_item['category'] = item['data']['filter']['category']
            category_filter_item['function'] = item['data']['filter']['function']
            category_filter_item['brand'] = item['data']['filter']['brand']
            yield category_filter_item
