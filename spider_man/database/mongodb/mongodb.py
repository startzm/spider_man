from pymongo import MongoClient

from spider_man.custom_settings import MONGO_URI, MONGO_DB

__all__ = ['MongoDB']


client = MongoClient(MONGO_URI)
MongoDB = client[MONGO_DB]

