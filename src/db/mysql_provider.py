#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
from abc import abstractmethod
from time import sleep
from generator.data_generator import generator


class BaseTable(object):
    """
    基础数据源类
    """

    def __init__(self, **kwargs):
      self.table_name = None
      self.columns = []
      if kwargs is not None:
        self.server = kwargs['server']
        self.user = kwargs['user']
        self.password = kwargs['password']
        self.database = kwargs['database']
        self.schema_name = kwargs['schema_name']
        self.table_name = kwargs['table_name']
        # self.column_names = [item['name'] for item in self.schema]
        # 调用子类初始化函数
        self.parse_columns()
      
    @abstractmethod
    def convert_sql(self):
      print("BaseTable: parse_columns")
      self.column_names = tuple(('"' + item.column_name + '"' for item in self.columns))
      self.data_type = tuple((item.data_type for item in self.columns))
      
      values = []
      for item in self.columns:
        values.append(generator(item.data_type, item.length, item.scale))
      
      sql = "insert into {0}.{1} ({2}) values ({3})".format(self.schema_name, self.table_name , ','.join(self.column_names) , ','.join(values))
      print(sql)
      self.save_data(sql)
    
    @abstractmethod
    def save_data(self, lines):
      print(lines)
      pass

    """
    def execut_sql(self, sql):
      try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("数据库执行成功")
        cur.close()

      except Exception as e: 
        print(str(e))
        print(sql)
        # 有异常就回滚
        conn.rollback()
        # 关闭连接
        cur.close()
        conn.close()
"""

    def get_cur_num(self):
        """
        必须将取值与计算同时锁住做原子计算，不然其他线程会执行产生多的数据
        :return:
        """
        with self.lock:
            self.cur_num.value += 1
            return self.cur_num.value - 1

    def format_data(self, columns):
        data = columns
        return data

    def fake_data(self):
        """
        sleep是为了防止产生数据后消费数据过慢
        :return:
        """

        while self.get_cur_num() < self.args.num:
            columns = self.fake_column(self.cur_num.value)
            self.queue.put(columns)

        sleep(0.1)
        self.isover.value = True

    def fake_column(self, current_num):
        columns = []
        for item in self.schema:
            columns.append(self.fakedata.do_fake(item['cmd'], item['args'], current_num))

        # 处理op操作，与多个字段有逻辑关系
        # 必须等第一遍完成后再处理一遍
        for idx, item in enumerate(self.schema):
            if item['cmd'] == 'op':
                columns[idx] = eval(item['args'][0])
        return columns

    def save(self):
        saved_records = 0
        while not self.isover.value or not self.queue.empty():
            lines = []
            i = 0
            while i < self.args.batch and (not self.isover.value or not self.queue.empty()):
                try:
                    lines.append(self.queue.get_nowait())
                    i += 1
                except:
                    pass
            self.save_data(lines)
            if self.args.interval:
                time.sleep(self.args.interval)
            saved_records += len(lines)
            del(lines)
            print('insert %d records' % saved_records)

