#!/usr/bin/python 
# -*- coding: utf-8 -*-

import Levenshtein as lvn
import redis
from string import maketrans 
import sys

intab = "ÉÖÓÊÅÍÃØÙÇÕÚÔÛÂÀÏĞÎËÄÆİß×ÑÌÈÒÜÁŞéöóêåíãøùçõúôûâàïğîëäæıÿ÷ñìèòüáş"
outtab = "QWERTYUIOP[]ASDFGHJKL;;ZXCVBNM,.qwertyuiop[]asdfghjkl;;zxcvbnm,."
trantab = maketrans(intab, outtab)

db = redis.Redis('localhost')

def isNumber(input):
	try:
		num = int(input)       
	except ValueError:
     		return False	
  	else:
		return True
		
def levenshtain(patt, dist):
	for key in db.scan_iter('pilot:*'): 
		name = db.hget(key, 'FirstName')
		val = lvn.distance(patt, name)
		if val <= dist:
			print 'dist={0}: {1}'.format(val, db.hgetall(key))

if len( sys.argv ) >= 2:
	if not isNumber(sys.argv[2]):
		raise Exception('Wrong number') 
	levenshtain(sys.argv[1].translate(trantab), int(sys.argv[2]))
#	levenshtain(sys.argv[1], int(sys.argv[2]))
else:
	print('Not enough arguments')