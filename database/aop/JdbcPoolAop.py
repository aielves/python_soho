"""
@created by shadow on 2018.03.04
@resume 数据库连接初始化拦截器
"""

# -*- coding: UTF-8 -*-

import functools

from database.jdbc.JdbcPool import JdbcPool


def InitJdbcPool(call_f):
    @functools.wraps(call_f)
    def wrapper(*args, **kwargs):
        try:
            call_r = call_f(*args, **kwargs)
            connect = JdbcPool.getConnect();
            return call_r.initialize(connect, connect.cursor())
        except Exception as err:
            raise Exception(err)
    return wrapper