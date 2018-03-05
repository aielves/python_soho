"""
@created by shadow on 2018.03.04
@resume 数据库操作类初始化拦截器
"""

# -*- coding: UTF-8 -*-

import functools

from database.jdbc.JdbcOperation import JdbcOperation


def InitJdbcOperation(call_f):
    @functools.wraps(call_f)
    def wrapper(*args, **kwargs):
        try:
            call_r = call_f(*args, **kwargs)
            call_r.jdbc = JdbcOperation()
            return call_r
        except Exception as err:
            raise Exception(err)
    return wrapper