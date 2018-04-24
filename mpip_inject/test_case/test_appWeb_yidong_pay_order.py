# coding=utf-8

import sys
sys.path.append("..")

import urllib
import unittest
import re
import time


from tools import file_read
from tools.key_value_sign import *
from tools.req import *

class authCode_order_revoke(unittest.TestCase):
# class AuthCode_refund_apply():
	# 读取文件
	data_file = '.\\test_data\\appWeb_yidong_pay_order.xlsx'
	url = "http://103.36.132.29:8080/mpip-gateway/pay/barcodepay"
	datalist = file_read.excel_table_value(filepath = data_file)
	data_key = ['mch_id','agent_id','v','timestamp','access_way',"consumer_id",'mch_trade_no','no_type','show_fee','real_fee','fee_type','title','detail','app_type','channel_id','notify_url','ext','goods_tag','sign_type']


	def test_case_0001(self, i = 1): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)


	def test_case_0002(self, i = 2): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)


	def test_case_0003(self, i = 3): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)


	def test_case_0004(self, i = 4): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0005(self, i = 5): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0006(self, i = 6): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0007(self, i = 7): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0008(self, i = 8): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0009(self, i = 9): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0010(self, i = 10): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0011(self, i = 11): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0012(self, i = 12): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0013(self, i = 13): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0014(self, i = 14): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0015(self, i = 15): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	def test_case_0016(self, i = 16): 
		key = "123456"
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload, key)
		self.resultsComparison(res,clean_data)
		

	# def test_case_0017(self, i = 17): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0018(self, i = 18): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0019(self, i = 19): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0020(self, i = 20): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0021(self, i = 21): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0022(self, i = 22): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0023(self, i = 23): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0024(self, i = 24): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0025(self, i = 25): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0026(self, i = 26): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0027(self, i = 27): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0028(self, i = 28): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0029(self, i = 29): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0030(self, i = 30): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0031(self, i = 31): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0032(self, i = 32): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0033(self, i = 33): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0034(self, i = 34): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0035(self, i = 35): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0036(self, i = 36): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0037(self, i = 37): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0038(self, i = 38): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0039(self, i = 39):  
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0040(self, i = 40): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0041(self, i = 41): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0042(self, i = 42): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0043(self, i = 43):  
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0044(self, i = 44): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0045(self, i = 45): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0046(self, i = 46): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0047(self, i = 47): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0048(self, i = 48): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0049(self, i = 49): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0050(self, i = 50): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)	


	# def test_case_0051(self, i = 51): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0052(self, i = 52): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0053(self, i = 53): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0054(self, i = 54): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0055(self, i = 55): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0056(self, i = 56): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0057(self, i = 57): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0058(self, i = 58): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0059(self, i = 59): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0060(self, i = 60): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0061(self, i = 61): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0062(self, i = 62): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0063(self, i = 63): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0064(self, i = 64): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0065(self, i = 65): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0066(self, i = 66): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0067(self, i = 67): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0068(self, i = 68): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0069(self, i = 69): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0070(self, i = 70): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0071(self, i = 71): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0072(self, i = 72):  
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0073(self, i = 73):  
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0074(self, i = 74):  
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0075(self, i = 75): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0076(self, i = 76):  
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0077(self, i = 77):  
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0078(self, i = 78): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0079(self, i = 79): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0080(self, i = 80): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0081(self, i = 81): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0082(self, i = 82): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0083(self, i = 83): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0084(self, i = 84): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0085(self, i = 85): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0086(self, i = 86): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0087(self, i = 87): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0088(self, i = 88): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0089(self, i = 89): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0090(self, i = 90): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0091(self, i = 91): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0092(self, i = 92): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0093(self, i = 93): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0094(self, i = 94): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0095(self, i = 95): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0096(self, i = 96): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0097(self, i = 97): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0098(self, i = 98): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0099(self, i = 99): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0100(self, i = 100): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0101(self, i = 101): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0102(self, i = 102): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0103(self, i = 103): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0104(self, i = 104): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0105(self, i = 105): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		


	# def test_case_0106(self, i = 106): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0107(self, i = 107): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0108(self, i = 108): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0109(self, i = 109): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0110(self, i = 110): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0111(self, i = 111): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0112(self, i = 112): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0113(self, i = 113): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0114(self, i = 114): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0115(self, i = 115): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0116(self, i = 116): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0117(self, i = 117): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0118(self, i = 118): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0119(self, i = 119): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0120(self, i = 120): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0121(self, i = 121): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0122(self, i = 122): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0123(self, i = 123): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0124(self, i = 124): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0125(self, i = 125): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0126(self, i = 126): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0127(self, i = 127): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0128(self, i = 128):  
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0129(self, i = 129): # 以下用例需要修改交易单号
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		


	# def test_case_0130(self, i = 130): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)


	# def test_case_0131(self, i = 131): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0132(self, i = 132): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0133(self, i = 133): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0134(self, i = 134): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0135(self, i = 135): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0136(self, i = 136): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0137(self, i = 137): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0138(self, i = 138): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0139(self, i = 139): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0140(self, i = 140): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0141(self, i = 141): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0142(self, i = 142): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0143(self, i = 143): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
		

	# def test_case_0144(self, i = 144): 
	# 	key = "123456"
	# 	clean_data = self._clean_data(self.datalist[i])
	# 	payload = self._get_payload(clean_data)
	# 	res = self.send_request(payload, key)
	# 	self.resultsComparison(res,clean_data)
																																																																																																																																																																																																																											
																																																								

	#初始化数据参数
	def _clean_data(self, data):
		for key, value in data.items():
			data[key] = value
		return data	


	def _get_payload(self,clean_data):
		params = {}
		
		print u'用例说明: ' + clean_data['note']
		
		for key in self.data_key: #获取除body外的其它参数
			if clean_data[key] == "null":
				continue
			elif clean_data[key] == "random":
				random = int(time.time())*1000
				params.update({key:str(random)})
			else:	
				params.update({key.encode('utf-8'):clean_data[key].encode('utf-8')})
		print self.url		
		print params	
		return params
		

	#获取签名			
	def get_sign(self,payload,key):
		return get_key_value_sign(payload, key)


	#发送请求
	def send_request(self,payload,key):
		headers = {}
		sign_value = self.get_sign(payload, key)
		payload["sign"] = sign_value
		res = req("GET", self.url, headers, payload)
		print u'返回结果: '+ res
		# print  u"获取请求后打印当前时间：",int(time.time())*1000
		return res
		
	
	#匹配字段，验证结果
	def resultsComparison(self, actual_results,i):
		expected_data  = self.expected_outcome_data(i)
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

# if __name__ == '__main__':

