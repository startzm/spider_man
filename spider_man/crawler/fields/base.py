from jsonpath import jsonpath
from lxml import etree

__all__ = ['FieldMeta', 'BaseField']


class FieldMeta():
    pass


class BaseField(FieldMeta):

    def __init__(self,
                 css_selector: str=None,
                 xpath_selector: str=None,
                 json_selector: str=None,
                 default=None,
                 many: bool=False):
        self.css_selector = css_selector
        self.xpath_selector = xpath_selector
        self.json_selector = json_selector
        self.default = default
        self.many = many
        self.results = []

    def _remove_elem(self, nums, val):
        coun = nums.count(val)
        for index in range(coun):
            nums.remove(val)
        return len(nums)

    def _get_elements(self,
                *,
                html_etree: etree._Element,
                json_dict: dict):
        if self.css_selector:
            elements = html_etree.cssselect(self.css_selector)
        elif self.xpath_selector:
            elements = html_etree.xpath(self.xpath_selector)
        elif self.json_selector:
            elements = jsonpath(json_dict, self.json_selector)
            if not elements:
                elements = []
        else:
            elements = []
        if not self.many:
            elements = elements[:1]
        return elements

    def _parse_element(self, element):
        raise NotImplementedError

    def extract(self,
                *,
                html_etree: etree._Element=None,
                json_dict: dict=None):
        elements = self._get_elements(html_etree=html_etree, json_dict=json_dict)

        # 当解析不到元素时
        if not elements and not self.default:
            return [] if self.many else None

        if elements:
            results = [self._parse_element(element) for element in elements]
        else:
            results = [self.default]
        return results if self.many else results[0]
