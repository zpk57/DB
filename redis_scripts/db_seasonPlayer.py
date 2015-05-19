from db_aggregation import seasonRaces 
from collections import OrderedDict

import redis 

def isNumber(input):
        try:
                num = int(input)
        except ValueError:
                return False
        else:
                return True

def seasonPlayer(season):
	if not isNumber(season):
		raise Exception('Wrong arg')
	if not db.hexists('season', season):
		print 'Season not found'
	else:
		seas = seasonRaces(season)
		total_res = {}
		for k,v in seas.items():
			for k1,v1 in v.items():
				dpoints = db.hmget('rule', 's{0}:{1}'.format(season,k1))[0]
				if not dpoints is None:
					if not v1['Pilot'] in total_res:
						total_res[v1['Pilot']] = 0
					total_res[v1['Pilot']] += int(dpoints)
		total = OrderedDict(sorted(total_res.items(), key=lambda x: x[1], reverse = True))  
		for k,v in total.items():
			dpilot = db.hgetall('pilot:{0}'.format(k))
			print '{0} {1} \t\t\t{2}'.format(dpilot['FirstName'], dpilot['LastName'], v)

db = redis.Redis('localhost')
