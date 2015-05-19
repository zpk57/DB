import redis
import random

def isNumber(input):
        try:
                num = int(input)
        except ValueError:
                return False
        else:
                return True 

def generate_qual_race(season, race):
	if not isNumber(race):
                raise Exception('Wrong param')
        if not db.hexists('race:track', race):
                print 'Race is not exists'	
	else:
		for key in db.hscan_iter('contract', 's{0}:*'.format(season)):
			who = key[0].replace('s{0}:'.format(season), '')
			pcar = db.hmget('powerlvl:s{0}:{1}'.format(season,who), 'Car')
			pskill = db.hmget('powerlvl:s{0}:{1}'.format(season,who), 'Skill')
			time = 148 + random.randint(-5, 5)
			time += random.random()
			if not pcar is None and not pskill is None:
				time -= (0.05 * int(pcar[0]) + 0.01 * int(pskill[0]))
			time = round(time,3)
			pipe = db.pipeline()
			pipe.hmset('qual', {'{0}:{1}'.format(race,who):time})
			pipe.execute()

def generate_qual_season(season):
	if not isNumber(season):
		raise Exception('Wrong param')
	if not db.hexists('season', season):
		print 'Season is not exists'
	else:
		for key in db.sscan_iter('race:s{0}'.format(season)):
			generate_qual_race(season, key)	
		
		

db = redis.Redis('localhost')
generate_qual_season(3)
