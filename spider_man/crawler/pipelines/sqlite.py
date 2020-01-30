import sqlite3

from scrapy.crawler import _get_spider_loader

from spider_man.database import SqliteDB
from spider_man.custom_settings import SQLITE_DB


class SqliteDBPipeline:
    SQLITE = 'sqlite'
    spider_name = ''
    table_name = ''
    db = None
    is_created = False
    conn = None
    c = None

    insert_statement = 'INSERT INTO %(table_name)s %(keys)s VALUES %(values)s'

    def open_spider(self, spider):
        for name in _get_spider_loader(spider.settings).list():
            self.spider_name = name
            self.table_name = self.spider_name.split('_')[0]
        self.db = SqliteDB(self.SQLITE, dbname=SQLITE_DB)
        self.conn = sqlite3.connect(SQLITE_DB)
        self.c = self.conn.cursor()

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if not self.is_created:
            self.create_tables(list(item.keys()))
            self.is_created = True
        else:
            keys = str(tuple(item.keys())).replace("'", '')
            values = str(tuple(item.values()))
            SQL = self.insert_statement % {
                'table_name': self.table_name,
                'keys': keys,
                'values': values
            }
            print(SQL)
            self.c.execute(SQL)
            self.conn.commit()
        return item

    def create_tables(self, columns):
        self.db.create_db_tables(self.table_name, columns)

