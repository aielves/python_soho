"""
@created by shadow on 2018.01.02
@resume 科学计算工具类,加减乘除保留自定义有效小数位(不保留四舍五入)
"""

# -*- coding: UTF-8 -*-

import decimal


def add(number1, number2, scale):
    return fmt(str(decimal.Decimal(number1).__add__(decimal.Decimal(number2))), scale)


def subtract(number1, number2, scale):
    return fmt(str(decimal.Decimal(number1).__sub__(decimal.Decimal(number2))), scale)


def divide(number1, number2, scale):
    return fmt(str(decimal.Decimal(number1) / (decimal.Decimal(number2))), scale)


def multiply(number1, number2, scale):
    return fmt(str(decimal.Decimal(number1).__mul__(decimal.Decimal(number2))), scale)


def lt(number1, number2):
    bool = decimal.Decimal(number1).compare(decimal.Decimal(number2));
    if (bool < 0):
        return True
    else:
        return False


def lte(number1, number2):
    bool = decimal.Decimal(number1).compare(decimal.Decimal(number2));
    if (bool <= 0):
        return True
    else:
        return False


def gt(number1, number2):
    bool = decimal.Decimal(number1).compare(decimal.Decimal(number2));
    if (bool > 0):
        return True
    else:
        return False


def gte(number1, number2):
    bool = decimal.Decimal(number1).compare(decimal.Decimal(number2));
    if (bool >= 0):
        return True
    else:
        return False


def fmt(number1, scale):
    scale = int(scale);  # 转成int类型
    if (scale <= 0):
        scale = 0
    number1 = str(number1);  # 转成str类型
    if ("." in number1):
        split_str = number1.split(".");  # 按小数点分割两块数值
        str1 = split_str[0]
        str2 = split_str[1]
        if (str2.__len__() > scale):  # 小数位数超出scale位,则保留scale位
            str2 = str2[0:scale]
        if (str2 != ""):
            str2 = cover4zero(str2, scale)
    else:
        str1 = number1
        if (scale > 0):
            str2 = cover4zero(0, scale);
    if (str2 != ""):
        return str1 + "." + str2
    else:
        return str1;


# 判断是否不足位数,不足则补0
def cover4zero(number2, scale):
    number2 = str(number2)
    if (number2.__len__() >= scale):
        return number2;
    start = 0
    end = scale - number2.__len__()
    while (start < end):
        number2 = number2 + "0";
        start = start + 1
    return number2


r = divide("5", "3.05", 7);
print(r)
