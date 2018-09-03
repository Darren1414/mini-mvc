#coding=utf-8

import os
import time
import datetime
import inspect
from conf.settings import BASE_DIR


def writelog(content):
    try:
        content = str(content)
        log_path = os.path.join(BASE_DIR, 'log')
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        date = time.strftime('%Y-%m-%d')
        filename = '%s.log' % str(date)
        file = os.path.join(log_path, filename)
        fp = open(file, 'a')

        now = datetime.datetime.now()
        content = str(inspect.stack()[1][3]) + ' ' + content
        strlog = '[' + str(now) + '] ' + content + '\n'
        print(strlog)
        fp.write(strlog)
        fp.close()
    except Exception, ex:
        print(str(ex))
