#coding=utf-8

import os

#上线改完False
DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings = {
    # 数据库(这里替换成你的mysql数据库)
    # username 替换你的数据库用户名
    # password 替换你的数据库密码
    # ip       替换你的数据库ip
    'SQLALCHEMY_DATABASE_URI': 'mysql://username:password@ip:3306/mini-mvc',
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,

    # cookie缓存时间
    'cookie_max_age': 60 * 60 * 24 * 2,

}
