#coding:utf-8

import xlrd

def excel_read(filepath,by_name=u'Sheet1'):
	data = xlrd.open_workbook(filepath)
	table = data.sheet_by_name(by_name)
	nrows = table.nrows #行数 
	colnames =  table.row_values(0) #字典key所在行，即参数的key 
	list =[]
	for rownum in range(1,nrows):		#数字1 即有效数据开始的行数为第1行（文档的第2行）
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			list.append(app)
	return list