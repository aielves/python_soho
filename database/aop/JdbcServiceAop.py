"""
@created by shadow on 2018.03.04
@resume 数据库事务拦截器
"""

# -*- coding: UTF-8 -*-

import functools

from sqlcode.SimpleJdbc import SimpleJdbc


def InitService(call_f):
    @functools.wraps(call_f)
    def wrapper(*args, **kwargs):
        try:
            call_r = call_f(*args, **kwargs)
            call_f.simpleJdbc = SimpleJdbc()
            return call_r
        except Exception as err:
            raise Exception(err)
    return wrapper

def Transactional(auto):
    def func_wrapper(call_f):
        @functools.wraps(call_f)
        def return_wrapper(*args, **kwargs):
            try:
                jdbc = args.__getitem__(0).simpleJdbc.jdbc
                call_r =  call_f(*args, **kwargs)  # call the wrapped function
                jdbc.commit()
                return  call_r
            except Exception as err:
                print(repr(err))
                if auto == True:
                    jdbc.rollback()
            finally:
                jdbc.release()
        return return_wrapper
    return func_wrapper
