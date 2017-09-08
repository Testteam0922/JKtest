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

class Nest_Agent_Create_Merchant(unittest.TestCase):
	
	data_file = ".\\test_data\\agent_create_merchant.xlsx"
	#读取数据
	listdata = file_read.excel_read(filepath = data_file)	
	
	def setUp(self):
		self.driver = webdriver.Chrome(chromedriver_path)
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get(login_addr)
		time.sleep(2)
		driver.find_element_by_name("username").send_keys(agent_login_name)
		driver.find_element_by_name("password").send_keys(agent_login_passwd)
		driver.find_element_by_xpath("//*[@id='form-validation']/div[5]/button").click()
		time.sleep(2)
	
	def case_run(self,i):
		driver = self.driver		
		self._agent_create_merchant(i)
		self.Assertequal(i)

	#用例
	def test_case_00001(self,i=0): self.case_run(i)
		
	#关闭浏览器
	def tearDown(self):
		self.driver.quit()

	def _agent_create_merchant(self, i ):
		driver = self.driver
		
		merchant_name = self.listdata[i]['merchant_name']
		merchant_nickname = self.listdata[i]['merchant_nickname']
		merchant_username = self.listdata[i]['merchant_username']
		merchant_country = self.listdata[i]['merchant_country']
		merchant_area = self.listdata[i]['merchant_area']
		merchant_address = self.listdata[i]['merchant_address']
		merchant_contacts = self.listdata[i]['merchant_contacts']
		merchant_phone = self.listdata[i]['merchant_phone']
		merchant_email = self.listdata[i]['merchant_email']
		merchant_coin_type = self.listdata[i]['merchant_coin_type']
		merchant_remark = self.listdata[i]['merchant_remark']
		uploadfile = self.listdata[i]['uploadfile']
		
		 
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/nav[1]/div[2]/div/div/ul/li[2]/a").click()
		time.sleep(1)
		driver.find_element_by_xpath("//*[@id='addnewshop']").click()
		time.sleep(0.5)
		driver.find_element_by_name("name").send_keys(merchant_name)
		time.sleep(0.5)
		driver.find_element_by_name("nickname").send_keys(merchant_nickname)
		time.sleep(0.5)
		driver.find_element_by_name("username").send_keys(merchant_username)
		time.sleep(0.5)
		driver.find_element_by_id("select2-country-container").click() #点击选择国家
		time.sleep(0.5)
		driver.find_element_by_xpath("//*[@id='form-main']/div[1]/div[4]/span[2]/span/span[1]/input").send_keys(merchant_country)
		driver.find_element_by_xpath("//*[@id='select2-country-results']/li[1]").click()		
		time.sleep(0.5)
		driver.find_element_by_name("area").send_keys(merchant_area)
		driver.find_element_by_name("address").send_keys(merchant_address)				
		driver.find_element_by_name("contact").send_keys(merchant_contacts)
		time.sleep(0.5)
		driver.find_element_by_name("phone").send_keys(merchant_phone)
		time.sleep(0.5)
		driver.find_element_by_name("email").send_keys(merchant_email)
		time.sleep(1)
		driver.find_element_by_xpath("//*[@id='form-main']/div[1]/div[10]/span[1]/span[1]/span/span[2]").click()
		time.sleep(0.5)
		driver.find_element_by_xpath("//*[@id='form-main']/div[1]/div[10]/span[2]/span/span[1]/input").send_keys(merchant_coin_type)
		driver.find_element_by_xpath("//*[@id='select2-fee_type-results']").click()
		time.sleep(0.5)	
		driver.find_element_by_name("remark").send_keys(merchant_remark)
		#上传文件
				
																			
		driver.find_element_by_xpath("//*[@id='form-main']/div[2]/button[2]").click()
		

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
				fail_pic_path = case_pic_path + "Nest_Admin_Create_Agent_%s.png"%(i+1)
				print "image" + fail_pic_path
				driver.get_screenshot_as_file(fail_pic_path)
				assert 0,u"~~~~~~Test Case Fail~~~~~~"				
		except NoSuchElementException:
			fail_pic_path = case_pic_path + "Nest_Admin_Create_Agent_%s.png"%(i+1)
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