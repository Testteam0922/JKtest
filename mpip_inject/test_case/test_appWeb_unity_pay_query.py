# coding=utf-8

import sys
sys.path.append("..")

import urllib
import unittest
import re
import time


from tools import file_read
from tools import random_string
from tools.key_value_sign import *
from tools.req import *

class appWeb_unity_pay_query(unittest.TestCase):
	# 读取文件
	data_file = '.\\test_data\\appWeb_unity_pay_query.xlsx'
	url = "http://103.36.132.29:8080/mpip-gateway/query/orderquery"
	datalist = file_read.excel_table_value(filepath = data_file)
	data_key = ['mch_id','agent_id','v','timestamp','mch_trade_no','mpip_no','third_no','sign_type']

	def case_action(self, i): 
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload,clean_data)
		self.resultsComparison(res,clean_data)

	#初始化数据参数
	def _clean_data(self, data):
		for key, value in data.items():
			data[key] = value
		return data	

	def _get_payload(self,clean_data):
		params = {}
		
		print u'用例说明: ' + clean_data['note'] #数据文件中对应的用例说明字段
		
		for key in self.data_key: #获取data_key参数的值
			if clean_data[key] == "null":	#当不传这个键值对时，在数据文件中填入null
				continue
			else:
				if clean_data[key] == "time":  #当数据文件中该字段的值为time时，使用时间格式代替
					now  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
					clean_data[key] = now
				elif clean_data[key] == "TimeStamp": #当数据文件中该字段的值为TimeStamp时，使用时间戳代替
					clean_data[key] = str(int(time.time())*1000)
				elif clean_data[key][0:13] == "string_length": #当需要指定随机字符串的长度时，数据文件输入string_length=32，长度自定
					string_length = int(clean_data[key][14:])
					clean_data[key] = random_string.my_random_string(string_length)
				params.update({key.encode('utf-8'):clean_data[key].encode('utf-8')})
		print self.url
		print params	
		return params
		

	#获取签名			
	def get_sign(self,payload,key):
		return get_key_value_sign(payload, key)


	#发送请求
	def send_request(self,payload,clean_data):
		headers = {}
		sign_value = self.get_sign(payload,clean_data['sign_key'].encode('utf-8'))#数据文件中对应的签名key字段
		payload["sign"] = sign_value
		res = req("GET", self.url, headers, payload)
		print u'返回结果: '+ res
		return res
		
	
	#匹配字段，验证结果
	def resultsComparison(self, actual_results,clean_data):
		expected_data  = self.expected_outcome_data(clean_data)
		no = 0
		success = []
		for i in range(len(expected_data)):
			pattern = re.compile(expected_data[i])
			match = pattern.search(actual_results)
			if match:
				pass
#				success.append(match.group())
			else:
				print u'参数: ' + expected_data[i] + u' 匹配失败'
				no = no + 1
#		print success
		self.assertEqual(0, no)
	
	
	#获取预期结果
	def expected_outcome_data(self,clean_data):
		expected_value = clean_data['expected_outcome_data']
		expected_value_list = expected_value.split(",")
		return expected_value_list

	#用列集
	def test_case_001	(self,i=1): self.case_action(i)
	def test_case_002	(self,i=2): self.case_action(i)
	def test_case_003	(self,i=3): self.case_action(i)
	def test_case_004	(self,i=4): self.case_action(i)
	def test_case_005	(self,i=5): self.case_action(i)
	def test_case_006	(self,i=6): self.case_action(i)
	def test_case_007	(self,i=7): self.case_action(i)
	def test_case_008	(self,i=8): self.case_action(i)
	def test_case_009	(self,i=9): self.case_action(i)
	def test_case_010	(self,i=10): self.case_action(i)
	def test_case_011	(self,i=11): self.case_action(i)
	def test_case_012	(self,i=12): self.case_action(i)
	def test_case_013	(self,i=13): self.case_action(i)
