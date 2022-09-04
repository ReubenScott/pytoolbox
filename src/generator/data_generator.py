'''
Created on 2022/08/30
https://zhuanlan.zhihu.com/p/234747828
@author: HOUSEI3929
'''

import configparser
from decimal import Decimal
import random
import time

from db.field_type import FieldType

cfg_path = 'rebulid_generate_sql_git\base_data\sql_header.ini'
cfg = configparser.ConfigParser()
cfg.read(cfg_path, encoding='utf-8')


def get_config_data(section, options):
    return cfg.get(section, options)


NUM_WORDS = "1234567890"
UPPER_WORDS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_WORDS = "abcdefghijklmnopqrstuvwxyz"


def random_int(length):
    """
    生成随机字符串
    :return:
    """
    sa = []
    length = random.randint(1, length);
    for i in range(length):
      rand = str(random.randint(0, 9));
      if(i == 0 and rand == "0"):
        rand = str(random.randint(1, 9));
      sa.append(rand)
    return ''.join(sa)
    

def random_str(length) -> str:
    """
    生成随机字符串
    :return:
    """
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = random.randint(1, length);
    sa = []
    
    for i in range(length):
      sa.append(random.choice(seed))
    return ''.join(sa)

    
def random_decimal(length:int, scale:int):
    """
    生成随机字符串
    :return:
    """
    if(scale > 0):
      sa = []
      for i in range(scale):
        rand = str(random.randint(0, 9));
        sa.append(rand)
      result = Decimal('%s.%s' % (random_int(length - scale), ''.join(sa)))
    else:
      result = Decimal('%s' % (random_int(length - scale)))
      
    return str(result)


def random_date():
    """
    报废车辆入库表
    :return:
    """
    # 生成数据容器
    insert_data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return insert_data


def random_json():
    """
    报废车辆入库表
    :return:
    """
    # 生成数据容器
    json = '{ "cargo_no": "12", "barcode ": ["123234", "1213124", "123123123"], "total": 1000 }'
    return json

    
def generator(field_type: FieldType, length:int, scale:int):
  # 列表内容统计器，对列表内的重复项进行数量统计
  if field_type == FieldType.STRING:
    return  "'" + random_str(length) + "'"
  elif field_type == FieldType.SMALLINT:
    return random_int(2)
  elif field_type == FieldType.INTEGER:
    return random_int(4)
  if field_type == FieldType.LONG:
    return random_int(8)
  elif field_type == FieldType.NUMERIC:
    return random_decimal(length, scale)
  elif field_type == FieldType.DATETIME:
    return  "'" + random_date() + "'"
  elif field_type == FieldType.JSON:
    return random_json()
  else:
    #  TODO
    print("TODO generator data by type")
    return random_str(5)


def qiuhe(data_list):
    """
    对列表内的数值进行求和
    :param data_list:
    :return:
    """
    total = 0
    for ele in range(0, len(data_list)):
        total = total + data_list[ele]
    return total


def main(prov, city, sql_num, sour_prov, sour_city):
    """
    启动数据自动写入的主方法
    :return:
    """
    features_type = input("请选择生成数据所属功能模块 1.车辆报废 2.梯次利用 3.资源再生")


if __name__ == "__main__":
  
    # 获取vin
    vin = random_str(7)
    print(vin)
 
    # 生成随机zqy_id,写入列表
    # insert_data.append(random_util.random_id())
    # # 生成随机vin,写入列表
    # insert_data.append(vin)
    # # 生成随机电池包数,写入列表
    # insert_data.append(random.randint(1, 10))
    # # 生成报废时间,写入列表
    # insert_data.append(random_util.random_date())
    #
        
