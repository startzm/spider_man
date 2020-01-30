from lxml import etree
from scrapy.http import Response

from spider_man.crawler.exceptions import *
from spider_man.crawler.fields import FieldMeta, ContainerField, FuncField

__all__ = ['BaseExtractor']


class ExtractorMeta(type):
    """
    Metaclass for an item
    """

    def __new__(cls, name, bases, attrs):
        __fields = dict({(field_name, attrs.pop(field_name))
                         for field_name, object in list(attrs.items())
                         if isinstance(object, FieldMeta)})
        attrs['__fields'] = __fields
        new_class = type.__new__(cls, name, bases, attrs)
        return new_class


class BaseExtractor(metaclass=ExtractorMeta):

    def __init__(self):
        self.ignore_item = False
        self.results = {}

    @classmethod
    def _extract(cls,
                 html_etree: etree._Element=None,
                 json_dict: dict=None,
                 response: Response=None):
        item_ins = cls()
        fields_dict = getattr(item_ins, '__fields', {})

        for field_name, field_value in fields_dict.items():
            parse_method = getattr(item_ins, f'parse_{field_name}', None)
            clean_method = getattr(item_ins, f'clean_{field_name}', None)

            # When parse method exists
            if parse_method and isinstance(field_value, FuncField):
                value = parse_method(response)
            else:
                value = field_value.extract(html_etree=html_etree, json_dict=json_dict)

            # When clean method exists
            if clean_method:
                value = clean_method(value)

            setattr(item_ins, field_name, value)
            item_ins.results[field_name] = value
        return item_ins

    @classmethod
    def _get_container_field(cls):
        item_ins = cls()
        container_fields = []
        fields_dict = getattr(item_ins, '__fields', {})

        for field_name, field_value in fields_dict.items():
            if isinstance(field_value, ContainerField):
                container_fields.append(field_value)

        if len(container_fields) == 0:
            raise ContainerFieldNotExistException

        if len(container_fields) > 1:
            raise ContainerFieldTooManyException
        return container_fields[0]

    @classmethod
    def _handle_reseponse_text(cls,
           response: Response = None,
           response_text: str=None):
        if not response:
            raise ResponseNotExistException

        if response_text:
            return response_text
        else:
            return response.text

    @classmethod
    def get_items(cls,
            response: Response=None,
            response_text: str=None):
        response_text = cls._handle_reseponse_text(response=response, response_text=response_text)

        html_etree = etree.HTML(response_text)
        container_field = cls._get_container_field()

        if container_field:
            container_field.many = True
            container_html_etree = container_field.extract(
                html_etree=html_etree
            )
            if container_html_etree:
                for each_html_etree in container_html_etree:
                    item = cls._extract(each_html_etree, response=response)
                    yield item

    @classmethod
    def get_item(cls,
            response: Response=None,
            response_text: str=None):
        response_text = cls._handle_reseponse_text(response=response, response_text=response_text)
        html_etree = etree.HTML(response_text)
        return cls._extract(html_etree, response=response)

    def __repr__(self):
        return f'<Item {self.results}>'