#coding=utf-8

import json
import traceback
from common.render import Render
from common.write_log import writelog
from flask_classy import FlaskView
from flask import request

class ViewBase(FlaskView):
    route_base = '/'

    def __init__(self):
        self.user = None
        self.params = {}

    #从url，表单，json获取参数，3个任意一个有参数，都可以解释
    def init_params(self):
        try:
            args = request.args or {}
            self.params = args

            form = request.form or {}
            for item in form:
                self.params[item] = form[item]

            data = json.loads(request.data or '{}')
            for item in data:
                self.params[item] = data[item]
        except:
            #这里不要写log
            pass

    def before_request(self, name, **kwargs):
        try:
            # 把每次请求记录，有迹可循
            content = 'remote_addr:%s, method:%s, url:%s, args:%s, data:%s' %\
                      (request.remote_addr, request.method, request.url, request.args, request.data)
            writelog(content)

            # 获取参数
            self.init_params()

            # 渲染器
            self._render = Render()

        except:
            writelog(traceback.format_exc())