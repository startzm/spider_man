from .base import BaseField


__all__ = ['IntegerField']


class IntegerField(BaseField):

    def _parse_element(self, element):
        strings = [node.strip() for node in element.itertext()]
        string = ''.join(strings)
        return int(string) if string else self.default
