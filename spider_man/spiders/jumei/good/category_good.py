import json

from spider_man.crawler.base.spider import BaseSpider
from spider_man.database import MongoDB
from spider_man.spiders.jumei.good.extractor import CategoryGoodPageExtractor


class CategoryGoodSpider(BaseSpider):
    # 爬虫名
    name = 'categoryGood_spider'

    default_seed_vals = []
    default_page_num = 10
    default_origin_url = 'http://m.jumei.com/search/index?category_id=%(seed_val)s&page=%(current_page)s&ajax=get'

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
        for item in CategoryGoodPageExtractor.get_items(response=response):
            if item:
                yield item
