#-*- coding:utf-8 -*-
#excel导入数据库 
import os
from myTools import Excel
from myTools import DB

# excel1 = excelToDb.excel()


param = {
	'path' : 'D:/avList.xls',
	'sheets' : 'Sheet1',
}

excel1 = Excel(param)
# excel1.test('1111111')
info = excel1.all_row_list()
# print(info)
info.pop(0) # 去掉表头

d = 'mywebsite'
db1 = DB(d)
num = 0
error_list = []
for l in info:
	# print(l)
	res = db1.insert(l)
	if res:
		num = num + 1
	else:
		error_list.append(l[0])


print(num)
print(error_list)


os.system("pause")