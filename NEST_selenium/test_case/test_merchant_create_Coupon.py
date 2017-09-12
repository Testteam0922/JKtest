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

class Nest_Merchant_Create_Coupon(unittest.TestCase):
	
	data_file = ".\\test_data\\merchant_create_coupon.xlsx"
	#读取数据
	listdata = file_read.excel_read(filepath = data_file)
	
	def setUp(self):
		self.driver = webdriver.Chrome(chromedriver_path)
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get(login_addr)
		time.sleep(2)
		driver.find_element_by_name("username").send_keys(merchant_login_name)
		driver.find_element_by_name("password").send_keys(merchant_login_passwd)
		driver.find_element_by_xpath("//*[@id='form-validation']/div[5]/button").click()
		time.sleep(2)

	def case_run(self,i):
		driver = self.driver
		self._merchant_create_coupon(i)
		self.Assertequal(i)
		
	#用例
	def test_case_00001(self,i=0): self.case_run(i)
	#关闭浏览器
	def tearDown(self):
		self.driver.quit()

	def _merchant_create_coupon(self,i):
		driver = self.driver
		coupon_title = self.listdata[i]['title']
		sub_title = self.listdata[i]['sub_title']
		coupon_type = self.listdata[i]['coupon_type']
		coupon_fee = self.listdata[i]['discount_num']
		expired_select = self.listdata[i]['expired_select']
		days = self.listdata[i]['days']
		expired_start = self.listdata[i]['expired_start']
		expired_end = self.listdata[i]['expired_end']
		coupon_explain = self.listdata[i]['coupon_explain']
		total_count = self.listdata[i]['total_count']
		use_count = self.listdata[i]['use_count']
		use_count_select = self.listdata[i]['use_count_select']
		get_count = self.listdata[i]['get_count']
		cost_start = self.listdata[i]['cost_start']
		coupon_max = self.listdata[i]['coupon_max']

		driver.find_element_by_xpath("/html/body/nav[1]/div[2]/div/div/ul/li[2]/a").click()
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/section/div/div[1]/div/section/div[4]/button").click()
		time.sleep(1)
		driver.find_element_by_id("title").send_keys(coupon_title)
		time.sleep(0.5)
		driver.find_element_by_id("sub_title").send_keys(sub_title)
		
		if coupon_type =='1':
			driver.find_element_by_xpath("//*[@id='coupon_type']/div/button[1]").click()
			time.sleep(0.5)
			driver.find_element_by_id("discount_num").send_keys(coupon_fee)
			time.sleep(0.5)
			
			if use_count_select == '1':
				driver.find_element_by_xpath("//*[@id='is_card']/button[1]").click()
			elif use_count_select == '2':
				driver.find_element_by_xpath("//*[@id='is_card']/button[2]").click()
			else:
				print u'use_count_select参数输入错误'
			time.sleep(0.5)
			driver.find_element_by_id("coupon_max").send_keys(coupon_max)
			time.sleep(0.5)
		elif coupon_type == '2':
			driver.find_element_by_xpath("//*[@id='coupon_type']/div/button[2]").click()
			time.sleep(0.5)
			driver.find_element_by_id("cash_num").send_keys(coupon_fee)
		elif coupon_type == '3':
			driver.find_element_by_xpath("//*[@id='coupon_type']/div/button[3]").click()
			time.sleep(0.5)
			driver.find_element_by_id("gift_num").send_keys(coupon_fee)
		else :
			print u'coupon_type参数输入错误'

		if expired_select == '1':		
			driver.find_element_by_xpath("//*[@id='expired_type']/div/button[1]").click()
			time.sleep(1)
			driver.find_element_by_id("expired_time").send_keys(days)
		elif expired_select == '2':
			driver.find_element_by_xpath("//*[@id='expired_type']/div/button[2]").click()
			
			js="$(\"input[id='expired_start']\").removeAttr('readonly')"
			driver.execute_script(js)
			elem = driver.find_element_by_id("expired_start")
			elem.clear()
			elem.send_keys(expired_start)	
			driver.find_element_by_xpath("//*[@id='expired_type']/label").click()
			time.sleep(1)
			js="$(\"input[id='expired_end']\").removeAttr('readonly')"
			driver.execute_script(js)
			elem = driver.find_element_by_id("expired_end")
			elem.clear()
			elem.send_keys(expired_end)	
			driver.find_element_by_xpath("//*[@id='expired_type']/label").click()
		else:
			print u'expired_select参数输入错误'
		time.sleep(0.5)
		driver.find_element_by_id("coupon_explain").send_keys(coupon_explain)
		time.sleep(0.5)
		driver.find_element_by_id("total_count").send_keys(total_count)
		time.sleep(0.5)
		driver.find_element_by_id("use_count").send_keys(use_count)
		time.sleep(0.5)
		if get_count == '':
			pass
		else:
			elem = driver.find_element_by_id("get_count")
			elem.clear()
			elem.send_keys(get_count)
		time.sleep(0.5)
		driver.find_element_by_id("cost_start").send_keys(cost_start)
		time.sleep(0.5)
		
		driver.find_element_by_xpath("//*[@id='coupon_form_main']/div[2]/button[2]").click()
		
	#断言
	def Assertequal(self, i):
		driver = self.driver
		xpath = self.listdata[i]["xpath"]
		expectValue=self.listdata[i]['expectValue']
		print u"预期结果:" + expectValue
		try:
			time.sleep(1)
			actualValue = driver.find_element_by_xpath(xpath).text
			print u"实际结果:" + actualValue
			#判断预期与实际结果是否相等，为真通过，为假截图
			vlue = self.assertCompare(expectValue,actualValue)
			if vlue:
				pass
			else:
				fail_pic_path = case_pic_path + "Nest_Merchant_Create_Coupon_%s.png"%(i+1)
				print "image" + fail_pic_path
				driver.get_screenshot_as_file(fail_pic_path)
				assert 0,u"~~~~~~Test Case Fail~~~~~~"				
		except NoSuchElementException:
			fail_pic_path = case_pic_path + "Nest_Merchant_Create_Coupon_%s.png"%(i+1)
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