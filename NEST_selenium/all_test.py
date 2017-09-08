# coding=utf-8

#import sys
#sys.path.append("\test_case")
import unittest
import HTMLTestRunner
import time, os

now  = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
allcase=".\\test_case"
report_name=".\\Report\\" + now + "test_all.html"

def createSuiteone():    #按顺序执行
	testunit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover

	for casefile in [ 
#								'test_admin_login.py',
#								'test_admin_create_LLF.py',
#								'test_admin_create_Agent.py',
								'test_agent_create_Merchant.py'
							]:
		testunit.addTest(discover(allcase, pattern = casefile ,top_level_dir = None))

	return testunit


def createSuitetwo():   #匹配文件 执行
	testunit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(allcase, 
		pattern = 'test_fund_create.py',
		top_level_dir = None)

	for suite in discover:
		for case in suite:
			testunit.addTests(case)
			#print testunit

	return testunit

if __name__ == '__main__':
	allcasename=createSuiteone()

	with open(report_name, 'w') as fp:
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
												title=u'HiPay管理系统自动化测试报告',
												description=u'测试用例结果'
												)
		runner.run(allcasename)
