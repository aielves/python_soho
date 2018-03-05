"""
@created by shadow on 2018.01.02
@resume 实现数据库DB查询模版方法
"""

# -*- coding: UTF-8 -*-

from database.aop.JdbcPoolAop import InitJdbcPool


@InitJdbcPool
class JdbcOperation:

    connect = None
    cursor = None

    def initialize(self, connect, cursor):
        self.connect = connect
        self.cursor = cursor
        return self

    def release(self):
        if self.cursor is not None:
            try:
                self.cursor.close()
            except Exception as err:
                print(repr(err))
        if self.connect is not None:
            try:
                self.connect.close()
            except Exception as err:
                print(repr(err))

    def rollback(self):
        if self.cursor is not None:
            try:
                self.cursor.close()
            except Exception as err:
                print(repr(err))
        if self.connect is not None:
            try:
                self.connect.rollback()
            except Exception as err:
                print(repr(err))

    def execute(self, sql, param):
        if self.cursor is not None:
            return self.cursor.execute(sql, param)
        else:
            return None

    def commit(self):
        if self.connect is not None:
            try:
                self.connect.commit()
            except Exception as err:
                raise Exception
