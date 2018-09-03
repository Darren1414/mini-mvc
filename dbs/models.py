# coding=utf-8
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 用户表(样例)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 手机
    phone = db.Column(db.String(40), nullable=False, index=True)
    # 密码，MD5后的值
    password = db.Column(db.String(255), default='')
    # token(用户登陆成功后令牌)
    token = db.Column(db.String(255), default='')
    # 姓名
    name = db.Column(db.String(255), index=True)
    # 邮箱
    email = db.Column(db.String(80), default='', index=True)
    # 逻辑删除
    is_delete = db.Column(db.Boolean, default=False)
    # 最近登陆时间
    login_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
