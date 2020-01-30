import uuid

import scrapy
import time
from scrapy import Request, FormRequest

from spider_man.crawler.logging.monitor import monitor_logger
from spider_man.custom_settings import MONGO_SETTINGS

__all__ = ['BaseSpider']


class BaseSpider(scrapy.Spider):
    # 默认源
    default_origin_url: str = ''
    # 默认请求
    default_origin_method: str = 'GET'
    # 默认请求
    default_origin_request_type: str = ''
    # 默认头
    default_origin_header: dict = None
    # 默认是否传递cookie
    default_origin_cookiejar: int = None
    # 默认cookie
    default_origin_cookie: dict = None

    # 默认是否使用代理类型: None, normal, short, realtime
    # normal 普通代理，不保证时效性
    # short 短效代理1~2分钟切换一次，期间使用同一IP
    # realtime 实时切换代理
    default_proxy_type: str = None
    # 是否降级切换(为了节省ip默认会做降级)
    default_proxy_demote: bool = True

    # 默认是否使用浏览器加载Ajax
    default_is_ajax: bool = None

    # 默认爬取页数
    default_page_num: int = 1
    # 每页默认条数
    default_page_size: int = 20
    # 每页偏移条数(非实际页面条数)
    default_page_offset_count: int = 10
    # 分页开始偏移URL
    default_page_start_offset: int = 1
    # 分页方式: default(默认分页)，manual(手动分页)
    default_page_next_method: str = 'default'

    # 种子值
    default_seed_vals: list = []
    # 默认开始页数
    default_current_page: int = 1

    # 爬虫配置
    custom_settings = MONGO_SETTINGS

    def _get_request_url(self, current_page, seed_val):
        request_url = self.default_origin_url

        if seed_val != 'default':
            seed_val = seed_val
        else:
            seed_val = None

        replace_map = [
            ('%(keyword)s', seed_val),
            ('%(seed_val)s', seed_val),

            ('%(current_page)s', current_page),

            ('%(page)s', current_page * self.default_page_offset_count),
            ('%(page_num)s', current_page * self.default_page_offset_count),
            ('%(offset)s', current_page * self.default_page_offset_count),

            ('%(size)s', self.default_page_size),
            ('%(limit)s', self.default_page_size),
            ('%(limits)s', self.default_page_size),

            ('%(time)s', int(time.time() * 1000)),
            ('%(timestamp)s', int(time.time() * 1000))
        ]

        for pattern in replace_map:
            request_url = request_url.replace(pattern[0], str(pattern[1]), 999)

        return request_url

    def _before_task(self):
        self._get_seed_val()

    def _get_seed_val(self):
        pass

    def _get_query_seed_val(self, seed_val):
        return seed_val

    def _get_request_header(self, current_page):
        return self.default_origin_header

    def _get_request_formdata(self, current_page):
        return None

    def _get_request_body(self, current_page):
        return None

    def _get_request_cookie(self, current_page):
        return self.default_origin_cookie

    def _get_request_meta(self, current_page):
        return {}

    def start_task(self):
        self.logger.info('Start Gen Request')
        self._before_task()

        page_num = self.default_page_num
        current_page = self.default_current_page

        # 页数偏移
        if self.default_page_next_method == 'manual':
            pages = [self.default_page_start_offset]
        else:
            if current_page != None:
                pages = [current_page]
            else:
                pages = range(self.default_page_start_offset, page_num + self.default_page_start_offset)

        # 种子集合
        if self.default_seed_vals:
            seed_vals = self.default_seed_vals
        else:
            seed_vals = ['default']
        for seed_val in seed_vals:
            for current_page in pages:
                request_urls = self._get_request_url(current_page, seed_val)
                request_formdata = self._get_request_formdata(current_page)
                request_body = self._get_request_body(current_page)
                request_header = self._get_request_header(current_page)
                request_cookie = self._get_request_cookie(current_page)
                request_meta = self._get_request_meta(current_page)

                # _get_request_url可生成多个链接的列表
                # 当生成单个链时，修正为单一链接
                if isinstance(request_urls, str):
                    request_urls = [request_urls]
                for request_url in request_urls:
                    basic_meta = {
                        'current_page': current_page,

                        'is_ajax': self.default_is_ajax,
                        'proxy_type': self.default_proxy_type,
                        'proxy_demote': self.default_proxy_demote,

                        'request_url': request_url,
                        'request_body': request_body,
                        'cookiejar': self.default_origin_cookiejar,
                    }
                    basic_meta.update(request_meta)

                    self.logger.info('Gen Request')
                    self.gen_monitor(seed_val)

                    if self.default_origin_request_type == 'FormRequest':
                        yield FormRequest(
                            request_url,
                            meta=basic_meta,
                            formdata=request_formdata,
                            headers=request_header,
                            cookies=request_cookie,
                            method=self.default_origin_method,
                            callback=self.parse,
                            dont_filter=True
                        )
                    else:
                        yield Request(
                            request_url,
                            meta=basic_meta,
                            body=request_body,
                            headers=request_header,
                            cookies=request_cookie,
                            method=self.default_origin_method,
                            callback=self.parse,
                            dont_filter=True
                        )

    def gen_monitor(self, seed_val):
        monitor_logger.info({
            'service': self.name,
            'step': 'start_task',
            'state': 200,
            'other': str(uuid.uuid1()),
            'text': seed_val,
            'logTime': int(time.time() * 1000),
            'cost': 0
        })

    def start_requests(self):
        return self.start_task()
