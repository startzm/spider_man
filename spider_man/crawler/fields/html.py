from lxml import etree

from .base import BaseField


__all__ = ['HtmlField']


class HtmlField(BaseField):

    def _parse_element(self, element):
        return etree.tostring(element).decode(encoding='utf-8')
