# coding=utf-8

import sys
sys.path.append("..")
#reload(sys)
#sys.setdefaultencoding('utf-8')

import urllib
import unittest
import re

from tools import file_read
from tools.key_value_sign import *
from tools.req import *
from tools.gl_pic import *

class Create_Order(unittest.TestCase):
	# 读取文件
	data_file = '.\\test_data\\cancel_order_terminal_data.xlsx'
	url = file_read.excel_table_url(filepath = data_file,by_name=u'Sheet1')
	payload = file_read.excel_table_value(filepath = data_file,by_name=u'Sheet1')

	key = "counect"

	def test_case_0001(self, i = 0):
		payload = self.payload[0]
		print payload
		res = self.send_request(payload)
		self.resultsComparison(res,i)

	#获取签名			
	def get_sign(self,payload):
		return get_key_value_sign(payload, self.key)
	#发送请求
	def send_request(self,payload):
		headers = {}
		sign_value = self.get_sign(payload)
		payload["sign"] = sign_value
		print  payload	

		res = req("POST", self.url, headers, payload)
		print 'actual_results:'+ res
		return res
		
	#匹配字段，验证结果
	def resultsComparison(self, String,i):
		expected_outcome_data  = self.expected_outcome_data(i)
		no = 0
		success = []
		for i in range(len(expected_outcome_data)):
			pattern = re.compile(expected_outcome_data[i])
			match = pattern.search(String)
			if match:
				success.append(match.group())
			else:
				print expected_outcome_data[i] + ' not find'
				no = no + 1

		print success
		if no != 0:
			assert 0,u'this case fail'