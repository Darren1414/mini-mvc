#coding=utf-8

import traceback
from views.view_base import ViewBase
from flask_classy import route
from common.middlewares import *
from controller.login_controller import LoginController

# 登陆
class LoginView(ViewBase):
    @route('/login', methods=['GET', 'POST'], endpoint='login')
    @verify_params(phone='string', password='string')
    def login(self):
        code = '11000'
        data = {}
        msg = '登陆失败，请配置好你的数据库，在login_controller补上登陆逻辑后测试.'

        try:
            phone = self.params.get('phone', '')
            password = self.params.get('password', '')

            controller = LoginController()
            result = controller.login(phone=phone, password=password)

            if result.get('token', ''):
                code = '10000'
                data = result
                msg = 'success'
        except:
            writelog(traceback.format_exc())

        return self._render.render_json(code=code, data=data, msg=msg)



