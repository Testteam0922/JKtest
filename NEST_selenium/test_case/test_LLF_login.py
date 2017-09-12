#coding:UTF-8

import sys
sys.path.append("..")

from ext import file_read
from conf.gl_config import *
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Nest_Llf_Login(unittest.TestCase):
	
	data_file = ".\\test_data\\llf_login.xlsx"
	#��ȡ����
	listdata = file_read.excel_read(filepath = data_file)	
	
	def setUp(self):
		self.driver = webdriver.Chrome(chromedriver_path)
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get(login_addr)

	
	def case_run(self,i):
		driver = self.driver		
		self._llf_login(i)
		self.Assertequal(i)

	#����
	def test_case_00001(self,i=0): self.case_run(i)
	def test_case_00002(self,i=1): self.case_run(i)	
		
	#�ر������
	def tearDown(self):
		self.driver.quit()

	def _llf_login(self, i ):
		driver = self.driver
		username = self.listdata[i]['username']
		password = self.listdata[i]['password']
		
		driver.find_element_by_name("username").send_keys(username)
		driver.find_element_by_name("password").send_keys(password)
		driver.find_element_by_xpath("//*[@id='form-validation']/div[5]/button").click()
		time.sleep(2)

	#����
	def Assertequal(self, i):
		driver = self.driver
		xpath = self.listdata[i]["xpath"]
		expectValue=self.listdata[i]['expectValue']
		print u"expectValue:" + expectValue
		try:
			time.sleep(1)
			actualValue = driver.find_element_by_xpath(xpath).text
			print u"actualValue:" + actualValue
			#�ж�Ԥ����ʵ�ʽ���Ƿ���ȣ�Ϊ��ͨ����Ϊ�ٽ�ͼ
			vlue = self.assertCompare(expectValue,actualValue)
			if vlue:
				pass
			else:
				fail_pic_path = case_pic_path + "Nest_Llf_Login_%s.png"%(i+1)
				print "image" + fail_pic_path
				driver.get_screenshot_as_file(fail_pic_path)
				assert 0,u"~~~~~~Test Case Fail~~~~~~"				
		except NoSuchElementException:
			fail_pic_path = case_pic_path + "Nest_Llf_Login_%s.png"%(i+1)
			print "image" + fail_pic_path
			driver.get_screenshot_as_file(fail_pic_path)
			assert 0,u"~~~~~~xpath not exist~~~~~~"
		time.sleep(1)

	#Ԥ����ʵ�ʱȽ�
	def assertCompare(self,expectValue,actualValue):
		flag=True
		driver = self.driver	
		try:
			self.assertEqual(expectValue, actualValue)
			return flag
		except:
			flag=False
			return flag