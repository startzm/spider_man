from scrapy.crawler import _get_spider_loader

from spider_man.database import RedisDB


class MongoDBPipeline(object):
    spider_name = ''
    db_name = ''
    college_set = None

    def __init__(self, settings):
        for name in _get_spider_loader(settings).list():
            self.spider_name = name
            self.db_name = self.spider_name.split('_')[0]

    def open_spider(self, spider):
        self.college_set = MongoDB[self.db_name]

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.college_set.insert(item)
        return item

