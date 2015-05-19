import redis
import random

db = redis.Redis('localhost')
	
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
			if not pcar[0] is None and not pskill[0] is None:
				time -= (0.1 * int(pcar[0]) + 0.05 * int(pskill[0]))
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
			print 'Qual {0} generated'.format(key)
		print 'Season qual {0} generated'.format(season)

def generate_race(season, race):
	if not isNumber(race):
		raise Exception('Wrong param')
	if not db.hexists('race:track', race):
		print 'Race is not exists'
	else:
		dtrack = db.hmget('race:track', race)
		dlap = db.hmget('track:{0}'.format(dtrack[0]), 'Lap')
		for i in range(int(dlap[0])):
			for key in db.hscan_iter('contract', 's{0}:*'.format(season)):
				who = key[0].replace('s{0}:'.format(season), '')
				pcar = db.hmget('powerlvl:s{0}:{1}'.format(season,who), 'Car')
				pskill = db.hmget('powerlvl:s{0}:{1}'.format(season,who), 'Skill')
				time = 148 + random.randint(-5, 5)
				time += random.random()
				if not pcar[0] is None and not pskill[0] is None:
					time -= (0.1 * int(pcar[0]) + 0.05 * int(pskill[0]))
				time = round(time,3)
				pipe = db.pipeline()
				pipe.hmset('time', {'{0}:{1}:{2}'.format(race,i+1,who):time})
				pipe.execute()

def generate_race_season(season):
        if not isNumber(season):
                raise Exception('Wrong param')
        if not db.hexists('season', season):
                print 'Season is not exists'
        else:
                for key in db.sscan_iter('race:s{0}'.format(season)):
                        generate_race(season, key)
			print 'Race {0} generated'.format(key)
		print 'Season {0} generated'.format(season)
		
def start_generate():
	generate_qual_season(1)
	generate_qual_season(2)
	generate_qual_season(3)
	generate_race_season(1)
	generate_race_season(2)
	generate_race_season(3)
