# coding=utf-8

################################################################
# 通用方法
################################################################

import re
import random
import datetime
import traceback


#得到随机字符串
def get_random_string(cnt, num=False):
    """
    :param cnt: 随机字符串的位数
    :param num: 是否纯数字
    :return:    返回cnt长度的随机字符串
    """

    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if num:
        string_list = num_list
    else:
        string_list = num_list + letter_list

    result = ''
    for i in range(cnt):
        result = result + random.choice(string_list)

    return result


# 列表转字符串
def list_to_string(in_list):
    result = ''
    try:
        if 'list' in str(type(in_list)):
            for item in in_list:
                result = result + str(item) + '|'

        result = result.strip('|')
    except:
        print(traceback.format_exc())

    return result


# 判断是否手机
def is_phone(instr):
    result = True
    try:
        instr = str(instr)

        if len(instr) != 11 or (not instr.isdigit()) or (not instr.startswith('1')):
            result = False
    except:
        pass

    return result

# 判断是否数字(整型或者浮点)
def is_digit(instr):
    result = False
    try:
        instr = str(instr)
        patten = re.compile(r'^[-+]?[0-9]+\.?[0-9]+$')
        if patten.match(instr):
            result = True
    except:
        pass
    return result

# 判断是否整数
def is_int(instr):
    result = False
    try:
        instr = str(instr)
        patten = re.compile(r'^[-+]?[0-9]+$')
        if patten.match(instr):
            result = True
    except:
        pass
    return result

# 数据库对象序列化
def model_serialize(model):
    if isinstance(model, list):
        result = []
        for model_item in model:
            model_dict = model_item.__dict__
            dict_item = {}
            for key in model_dict:
                if str(key).startswith('_'):
                    continue
                dict_item[key] = model_dict[key]
            result.append(dict_item)
    else:
        result = {}
        model_dict = model.__dict__
        for key in model_dict:
            if str(key).startswith('_'):
                continue
            result[key] = model_dict[key]
    return result
