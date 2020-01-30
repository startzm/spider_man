from spider_man.crawler.utils.user_agent import FakeChromeUA


class UserAgentMiddleware(object):
    """ 随机更换User-Agent """

    def process_request(self, request, spider):
        request.headers['User-Agent'] = FakeChromeUA.get_ua()
        request.headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'


class BaiduUserAgentMiddleware(object):
    """ 使用baidu User-Agent """

    def process_request(self, request, spider):
        request.headers['User-Agent'] = 'Baiduspider-news'
        request.headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'


class UniqueUserAgentMiddleware(object):
    """ 使用Unique User-Agent """

    def process_request(self, request, spider):
        request.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) ' \
                                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 ' \
                                        'Safari/537.36'
        request.headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
