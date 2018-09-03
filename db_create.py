#coding=utf-8

#######################################################
# 这个文件的作用是做一些数据库初始化的工作
# 用法 python db_create.py
#######################################################

from manager import db

# 主函数
if __name__ == '__main__':
    # 创建所有表
    db.create_all()
    db.session.commit()

    print('finished')
