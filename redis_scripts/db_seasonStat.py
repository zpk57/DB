from db_aggregation import seasonRaces 
import redis 

def isNumber(input):
        try:
                num = int(input)
        except ValueError:
                return False
        else:
                return True

def seasonStat(season):
        if not isNumber(season):
                raise Exception('Wrong arg')
        if not db.hexists('season', season):
                print 'Season not found'
        else:
		seas = seasonRaces(season)

	for k,v in seas.items():
		dtrack = db.hmget('race:track',k) 	
		dtrackName = db.hmget('track:{0}'.format(dtrack[0]), 'Name')	
		print dtrackName
		for k1,v1 in v.items():
			dpilot = db.hgetall('pilot:{0}'.format(v1['Pilot']))
			dpoints = db.hmget('rule', 's{0}:{1}'.format(3,k1))[0]
			if dpoints is None:
				dpoints = 0
			print '{0} {1}\t\t\t\t{2}\t\t{3}'.format(dpilot['FirstName'], dpilot['LastName'], k1, dpoints)
		print ''

db = redis.Redis('localhost')
