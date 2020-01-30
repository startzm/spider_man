from .base import BaseField


__all__ = ['JsonField']


class JsonField(BaseField):

    def _parse_element(self, element):
        return element