#!/usr/bin/env python
# -*- coding:utf-8 -*-
from enum import Enum, unique


# https://docs.python.org/3/library/enum.html
# https://icode.best/i/20040935950696
# https://icode.best/i/37984843543219
# @unique
class FieldType(Enum):
  String = 'STRING', 'VARCHAR'
  BigInteger = 'LONG'
  Numeric = 'DECIMAL'
  Date = 'DATE',
  Time = 'TIME',
  DateTime = 'TIMESTAMP'
  Interval = 'INTERVAL'
  # SmallInteger = 7
  # Float = 9
  # Text = 3
  # LargeBinary = 3
  # PickleType = 3
  # Unicode = 3
  # UnicodeText = 3
  # Boolean = 3
  
  @staticmethod
  def list():
    return list(map(lambda c: c.value, FieldType))
  
  @staticmethod
  def get_type(type_name):
    for name, item in FieldType.__members__.items():
      print(f'name: {name}, member: {item}, value: {item.value}')
      
      if type_name in item.value:
        return item
      
  def get_length(self, color):
      if color == FieldType.RED:
          print('Color is red')
      elif color == FieldType.GREEN:
          print('Color is green')
      else:
          print('not defined')


if __name__ == '__main__':
  # print(FieldType.list())
  
  print(FieldType.get_type('DATE'))
  
  # for shake in FieldType:
  #   print(shake)
  # models.AutoField
    
# {0: 'DECIMAL',
# 1: 'TINY',
# 2: 'SHORT',
# 3: 'LONG',
# 4: 'FLOAT',
# 5: 'DOUBLE',
# 6: 'NULL',
# 7: 'TIMESTAMP',
# 8: 'LONGLONG',
# 9: 'INT24',
# 10: 'DATE',
# 11: 'TIME',
# 12: 'DATETIME',
# 13: 'YEAR',
# 14: 'NEWDATE',
# 15: 'VARCHAR',
# 16: 'BIT',
# 246: 'NEWDECIMAL',
# 247: 'INTERVAL',
# 248: 'SET',
# 249: 'TINY_BLOB',
# 250: 'MEDIUM_BLOB',
# 251: 'LONG_BLOB',
# 252: 'BLOB',
# 253: 'VAR_STRING',
# 254: 'STRING',
# 255: 'GEOMETRY'} 
