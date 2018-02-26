"""
@created by shadow on 2018.01.02
@resume 数据库连接池实现类
"""

# -*- coding: UTF-8 -*-

import threading

import MySQLdb
from DBUtils.PooledDB import PooledDB

from database import DbConfig as Config

lock = threading.Lock()  # 连接池初始化需要资源锁保证线程安全


class DbPool(object):
    pool = None;

    @staticmethod
    def init():
        if DbPool.pool is None:
            if lock.acquire():
                print(u'初始化数据库连接池')
                DbPool.pool = PooledDB(creator=MySQLdb, mincached=Config.DB_MIN_CACHED,
                                       maxcached=Config.DB_MAX_CACHED,
                                       maxshared=Config.DB_MAX_SHARED,
                                       maxconnections=Config.DB_MAX_CONNECYIONS,
                                       blocking=Config.DB_BLOCKING, maxusage=Config.DB_MAX_USAGE,
                                       setsession=Config.DB_SET_SESSION,
                                       host=Config.DB_HOST, port=Config.DB_PORT,
                                       user=Config.DB_USER, passwd=Config.DB_PASSWORD,
                                       db=Config.DB_DBNAME, use_unicode=False, charset=Config.DB_CHARSET)
                lock.release()  # 释放资源锁
        return DbPool.pool.connection()

    @staticmethod
    def close(connect, cursor):
        cursor.close()
        connect.close()
        # print(u'释放资源:connect和cursor');


if __name__ == "__main__":
    for i in range(0, 10):
        connect = DbPool.init();
        cursor = connect.cursor()
        sql = "select * from oauth_user where id = '%s' or username = '%s'" % ('110', 'admin')
        result = cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        # for item in result:
        #     print(item)
        DbPool.close(connect, cursor)
