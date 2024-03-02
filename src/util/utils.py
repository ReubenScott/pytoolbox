#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
import functools
import os
import json
import re
import time


def save2file(items, outfile):
    """
    将数据保存到文件
    :param items:
    :param outfile:
    :param spliter:
    :return:
    """
    with open(outfile, 'a+') as fp:
        fp.writelines(items)


def json_item(column_names, item):
    map = dict(zip(column_names, item))
    return json.dumps(map)


def count_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        now = time.time()
        timeused = float((now - start))
        print('time used: %.3f s' % timeused)
        return ret
    return wrapper




def diffdate(date1, date2):
    """
    #计算两个日期相差天数，自定义函数名，和两个日期的变量名。
    :param date1:
    :param date2:
    :return:
    """
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')

    return (date2-date1).days


