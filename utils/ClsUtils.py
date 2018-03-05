"""
@created by shadow on 2018.02.27
@resume Class反射工具类
"""

# -*- coding: UTF-8 -*-

import importlib


class ClsUtils:

    @staticmethod
    def getClass(module, dname):
        try:
            newmod = importlib.import_module(str(module))
            newcls = getattr(newmod, str(dname))
            return newcls()
        except Exception as err:
            print(str(module) + "." + str(dname) + "构建实例失败: " + repr(err))

    @staticmethod
    def getFields(clsobj):
        if clsobj is None:
            return None
        keyArr = []
        for key in clsobj.__dict__.keys():
            keyArr.append(str(key))
        if keyArr.__len__() == 0:
            return None
        else:
            return keyArr
