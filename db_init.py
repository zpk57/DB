import redis
from datetime import date

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
	l = 'season:{0}'.format(dcount+1)
	r = '{0} {1} {2}'.format(datebegin, dateend, count)
	pipe = db.pipeline()
	pipe.set(l, r)
	pipe.incr('season:count')				#use count as id
	pipe.execute()
def add_rules(season, place, points):
	if not isNumber(season) or not isNumber(place) or not isNumber(points):
		raise Exception('Wrong param')
	if not db.exists('season:{0}'.format(season)):
		print 'Not such season for a rule'
	else:
		l = 'rule:s{0}:{1}'.format(season,place)
		pipe = db.pipeline()
		pipe.set(l, points)
		pipe.execute()
def add_country(fullname, shortname):
	if not db.sismember('country', shortname):
		l = 'country:{0}'.format(shortname)
		pipe = db.pipeline()
		pipe.sadd('country', shortname) 		#we can see all avaliable countries
		pipe.set(l, fullname)
		pipe.execute()
	else:
		print 'Country already created'
def add_track(name, country, laps):
	if not isNumber(laps):
		raise Exception('Wrong param')
	if not db.exists('country:{0}'.format(country)): 
		print 'Country not found'
	else:
		if not db.hexists('track:lookup:name', name):
			dcount = int(db.get('track:count'))
			pipe = db.pipeline()
			pipe.hset('track:lookup:name', name, dcount+1)
			pipe.set('track:{0}'.format(dcount+1), '{0}|{1}'.format(name,country))
			pipe.set('track:lap:{0}'.format(dcount+1), laps)  
			pipe.incr('track:count')
			pipe.execute()
		else:
			print 'Track already created'
def add_race(season, track):
	if not isNumber(season) or not isNumber(track):
		raise Exception('Wrong param')
	if db.exists('season:{0}'.format(season)) and db.exists('track:{0}'.format(track)):
		dcount = int(db.get('race:count'))
		pipe = db.pipeline()
		pipe.sadd('race:s{0}'.format(season), dcount+1)
		pipe.set('race:{0}'.format(dcount+1), track)
		pipe.incr('race:count')
		pipe.execute()
	else:
		print 'Incorrect season or track'
def add_team(name, country):
	if not db.exists('country:{0}'.format(country)): 
		print 'Country not found'
	else:
		if not db.hexists('team:lookup:name', name):
			dcount = int(db.get('team:count'))
			pipe = db.pipeline()
			pipe.hset('team:lookup:name', name, dcount+1)
			pipe.set('team:{0}'.format(dcount+1), '{0}|{1}'.format(name,country))
			pipe.incr('team:count')
			pipe.execute()
		else:
			print 'Team already created'
def add_pilot(name, surname, shortname, country):
	if not db.exists('country:{0}'.format(country)): 
		print 'Country not found'
	else:
		pipe = db.pipeline()
		pipe.hmset('pilot:{0}'.format(shortname), {'FirstName':name, 'LastName':surname, 'Country':country})
		pipe.execute()
def add_contract(season, pilot, team):
	if not db.exists('season:{0}'.format(season)) or not db.exists('pilot:{0}'.format(pilot)) or not db.hexists('team:lookup:name', team):
		print 'Wrong Argument'
	else:
		dteam = db.hget('team:lookup:name', team)
		pipe = db.pipeline()
		pipe.set('contract:s{0}:{1}'.format(season,pilot), dteam)
		pipe.execute()
def add_powerlvl(season, pilot, car, skill):
	if not db.exists('season:{0}'.format(season)) or not db.exists('pilot:{0}'.format(pilot)):
		print 'Wrong Argument'
	else:
		pipe = db.pipeline()
		pipe.hmset('powerlvl:s{0}:{1}'.format(season,pilot), {'Car':car, 'Skill':skill})	
		pipe.execute()

db = redis.Redis('localhost')
db.flushall()
db.set('season:count', 0)
db.set('track:count', 0)
db.set('race:count', 0)
db.set('team:count', 0)

#adding seasons
add_season(date(2000, 3, 4), date(2000, 10, 14), 22)
add_season(date(2001, 3, 12), date(2001, 10, 22), 22)
add_season(date(2014, 3, 16), date(2014, 11, 23), 22)

#adding rules
add_rules(1,1,10)
add_rules(1,2,6)
add_rules(1,3,4)
add_rules(1,4,3)
add_rules(1,5,2)
add_rules(1,6,1)

