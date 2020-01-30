# -*- coding: utf-8 -*-

# 该文件存储用户自定义设置

# mongoDB配置
# URI为地址，DB为数据库名
MONGO_URI = 'localhost'
MONGO_DB = 'shopping'


# sqlite3配置
# SQLITE_DB为数据库名,默认存放路径：根目录/database/sqlite
SQLITE_DB = 'jumei.sqlite'


# redis配置
# HOST为地址，PORT为端口
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

CHROME_FILEPATH = '/drivers/chromedriver'
# SPLASH_URL = config.SPLASH_URL
# SPLASH_SETTINGS = config.SPLASH_SETTINGS

# 配置数据处理PIPELINE
SQLITE_PIPELINE = 'spider_man.crawler.pipelines.sqlite.SqliteDBPipeline'
MONGODB_PIPELINE = 'spider_man.crawler.pipelines.mongo.MongoDBPipeline'


MONGO_SETTINGS = {
    'ITEM_PIPELINES': {MONGODB_PIPELINE: 300}
}

SQLITE_SETTINGS = {
    'ITEM_PIPELINES': {SQLITE_PIPELINE: 300}
}