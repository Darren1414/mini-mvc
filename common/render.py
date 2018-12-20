#coding=utf-8

import os
import re
import types
# import json
import time
import traceback
from common.write_log import writelog
from xml.dom import minidom
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
from flask import request, make_response, json
from flask import render_template

class Render():

    def __init__(self):
        self.request_start_time = time.time()

    # 返回文本
    def render_txt(self, data, status_code=200):
        writelog(request.remote_addr + ' render_txt:' + str(data) + '\n')
        try:
            response = make_response(data)
            response.headers['Content-Type'] = 'text/plain'

            return response, status_code
        except:
            writelog(traceback.format_exc())

    # 返回json
    def render_json(self, code, data, msg='', status_code=200, set_cookie=None):
        writelog(request.remote_addr + ' render_json:' + str(data) + '\n')
        try:
            # python默认参数是不能为字典或者列表的，要像下面这样给默认值（直接set_cookie={}是错的）。
            if set_cookie is None:
                set_cookie = {}

            exec_time = time.time() - self.request_start_time
            data = {'code': code, 'time': exec_time, 'data': data, 'msg': msg}

            response = make_response(json.dumps(data))
            response.headers['Content-Type'] = 'application/json;charset=utf-8'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
            response.headers['Access-Control-Request-Method'] = 'POST, GET'
            response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')

            if request.headers.get('Origin', ''):
                response.headers['Access-Control-Allow-Credentials'] = 'true'

            if set_cookie:
                max_age = set_cookie['max_age']
                cookies = set_cookie['cookies']
                for key in cookies:
                    response.set_cookie(key, cookies[key], max_age=max_age)

            return response, status_code
        except:
            writelog(traceback.format_exc())

    # 返回html
    def rend_template(self, template, set_cookie=None, status_code=200, **kwargs):
        writelog(request.remote_addr + ' rend_template:' + template + '\n')
        try:
            if set_cookie is None:
                set_cookie = {}

            response = make_response(render_template(template, **kwargs))
            response.headers['Content-Type'] = 'text/html; charset=utf-8'

            if set_cookie:
                for key in set_cookie['cookies']:
                    response.set_cookie(key, set_cookie['cookies'][key], max_age=set_cookie['max_age'])

            return response, status_code
        except:
            writelog(traceback.format_exc())

    # 返回xml
    def render_xml(self, root, data, status_code=200):
        writelog(request.remote_addr + ' rend_xml:' + str(data) + '\n')
        try:
            response = make_response(self.__dict2xmlstring(root, data))
            response.headers['Content-Type'] = 'application/xml'

            return response, status_code
        except:
            writelog(traceback.format_exc())

    # 返回文件
    def render_file(self, out_file, status_code=200, headers=None, auto_delete=False):
        if headers is None:
            headers = {}

        writelog(request.remote_addr + ' render_file:' + str(out_file) + '\n')
        try:
            fp = open(out_file, 'rb')
            response = make_response(fp.read())
            response.headers["Content-Disposition"] = "attachment; filename=" + out_file.split(os.path.sep)[-1]
            fp.close()

            response.headers['Access-Control-Request-Method'] = 'POST, GET, OPTIONS'
            response.headers['Access-Control-Allow-Origin'] = headers.get('Origin', '*')

            if headers.get('Origin', ''):
                response.headers['Access-Control-Allow-Credentials'] = 'true'

            if auto_delete and os.path.exists(out_file):
                os.remove(out_file)

            return response, status_code
        except:
            writelog(traceback.format_exc())

    def __get_format_from_headers(self, headers):
        try:
            return re.findall("application\/(json)", headers)[0]
        except:
            return 'json'

    def __dict2xmlstring(self, root, data):
        et = dict2xml(root, data)
        return minidom.parseString(ET.tostring(et, encoding='utf-8', method='xml')).toprettyxml()


def dict2xml(root, content):
    if type(content) != types.ListType and type(content) != types.TupleType and type(content) != types.DictType:
        e = Element(root)
        e.text = str(content)
        return e
    e = Element(root)
    for key in content:
        if type(content[key]) == list:
            for one in content[key]:
                e.append(dict2xml(key,one))
        else:
            e.append(dict2xml(key,content[key]))
    return e