add_rules(2,1,10)
add_rules(2,2,6)
add_rules(2,3,4)
add_rules(2,5,2)
add_rules(2,6,1)

add_rules(3,1,25)
add_rules(3,2,18)
add_rules(3,3,15)
add_rules(3,4,12)
add_rules(3,5,10)
add_rules(3,6,8)
add_rules(3,7,6)
add_rules(3,8,4)
add_rules(3,9,2)
add_rules(3,10,1)

#adding countries
add_country('United Kingdom', 'UK');
add_country('Italia', 'ITA');
add_country('Irlandia', 'IRL');
add_country('France', 'FRA');
add_country('Switzerland', 'SUI');
add_country('Finland', 'FIN');
add_country('Germany', 'GER');
add_country('Brazil', 'BRA');
add_country('Austria', 'AUT');
add_country('Spain', 'SPA');
add_country('Argentina', 'ARG');
add_country('Netherlands', 'NED');
add_country('Canada', 'CAN');
add_country('Australia', 'AUS');
add_country('Monaco', 'MON');
add_country('Hungary', 'HUN');
add_country('Belgium', 'BEL');
add_country('United States of America', 'USA');
add_country('Japan', 'JAP');
add_country('Malaysia', 'MAL');
add_country('Colombia', 'COL');
add_country('Czech Republic', 'CZE');
add_country('India', 'IND');
add_country('Russian Federation', 'RUS');
add_country('Sweden', 'SWE');	 
add_country('Mexico', 'MEX');
add_country('Venezuela', 'VEN');
add_country('Denmark', 'DEN');
add_country('Bahrain', 'BAH');
add_country('China', 'CHI');
add_country('Singapore', 'SIN');
add_country('United Arab Emirates', 'UAE');

#adding tracks
add_track('Melbourne', 'AUS', 58);
add_track('San Paolo', 'BRA', 71);
add_track('Imola', 'ITA', 62);
add_track('Silverstone', 'UK', 52);
add_track('Cataluniya', 'SPA', 66);
add_track('Nurburgring', 'GER', 56);
add_track('Monte-Carlo', 'MON', 78);
add_track('Magny-Cours', 'BRA', 70);
add_track('A1-Ring', 'AUT', 71);
add_track('Hungaroling', 'HUN', 70);
add_track('Hockenheimring', 'GER', 67);
add_track('Spa-Francorchamps', 'BEL', 44);
add_track('Monza', 'ITA', 53);
add_track('Indianapolis', 'USA', 56);
add_track('Suzuka', 'JAP', 53);
add_track('Sepang', 'MAL', 56);
add_track('Montreal', 'CAN', 70);
add_track('Sakhir', 'BAH', 57);
add_track('Shanghai', 'CHI', 56);
add_track('Marina Bay', 'SIN', 61);
add_track('Sochi Autodrom', 'RUS', 53);
add_track('Austin', 'USA', 56);
add_track('Yas Marina', 'UAE', 55);

#adding races
add_race(1,1);
add_race(1,2);
add_race(1,3);
add_race(1,4);
add_race(1,5);
add_race(1,6);
add_race(1,7);
add_race(1,8);
add_race(1,9);
add_race(1,10);
add_race(1,11);
add_race(1,12);
add_race(1,13);
add_race(1,14);
add_race(1,15);
add_race(1,16);
add_race(1,17);
add_race(2,1);
add_race(2,2);
add_race(2,3);
add_race(2,4);
add_race(2,5);
add_race(2,6);
add_race(2,7);
add_race(2,8);
add_race(2,9);
add_race(2,10);
add_race(2,11);
add_race(2,12);
add_race(2,13);
add_race(2,14);
add_race(2,15);
add_race(2,16);
add_race(2,17);
add_race(3,1);
add_race(3,16);
add_race(3,18);
add_race(3,19);
add_race(3,5);
add_race(3,7);
add_race(3,17);
add_race(3,9);
add_race(3,4);
add_race(3,11);
add_race(3,10);
add_race(3,12);
add_race(3,13);
add_race(3,20);
add_race(3,15);
add_race(3,21);
add_race(3,22);
add_race(3,2);
add_race(3,23);

