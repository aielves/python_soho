class IDEntity:
    def __init__(self):
        self.id = None


class Crud:
    # 数据库保存方法
    def insert(self, *args):
        pass

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

#
# class OAuthUser(IDEntity):
#     def __init__(self):
#         super().__init__()
#         self.name = None
