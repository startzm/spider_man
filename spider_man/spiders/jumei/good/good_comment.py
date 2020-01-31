from spider_man.crawler.base.spider import BaseSpider
from spider_man.database import MongoDB
from spider_man.spiders.jumei.good.extractor import GoodCommentPageExtractor

__all__ = ['GoodCommentSpider']


class GoodCommentSpider(BaseSpider):
    # 爬取商品评价
    name = 'goodComment_spider'

    default_seed_vals = []
    default_origin_url = 'http://koubei.jumei.com/api/v1/getThreadAndReportAndComment.html?' \
                         'product_id=%(seed_val)s&is_pop=1&order=image&page=1&page_size=20'

    collect = 'categoryGood'

    def _get_seed_val(self):
        # 获取种子
        for good in MongoDB[self.collect].find():
            if 'product_id' in good:
                self.default_seed_vals.append(good['product_id'])

    def parse(self, response):
        # 解析html
        self.logger.info('Requested url: %s', response.url)
        item = GoodCommentPageExtractor.get_item(response=response)
        if item:
            yield item
