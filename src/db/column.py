#!/usr/bin/env python
# -*- coding:utf-8 -*-
from db.field_type import FieldType


class Column(object):

  def __init__(self, *args):
    # 保存文件名
    self.position = args[0]
    # m3u地址
    self.column_name = args[1]
    # 保存文件路径
    self.data_type = FieldType.get_type(args[2])
    # cookie
    self.length = args[3]
    
    self.scale = args[4]
    
    # 可简化为conn = pymssql.connect(host='localhost', user='sa', password='123456', database='pubs')
