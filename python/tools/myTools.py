#-*- coding:utf-8 -*-

import os
import pymysql
import xlrd

class Excel:

	path = ''
	sheets = ''
	
	def __init__(self,param):
		self.path = param['path']
		self.sheets = param['sheets']
		self.workbook = xlrd.open_workbook(self.path)
		self.sheet = self.workbook.sheet_by_name(self.sheets)
			
	# 行内容	
	def get_row_info(self,n):
		rows = self.sheet.row_values(n) 
		return rows

	# 列内容
	def get_cols_info(self,n):
		cols = self.sheet.col_values(n) 
		return cols
	
	def row_info_list(self,min,max):
		info_list = []
		for i in range(min,max+1):
			rows = self.get_row_info(i)
			info_list.insert(i,rows)
			# print(i)
		return info_list
		
	def all_row_list(self):
		info_list = []
		row = self.sheet.nrows  # 总行数
		for i in range(row):
			rows = self.get_row_info(i)
			info_list.insert(i,rows)
		return info_list
		
	def cols_info_list(self,min,max):
		info_list = []
		for i in range(min,max+1):
			cols = self.get_cols_info(i)
			info_list.insert(i,cols)
			# print(i)
		return info_list
		
	def all_cols_list(self):
		info_list = []
		col = self.sheet.ncols  # 总列数
		for i in range(col):
			cols = self.get_cols_info(i)
			info_list.insert(i,cols)
		return info_list
		

class DB:
	
	__host = 'localhost'
	__user = 'root'
	__password = 'xuxubarca'
	
	def __init__(self,d):
		self.db = pymysql.connect(host=self.__host, user=self.__user, passwd= self.__password, db=d, charset='utf8')
		self.cursor = self.db.cursor()

		
	def select(self):
		pass
		# print(db)

	def insert(self,param):
		sql = "INSERT INTO movie(id,tp,actor,title,grade,quality,srt,upload) \
			VALUES ('%s', '%d', '%s', '%s', '%d', '%d', '%d','%d')" % \
			(param[0],param[2],param[3],param[4],param[5],param[6],param[7],param[8])
		# print(sql)	

		try:
			self.cursor.execute(sql)
			self.db.commit()
			return 1
		except:
			self.db.rollback()
			return 0
			
			
			
			
	
	
