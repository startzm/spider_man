from .base import BaseField


__all__ = ['ContainerField']


class ContainerField(BaseField):

    def _parse_element(self, element):
        return element
