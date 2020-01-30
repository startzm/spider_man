import base64
import os
import time
import hashlib
import dateparser
import moment
import urllib
import json
import re

from datetime import datetime
from urllib.parse import urlparse
from dateparser.search import search_dates

from .timeutils import TimeUtils


__all__ = ['md5', 'parse_time']


# md5加密
def md5(code, length=None):
    res = hashlib.md5(code.encode('utf8')).hexdigest()
    if length is None:
        return res
    else:
        return res[:length]

# 获取url参数
def url_query_to_dict(url):
    query = urllib.parse.urlparse(url).query
    return dict([(k, v[0]) for k, v in urllib.parse.parse_qs(query).items()])

# 解析时间
def parse_time(time_str):
    def _search_dates(str):
        datetime = search_dates(str,
                                languages=['zh'],
                                settings={
                                    'DATE_ORDER': 'YMD',
                                    'STRICT_PARSING': True,
                                    'PREFER_LANGUAGE_DATE_ORDER': True,
                                    'PREFER_DATES_FROM': 'past'
                                })
        return int(time.mktime(datetime[0][1].timetuple())) * 1000

    def _is_valid_hour_time(str):
        '''判断是否是一个有效的日期字符串'''
        try:
            time.strptime(str, '%H:%M')
            return True
        except:
            return False

    def _format_date(time_str):
        '''
            格式化时间以便可以正常解析
            1、转化 年、月、日 为 -
            2、去掉 . 为 -
        '''
        if '月' in time_str and '日' in time_str:
            time_str = time_str\
                    .replace('年', '-')\
                    .replace('月', '-')\
                    .replace('日', ' ')

        if '.' in time_str:
            time_str = time_str\
                    .replace('.', '-')
        return time_str

    time_str = _format_date(time_str)
    # 格式化时间
    if _is_valid_hour_time(time_str):
        time_str = ' '.join([
            datetime.now().strftime('%Y-%m-%d'),
            time_str
        ])

    if '刚刚' in time_str or '刚才' in time_str:
        return int(time.time() * 1000)
    elif len(time_str.split('-')) == 2 or '前' in time_str:
        date_tuple = search_dates(str(time_str))
        if date_tuple:
            return int(time.mktime(date_tuple[0][1].timetuple()) * 1000)
        else:
            parse_time = dateparser.parse(str(time_str))
            return int(time.mktime(parse_time.timetuple()) * 1000)
    else:
        timestamp = None
        try:
            timestamp = _search_dates(time_str)
        except:
            moment_time = moment.date(time_str)
            if moment_time:
                timestamp = _search_dates(moment_time.format('YYYY-M-D H:m:s'))
        finally:
            return timestamp

# 通过文本获取时间戳
def get_timestamp(datestr):
    return int(time.mktime(dateparser.parse(datestr).timetuple())) * 1000

# 获取当前时间离0点时间差
def get_offset_today():
    zero_stamp = int(time.mktime(dateparser.parse('今天 00:00').timetuple())) * 1000
    return time.time() * 1000 - zero_stamp

# 生成验证信息
def gen_authorization():
    env = os.environ.get('spider_man_env', 'dev')
    env = env.split('_')[0]
    if env == 'local':
        env = 'dev'
    return md5(env)

# 判断是否为json
def is_json(json_str):
    try:
        json.loads(json_str)
    except ValueError as e:
        return False
    return True

# 生成uuid
def get_url_uuid(origin_url):
    if origin_url.startswith('https://'):
        origin_url = origin_url.replace('https://', 'http://', 1)
    origin_url = trim(origin_url, '/')
    return md5(origin_url)


def trim_left(str, replace_str):
    if str.startswith(replace_str):
        return str[len(replace_str):]
    return str

def trim_right(str, replace_str):
    if str.endswith(replace_str):
        return str[0: -len(replace_str)]
    return str

def trim(str, replace_str):
    return_str = trim_left(str, replace_str)
    return trim_right(return_str, replace_str)

# 过滤HTML
def filter_html(html):
    pattern = re.compile(r'<[^>]+>', re.S)
    return pattern.sub('', html)

# base64 decode
def base64decode(origin_str):
    if(len(origin_str) % 3 == 1):
        origin_str += '=='
    elif(len(origin_str)%3 == 2):
        origin_str += '='
    origin_str = bytes(origin_str, encoding='utf8')
    return base64.b64decode(origin_str).decode()

# 如果只有日期没有时间，hour, minute, second转换成当前采集时间
def optimazat_pubtime(timestamp):
    """
    如果只有日期没有时间，hour, minute, second转换成当前采集时间
    """
    if timestamp:
        if TimeUtils.is_zero_time(timestamp):
            now_date = time.strftime('%Y-%m-%d %H:%M:%S')
            target_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp/1000))
            target_date = target_date[:-8] + now_date[-8:]
            timestamp = int(time.mktime(time.strptime(target_date, '%Y-%m-%d %H:%M:%S'))) * 1000
    return timestamp