import scrapy

from spider_man.crawler.extractors import JsonExtractor
from spider_man.crawler.fields import ContainerField, JsonField
from spider_man.custom_settings import MONGO_SETTINGS
from spider_man.spiders.jumei.category.items.index_category_item import CategoryItem


class IndexCategoryExtractor(JsonExtractor):
    container = ContainerField(json_selector='$.data[*]')
    category_id = JsonField(json_selector='$.category_id')
    name = JsonField(json_selector='$.name')
    sub_categories = JsonField(json_selector='$.sub_categories')


class IndexCategorySpider(scrapy.Spider):
    # 首页商品分类
    name = 'category_spider'

    start_urls = ['http://mobile.jumei.com/msapi/mall/allcategories.json']

    custom_settings = MONGO_SETTINGS

    def parse(self, response):
        self.logger.info('Requested url: %s', response.url)
        for item in IndexCategoryExtractor.get_items(response=response):
            type_item = CategoryItem()
            type_item['category_id'] = item.category_id
            type_item['name'] = item.name
            type_item['sub_categories'] = item.sub_categories
            yield type_item
