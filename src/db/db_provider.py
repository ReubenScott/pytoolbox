# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:      test_socks
# Date:      2020/4/14
#-------------------------------------------------------------------------------
import traceback

from generator.data_generator import generator


class DBProvider(object):
    """
    基础数据源类
    """
    
    def __init__(self, **kwargs):
        # TODO 
      if kwargs is not None:
        self.provider = kwargs['provider']
        self.server = kwargs['server']
        self.user = kwargs['user']
        self.password = kwargs['password']
        # self.database = kwargs['database']
        # self.schema_name = kwargs['schema_name']
        # self.table_name = kwargs['table_name']
        # self.column_names = [item['name'] for item in self.schema]
        # 调用子类初始化函数
        
        self.connect = self.init_connect()
        self.dbnames = []
        self.get_dbnames()
        self.current_schema = None
        self.current_table = None

    def init_connect(self):
      pass
      
    def get_dbnames(self):
        pass
      
    def choose_database(self) -> []:
        pass
      
    def choose_schema(self) -> []:
        pass
      
    def parse_columns(self, table_name) -> []:
      pass
      
    def insert_random_data(self, table_name, count):
      try:
        columns = self.parse_columns(table_name)
        column_names = tuple(('"' + item.column_name + '"' for item in columns))
        # data_type = tuple((item.data_type for item in columns))
        
        # self.connect = pymssql.connect(self.server, self.user, self.password, self.database)
        cursor = self.connect.cursor()
        
        for i in range(int(count)):
          values = []
          for item in columns:
            values.append(generator(item.data_type, item.length, item.scale))
        
          sql = "insert into {0}.{1} ({2}) values ({3})".format(self.current_schema, self.current_table , ','.join(column_names) , ','.join(values))
          print(sql)
          cursor.execute(sql)
              
        self.connect.commit()
        cursor.close()
        return True
      except:
        print(traceback.format_exc())
        return False
        
