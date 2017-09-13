#coding:UTF-8

import sys
sys.path.append("..")

from ext import file_read
from conf.gl_config import *
import unittest
import time
import SendKeys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Nest_Admin_Create_HitaCard_Batch(unittest.TestCase):
	
	data_file = ".\\test_data\\admin_create_hitaCard_batch.xlsx"
	#读取数据
	listdata = file_read.excel_read(filepath = data_file)	
	
	def setUp(self):
		self.driver = webdriver.Chrome(chromedriver_path)
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get(login_addr)
		time.sleep(2)
		driver.find_element_by_name("username").send_keys(admin_login_name)
		driver.find_element_by_name("password").send_keys(admin_login_passwd)
		driver.find_element_by_xpath("//*[@id='form-validation']/div[5]/button").click()
		time.sleep(2)
	
	def case_run(self,i):
		driver = self.driver		
		self._admin_create_hitacard(i)
		self.Assertequal(i)

	#用例
	def test_case_00001(self,i=0): self.case_run(i)
		
	#关闭浏览器
	def tearDown(self):
		self.driver.quit()

	def _admin_create_hitacard(self, i ):
		driver = self.driver
	
		remark = self.listdata[i]["remark"]
			 
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/nav[1]/div[2]/div/div[1]/ul/li[7]/a").click()
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/section/div/div[1]/div/section/div[4]/button[2]").click()
		time.sleep(0.5)

		driver.find_element_by_id("file").click()
		time.sleep(3)
		SendKeys.SendKeys(card_file)
		SendKeys.SendKeys("{ENTER}")
		# 中文输入法需要多一个回车
		#SendKeys.SendKeys("{ENTER}")	
			
		time.sleep(0.5)
		driver.find_element_by_id("aremark").send_keys(remark)
		time.sleep(1)
		driver.find_element_by_xpath("//*[@id='form-main-batch']/div[2]/button[2]").click()
		

	#断言
	def Assertequal(self, i):
		driver = self.driver
		xpath = self.listdata[i]["xpath"]
		expectValue=self.listdata[i]['expectValue']
		print u"expectValue:" + expectValue
		try:
			time.sleep(1)
			actualValue = driver.find_element_by_xpath(xpath).text
			print u"actualValue:" + actualValue
			#判断预期与实际结果是否相等，为真通过，为假截图
			vlue = self.assertCompare(expectValue,actualValue)
			if vlue:
				pass
			else:
				fail_pic_path = case_pic_path + "Nest_Admin_Create_HitaCard_Batch_%s.png"%(i+1)
				print "image" + fail_pic_path
				driver.get_screenshot_as_file(fail_pic_path)
				assert 0,u"~~~~~~Test Case Fail~~~~~~"				
		except NoSuchElementException:
			fail_pic_path = case_pic_path + "Nest_Admin_Create_HitaCard_Batch_%s.png"%(i+1)
			print "image" + fail_pic_path
			driver.get_screenshot_as_file(fail_pic_path)
			assert 0,u"~~~~~~xpath not exist~~~~~~"
		time.sleep(1)

	#预期与实际比较
	def assertCompare(self,expectValue,actualValue):
		flag=True
		driver = self.driver	
		try:
			self.assertEqual(expectValue, actualValue)
			return flag
		except:
			flag=False
			return flag