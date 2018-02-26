"""
@created by shadow on 2018.01.02
@resume SQL逻辑运算实现
"""

# -*- coding: UTF-8 -*-

class SqlSymbol:
    EQ = " = "
    NOTEQ = " <> "
    LT = " < "
    LTE = " <= "
    GT = " > "
    GTE = " >= "
    ISNULL = " IS NULL ";
    NOTNULL = " IS NOT NULL "
    BETWEEN = " BETWEEN "
    NOTBETWEEN = " NOT BETWEEN "
    IN = " IN "
    NOTIN = " NOT IN "
    LIKE = " LIKE "
    NOTLIKE = " NOT LIKE "
    OR = " OR "
    ORDERBY = " ORDER BY "


class SortBy:
    ASC = " ASC ";
    DESC = " DESC ";


class Condition:
    def __init__(self, symbol, key, value):
        self.symbol = symbol
        self.key = key
        self.value = value


class Pageable:
    def __init__(self, pageNo, pageSize):
        self.pageNo = pageNo
        self.pageSize = pageSize
        self.pageTotal = 0
        self.pageNumber = 0
        self.data = None


class Cnd:
    def __init__(self):
        self.coditArr = []
        self.distinctArr = []
        self.groupbyArr = []
        self.fieldsArr = []
        self.otherArr = []
        self.onlyField = ""
        self.pageable = None

    # 等于条件
    def eq(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.EQ, key, value))
        return self;

    # 不等于条件
    def noteq(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.NOTEQ, key, value))
        return self;

    # 小于条件
    def lt(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.LT, key, value))
        return self;

    # 小于等于条件
    def lte(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.LTE, key, value))
        return self;

    # 大于条件
    def gt(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.GT, key, value))
        return self;

    # 大于等于条件
    def gte(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.GTE, key, value))
        return self;

    # 为空条件
    def isnull(self, key):
        self.coditArr.append(Condition(SqlSymbol.ISNULL, key, None))
        return self;

    # 不为空条件
    def notnull(self, key):
        self.coditArr.append(Condition(SqlSymbol.NOTNULL, key, None))
        return self;

    # 等于区间条件
    def between(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.BETWEEN, key, value))
        return self;

    # 不等于区间条件
    def notbetween(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.NOTBETWEEN, key, value))
        return self;

    # 等于集合区间条件
    def in_(self, key, *value):
        self.coditArr.append(Condition(SqlSymbol.IN, key, value))
        return self;

    # 不等于集合区间条件
    def notin_(self, key, *value):
        self.coditArr.append(Condition(SqlSymbol.NOTIN, key, value))
        return self;

    # 等于模糊字符条件
    def like(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.LIKE, key, value))
        return self;

    # 不等于模糊字符条件
    def notlike(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.NOTLIKE, key, value))
        return self;

    # 或条件
    def or_(self, *value):
        self.coditArr.append(Condition(SqlSymbol.OR, None, value))
        return self;

    # 分页条件
    def limit(self, pageNo, pageSize):
        self.pageable = Pageable(pageNo, pageSize)
        return self;

    # 字段去重条件
    def distinct(self, *keys):
        for key in keys:
            self.distinctArr.append(key)
        return self;

    # 字段分组条件
    def groupby(self, *keys):
        for key in keys:
            self.groupbyArr.append(key)
        return self;

    # 排序字段条件
    def orderby(self, key, value):
        self.coditArr.append(Condition(SqlSymbol.ORDERBY, key, value))
        return self;

    # 指定查询多个字段列
    def fields(self, *keys):
        for key in keys:
            self.fieldsArr.append(key)
        return self;

    # 指定查询单个字段列
    def only(self, key):
        self.onlyField = str(key)
        return self;

    # 获取逻辑条件集合
    def getConditions(self):
        return self.coditArr

    # 获取分页对象
    def getPageable(self):
        return self.pageable

    # 根据条件更新字段
    def addUpdateKeyValue(self, key, value):
        pass
        return self;

    # 指定额外的字段参数
    def addOther(self, key, value):
        pass
        return self;

    def clone(self):
        cnd = Cnd()
        cnd.coditArr = self.coditArr
        cnd.distinctArr = self.distinctArr
        cnd.groupbyArr = self.groupbyArr
        cnd.fieldsArr = self.fieldsArr
        cnd.otherArr = self.otherArr
        cnd.onlyField = self.onlyField
        cnd.pageable = self.pageable
        return cnd


if __name__ == '__main__':
    cnd1 = Cnd();
    cnd1.eq("id", 1).in_("test", 1, 2).fields("id", "name", "nick").only("test").limit(1, 10)

    cnd = cnd1.clone()


    for condition in cnd.coditArr:
        print(str(condition.symbol) + "---" + str(condition.key) + "---" + str(condition.value))
    for field in cnd.fieldsArr:
        print(field)
    for goupby in cnd.groupbyArr:
        print(goupby)
    print(cnd.onlyField)

    pageable = cnd.pageable
    if (pageable != None):
        print(str(pageable.pageNo) + "---" + str(pageable.pageSize))
