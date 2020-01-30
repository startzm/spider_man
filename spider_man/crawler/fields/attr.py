from .base import BaseField

__all__ = ['AttrField']


class AttrField(BaseField):

    def __init__(self,
                 attr,
                 css_selector: str=None,
                 xpath_selector: str=None,
                 default='',
                 many: bool=False):
        super(AttrField, self).__init__(
            css_selector=css_selector,
            xpath_selector=xpath_selector,
            default=default,
            many=many)
        self.attr = attr

    def _parse_element(self, element):
        return element.get(self.attr)