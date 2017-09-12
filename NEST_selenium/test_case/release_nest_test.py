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

class Release_Nese_Test(unittest.TestCase):
	
	data_file = ".\\test_data\\merchant_create_coupon.xlsx"
	#读取数据
	listdata = file_read.excel_read(filepath = data_file)