#coding:utf-8

import re
import xlrd

def get_url(filepath):
	pattern = re.compile(r'^url')

	f = open(filepath, 'r')
	try:
		for line in f:
			match = pattern.match(line)

			if match:
				return unicode(line, 'utf-8').encode('utf-8').split(",")[1]
	finally:
		f.close()

def get_prm_key(filepath):
	pattern = re.compile(r'^payload')

	f = open(filepath, 'r')
	try:
		for line in f:
			match = pattern.match(line)

			if match:
				return unicode(line, 'utf-8').encode('utf-8').split(",")[1:]
	finally:
		f.close()

def get_prm_value(filepath):
	pattern = re.compile(r'^,`')
	value_list = []

	f = open(filepath, 'r')
	try:
		for line in f:
			match = pattern.match(line)

			if match:
				value_list.append(unicode(line, 'utf-8').encode('utf-8').split(",`")[1:])
	finally:
		f.close()
	return value_list


def excel_table_value(filepath,by_name=u'Sheet1'):
	data = xlrd.open_workbook(filepath)
	table = data.sheet_by_name(by_name)
	nrows = table.nrows #行数 
	colnames =  table.row_values(2) #某一行数据 
	list =[]
	for rownum in range(3,nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			list.append(app)
	return list


def excel_table_url(filepath,by_name=u'Sheet1'):
	data = xlrd.open_workbook(filepath)
	table = data.sheet_by_name(by_name)
	nrows = 2
	colnames =  table.row_values(0) #某一行数据 
	list =[]
	for rownum in range(1,nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			list.append(app)
	return list