#adding teams
add_team('McLaren', 'UK');
add_team('Ferrari', 'ITA');
add_team('Jordan', 'IRL');
add_team('Jaguar', 'UK');
add_team('Williams', 'UK');
add_team('Benetton', 'ITA');
add_team('Peugeot', 'FRA');
add_team('Sauber', 'SUI');
add_team('Arrows', 'UK');
add_team('Minardi', 'ITA');
add_team('BAR', 'UK');
add_team('ProstAcer', 'FRA')
add_team('Caterham', 'MAL');
add_team('Force India', 'IND');
add_team('Lotus', 'UK');
add_team('Marussia', 'RUS');
add_team('Mercedes', 'GER');
add_team('Red Bull', 'AUT');
add_team('Toro Rosso', 'ITA');

#adding pilots
add_pilot('Mika', 'Hakkinen', 'HAK', 'FIN');
add_pilot('David', 'Coulthard', 'COL', 'UK');
add_pilot('Michael', 'Schumacher', 'MSC', 'GER');
add_pilot('Rubens', 'Barrichello', 'BAR', 'BRA');
add_pilot('Heinz', 'Frentzen', 'FRE', 'GER');
add_pilot('Jarno', 'Trulli', 'TRU', 'ITA');
add_pilot('Eddie', 'Irvine', 'IRV', 'UK');
add_pilot('Johnny', 'Herbert', 'HRB', 'GER');
add_pilot('Ralf', 'Schumacher', 'RSC', 'GER');
add_pilot('Jenson', 'Button', 'BUT', 'UK');
add_pilot('Giancarlo', 'Fisichella', 'FIS', 'ITA');
add_pilot('Alexander', 'Wurz', 'WUR', 'AUT');
add_pilot('Jean', 'Alesi', 'ALE', 'FRA');
add_pilot('Nick', 'Heidfeld', 'HID', 'GER');
add_pilot('Pedro', 'Diniz', 'DIN', 'BRA');
add_pilot('Mika', 'Salo', 'SAL', 'FIN');
add_pilot('Pedro', 'de la Rosa', 'DLR', 'SPA');
add_pilot('Jos', 'Verstappen', 'VER', 'NED');
add_pilot('Marc', 'Gene', 'GEN', 'SPA');
add_pilot('Gaston', 'Mazzacane', 'MZC', 'ARG');
add_pilot('Jacques', 'Villeneuve', 'VIL', 'CAN');
add_pilot('Ricardo', 'Zonta', 'ZON', 'BRA');
add_pilot('Juan Pablo', 'Montoya', 'MON', 'COL');
add_pilot('Oliver', 'Panis', 'PAN', 'FRA');
add_pilot('Enrique', 'Bernoldi', 'BER', 'BRA');
add_pilot('Kimi', 'Raikkonen', 'RAI', 'FIN');
add_pilot('Tarso', 'Marques', 'MRQ', 'BRA');
add_pilot('Fernando', 'Alonso', 'ALO', 'SPA');
add_pilot('Luciano', 'Burti', 'BUR', 'BRA');
add_pilot('Tomas', 'Enge', 'ENE', 'CZE');
add_pilot('Marcus', 'Ericsson', 'ERI', 'SWE');
add_pilot('Kamui', 'Kobayashi', 'KOB', 'JAP');
add_pilot('Sergio', 'Perez', 'PER', 'MEX');
add_pilot('Nico', 'Hulkenberg', 'HUL', 'GER');
add_pilot('Roman', 'Grosjean', 'GRO', 'FRA');
add_pilot('Pastor', 'Maldonado', 'MAL', 'VEN');
add_pilot('Max', 'Chilton', 'CHI', 'UK');
add_pilot('Jules', 'Bianchi', 'BIA', 'FRA');
add_pilot('Kevin', 'Magnussen', 'MAG', 'DEN');
add_pilot('Nico', 'Rosberg', 'ROS', 'GER');
add_pilot('Lewis', 'Hamilton', 'HAM', 'UK');
add_pilot('Sebastian', 'Vettel', 'VET', 'GER');
add_pilot('Daniel', 'Ricciardo', 'RIC', 'AUS');
add_pilot('Esteban', 'Gutierrez', 'GUT', 'MEX');
add_pilot('Adrian', 'Sutil', 'SUT', 'GER');
add_pilot('Jean-Eric', 'Vergne', 'VRN', 'FRA');
add_pilot('Daniil', 'Kvyat', 'KVY', 'RUS');
add_pilot('Felipe', 'Massa', 'MAS', 'BRA');
add_pilot('Valtteri', 'Bottas', 'BOT', 'FIN');

