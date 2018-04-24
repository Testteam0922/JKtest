# coding: utf-8

import md5, operator
import hashlib

def get_key_value_sign(dict, k):
	''' 键值排序加key值加密'''
	key_dict = sorted(dict.keys())
	ss = ""
	for key_value in key_dict:
		if dict[key_value] == "":
			continue 
		else:
			ss = ss + key_value + "=" + dict[key_value] + "&"
	# #print key	

	# for key_value in key_dict:
	# 	ss = ss + key_value + "=" + dict[key_value] + "&"
	# #print key	


	ss = ss + "key" + "=" + k	
	#print ss
	m = hashlib.md5()
	m.update(ss)
	return m.hexdigest()