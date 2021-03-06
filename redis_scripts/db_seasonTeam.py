from db_aggregation import seasonRaces
from collections import OrderedDict
from prettytable import PrettyTable

import redis 

def isNumber(input):
        try:
                num = int(input)
        except ValueError:
                return False
        else:
                return True

def seasonTeam(season):
        if not isNumber(season):
                raise Exception('Wrong arg')
        if not db.hexists('season', season):
                print 'Season not found'
        else:
		x = PrettyTable(['Team', 'Points'])
		seas = seasonRaces(season)
		total_res = {}
		for k,v in seas.items():
			for k1,v1 in v.items():
				dpoints = db.hmget('rule', 's{0}:{1}'.format(season,k1))[0]
				if not dpoints is None:
					dteam = db.hmget('contract', 's{0}:{1}'.format(season, v1['Pilot']))[0]
					if not dteam in total_res:
						total_res[dteam] = 0
					total_res[dteam] += int(dpoints)
		
		total = OrderedDict(sorted(total_res.items(), key=lambda x: x[1], reverse = True))  
		for k,v in total.items():
			dteamName = db.hmget('team:{0}'.format(k), 'TeamName')
			x.add_row([dteamName[0], v])
		print x

db = redis.Redis('localhost')
