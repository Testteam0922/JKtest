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
#class AuthCode_Pay_Query():
	# 读取文件
	data_file = '.\\test_data\\authCode_pay_query.csv'
	url = file_read.get_url(filepath = data_file)
	# url = "http://103.36.132.29:8080/mpip-gateway/query/orderquery"
	prm_key = file_read.get_prm_key(filepath = data_file)
	prm_value_list = file_read.get_prm_value(filepath = data_file)

	def test_case_0001(self, i = 0): #4
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0002(self, i = 1): #5
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0003(self, i = 2): #6
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0004(self, i = 3): #7
		key = ""
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)			
	
	def test_case_0005(self, i = 4): #8
		key = "222222"
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

	def test_case_0035(self, i = 34): #38
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	

	def test_case_0036(self, i = 35): #39
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)						
								
	def test_case_0037(self, i = 36): #40
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)						
											
	def test_case_0038(self, i = 37): #41
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0039(self, i = 38): #42
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0040(self, i = 39): #43
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)																									
		
	def test_case_0041(self, i = 40): #44
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0042(self, i = 41): #45
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)																											
			
	def test_case_0043(self, i = 42): #46
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)		

	def test_case_0044(self, i = 43): #47
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	

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

	def test_case_0048(self, i = 47): #51
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)		

	def test_case_0049(self, i = 48): #52
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
	def test_case_0050(self, i = 49): #53
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
	def test_case_0051(self, i = 50): #54
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)				

	def test_case_0052(self, i = 51): #55
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	

	def test_case_0053(self, i = 52): #56
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
	def test_case_0054(self, i = 53): #57
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)		

	def test_case_0055(self, i = 54): #58
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)		

	def test_case_0056(self, i = 55): #59
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)		

	def test_case_0057(self, i = 56): #60
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	

	def test_case_0058(self, i = 57): #61
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
	def test_case_0059(self, i = 58): #62
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)		
		
	def test_case_0060(self, i = 59): #63
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
	def test_case_0061(self, i = 60): #64
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
	def test_case_0062(self, i = 61): #65
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)				
			
	def test_case_0063(self, i = 62): #66
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
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
									
	def test_case_0072(self, i = 71): #75
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)											
										
	def test_case_0073(self, i = 72): #76
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)																

	def test_case_0074(self, i = 73): #77
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

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

	def test_case_0077(self, i = 76): #80
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	

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
		
	def test_case_0081(self, i = 80): #84
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	

	def test_case_0082(self, i = 81): #85
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
	def test_case_0083(self, i = 82): #86
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	

	def test_case_0084(self, i = 83): #87
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)	
		
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
				
	def test_case_0094(self, i = 93): #97
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0095(self, i = 94): #98
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0096(self, i = 95): #99
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0097(self, i = 96): #100
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0098(self, i = 97): #101
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0099(self, i = 98): #102
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0100(self, i = 99): #103
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)

	def test_case_0101(self, i = 100): #104
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)
		
	def test_case_0102(self, i = 101): #105
		key = "123456"
		payload = self._get_payload(i)
		res = self.send_request(payload,key)
		self.resultsComparison(res,i)												
									
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
			


