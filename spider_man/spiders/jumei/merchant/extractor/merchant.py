import re

from spider_man.crawler.extractors import BaseExtractor, JsonExtractor
from spider_man.crawler.fields import TextField, AttrField, FuncField, JsonField
from spider_man.spiders.jumei.merchant.items import MerchantItem

__all__ = ['MerchantPageExtractor', 'MerchantCollectionExtractor']


class MerchantPageExtractor():
    @classmethod
    def get_item(cls, response):
        return cls._extract(response)

    @classmethod
    def _extract(cls, response):
        item = MerchantExtractor.get_item(response)

        merchant_item = MerchantItem()
        merchant_item['store_id'] = item.storeId
        merchant_item['name'] = item.name
        merchant_item['logo'] = item.logo
        merchant_item['backgroundImg'] = item.backgroundImg
        merchant_item['certification'] = item.certification
        return merchant_item


class MerchantExtractor(BaseExtractor):
    storeId = FuncField()
    name = TextField(css_selector='div.shop-name h3')
    logo = AttrField(css_selector='h3.shop-logo img', attr='src')
    backgroundImg = AttrField(css_selector='div.shop-sign', attr='style')
    certification = TextField(css_selector='p#empower-icon')

    def parse_storeId(self, response):
        store_id = re.findall(r'store/(.*?)\.html', response.url)
        return store_id[0]

    def clean_backgroundImg(self, backgroundImg_text):
        if backgroundImg_text:
            backgroundImg = re.findall(r'background:url\((.*?)\)', backgroundImg_text)
            if backgroundImg:
                return backgroundImg[0]

    def clean_certification(self, certification_text):
        if certification_text:
            return certification_text
        else:
            return ''


class MerchantCollectionExtractor(JsonExtractor):
    collection = JsonField(json_selector='$.store.fav_count')


