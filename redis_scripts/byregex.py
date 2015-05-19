#!/usr/bin/python 
# -*- coding: utf-8 -*-

import re
import redis
from string import maketrans 
import sys

intab = "ÉÖÓÊÅÍÃØÙÇÕÚÔÛÂÀÏÐÎËÄÆÝß×ÑÌÈÒÜÁÞéöóêåíãøùçõúôûâàïðîëäæýÿ÷ñìèòüáþ"
outtab = "QWERTYUIOP[]ASDFGHJKL;;ZXCVBNM,.qwertyuiop[]asdfghjkl;;zxcvbnm,."
trantab = maketrans(intab, outtab)

db = redis.Redis('localhost')

def byregex(patt):
	for key in db.scan_iter('pilot:*'): 
		name = db.hget(key, 'FirstName')
		val = re.search(patt, name)
		if val != None:
			print '{0}'.format(db.hgetall(key))

if len( sys.argv ) >= 1:
	byregex(sys.argv[1].translate(trantab))
#	byregex(sys.argv[1])
else:
	print('Not enough arguments')