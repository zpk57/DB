import redis
from datetime import date

db = redis.Redis('localhost')

def isNumber(input):
	try:
		num = int(input)       
	except ValueError:
     		return False	
  	else:
		return True

def add_season(datebegin, dateend, count):
	if not isNumber(count):
		raise Exception('Wrong param') 
	dcount = int(db.get('season:count'))
	value = '{0} {1} {2}'.format(datebegin, dateend, count)
	pipe = db.pipeline()
	pipe.hset('season', dcount+1, value)
	pipe.incr('season:count')				#use count as id
	pipe.execute()
def add_rules(season, place, points):
	if not isNumber(season) or not isNumber(place) or not isNumber(points):
		raise Exception('Wrong param')
	if not db.hexists('season', season):
		print 'Not such season for a rule'
	else:
		l = 's{0}:{1}'.format(season,place)
		pipe = db.pipeline()
		pipe.hset('rule', l, points)
		pipe.execute()
def add_country(fullname, shortname):
	pipe = db.pipeline()
	pipe.hset('country', shortname, fullname) 		#we can see all avaliable countries
	pipe.execute()
def add_track(name, country, laps):
	if not isNumber(laps):
		raise Exception('Wrong laps param')
	if not db.hexists('country', country): 
		print 'Country not found'
	else:
		if not db.hexists('track:lookup:name', name):
			dcount = int(db.get('track:count'))
			pipe = db.pipeline()
			pipe.hset('track:lookup:name', name, dcount+1)
			pipe.hset('track:{0}'.format(dcount+1), 'CountryShortName', country)
			pipe.hset('track:{0}'.format(dcount+1), 'Name', name)
			pipe.hset('track:{0}'.format(dcount+1), 'Lap', laps)
			pipe.incr('track:count')
			pipe.execute()
		else:
			print 'Track already created'
def add_race(season, track):
	if not isNumber(season) or not isNumber(track):
		raise Exception('Wrong param')
	if db.hexists('season', season) and db.exists('track:{0}'.format(track)):
		dcount = int(db.get('race:count'))
		pipe = db.pipeline()
		pipe.sadd('race:s{0}'.format(season), dcount+1)
		pipe.hset('race:track', dcount+1, track)
		pipe.incr('race:count')
		pipe.execute()
	else:
		print 'Incorrect season or track'
def add_team(name, country):
	if not db.hexists('country', country): 
		print 'Country not found'
	else:
		if not db.hexists('team:lookup:name', name):
			dcount = int(db.get('team:count'))
			pipe = db.pipeline()
			pipe.hset('team:lookup:name', name, dcount+1)
			pipe.hset('team:{0}'.format(dcount+1), 'TeamName', name)
			pipe.hset('team:{0}'.format(dcount+1), 'CountryShortName', country)
			pipe.incr('team:count')
			pipe.execute()
		else:
			print 'Team already created'
def add_pilot(name, surname, shortname, country):
	if not db.hexists('country', country): 
		print 'Country not found'
	else:
		pipe = db.pipeline()
		pipe.hset('pilot:{0}'.format(shortname), 'FirstName', name)
		pipe.hset('pilot:{0}'.format(shortname), 'LastName', surname)
		pipe.hset('pilot:{0}'.format(shortname), 'CountryShortName', country)
		pipe.execute()
def add_contract(season, pilot, team):
	if not db.hexists('season', season) or not db.exists('pilot:{0}'.format(pilot)) or not db.hexists('team:lookup:name', team):
		print 'Wrong Argument'
	else:
		dteam = db.hget('team:lookup:name', team)
		pipe = db.pipeline()
		pipe.hset('contract', 's{0}:{1}'.format(season,pilot), dteam)
		pipe.execute()
def add_powerlvl(season, pilot, car, skill):
	if not db.hexists('season', season) or not db.exists('pilot:{0}'.format(pilot)):
		print 'Wrong Argument'
	else:
		pipe = db.pipeline()
		pipe.hmset('powerlvl:s{0}:{1}'.format(season,pilot), {'Car':car, 'Skill':skill})	
		pipe.execute()
		