from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

from spider_man.custom_settings import SQLITE_DB

__all__ = ['SqliteDB']

SQLITE = 'sqlite'


class SqliteDB:
    # sqlite初始化
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print('使用Sqlite数据库：', self.db_engine)
        else:
            print("连接数据库失败！")

    def create_db_tables(self, table_name, columns):
        # 创建数据表，需要传入两个参数:str类型的表名和list类型的所有字段名
        # 默认创建一个_id字段为主键
        metadata = MetaData()

        column_list = []
        column_list.append(Column('_id', Integer, primary_key=True, autoincrement=True))
        for column_name in columns:
            column_list.append(Column(column_name, String))

        table = Table(table_name, metadata, *column_list)

        try:
            metadata.create_all(self.db_engine)
            print("创建表格成功：", table_name)
        except Exception as e:
            print("创建表格失败")
            print(e)
