# coding: utf-8

import md5, operator

def get_key_value_sign(pars, k):
	''' 值排序，键值KEY签名 '''
	sig_str = ""
	pars = sorted(pars.items(), key = operator.itemgetter(0))
	for tul in pars:
		sig_str += tul[0] + "=" + tul[1] + "&"
	sig_str = sig_str[:-1] + "&key=" + k
	
	m = md5.new()
	m.update(sig_str)
	return m.hexdigest().upper()