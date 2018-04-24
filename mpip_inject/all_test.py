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
				'test_authCode_pay_order.py',
				'test_authCode_pay_query.py',
				'test_authCode_refund_apply.py',
				'test_authCode_refund_query.py',
				'test_authCode_order_revoke.py',
				'test_appWeb_yidong_pay_order.py',
				'test_returnCode_pay_query.py',
				'test_returnCode_refund_query.py',
				'test_returnCode_refund_apply.py',
				'test_returnCode_pay_order.py',
				'test_appWeb_unity_pay_query.py',
				'test_appWeb_unity_refund_query.py',
				'test_appWeb_unity_refund_apply.py',
				'test_appWeb_unity_pay_order.py',
				'test_appWeb_movement_pay_order.py',
				'test_appWeb_movement_pay_query.py',
				'test_appWeb_movement_refund_apply.py',
				'test_appWeb_movement_refund_query.py',
							]:
		testunit.addTest(discover(allcase, pattern = casefile ,top_level_dir = None))

	return testunit

if __name__ == '__main__':
	allcasename=createSuiteone()

	with open(report_name, 'w') as fp:
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
												title=u'mpip自动化测试报告',
												description=u'测试用例结果'
												)
		runner.run(allcasename)
