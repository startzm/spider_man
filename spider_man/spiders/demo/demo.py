import json

from spider_man.crawler.base.spider import BaseSpider
from spider_man.crawler.extractors import JsonExtractor
from spider_man.crawler.fields import ContainerField, JsonField
from spider_man.database import MongoDB
from spider_man.spiders.demo.items.category_filter_item import CategoryFilterItem


class CategoryFilterExtractor(JsonExtractor):
    container = ContainerField(json_selector='$.data.filter.[*]')
    category = JsonField(json_selector='$.category')
    function = JsonField(json_selector='$.function')
    brand = JsonField(json_selector='$.brand')


class DemoSpider(BaseSpider):
    # 爬虫名
    name = 'demo_spider'
    # 种子集合
    default_seed_vals = []
    # 默认URL
    default_origin_url = 'http://m.jumei.com/search/index?category_id=%(seed_val)s&ajax=get'
    # 从mongodb集合获取种子
    collect = 'category'

    def _get_seed_val(self):
        # 获取种子
        for category in MongoDB[self.collect].find():
            if 'sub_categories' in category:
                for sub_category in category['sub_categories']:
                    self.default_seed_vals.append(sub_category['category_id'])

    def parse(self, response):
        # 解析html
        self.logger.info('Requested url: %s', response.url)
        item = json.loads(response.text)
        if item:
            category_filter_item = CategoryFilterItem()
            category_filter_item['category_id'] = item['category_id']
            category_filter_item['category'] = item['data']['filter']['category']
            category_filter_item['function'] = item['data']['filter']['function']
            category_filter_item['brand'] = item['data']['filter']['brand']
            yield category_filter_item
