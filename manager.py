#coding=utf-8

import sys
import conf.settings
from dbs.models import db
from flask import Flask
from flask_script import Manager
from main import register_view

app = Flask(__name__)
# 装载配置
app.debug = conf.settings.DEBUG
app.config.update(conf.settings.settings)
# 数据库
db.app = app
db.init_app(app)

manager = Manager(app)
# 注册路由
register_view(app)


if __name__ == '__main__':
    manager.run()
