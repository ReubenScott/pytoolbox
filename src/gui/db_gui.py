#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import Tk, StringVar , LabelFrame, Label, Entry, Button, Frame 
from tkinter import ttk
from tkinter.constants import N, NSEW, VERTICAL, NS, SUNKEN, W, BOTTOM, X, Y, TOP, \
  YES, LEFT, BOTH

from db.sqlserver_provider import SQLServerProvider


class DBToolGui():
  
  def show_database(self):
    provider = self.provider_chosen.get()
    host = self.host_text.get()
    user = self.user_text.get()
    password = self.password_text.get()
    
    # 数据库的；连接配置信息
    dbconf = {
      'provider': provider,
      'server': host,
      'user': user,
      'password': password,
      # 'database': "BIDB",
      # 'schema_name': 'dbo',
      # 'table_name': 'tur_margin_xone',
      # 'charset': "utf8"
    }
    
    if provider == 'SQL Server':
      self.db_provider = SQLServerProvider(**dbconf)
      
    # DBProvider(provider, **dbconf)
    self.database_chosen['values'] = self.db_provider.dbnames
    self.database_chosen.current(0)  # 设置下拉列表默认显示的值，
    self.db_select(self.database_chosen.get())
  
  def db_select(self, event):
    self.current_db = self.database_chosen.get()
    self.schema_chosen['values'] = self.db_provider.choose_database(self.current_db)
    self.schema_chosen.current(0)  # 设置下拉列表默认显示的值，
    self.schema_select(self.schema_chosen.get())
    
  def schema_select(self, event):
    self.current_schema = self.schema_chosen.get()
    tables = self.db_provider.choose_schema(self.current_schema)
    self.show_table_list(tables)
      
  def __init__(self, window):
    self.window = window
    # 当前数据库
    self.current_db = None
    # 当前模式
    self.current_schema = None
    # 当前表
    self.current_table = None
      
  def set_init_window(self):
     
    # 使用Frame增加一层容器
    fm = Frame()
    fm.pack(side=TOP, fill=X)
    
    # 状态栏。
    self.statusbar = Label(text="status", bd=1, relief=SUNKEN, anchor=W)
    self.statusbar.pack(side=BOTTOM, fill=X)
    
    labelframe = LabelFrame(fm, text="配置")
    labelframe.grid(row=0, column=0, sticky=N)
    # .grid(column=1, row=1)  # 设置其在界面中出现的位置   column代表列    row 代表行
    # //.grid(column=0, row=0, padx=5, pady=5)
    
    Label(labelframe, text="数据库类型：").grid(row=0, column=0)
    
    # 创建一个下拉列表
    self.provider_chosen = ttk.Combobox(labelframe, width=12)
    self.provider_chosen['values'] = ('SQL Server', 'PostgreSQL', 4, 42, 100)  # 设置下拉列表的值
    self.provider_chosen.grid(row=0, column=1)
    # .grid(column=1, row=1)  # 设置其在界面中出现的位置   column代表列    row 代表行
    self.provider_chosen.current(0)  # 设置下拉列表默认显示的值， 0为 numberChosen['values'] 的下标值
    
    Label(labelframe, text="数据库URL：").grid(row=1, column=0)
    
    self.host_text = Entry(labelframe, show=None)
    self.host_text.insert('0', '18.177.192.22')
    self.host_text.grid(row=1, column=1)
    
    Label(labelframe, text="User：").grid(row=2, column=0)
    self.user_text = Entry(labelframe, show=None)
    self.user_text.insert('0', 'sasdb_isysuser')
    self.user_text.grid(row=2, column=1)
    
    Label(labelframe, text="Passwd：").grid(row=3, column=0)
    self.password_text = Entry(labelframe, show=None)
    self.password_text.insert('0', 'sasdb_isysuser@Passw0rd')
    self.password_text.grid(row=3, column=1)
    
    # 创建一个下拉列表
    Label(labelframe, text="数据库名：").grid(row=4, column=0)
    self.database_chosen = ttk.Combobox(labelframe, width=12)
    self.database_chosen.grid(row=4, column=1)
    self.database_chosen.bind('<<ComboboxSelected>>', self.db_select)
    
    # 创建一个下拉列表
    Label(labelframe, text="模式名：").grid(row=5, column=0)
    self.schema_chosen = ttk.Combobox(labelframe, width=12)
    self.schema_chosen.grid(row=5, column=1)
    self.schema_chosen.bind('<<ComboboxSelected>>', self.schema_select)
    
    Button(labelframe, text='连接', command=self.show_database).grid(row=6, column=0)
    Button(labelframe, text='断开').grid(row=6, column=1)
    
    # 功能
    action_labelframe = LabelFrame(fm, text="功能")
    action_labelframe.grid(row=1, column=0, sticky=N)
    
    # 创建一个下拉列表
    Label(action_labelframe, text="条数：").grid(row=0, column=0)
    self.count_chosen = ttk.Combobox(action_labelframe, width=12)
    self.count_chosen.grid(row=0, column=1)
    self.count_chosen['values'] = (1, 10, 20, 50, 100)  # 设置下拉列表的值
    self.count_chosen.current(0)  # 设置下拉列表默认显示的值， 0为 numberChosen['values'] 的下标值
    
    Button(action_labelframe, text='插入随机数据', command=self.insert_radom).grid(row=0, column=2)
    
    # 表名的展示
    table_labelframe = LabelFrame(fm, text="表名列表")
    table_labelframe.grid(row=0, column=1, rowspan=2, sticky=NSEW)
    
    # 定义树形结构与滚动条
    self.table_tree = ttk.Treeview(table_labelframe, show="headings", columns=("a", "b"), height=30)    
    self.vbar = ttk.Scrollbar(table_labelframe, orient=VERTICAL, command=self.table_tree.yview)       
    self.table_tree.configure(yscrollcommand=self.vbar.set)
    
    # 表格的标题
    self.table_tree.heading("a", text="序号")
    self.table_tree.heading("b", text="表名")
    
    self.table_tree.column("a", width=50, anchor="w")
    self.table_tree.column("b", width=300, anchor="w")
        
    self.table_tree.grid(row=0, column=0, sticky=NSEW)
    self.table_tree.bind("<ButtonRelease-1>", self.on_tree_click)
    self.vbar.grid(row=0, column=1, sticky=NS)
    
  # 显示列表
  def show_table_list(self, tables):
    items = self.table_tree.get_children() 
    [self.table_tree.delete(item) for item in items]
    for index, table_info in enumerate(tables):
            # print("%-*s| %s | %*s |%*s\n"%(20,index,wifi_info.ssid,wifi_info.bssid,,wifi_info.signal))
      self.table_tree.insert("", 'end', values=(index + 1, table_info))
      # print("| %s | %s | %s | %s \n"%(index,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))
  
  # Treeview绑定事件
  def on_tree_click(self, event):
    self.current_table = self.table_tree.item(event.widget.selection(), "values")[1]
    # print("you clicked on",self.wifi_tree.item(self.sels,"values")[1])    
    
  # 随机插入
  def insert_radom(self):
    message = "Insert {1} recod into {0} : {2}"
    if self.current_table:
      ret = self.db_provider.insert_random_data(self.current_table, self.count_chosen.get())
      if ret:
        ret = "Success"
      else:
        ret = "Failed"
      self.statusbar['text'] = message.format(self.current_table, self.count_chosen.get(), ret)


def gui_start():
  window = Tk()
  window.title('Data Tool')
  window.geometry('800x800')
  ui = DBToolGui(window)
  ui.set_init_window()
  
  window.mainloop()

  
gui_start()
