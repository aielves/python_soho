"""
@created by shadow on 2018.01.02
@resume 数据库连接池实现类
"""

# -*- coding: UTF-8 -*-

import threading

import MySQLdb
from DBUtils.PooledDB import PooledDB

from database.conf import DbConfig as Config
from utils.ClsUtils import ClsUtils

lock = threading.Lock()  # 连接池初始化需要资源锁保证线程安全


class JdbcPool(object):

    pool = None;

    @staticmethod
    def getConnect():
        if JdbcPool.pool is None:
            if lock.acquire():
                if JdbcPool.pool is None:
                    print(u'初始化数据库连接池')
                    try:
                        JdbcPool.pool = PooledDB(creator=MySQLdb, mincached=Config.DB_MIN_CACHED,
                                               maxcached=Config.DB_MAX_CACHED,
                                               maxshared=Config.DB_MAX_SHARED,
                                               maxconnections=Config.DB_MAX_CONNECYIONS,
                                               blocking=Config.DB_BLOCKING, maxusage=Config.DB_MAX_USAGE,
                                               setsession=Config.DB_SET_SESSION,
                                               host=Config.DB_HOST, port=Config.DB_PORT,
                                               user=Config.DB_USER, passwd=Config.DB_PASSWORD,
                                               db=Config.DB_DBNAME, use_unicode=False, charset=Config.DB_CHARSET)
                    except Exception as err:
                        print(u'数据库连接池初始化异常: ' + repr(err))
                    finally:
                        lock.release()  # 释放资源锁
        return JdbcPool.pool.connection()

    @staticmethod
    def close(connect, cursor):
        try:
            cursor.close()
            connect.close()
        except Exception as err:
            print(u'释放资源失败: ' + repr(err))


if __name__ == "__main__":
    user = ClsUtils.getClass("database.domain.IDEntity", "TestUser")
    keys = ClsUtils.getFields(user)
    size = keys.__len__();
    keyArr = []
    fields = str("")
    for key in keys:
        keyArr.append(key)
        fields += "," + key
    fields = fields[1:fields.__len__()]
    print(keyArr)
    connect = JdbcPool.getConnect();
    cursor = connect.cursor()
    sql = "select " + fields + " from oauth_user where id = '%s' or username = '%s'" % ('110', 'admin')
    print(sql)
    result = cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    for i in range(size):
        item = result[i]
        field = keyArr[i]
        if isinstance(item, int):
            item = int(item)
        if isinstance(item, str):
            item = str(item)
        if isinstance(item, bytes):
            item = item.decode()
        user.__setattr__(field, item)
    print(user.id)
    print(user.nickname)
    print(user.ctime)
    # 关闭数据库资源
    JdbcPool.close(connect, cursor)