#add contracts
add_contract(1, 'HAK','McLaren');
add_contract(1, 'COL','McLaren');
add_contract(1, 'MSC','Ferrari');
add_contract(1, 'BAR','Ferrari');
add_contract(1, 'FRE','Jordan');
add_contract(1, 'TRU','Jordan');
add_contract(1, 'IRV','Jaguar');
add_contract(1, 'HRB','Jaguar');
add_contract(1, 'RSC','Williams');
add_contract(1, 'BUT','Williams');
add_contract(1, 'FIS','Benetton');
add_contract(1, 'WUR','Benetton');
add_contract(1, 'ALE','Peugeot');
add_contract(1, 'HID','Peugeot');
add_contract(1, 'DIN','Sauber');
add_contract(1, 'SAL','Sauber');
add_contract(1, 'DLR','Arrows');
add_contract(1, 'VER','Arrows');
add_contract(1, 'GEN','Minardi');
add_contract(1, 'MZC','Minardi');
add_contract(1, 'VIL','BAR');
add_contract(1, 'ZON','BAR');
add_contract(2, 'HAK','McLaren');
add_contract(2, 'COL','McLaren');
add_contract(2, 'MSC','Ferrari');
add_contract(2, 'BAR','Ferrari');
add_contract(2, 'FRE','Jordan');
add_contract(2, 'TRU','Jordan');
add_contract(2, 'IRV','Jaguar');
add_contract(2, 'DLR','Jaguar');
add_contract(2, 'RSC','Williams');
add_contract(2, 'MON','Williams');
add_contract(2, 'FIS','Benetton');
add_contract(2, 'BUT','Benetton');
add_contract(2, 'HID','Sauber');
add_contract(2, 'RAI','Sauber');
add_contract(2, 'BER','Arrows');
add_contract(2, 'VER','Arrows');
add_contract(2, 'ALO','Minardi');
add_contract(2, 'MRQ','Minardi');
add_contract(2, 'PAN','BAR');
add_contract(2, 'VIL','BAR');
add_contract(2, 'ENE','ProstAcer');
add_contract(2, 'ALE','ProstAcer');
add_contract(3, 'ERI','Caterham');
add_contract(3, 'KOB','Caterham');
add_contract(3, 'RAI','Ferrari');
add_contract(3, 'ALO','Ferrari');
add_contract(3, 'PER','Force India');
add_contract(3, 'HUL','Force India');
add_contract(3, 'GRO','Lotus');
add_contract(3, 'MAL','Lotus');
add_contract(3, 'CHI','Marussia');
add_contract(3, 'BIA','Marussia');
add_contract(3, 'MAG','McLaren');
add_contract(3, 'BUT','McLaren');
add_contract(3, 'ROS','Mercedes');
add_contract(3, 'HAM','Mercedes');
add_contract(3, 'VET','Red Bull');
add_contract(3, 'RIC','Red Bull');
add_contract(3, 'GUT','Sauber');
add_contract(3, 'SUT','Sauber');
add_contract(3, 'VRN','Toro Rosso');
add_contract(3, 'KVY','Toro Rosso');
add_contract(3, 'MAS','Williams');
add_contract(3, 'BOT','Williams');

#add powerlevel
add_powerlvl(3, 'ERI',3,4);
add_powerlvl(3, 'KOB',3,5);
add_powerlvl(3, 'RAI',7,9);
add_powerlvl(3, 'ALO',7,10);
add_powerlvl(3, 'PER',6,7);
add_powerlvl(3, 'HUL',6,8);
add_powerlvl(3, 'GRO',5,7);
add_powerlvl(3, 'MAL',5,6);
add_powerlvl(3, 'CHI',4,6);
add_powerlvl(3, 'BIA',4,7);
add_powerlvl(3, 'MAG',8,7);
add_powerlvl(3, 'BUT',8,8);
add_powerlvl(3, 'ROS',9, 9);
add_powerlvl(3, 'HAM',9,10);
add_powerlvl(3, 'VET',8,10);
add_powerlvl(3, 'RIC',8,8);
add_powerlvl(3, 'GUT',7,6);
add_powerlvl(3, 'SUT',7,7);
add_powerlvl(3, 'VRN',6,8);
add_powerlvl(3, 'KVY',6,7);
add_powerlvl(3, 'MAS',8,8);
add_powerlvl(3, 'BOT',8,7);
