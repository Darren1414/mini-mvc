#coding=utf-8

import views

# 注册view
def register_view(app):
    # 登陆
    views.login_views.LoginView.register(app, route_prefix='/')
