import redis
from datetime import date

db = redis.Redis('localhost')

def delete_season(SeasonId):
	if not isNumber(SeasonId):
		raise Exception('Wrong param') 
	pipe = db.pipeline()
	for val in db.smembers('race:s{0}'.format(SeasonId)):
		pipe.hdel('race:track', val)	
	pipe.delete('race:s{0}'.format(SeasonId))
	pipe.hdel('season', SeasonId)	
#	pipe.hdel('rule', 's{0}:*'.format(season))
	pipe.execute()
def delete_rules(season, place):
	if not isNumber(season) or not isNumber(place):
		raise Exception('Wrong param')
	if not db.hexists('season', season):
		print 'Not such season for a rule'
	else:
		l = 's{0}:{1}'.format(season,place)
		pipe = db.pipeline()
		pipe.hdel('rule', l)
		pipe.execute()
def delete_country(shortname):
	pipe = db.pipeline()
	pipe.hdel('country', shortname) 		#we can see all avaliable countries
	pipe.execute()
def delete_track(TrackName):
	if db.hexists('track:lookup:name', TrackName):
		dcount = int(db.hget('track:lookup:name', TrackName))
		pipe = db.pipeline()
		pipe.delete('track:{0}'.format(dcount))
		pipe.hdel('track:lookup:name', TrackName)
		pipe.execute()
def delete_race(SeasonID, RaceId):
	if not isNumber(RaceId):
		raise Exception('Wrong param')
	if db.hexists('season', season) and db.exists('track:{0}'.format(track)):
		pipe = db.pipeline()
		pipe.srem('race:s{0}'.format(SeasonID), RaceId)
		pipe.hdel('race:track', RaceId)
		pipe.execute()
	else:
		print 'Incorrect season or track'
def delete_team(name):
	if db.hexists('team:lookup:name', name):
		id = db.get('team:lookup:name', name)
		pipe = db.pipeline()
		pipe.hdel('team:lookup:name', name)
		pipe.delete('team:{0}'.format(id))
		pipe.execute()
def delete_pilot(shortname):
	pipe = db.pipeline()
	pipe.delete('pilot:{0}'.format(shortname))
	pipe.execute()
def add_contract(season, pilot):
	if not isNumber(season):
		print 'Wrong Argument'
	else:
		pipe = db.pipeline()
		pipe.hdel('contract', 's{0}:{1}'.format(season,pilot))
		pipe.execute()
def del_powerlvl(season, pilot):
	if not isNumber(season):
		print 'Wrong Argument'
	else:
		pipe = db.pipeline()
		pipe.delete('powerlvl:s{0}:{1}'.format(season,pilot))	
		pipe.execute()
