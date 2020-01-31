from scrapy import Request

from spider_man.crawler.base.spider import BaseSpider
from spider_man.database import MongoDB
from spider_man.spiders.jumei.merchant.extractor import MerchantPageExtractor,\
    MerchantCollectionExtractor

__all__ = ['MerchantSpider']


class MerchantSpider(BaseSpider):
    # 爬取商家信息
    name = 'merchant_spider'

    default_seed_vals = []
    default_origin_url = 'http://h5.jumei.com/s/store/%(seed_val)s.html'

    # 获取收藏人数URL
    default_collection_url = 'http://h5.jumei.com/pop/ajaxStoreFavStatus?store_id=%(seed_val)s'

    collect = 'goodStaticDetail'

    def _get_seed_val(self):
        # 获取种子
        for good in MongoDB[self.collect].find():
            if 'store_id' in good:
                self.default_seed_vals.append(good['store_id'])
        self.default_seed_vals = list(set(self.default_seed_vals))

    def parse(self, response):
        # 解析html
        self.logger.info('Requested url: %s', response.url)
        item = MerchantPageExtractor.get_item(response=response)
        if item:
            url = self.default_collection_url % {
                'seed_val': item['store_id']
            }
            yield Request(
                url,
                meta={
                    'item': item
                },
                callback=self.parse_collection
            )

    def parse_collection(self, response):
        # 解析收藏人数
        self.logger.info('Requested url: %s', response.url)
        item = response.meta.get('item')
        item['collection'] = MerchantCollectionExtractor.get_item(response).collection
        yield item
