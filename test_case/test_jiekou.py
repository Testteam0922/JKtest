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
	data_file = '.\\test_data\\cancel_order_terminal_data.csv'
	url = file_read.get_url(filepath = data_file)
	prm_key = file_read.get_prm_key(filepath = data_file)
	prm_value_list = file_read.get_prm_value(filepath = data_file)


	#sign = ""
	key = "dc9204db4fffde50eac75ce955ca55f8"
	#key = "counect"

	def test_case_0001(self, i = 2):
		payload = self._get_payload(i)
		print payload
		res = self.send_request(payload)
		self.resultsComparison(res,i)

	#获取签名参数	
	def _get_payload(self, i):
		params = {}
		for len_arr in range(len(self.prm_key)):
			#params.update({urllib.quote(self.prm_key[len_arr].strip("\n")):urllib.quote(self.prm_value_list[0][len_arr].strip("\n"))})
			if self.prm_key[len_arr].strip("\n") == "note":
				print unicode(self.prm_value_list[i][len_arr].strip("\n"),'utf-8')
				continue
			elif self.prm_key[len_arr].strip("\n") == "no":
				continue
			elif self.prm_key[len_arr].strip("\n") == "expected_outcome_data":
				continue
			else:
				params.update({self.prm_key[len_arr].strip("\n"):self.prm_value_list[i][len_arr].strip("\n")})
		return params
	#获取需要验证的参数
	def expected_outcome_data(self,i):
		expected_outcome_data = []
		for len_arr in range(len(self.prm_key)):				
			if self.prm_key[len_arr].strip("\n") == "expected_outcome_data":
				s = self.prm_value_list[i][len_arr].strip("\n")
				s_list = s.split(",")
				expected_outcome_data = expected_outcome_data + s_list
			else:
				continue
		return expected_outcome_data
	#获取签名			
	def get_sign(self,payload):
		return get_key_value_sign(payload, self.key)
	#发送请求
	def send_request(self,payload):
		headers = {}
		sign_value = self.get_sign(payload)
		payload["sign"] = sign_value
		print payload	

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