"""
@created by shadow on 2018.01.02
@resume SQL默认CRUD功能实现
"""

# -*- coding: UTF-8 -*-
from database.aop.JdbcOperationAop import InitJdbcOperation
from utils.ClsUtils import ClsUtils


@InitJdbcOperation
class SimpleJdbc:

    jdbc = None

    # 数据库保存方法
    def save(self, model):
        if model is None:
            print(u'保存对象不能为空')
            return 0
        fields = ClsUtils.getFields(model)
        if fields is None:
            print(u'保存对象字段不能为空')
            return 0
        part1 = str("")
        part2 = str("")
        param = []
        for field in fields:
            part1 += "," + field
            part2 += ",%s"
            value = model.__getattribute__(field)
            if isinstance(value, int):
                param.append(int(value))
            elif isinstance(value, str):
                param.append(str(value))
            else:
                param.append(None)
        part1 = part1[1:part1.__len__()]
        part2 = part2[1:part2.__len__()]
        sql = 'insert into ' + model.getTableName() + '(' + part1 + ') values(' + part2 + ')'
        return self.jdbc.execute(sql, param)

    # 数据库修改方法
    def update(self, *args):
        pass

    # 数据库删除方法
    def delete(self, *args):
        pass

    # 数据库通过ID查询方法
    def findById(self, *args):
        pass

    # 数据库查询单条记录方法
    def findOneByCnd(self, *args):
        pass

    # 数据库查询多条记录方法
    def findByCnd(self, *args):
        pass

    # 数据库查询全部记录方法
    def findAll(self):
        pass

    # 数据库查询单独的字段单条集合
    def findOnlyOneByCnd(self, *args):
        pass

    # 数据库查询单独的字段集合
    def findOnlyByCnd(self, *args):
        pass

    # 数据库统计总记录数
    def countAll(self, *args):
        pass

    # 数据库按条件统计总记录数
    def countByCnd(self, *args):
        pass

