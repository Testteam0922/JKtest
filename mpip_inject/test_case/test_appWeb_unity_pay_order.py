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

class appWeb_unity_pay_order(unittest.TestCase):
	# 读取文件
	data_file = '.\\test_data\\appWeb_unity_pay_order.xlsx'
	url = "http://103.36.132.29:8080/mpip-gateway/pay/preorder"
	datalist = file_read.excel_table_value(filepath = data_file)
	data_key = ['mch_id','agent_id','v','timestamp','sn','time_expire',\
	'mch_trade_no','no_type','show_fee','real_fee','fee_type','title',\
	'notify_url','callback_url','ext','sign_type','goods_tag','show_landing']
	detail = ['detail','detail_param_1','detail_param_2','detail_param_3','detail_param_4','detail_param_5']

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

		detail_json = ""
		for key in self.detail:	#将detail的参数拼接成字符串
			if key =="detail":
				if clean_data[key] =='null':
					break
				else:
					pass
			elif detail_json =="":
				detail_json=detail_json+clean_data[key].encode('utf-8')
			else:
				detail_json = detail_json + "," + clean_data[key].encode('utf-8')

			params.update({self.detail[0].encode('utf-8'):detail_json})

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
	def test_case_014	(self,i=14): self.case_action(i)
	def test_case_015	(self,i=15): self.case_action(i)
	def test_case_016	(self,i=16): self.case_action(i)
	def test_case_017	(self,i=17): self.case_action(i)
	def test_case_018	(self,i=18): self.case_action(i)
	def test_case_019	(self,i=19): self.case_action(i)
	def test_case_020	(self,i=20): self.case_action(i)
	def test_case_021	(self,i=21): self.case_action(i)
	def test_case_022	(self,i=22): self.case_action(i)
	def test_case_023	(self,i=23): self.case_action(i)
	def test_case_024	(self,i=24): self.case_action(i)
	def test_case_025	(self,i=25): self.case_action(i)
	def test_case_026	(self,i=26): self.case_action(i)
	def test_case_027	(self,i=27): self.case_action(i)
	def test_case_028	(self,i=28): self.case_action(i)
	def test_case_029	(self,i=29): self.case_action(i)
	def test_case_030	(self,i=30): self.case_action(i)
	def test_case_031	(self,i=31): self.case_action(i)
	def test_case_032	(self,i=32): self.case_action(i)
	def test_case_033	(self,i=33): self.case_action(i)
	def test_case_034	(self,i=34): self.case_action(i)
	def test_case_035	(self,i=35): self.case_action(i)
	def test_case_036	(self,i=36): self.case_action(i)
	def test_case_037	(self,i=37): self.case_action(i)
	def test_case_038	(self,i=38): self.case_action(i)
	def test_case_039	(self,i=39): self.case_action(i)
	def test_case_040	(self,i=40): self.case_action(i)
	def test_case_041	(self,i=41): self.case_action(i)
	def test_case_042	(self,i=42): self.case_action(i)
	def test_case_043	(self,i=43): self.case_action(i)
	def test_case_044	(self,i=44): self.case_action(i)
	def test_case_045	(self,i=45): self.case_action(i)
	def test_case_046	(self,i=46): self.case_action(i)
	def test_case_047	(self,i=47): self.case_action(i)
	def test_case_048	(self,i=48): self.case_action(i)
	def test_case_049	(self,i=49): self.case_action(i)
	def test_case_050	(self,i=50): self.case_action(i)
	def test_case_051	(self,i=51): self.case_action(i)
	def test_case_052	(self,i=52): self.case_action(i)
	def test_case_053	(self,i=53): self.case_action(i)
	def test_case_054	(self,i=54): self.case_action(i)
	def test_case_055	(self,i=55): self.case_action(i)
	def test_case_056	(self,i=56): self.case_action(i)
	def test_case_057	(self,i=57): self.case_action(i)
	def test_case_058	(self,i=58): self.case_action(i)
	def test_case_059	(self,i=59): self.case_action(i)
	def test_case_060	(self,i=60): self.case_action(i)
	def test_case_061	(self,i=61): self.case_action(i)
	def test_case_062	(self,i=62): self.case_action(i)
	def test_case_063	(self,i=63): self.case_action(i)
	def test_case_064	(self,i=64): self.case_action(i)
	def test_case_065	(self,i=65): self.case_action(i)
	def test_case_066	(self,i=66): self.case_action(i)
	def test_case_067	(self,i=67): self.case_action(i)
	def test_case_068	(self,i=68): self.case_action(i)
	def test_case_069	(self,i=69): self.case_action(i)
	def test_case_070	(self,i=70): self.case_action(i)
	def test_case_071	(self,i=71): self.case_action(i)
	def test_case_072	(self,i=72): self.case_action(i)
	def test_case_073	(self,i=73): self.case_action(i)
	def test_case_074	(self,i=74): self.case_action(i)
	def test_case_075	(self,i=75): self.case_action(i)
	def test_case_076	(self,i=76): self.case_action(i)
	def test_case_077	(self,i=77): self.case_action(i)
	def test_case_078	(self,i=78): self.case_action(i)
	def test_case_079	(self,i=79): self.case_action(i)
	def test_case_080	(self,i=80): self.case_action(i)
	def test_case_081	(self,i=81): self.case_action(i)
	def test_case_082	(self,i=82): self.case_action(i)
	def test_case_083	(self,i=83): self.case_action(i)
	def test_case_084	(self,i=84): self.case_action(i)
	def test_case_085	(self,i=85): self.case_action(i)
	def test_case_086	(self,i=86): self.case_action(i)
	def test_case_087	(self,i=87): self.case_action(i)
	def test_case_088	(self,i=88): self.case_action(i)
	def test_case_089	(self,i=89): self.case_action(i)
	def test_case_090	(self,i=90): self.case_action(i)
	def test_case_091	(self,i=91): self.case_action(i)
	def test_case_092	(self,i=92): self.case_action(i)
	def test_case_093	(self,i=93): self.case_action(i)
	def test_case_094	(self,i=94): self.case_action(i)
	def test_case_095	(self,i=95): self.case_action(i)
	def test_case_096	(self,i=96): self.case_action(i)
	def test_case_097	(self,i=97): self.case_action(i)
	def test_case_098	(self,i=98): self.case_action(i)
	def test_case_099	(self,i=99): self.case_action(i)
	def test_case_100	(self,i=100): self.case_action(i)
	def test_case_101	(self,i=101): self.case_action(i)
	def test_case_102	(self,i=102): self.case_action(i)
	def test_case_103	(self,i=103): self.case_action(i)
	def test_case_104	(self,i=104): self.case_action(i)
	def test_case_105	(self,i=105): self.case_action(i)
	def test_case_106	(self,i=106): self.case_action(i)
	def test_case_107	(self,i=107): self.case_action(i)
	def test_case_108	(self,i=108): self.case_action(i)
	def test_case_109	(self,i=109): self.case_action(i)
	def test_case_110	(self,i=110): self.case_action(i)
	def test_case_111	(self,i=111): self.case_action(i)
	def test_case_112	(self,i=112): self.case_action(i)
	def test_case_113	(self,i=113): self.case_action(i)
	def test_case_114	(self,i=114): self.case_action(i)
	def test_case_115	(self,i=115): self.case_action(i)
	def test_case_116	(self,i=116): self.case_action(i)
	def test_case_117	(self,i=117): self.case_action(i)
	def test_case_118	(self,i=118): self.case_action(i)
	def test_case_119	(self,i=119): self.case_action(i)
	def test_case_120	(self,i=120): self.case_action(i)
	def test_case_121	(self,i=121): self.case_action(i)
	def test_case_122	(self,i=122): self.case_action(i)
	def test_case_123	(self,i=123): self.case_action(i)
	def test_case_124	(self,i=124): self.case_action(i)
	def test_case_125	(self,i=125): self.case_action(i)
	def test_case_126	(self,i=126): self.case_action(i)
	def test_case_127	(self,i=127): self.case_action(i)
	def test_case_128	(self,i=128): self.case_action(i)
	def test_case_129	(self,i=129): self.case_action(i)
	def test_case_130	(self,i=130): self.case_action(i)
	def test_case_131	(self,i=131): self.case_action(i)
	def test_case_132	(self,i=132): self.case_action(i)
	def test_case_133	(self,i=133): self.case_action(i)
	def test_case_134	(self,i=134): self.case_action(i)
	def test_case_135	(self,i=135): self.case_action(i)
	def test_case_136	(self,i=136): self.case_action(i)
	def test_case_137	(self,i=137): self.case_action(i)
	def test_case_138	(self,i=138): self.case_action(i)
	def test_case_139	(self,i=139): self.case_action(i)
	def test_case_140	(self,i=140): self.case_action(i)
	def test_case_141	(self,i=141): self.case_action(i)
	def test_case_142	(self,i=142): self.case_action(i)
	def test_case_143	(self,i=143): self.case_action(i)
	def test_case_144	(self,i=144): self.case_action(i)
	def test_case_145	(self,i=145): self.case_action(i)
	def test_case_146	(self,i=146): self.case_action(i)
	def test_case_147	(self,i=147): self.case_action(i)
	def test_case_148	(self,i=148): self.case_action(i)
	def test_case_149	(self,i=149): self.case_action(i)
	def test_case_150	(self,i=150): self.case_action(i)
	def test_case_151	(self,i=151): self.case_action(i)
	def test_case_152	(self,i=152): self.case_action(i)
	def test_case_153	(self,i=153): self.case_action(i)
	def test_case_154	(self,i=154): self.case_action(i)
	def test_case_155	(self,i=155): self.case_action(i)
	def test_case_156	(self,i=156): self.case_action(i)
	def test_case_157	(self,i=157): self.case_action(i)
	def test_case_158	(self,i=158): self.case_action(i)
	def test_case_159	(self,i=159): self.case_action(i)
	def test_case_160	(self,i=160): self.case_action(i)
	def test_case_161	(self,i=161): self.case_action(i)
	def test_case_162	(self,i=162): self.case_action(i)
	def test_case_163	(self,i=163): self.case_action(i)
	def test_case_164	(self,i=164): self.case_action(i)
	def test_case_165	(self,i=165): self.case_action(i)
	def test_case_166	(self,i=166): self.case_action(i)
	def test_case_167	(self,i=167): self.case_action(i)
	def test_case_168	(self,i=168): self.case_action(i)
	def test_case_169	(self,i=169): self.case_action(i)
	def test_case_170	(self,i=170): self.case_action(i)
	def test_case_171	(self,i=171): self.case_action(i)
	def test_case_172	(self,i=172): self.case_action(i)
	def test_case_173	(self,i=173): self.case_action(i)
	def test_case_174	(self,i=174): self.case_action(i)
	def test_case_175	(self,i=175): self.case_action(i)
	def test_case_176	(self,i=176): self.case_action(i)
	def test_case_177	(self,i=177): self.case_action(i)
	def test_case_178	(self,i=178): self.case_action(i)
	def test_case_179	(self,i=179): self.case_action(i)
	def test_case_180	(self,i=180): self.case_action(i)
	def test_case_181	(self,i=181): self.case_action(i)
	def test_case_182	(self,i=182): self.case_action(i)
	def test_case_183	(self,i=183): self.case_action(i)
	def test_case_184	(self,i=184): self.case_action(i)
	def test_case_185	(self,i=185): self.case_action(i)
	def test_case_186	(self,i=186): self.case_action(i)