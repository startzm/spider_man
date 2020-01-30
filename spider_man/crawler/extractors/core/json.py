import json

from scrapy.http import Response
from .base import BaseExtractor


__all__ = ['JsonExtractor']


class JsonExtractor(BaseExtractor):

    @classmethod
    def get_items(cls,
            response: Response=None,
            response_text: object=None):
        response_text = cls._handle_reseponse_text(response=response, response_text=response_text)

        # 添加类型判断
        if isinstance(response_text, str):
            json_dict = json.loads(response_text)
        else:
            json_dict = response_text

        container_field = cls._get_container_field()

        if container_field:
            container_field.many = True
            container_array = container_field.extract(
                json_dict=json_dict
            )

            if container_array:
                for each_dict in container_array:
                    item = cls._extract(json_dict=each_dict, response=response)
                    yield item

    @classmethod
    def get_item(cls,
                 response: Response = None,
                 response_text: str = None):
        response_text = cls._handle_reseponse_text(response=response, response_text=response_text)

        # 添加类型判断
        if isinstance(response_text, str):
            json_dict = json.loads(response_text)
        else:
            json_dict = response_text

        return cls._extract(json_dict=json_dict, response=response)
