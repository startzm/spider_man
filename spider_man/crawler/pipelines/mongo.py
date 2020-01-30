from scrapy.crawler import _get_spider_loader

from spider_man.database import MongoDB


class MongoDBPipeline(object):
    spider_name = ''
    db_name = ''
    college_set = None

    # def __init__(self, settings):
    #     if not self.spider_name:
    #         for name in _get_spider_loader(settings).list():
    #             self.spider_name = name
    #
    # @classmethod
    # def from_crawler(cls, spider):
    #     return cls(spider.settings)

    def open_spider(self, spider):
        # 取爬虫名‘_’之前的字符为集合名
        print('使用mongoDB')
        self.spider_name = spider.name
        if self.spider_name:
            self.db_name = self.spider_name.split('_')[0]
            self.college_set = MongoDB[self.db_name]
            print('使用集合', self.db_name)
        else:
            print('获取爬虫失败')

    def close_spider(self, spider):
        # self.spider_name = ''
        # print('guanbi')
        pass

    def process_item(self, item, spider):
        self.college_set.insert(item)
        return item

