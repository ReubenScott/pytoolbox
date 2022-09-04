#!/usr/bin/env python
# -*- coding:utf-8 -*-

import traceback

import pymssql  # sqlserver

from db.column import Column
from db.db_provider import DBProvider


class SQLServerProvider(DBProvider):
  
  def init_connect(self):
    try:
      return pymssql.connect(self.server, self.user, self.password)
      # 可简化为conn = pymssql.connect(host='localhost', user='sa', password='123456', database='pubs')
    except:
      print(traceback.format_exc())
      exit(1)
  
  def get_dbnames(self):
    """
      获取数据库名
    """
    try:
      cursor = self.connect.cursor()
      
      sql = "Select Name FROM Master..SysDatabases orDER BY Name"
      
      cursor.execute(sql)
      
      rows = cursor.fetchall()
      for row in rows: 
        # TODO  去除自增长
        self.dbnames.append(row[0])
          
      # 关闭连接
      cursor.close()
    except:
      print(traceback.format_exc())
      exit(1)
    
  def choose_database(self, database) -> []:
    """
      获取数据库名
    """
    try:
      self.current_db = database
      cursor = self.connect.cursor()
      
      sql = "USE {0}".format(self.current_db)
      
      cursor.execute(sql)
      
      sql = "SELECT name AS schema_name FROM sys.schemas order by schema_id asc"
      
      cursor.execute(sql)
      
      schemas = []
      rows = cursor.fetchall()
      for row in rows: 
        # TODO  去除自增长
        schemas.append(row[0])
          
      # 关闭连接
      cursor.close()
      return schemas
    except:
      print(traceback.format_exc())
      
  def choose_schema(self, schema) -> []:
    """
      获取数据库名下的所有表
    """
    try:
      self.current_schema = schema
      cursor = self.connect.cursor()
      
      # sql = "USE {0}".format(self.current_db)
      # cursor.execute(sql)
      
      sql = """
        SELECT
          t.name AS table_name
        FROM sys.tables t
          INNER JOIN sys.schemas s
          ON t.schema_id = s.schema_id
        WHERE s.name = '{0}'
         order by 1 asc
      """.format(self.current_schema)
      cursor.execute(sql)
      
      tables = []
      rows = cursor.fetchall()
      for row in rows: 
        # TODO  去除自增长
        tables.append(row[0])
          
      # 关闭连接
      cursor.close()
      return tables
    except:
      print(traceback.format_exc())

  def parse_columns(self, table_name) -> []:
    
    """
     获取数据表字段    
    """
    try:
      print("SQLServerTable: parse_columns")
      self.current_table = table_name
      cursor = self.connect.cursor()
      
      # sql = "USE {0}".format(self.current_db)
      # cursor.execute(sql)
      
      # 获取数据库指定表的字段信息
      sql = '''
        select
          ordinal_position,
          column_name,
          data_type,
          ISNULL(ISNULL(ISNULL(character_maximum_length,numeric_precision),datetime_precision),1) AS length,
          ISNULL(numeric_scale,0)  AS scale,
          is_nullable AS is_nullable,
          ISNULL(column_default,'') AS column_default
        from information_schema.columns where table_schema='{0}' and table_name='{1}'
      '''.format(self.current_schema, self.current_table)
  
      print(sql)
      # "SELECT * from tur_margin_xone"
      
      # table_catalog    
      # table_schema    
      # table_name    
      # column_name    
      # ordinal_position    
      # column_default    
      # is_nullable    
      # data_type    
      # character_maximum_length    
      # character_octet_length    
      # numeric_precision    
      # numeric_precision_radix    
      # numeric_scale    
      # datetime_precision    
      
      cursor.execute(sql)
      rows = cursor.fetchall()
    
      columns = []
      for row in rows: 
        # TODO  去除自增长
        columns.append(Column(*row))
          
      # 关闭连接
      cursor.close()
      
      return columns
    except:
      print(traceback.format_exc())
      exit(1)
  
      
if __name__ == "__main__":
  
  # 数据库的；连接配置信息
  dbconf = {
    'server': '18.177.192.22',
    'user': "sasdb_isysuser",
    'password': "sasdb_isysuser@Passw0rd",
    'database': "BIDB",
    'schema_name': 'dbo',
    'table_name': 'tur_margin_xone',
    'charset': "utf8"
  }
        # host=,
        # port=,
        # charset='utf8'
  
  # server = '18.177.192.22'
  # user = "sasdb_isysuser"
  # password = "sasdb_isysuser@Passw0rd"
  # database = "SASBI"
  
  # SQLServerTable(**dbconf).convert_sql()
  # .parse_columns(schema_name, table_name)
  # // .init(server, user, password, database)
  
