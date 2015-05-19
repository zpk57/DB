#!/usr/bin/python 
#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import Levenshtein as lvn
import redis
from string import maketrans 
import sys

intab = "ÉÖÓÊÅÍÃØÙÇÕÚÔÛÂÀÏÐÎËÄÆÝß×ÑÌÈÒÜÁÞéöóêåíãøùçõúôûâàïðîëäæýÿ÷ñìèòüáþ"
outtab = "QWERTYUIOP[]ASDFGHJKL;;ZXCVBNM,.qwertyuiop[]asdfghjkl;;zxcvbnm,."
trantab = maketrans(intab, outtab)

db = redis.Redis('localhost')

def isNumber(input):
	try:
		num = float(input)       
	except ValueError:
     		return False	
  	else:
		return True
		
def jarowinkler(patt, dist):
	for key in db.scan_iter('pilot:*'): 
		name = db.hget(key, 'FirstName')
		val = lvn.ratio(patt, name)
		if val >= dist:
			print 'dist={0}: {1}'.format(val, db.hgetall(key))

if len( sys.argv ) >= 2:
	if not isNumber(sys.argv[2]):
		raise Exception('Wrong number') 
	jarowinkler(sys.argv[1].translate(trantab), float(sys.argv[2]))
#	jarowinkler(sys.argv[1], float(sys.argv[2]))
else:
	print('Not enough arguments')