import redis

from spider_man.custom_settings import REDIS_HOST, REDIS_PORT

__all__ = ['RedisDB']


pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT)
RedisDB = redis.StrictRedis(connection_pool=pool)