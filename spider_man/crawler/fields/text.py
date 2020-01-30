import re
from html import unescape
from lxml import etree
from w3lib.html import remove_tags

from .base import BaseField


__all__ = ['TextField']


class TextField(BaseField):

    def _parse_element(self, element):
        string = remove_tags(etree.tostring(element, encoding='utf-8', pretty_print=True, method='html'))
        if string:
            string = unescape(string)
            string = re.sub(r'(\r\n|\n|\r)', '', string)
            string = string.strip()
        return string if string else self.default
