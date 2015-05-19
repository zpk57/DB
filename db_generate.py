import redis

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
        if not db.exists('race:{0}'.format(season)):
                print 'Race is not exists'	
	else:
		for key in db.scan_iter():
			print key
			

def generate_qual_season(season):
	if not isNumber(season):
		raise Exception('Wrong param')
	if not db.exists('season:{0}'.format(season)):
		print 'Season is not exists'
	else:
		a = 23
		
		

db = redis.Redis('localhost')
generate_qual_race(1,1)
