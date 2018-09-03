#coding=utf-8

import uuid
import traceback
from dbs.models import *
from common.write_log import writelog
from controller.controller_base import ControllerBase


class LoginController(ControllerBase):

    def __init__(self):
        super(LoginController, self).__init__()

    def login(self, phone, password):
        result = {}
        try:
            # 从数据库查询用户信息，如果正确，产生一个uuid，返回
            user_item = self.db.session.query(User).filter(User.phone == phone, User.password == password).first()
            if user_item:
                token = uuid.uuid1().get_hex()
                user_item.token = token
                user_item.login_time = datetime.datetime.now()
                self.db.session.commit()

                result['token'] = token
        except:
            writelog(traceback.format_exc())

        return result
