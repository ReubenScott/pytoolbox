#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

import psycopg2
from db.db_provider import DBProvider
from util.utils import count_time, json_item


class PgSQLProvider(DBProvider):

    # def init(self ):
        # self.producer = KafkaProducer(bootstrap_servers=self.args.connect)
        # self.init_window_name = init_window_name

    def construct_self_rows(self):
        return []

    def save_data(self, content):
        self.producer.send(self.args.table, bytes(content.encode('utf-8')))

    # def save_data(self, lines):
    #     for line in lines:
    #         content = self.format_data(line)
    #         self.producer.send(self.args.table, bytes(content.encode('utf-8')))
    #         if self.args.interval:
    #             time.sleep(self.args.interval)

    @count_time
    def do_fake(self):
        i = 0
        try:
            while i < self.args.num:
                i += 1
                columns = self.fake_column(i)
                content = self.format_data(columns)
                if self.args.outprint:
                    print(content)
                self.save_data(content)
                print('insert %d records' % i)
                if self.args.interval:
                    time.sleep(self.args.interval)
        except KeyboardInterrupt:
            print("generated records : %d" % i)
            print("insert records : %d" % i)

    def format_data(self, columns):
        if self.args.metaj:
            data = self.metaj_content % tuple(columns)
            data = data.strip()
        else:
            data = json_item(self.column_names, columns)

        return data
    

if __name__ == "__main__":
    
    conn = psycopg2.connect(database="postgres", user="postgres", password="HOUSEI20220511", host="192.168.1.34", port="5432")
    print("Opened database successfully")
    cur = conn.cursor()

    schema_name = 'public'
    table_name = 'tur_margin_xone'
    # 获取数据库指定表的字段信息

    sql = "select * from information_schema.columns where table_schema='{0}' and table_name='{1}'".format(schema_name, table_name)
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

    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows: 
        print(row[7])
        # print("ordinal_position = ", row[4])
        # print("column_name = ", row[3])
        # print("data_type = ", row[7])
        # print("SALARY = ", row[3]) 
    conn.close()
    
    # character varying
    # integer
    # jsonb
    # numeric
    # smallint
    # timestamp without time zone
    
