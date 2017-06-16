# coding: utf-8

import requests
import datetime

from datetime import datetime
def req(methord, url, headers, payload, payloadmethord = "data", file_type = "text"):
	ISOTIMEFORMAT= '%Y-%m-%d %X'
	before = datetime.now()
	try:
		if methord == "GET":
			r = requests.get(url, headers = headers, params = payload)
		elif methord == "POST":
			if payloadmethord == "data":
				r = requests.post(url, headers = headers, data = payload)
			elif payloadmethord == "params":
				r = requests.post(url, headers = headers, params = payload)
	except requests.exceptions.ConnectTimeout:
		print "Network Conection is Timeout."
	
	after = datetime.now()
	#tt = (after-before).seconds
	time = '%d'%(after-before).seconds
	print u'请求用时:'+ time

	if file_type == "binary":
		return r.content
	else:
		return r.text
