#coding:utf-8

import csv
import xlrd

def read_csv(filepath):
	rows=[]
	with open(filepath, 'rb') as csvfile:
		try:
			spamreader = csv.DictReader(csvfile)
			for row in spamreader:
				rows.append(row)
		except:
			tmp=1
	return rows



def excel_read(filepath,by_name=u'Sheet1'):
	data = xlrd.open_workbook(filepath)
	table = data.sheet_by_name(by_name)
	nrows = table.nrows #行数 
	colnames =  table.row_values(1) #字典key所在行，即参数的key 
	list =[]
	for rownum in range(3,nrows):		#数字3 即有效数据开始的行数为第三行（文档的第四行）
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i][1:]
			list.append(app)
	return list
