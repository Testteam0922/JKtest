# coding=utf-8

import sys
sys.path.append("..")

import urllib
import unittest
import re

from tools import file_read
from tools.key_value_sign import *
from tools.req import *

class AuthCode_Pay_Query(unittest.TestCase):
#class AuthCode_Pay_Order():
	# 读取文件
	data_file = '.\\test_data\\authCode_pay_order.csv'
	url = file_read.get_url(filepath = data_file)
	# url = "http://103.36.132.29:8080/mpip-gateway/query/orderquery"
	prm_key = file_read.get_prm_key(filepath = data_file)
	prm_value_list = file_read.get_prm_value(filepath = data_file)


	def test_case_0001(self, i = 0): #4
		key = ""
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0002(self, i = 1): #5
		key = "222222"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0003(self, i = 2): #6
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0004(self, i = 3): #7
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0005(self, i = 4): #8
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0006(self, i = 5): #9
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0007(self, i = 6): #10
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)				

	def test_case_0008(self, i = 7): #11
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0009(self, i = 8): #12
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0010(self, i = 9): #13
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0011(self, i = 10): #14
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0012(self, i = 11): #15
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0013(self, i = 12): #16
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0014(self, i = 13): #17
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0015(self, i = 14): #18
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0016(self, i = 15): #19
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0017(self, i = 16): #20
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0018(self, i = 17): #21
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0019(self, i = 18): #22
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0020(self, i = 19): #23
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0021(self, i = 20): #24
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0022(self, i = 21): #25
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0023(self, i = 22): #26
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0024(self, i = 23): #27
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0025(self, i = 24): #28
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0026(self, i = 25): #29
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0027(self, i = 26): #30
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0028(self, i = 27): #31
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0029(self, i = 28): #32
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0030(self, i = 29): #33
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0031(self, i = 30): #34
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0032(self, i = 31): #35
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)																						
									
	def test_case_0033(self, i = 32): #36
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0034(self, i = 33): #37
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0035(self, i = 34): #38 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0036(self, i = 35): #39 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0037(self, i = 36): #40 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0038(self, i = 37): #41 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0039(self, i = 38): #42 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0040(self, i = 39): #43 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0041(self, i = 40): #44 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0042(self, i = 41): #45 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0043(self, i = 42): #46 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0044(self, i = 43): #47 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0045(self, i = 44): #48
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0046(self, i = 45): #49
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0047(self, i = 46): #50
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0048(self, i = 47): #51 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0049(self, i = 48): #52 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0050(self, i = 49): #53 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0051(self, i = 50): #54 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0052(self, i = 51): #55 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0053(self, i = 52): #56 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0054(self, i = 53): #57 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0055(self, i = 54): #58
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0056(self, i = 55): #59 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0057(self, i = 56): #60 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0058(self, i = 57): #61
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0059(self, i = 58): #62 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0060(self, i = 59): #63 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0061(self, i = 60): #64 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0062(self, i = 61): #65
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0063(self, i = 62): #66 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0064(self, i = 63): #67
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0065(self, i = 64): #68
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0066(self, i = 65): #69
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0067(self, i = 66): #70
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0068(self, i = 67): #71
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0069(self, i = 68): #72
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0070(self, i = 69): #73
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0071(self, i = 70): #74
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0072(self, i = 71): #75 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0073(self, i = 72): #76
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0074(self, i = 73): #77 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0075(self, i = 74): #78
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0076(self, i = 75): #79
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0077(self, i = 76): #80 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0078(self, i = 77): #81
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0079(self, i = 78): #82
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0080(self, i = 79): #83
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0081(self, i = 80): #84 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0082(self, i = 81): #85 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0083(self, i = 82): #86
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0084(self, i = 83): #87 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0085(self, i = 84): #88
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0086(self, i = 85): #89
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0087(self, i = 86): #90
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0088(self, i = 87): #91
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0089(self, i = 88): #92
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0090(self, i = 89): #93
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0091(self, i = 90): #94
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0092(self, i = 91): #95
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0093(self, i = 92): #96
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0094(self, i = 93): #97 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0095(self, i = 94): #98 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0096(self, i = 95): #99
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0097(self, i = 96): #100 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0098(self, i = 97): #101 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0099(self, i = 98): #102
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0100(self, i = 99): #103 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0101(self, i = 100): #104 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0102(self, i = 101): #105 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0103(self, i = 102): #106
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0104(self, i = 103): #107
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	# def test_case_0105(self, i = 104): #108 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0106(self, i = 105): #109
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0107(self, i = 106): #110
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0108(self, i = 107): #111
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0109(self, i = 108): #112
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0110(self, i = 109): #113
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0111(self, i = 110): #114
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0112(self, i = 111): #115
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0113(self, i = 112): #116 手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0114(self, i = 113): #117
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0115(self, i = 114): #118
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0116(self, i = 115): #119
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0117(self, i = 116): #120
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0118(self, i = 117): #121  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)

	# def test_case_0119(self, i = 118): #122  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)

	# def test_case_0120(self, i = 119): #123  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0121(self, i = 120): #124  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0122(self, i = 121): #125  手动执行
	# 	key = "123456" 
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0123(self, i = 122): #126  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0124(self, i = 123): #127  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)													

	# def test_case_0125(self, i = 124): #128  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0126(self, i = 125): #129
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)		

	# def test_case_0127(self, i = 126): #130  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0128(self, i = 127): #131
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0129(self, i = 128): #132
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0130(self, i = 129): #133
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0131(self, i = 130): #134
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0132(self, i = 131): #135  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0133(self, i = 132): #136  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0134(self, i = 133): #137  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0135(self, i = 134): #138  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0136(self, i = 135): #139  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0137(self, i = 136): #140  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0138(self, i = 137): #141  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0139(self, i = 138): #142  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0140(self, i = 139): #143  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0141(self, i = 140): #144
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0142(self, i = 141): #145
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0143(self, i = 142): #146
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0144(self, i = 143): #147  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0145(self, i = 144): #148  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0146(self, i = 145): #149  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0147(self, i = 146): #150  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0148(self, i = 147): #151  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0149(self, i = 148): #152  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0150(self, i = 149): #153  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)																									

	# def test_case_0151(self, i = 150): #154  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0152(self, i = 151): #155
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0153(self, i = 152): #156  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0154(self, i = 153): #157  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0155(self, i = 154): #158  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0156(self, i = 155): #159  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0157(self, i = 156): #160  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0158(self, i = 157): #161  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0159(self, i = 158): #162  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0160(self, i = 159): #163  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0161(self, i = 160): #164  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0162(self, i = 161): #165  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0163(self, i = 162): #166
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0164(self, i = 163): #167
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0165(self, i = 164): #168
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0166(self, i = 165): #169
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0167(self, i = 166): #170
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0168(self, i = 167): #171
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0169(self, i = 168): #172
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0170(self, i = 169): #173
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0171(self, i = 170): #174
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0172(self, i = 171): #175  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0173(self, i = 172): #176
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0174(self, i = 173): #177  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0175(self, i = 174): #178
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0176(self, i = 175): #179
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0177(self, i = 176): #180
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0178(self, i = 177): #181  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0179(self, i = 178): #182  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0180(self, i = 179): #183  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0181(self, i = 180): #184  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0182(self, i = 181): #185  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0183(self, i = 182): #186  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0184(self, i = 183): #187  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0185(self, i = 184): #188  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0186(self, i = 185): #189  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0187(self, i = 186): #190  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0188(self, i = 187): #191
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0189(self, i = 188): #192  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0190(self, i = 189): #193
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0191(self, i = 190): #194
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0192(self, i = 191): #195
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0193(self, i = 192): #196
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)							

	def test_case_0194(self, i = 193): #197
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0195(self, i = 194): #198
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0196(self, i = 195): #199
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0197(self, i = 196): #200  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0198(self, i = 197): #201
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0199(self, i = 198): #202
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0200(self, i = 199): #203
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0201(self, i = 200): #204  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0202(self, i = 201): #205
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0203(self, i = 202): #206
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0204(self, i = 203): #207
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0205(self, i = 204): #208
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0206(self, i = 205): #209
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0207(self, i = 206): #210
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0208(self, i = 207): #211
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0209(self, i = 208): #212  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0210(self, i = 209): #213
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0211(self, i = 210): #214
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0212(self, i = 211): #215
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0213(self, i = 212): #216
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0214(self, i = 213): #217
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0215(self, i = 214): #218
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0216(self, i = 215): #219
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0217(self, i = 216): #220
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0218(self, i = 217): #221
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0219(self, i = 218): #222
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0220(self, i = 219): #223
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0221(self, i = 220): #224
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0222(self, i = 221): #225
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0223(self, i = 222): #226  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0224(self, i = 223): #227  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0225(self, i = 224): #228
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0226(self, i = 225): #229
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	# def test_case_0227(self, i = 226): #230  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)

	# def test_case_0228(self, i = 227): #231  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0229(self, i = 228): #232  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0230(self, i = 229): #233
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0231(self, i = 230): #234
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0232(self, i = 231): #235
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0233(self, i = 232): #236
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0234(self, i = 233): #237
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0234(self, i = 233): #237
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0235(self, i = 234): #238
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0236(self, i = 235): #239
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0237(self, i = 236): #240  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0238(self, i = 237): #241
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0239(self, i = 238): #242
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0240(self, i = 239): #243  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0241(self, i = 240): #244  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0242(self, i = 241): #245  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0243(self, i = 242): #246  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0244(self, i = 243): #247  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0245(self, i = 244): #248  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0246(self, i = 245): #249  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0247(self, i = 246): #250  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0248(self, i = 247): #251  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0249(self, i = 248): #252  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0250(self, i = 249): #253
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0251(self, i = 250): #254
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0252(self, i = 251): #255
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0253(self, i = 252): #256
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0254(self, i = 253): #257
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0255(self, i = 254): #258
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0256(self, i = 255): #259
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0257(self, i = 256): #260
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0258(self, i = 257): #261
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0259(self, i = 258): #262
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0260(self, i = 259): #263
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0261(self, i = 260): #264
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0262(self, i = 261): #265  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	def test_case_0263(self, i = 262): #266
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	# def test_case_0264(self, i = 263): #267  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)																																																																						
									
	# def test_case_0265(self, i = 264): #268  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)

	# def test_case_0266(self, i = 265): #269  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0267(self, i = 266): #270  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0268(self, i = 267): #271  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0269(self, i = 268): #272  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0270(self, i = 269): #273  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0271(self, i = 270): #274  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0272(self, i = 271): #275  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0273(self, i = 272): #276  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0274(self, i = 273): #277  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0275(self, i = 274): #278  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0276(self, i = 275): #279  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0277(self, i = 276): #280  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0278(self, i = 277): #281  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)
		
	# def test_case_0279(self, i = 278): #282  手动执行
	# 	key = "123456"
	# 	payload = self._get_payload(i)
	# 	res = self.send_request(payload,key)
	# 	self.resultsComparison(res,i)																																																										
																														
										
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
			elif self.prm_value_list[i][len_arr].strip("\n") == "null":
				continue
			else:
				params.update({self.prm_key[len_arr].strip("\n"):self.prm_value_list[i][len_arr].strip("\n")})
				#params.update({self.prm_key[len_arr].strip("\n"):unicode(self.prm_value_list[i][len_arr].strip("\n"),'utf-8')})


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
	def get_sign(self,payload,key):
		# print get_key_value_sign(payload,key)
		return get_key_value_sign(payload,key)
	#发送请求
	def send_request(self,payload,key):
		headers = {}
		sign_value = self.get_sign(payload,key)
		payload["sign"] = sign_value

		res = req("POST", self.url, headers, payload)
		print 'actual_results:'+ res
		return res


		
	#匹配字段，验证结果
	def resultsComparison(self, String,i):
		expected_outcome_data  = self.expected_outcome_data(i)
		no = 0
		success = []
		for i in range(len(expected_outcome_data)):
			pattern = re.compile(unicode(expected_outcome_data[i],'utf-8'))
			match = pattern.search(String)
			try:
				if match:
					#Zpass
					success.append(match.group())
				else:
					print expected_outcome_data[i] + ' not find'
					no = no + 1
					assert 0,u'this case fail'
			except:
				assert 0,u'this case fail'
				

		# print success
		# if no != 0:
		# assert 0,u'this case fail'	
			


# if __name__ == '__main__':
# 	test = AuthCode_Pay_Order()
# 	test.test_case_0106(105)