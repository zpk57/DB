#!/usr/bin/python 
#!/usr/bin/env python 
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
		
def hamming(patt, dist):
	for key in db.scan_iter('pilot:*'): 
		name = db.hget(key, 'FirstName')
		if len(name) == len(patt):
			leng = 0
			for i in range(0,len(name)):
				if name[i] != patt[i]:
					leng += 1;
			if leng <= dist:
				print 'dist={0}: {1}'.format(leng, db.hgetall(key))

if len( sys.argv ) >= 2:
	if not isNumber(sys.argv[2]):
		raise Exception('Wrong number') 
	hamming(sys.argv[1].translate(trantab), int(sys.argv[2]))
#	hamming(sys.argv[1], int(sys.argv[2]))
else:
	print('Not enough arguments')