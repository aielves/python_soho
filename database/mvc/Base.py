"""
@created by shadow on 2018.01.02
@resume 基本MVC模板方法,模板类
"""

# -*- coding: UTF-8 -*-

class IDEntity(object):

    def __init__(self):
        self.id = None

    def getTableName(self):
        pass



class BaseService():

    simpleJdbc = None

