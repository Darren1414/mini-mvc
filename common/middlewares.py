#coding=utf-8

import functools
from common.utils import *
from common.write_log import writelog

# 校验参数(可以校验string，number，int)
def verify_params(**kwargs):
    def decorator(method):
        @functools.wraps(method)
        def wrapper(view):
            try:
                for key in kwargs:
                    value = str(view.params.get(key, ''))
                    if not value:
                        return view._render.render_json(code='11000', data={}, msg='%s is empty!' % str(key))
                    # 字符串形式(默认接到的都是字符串)
                    if kwargs[key] == 'string':
                        pass
                    # 数值型
                    if kwargs[key] == 'number':
                        if not is_digit(value):
                            return view._render.render_json(code='11000', data={}, msg='%s must be digit!' % str(key))
                    # 整型
                    if kwargs[key] == 'int':
                        if not is_int(value):
                            return view._render.render_json(code='11000', data={}, msg='%s must be int!' % str(key))
            except:
                writelog(traceback.format_exc())

            return method(view)
        return wrapper
    return decorator