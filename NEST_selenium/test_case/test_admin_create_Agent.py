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

class Nest_Admin_Create_Agent(unittest.TestCase):
	
	data_file = ".\\test_data\\admin_create_agent.xlsx"
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
		self._admin_create_agent(i)
#		self.Assertequal(i)

	#用例
	def test_case_00001(self,i=0): self.case_run(i)
		
	#关闭浏览器
#	def tearDown(self):
#		self.driver.quit()

	def _admin_create_agent(self, i ):
		driver = self.driver
		
		agent_name = self.listdata[i]['agent_name']
		agent_nickname = self.listdata[i]['agent_nickname']
		agent_username = self.listdata[i]['agent_username']
		agent_contacts = self.listdata[i]['agent_contacts']
		agent_phone = self.listdata[i]['agent_phone']
		agent_email = self.listdata[i]['agent_email']
		agent_address = self.listdata[i]['agent_address']
		agent_rank = self.listdata[i]['agent_rank']
		agent_coin_type = self.listdata[i]['agent_coin_type']
		
		 
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/nav[1]/div[2]/div/div[1]/ul/li[3]/a").click()
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/section/div/div[1]/div/section/div[4]/button").click()
		time.sleep(0.5)
		driver.find_element_by_name("name").send_keys(agent_name)
		time.sleep(0.5)
		driver.find_element_by_name("nickname").send_keys(agent_nickname)
		time.sleep(0.5)
		driver.find_element_by_name("agent_user_name").send_keys(agent_username)
		time.sleep(0.5)
		driver.find_element_by_name("contact").send_keys(agent_contacts)
		time.sleep(0.5)
		driver.find_element_by_name("phone").send_keys(agent_phone)
		time.sleep(0.5)
		driver.find_element_by_name("email").send_keys(agent_email)
		time.sleep(0.5)
		driver.find_element_by_name("address").send_keys(agent_address)				
		time.sleep(0.5)
		driver.find_element_by_name("agent_rank").click()
		if agent_rank == '1' :
			driver.find_element_by_xpath("//*[@id='agent_rank']/option[2]").click()
		elif agent_rank == '2' :
			driver.find_element_by_xpath("//*[@id='agent_rank']/option[3]").click()
		elif agent_rank == '3' :
			driver.find_element_by_xpath("//*[@id='agent_rank']/option[4]").click()		
		time.sleep(1)
		driver.find_element_by_xpath("//*[@id='form-main']/div[1]/div[10]/span/span[1]/span/span[2]").click()
		time.sleep(0.5)
		driver.find_element_by_xpath("//*[@id='form-main']/div[1]/div[10]/span[2]/span/span[1]/input").send_keys(agent_coin_type)
		driver.find_element_by_xpath("//*[@id='select2-coin_type-results']").click()
																			
		driver.find_element_by_xpath("//*[@id='confirm']").click()
		

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