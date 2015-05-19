import redis
from collections import OrderedDict

def isNumber(input):
        try:
                num = int(input)
        except ValueError:
                return False
        else:
                return True

def raceStat(season, race):
	result = {} 
	if not isNumber(race):
		raise Exception('Wrong arg')	
	if not db.hexists('race:track', race):
		print 'Race is not found'
	else:
		dtrack = db.hmget('race:track', race)
		dlap = db.hmget('track:{0}'.format(dtrack[0]), 'Lap')
                for key in db.hscan_iter('contract', 's{0}:*'.format(season)):
                        who = key[0].replace('s{0}:'.format(season), '')
			result[who] = 0	
			for i in range(int(dlap[0])):
				result[who] += float(db.hmget('time', '{0}:{1}:{2}'.format(race,i+1,who))[0])
	sort_result = OrderedDict(sorted(result.items(), key=lambda x: x[1]))
	i = 1 
	for k,v in sort_result.items():
		sort_result[k] = i	
		i += 1
	return sort_result

def qualStat(season, race):
	result = {} 
	if not isNumber(race):
		raise Exception('Wrong arg')	
	if not db.hexists('race:track', race):
		print 'Race is not found'
	else:
                for key in db.hscan_iter('contract', 's{0}:*'.format(season)):
                        who = key[0].replace('s{0}:'.format(season), '')
			result[who] = float(db.hmget('qual', '{0}:{1}'.format(race,who))[0])	
	sort_result = OrderedDict(sorted(result.items(), key=lambda x: x[1]))
	i = 1 
	for k,v in sort_result.items():
		sort_result[k]=i
		i += 1
	return sort_result

def raceInfo(season, race):
	result = {}
	qualPos = qualStat(season, race)	
	racePos = raceStat(season, race)
	for k,v in racePos.items():
		result[v] = {'Pilot':k, 'Qualification':qualPos[k]}	
	return result

def seasonRaces(season):
        result = {}
        if not isNumber(season):
                raise Exception('Wrong param')
        if not db.hexists('season', season):
                print 'Season not found'
        else:
                draces = db.smembers('race:s{0}'.format(season))
		draces = sorted(draces)
                for i in draces:
                        result[i] = raceInfo(season, i)

        return result

db = redis.Redis('localhost')
