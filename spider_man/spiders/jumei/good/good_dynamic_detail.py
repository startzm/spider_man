from spider_man.crawler.base.spider import BaseSpider
from spider_man.database import MongoDB
from spider_man.spiders.jumei.good.extractor import GoodDynamicDetailPageExtractor


class GoodDynamicDetailSpider(BaseSpider):
    # 爬虫名
    name = 'goodDynamicDetail_spider'

    default_seed_vals = []
    default_origin_url = 'http://m.jumei.com/product/ajaxDynamicDetail?item_id=%(item_id)s&type=%(type)s'

    collect = 'categoryGood'

    def _get_request_url(self, current_page, seed_val):
        urls = []
        ids, types = self.get_good_id(self.collect)
        for id, type in zip(ids, types):
            urls.append(self.default_origin_url % {
                'item_id': id,
                'type': type
            })
        return urls

    def get_good_id(self, collect):
        # 获取种子
        good_ids = []
        good_types = []
        for good in MongoDB[collect].find():
            if 'type' in good and 'item_id' in good:
                good_ids.append(good['item_id'])
                good_types.append(good['type'])
        return good_ids, good_types

    def parse(self, response):
        # 解析html
        self.logger.info('Requested url: %s', response.url)
        item = GoodDynamicDetailPageExtractor.get_item(response=response)
        if item:
            yield item