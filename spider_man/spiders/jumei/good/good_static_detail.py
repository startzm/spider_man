from scrapy import Request

from spider_man.crawler.base.spider import BaseSpider
from spider_man.database import MongoDB
from spider_man.spiders.jumei.good.extractor import GoodStaticDetailPageExtractor,\
    GoodDetailCommentPageExtractor


class GoodStaticDetailSpider(BaseSpider):
    # 爬虫名
    name = 'goodStaticDetail_spider'

    default_seed_vals = []
    # 详情页url
    default_origin_url = 'http://m.jumei.com/product/ajaxStaticDetail?item_id=%(item_id)s&type=%(type)s'
    # 详情页评价URL
    default_comment_url = 'http://koubei.jumei.com/api/v1/getThreadAndReportAndComment.html?' \
                          'product_id=%(product_id)s&is_pop=1&order=image&page=1&page_size=3'

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
        item = GoodStaticDetailPageExtractor.get_item(response=response)
        if item:
            comment_url = self.default_comment_url % {
                'product_id': item['product_id']
            }
            yield Request(
                comment_url,
                meta={
                    'item': item
                },
                callback=self.parse_comment
            )

    def parse_comment(self, response):
        # 爬取详情页评价，默认加载3条
        self.logger.info('Requested url: %s', response.url)
        yield GoodDetailCommentPageExtractor.get_item(response=response)
