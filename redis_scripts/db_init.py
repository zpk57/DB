#!/usr/bin/python 

import redis
from datetime import date
import db_add as db_add

def init():
	db = redis.Redis('localhost')
	db.flushall()
	db.set('season:count', 0)
	db.set('track:count', 0)
	db.set('race:count', 0)
	db.set('team:count', 0)

	#adding seasons
	db_add.add_season(date(2000, 3, 4), date(2000, 10, 14), 22)
	db_add.add_season(date(2001, 3, 12), date(2001, 10, 22), 22)
	db_add.add_season(date(2014, 3, 16), date(2014, 11, 23), 22)

	#adding rules
	db_add.add_rules(1,1,10)
	db_add.add_rules(1,2,6)
	db_add.add_rules(1,3,4)
	db_add.add_rules(1,4,3)
	db_add.add_rules(1,5,2)
	db_add.add_rules(1,6,1)

	db_add.add_rules(2,1,10)
	db_add.add_rules(2,2,6)
	db_add.add_rules(2,3,4)
	db_add.add_rules(2,5,2)
	db_add.add_rules(2,6,1)

	db_add.add_rules(3,1,25)
	db_add.add_rules(3,2,18)
	db_add.add_rules(3,3,15)
	db_add.add_rules(3,4,12)
	db_add.add_rules(3,5,10)
	db_add.add_rules(3,6,8)
	db_add.add_rules(3,7,6)
	db_add.add_rules(3,8,4)
	db_add.add_rules(3,9,2)
	db_add.add_rules(3,10,1)

	#adding countries
	db_add.add_country('United Kingdom', 'UK');
	db_add.add_country('Italia', 'ITA');
	db_add.add_country('Irlandia', 'IRL');
	db_add.add_country('France', 'FRA');
	db_add.add_country('Switzerland', 'SUI');
	db_add.add_country('Finland', 'FIN');
	db_add.add_country('Germany', 'GER');
	db_add.add_country('Brazil', 'BRA');
	db_add.add_country('Austria', 'AUT');
	db_add.add_country('Spain', 'SPA');
	db_add.add_country('Argentina', 'ARG');
	db_add.add_country('Netherlands', 'NED');
	db_add.add_country('Canada', 'CAN');
	db_add.add_country('Australia', 'AUS');
	db_add.add_country('Monaco', 'MON');
	db_add.add_country('Hungary', 'HUN');
	db_add.add_country('Belgium', 'BEL');
	db_add.add_country('United States of America', 'USA');
	db_add.add_country('Japan', 'JAP');
	db_add.add_country('Malaysia', 'MAL');
	db_add.add_country('Colombia', 'COL');
	db_add.add_country('Czech Republic', 'CZE');
	db_add.add_country('India', 'IND');
	db_add.add_country('Russian Federation', 'RUS');
	db_add.add_country('Sweden', 'SWE');	 
	db_add.add_country('Mexico', 'MEX');
	db_add.add_country('Venezuela', 'VEN');
	db_add.add_country('Denmark', 'DEN');
	db_add.add_country('Bahrain', 'BAH');
	db_add.add_country('China', 'CHI');
	db_add.add_country('Singapore', 'SIN');
	db_add.add_country('United Arab Emirates', 'UAE');

	#adding tracks
	db_add.add_track('Melbourne', 'AUS', 58);
	db_add.add_track('San Paolo', 'BRA', 71);
	db_add.add_track('Imola', 'ITA', 62);
	db_add.add_track('Silverstone', 'UK', 52);
	db_add.add_track('Cataluniya', 'SPA', 66);
	db_add.add_track('Nurburgring', 'GER', 56);
	db_add.add_track('Monte-Carlo', 'MON', 78);
	db_add.add_track('Magny-Cours', 'BRA', 70);
	db_add.add_track('A1-Ring', 'AUT', 71);
	db_add.add_track('Hungaroling', 'HUN', 70);
	db_add.add_track('Hockenheimring', 'GER', 67);
	db_add.add_track('Spa-Francorchamps', 'BEL', 44);
	db_add.add_track('Monza', 'ITA', 53);
	db_add.add_track('Indianapolis', 'USA', 56);
	db_add.add_track('Suzuka', 'JAP', 53);
	db_add.add_track('Sepang', 'MAL', 56);
	db_add.add_track('Montreal', 'CAN', 70);
	db_add.add_track('Sakhir', 'BAH', 57);
	db_add.add_track('Shanghai', 'CHI', 56);
	db_add.add_track('Marina Bay', 'SIN', 61);
	db_add.add_track('Sochi Autodrom', 'RUS', 53);
	db_add.add_track('Austin', 'USA', 56);
	db_add.add_track('Yas Marina', 'UAE', 55);

	#adding races
	db_add.add_race(1,1);
	db_add.add_race(1,2);
	db_add.add_race(1,3);
	db_add.add_race(1,4);
	db_add.add_race(1,5);
	db_add.add_race(1,6);
	db_add.add_race(1,7);
	db_add.add_race(1,8);
	db_add.add_race(1,9);
	db_add.add_race(1,10);
	db_add.add_race(1,11);
	db_add.add_race(1,12);
	db_add.add_race(1,13);
	db_add.add_race(1,14);
	db_add.add_race(1,15);
	db_add.add_race(1,16);
	db_add.add_race(1,17);
	db_add.add_race(2,1);
	db_add.add_race(2,2);
	db_add.add_race(2,3);
	db_add.add_race(2,4);
	db_add.add_race(2,5);
	db_add.add_race(2,6);
	db_add.add_race(2,7);
	db_add.add_race(2,8);
	db_add.add_race(2,9);
	db_add.add_race(2,10);
	db_add.add_race(2,11);
	db_add.add_race(2,12);
	db_add.add_race(2,13);
	db_add.add_race(2,14);
	db_add.add_race(2,15);
	db_add.add_race(2,16);
	db_add.add_race(2,17);
	db_add.add_race(3,1);
	db_add.add_race(3,16);
	db_add.add_race(3,18);
	db_add.add_race(3,19);
	db_add.add_race(3,5);
	db_add.add_race(3,7);
	db_add.add_race(3,17);
	db_add.add_race(3,9);
	db_add.add_race(3,4);
	db_add.add_race(3,11);
	db_add.add_race(3,10);
	db_add.add_race(3,12);
	db_add.add_race(3,13);
	db_add.add_race(3,20);
	db_add.add_race(3,15);
	db_add.add_race(3,21);
	db_add.add_race(3,22);
	db_add.add_race(3,2);
	db_add.add_race(3,23);

	#adding teams
	db_add.add_team('McLaren', 'UK');
	db_add.add_team('Ferrari', 'ITA');
	db_add.add_team('Jordan', 'IRL');
	db_add.add_team('Jaguar', 'UK');
	db_add.add_team('Williams', 'UK');
	db_add.add_team('Benetton', 'ITA');
	db_add.add_team('Peugeot', 'FRA');
	db_add.add_team('Sauber', 'SUI');
	db_add.add_team('Arrows', 'UK');
	db_add.add_team('Minardi', 'ITA');
	db_add.add_team('BAR', 'UK');
	db_add.add_team('ProstAcer', 'FRA')
	db_add.add_team('Caterham', 'MAL');
	db_add.add_team('Force India', 'IND');
	db_add.add_team('Lotus', 'UK');
	db_add.add_team('Marussia', 'RUS');
	db_add.add_team('Mercedes', 'GER');
	db_add.add_team('Red Bull', 'AUT');
	db_add.add_team('Toro Rosso', 'ITA');

	#adding pilots
	db_add.add_pilot('Mika', 'Hakkinen', 'HAK', 'FIN');
	db_add.add_pilot('David', 'Coulthard', 'COL', 'UK');
	db_add.add_pilot('Michael', 'Schumacher', 'MSC', 'GER');
	db_add.add_pilot('Rubens', 'Barrichello', 'BAR', 'BRA');
	db_add.add_pilot('Heinz', 'Frentzen', 'FRE', 'GER');
	db_add.add_pilot('Jarno', 'Trulli', 'TRU', 'ITA');
	db_add.add_pilot('Eddie', 'Irvine', 'IRV', 'UK');
	db_add.add_pilot('Johnny', 'Herbert', 'HRB', 'GER');
	db_add.add_pilot('Ralf', 'Schumacher', 'RSC', 'GER');
	db_add.add_pilot('Jenson', 'Button', 'BUT', 'UK');
	db_add.add_pilot('Giancarlo', 'Fisichella', 'FIS', 'ITA');
	db_add.add_pilot('Alexander', 'Wurz', 'WUR', 'AUT');
	db_add.add_pilot('Jean', 'Alesi', 'ALE', 'FRA');
	db_add.add_pilot('Nick', 'Heidfeld', 'HID', 'GER');
	db_add.add_pilot('Pedro', 'Diniz', 'DIN', 'BRA');
	db_add.add_pilot('Mika', 'Salo', 'SAL', 'FIN');
	db_add.add_pilot('Pedro', 'de la Rosa', 'DLR', 'SPA');
	db_add.add_pilot('Jos', 'Verstappen', 'VER', 'NED');
	db_add.add_pilot('Marc', 'Gene', 'GEN', 'SPA');
	db_add.add_pilot('Gaston', 'Mazzacane', 'MZC', 'ARG');
	db_add.add_pilot('Jacques', 'Villeneuve', 'VIL', 'CAN');
	db_add.add_pilot('Ricardo', 'Zonta', 'ZON', 'BRA');
	db_add.add_pilot('Juan Pablo', 'Montoya', 'MON', 'COL');
	db_add.add_pilot('Oliver', 'Panis', 'PAN', 'FRA');
	db_add.add_pilot('Enrique', 'Bernoldi', 'BER', 'BRA');
	db_add.add_pilot('Kimi', 'Raikkonen', 'RAI', 'FIN');
	db_add.add_pilot('Tarso', 'Marques', 'MRQ', 'BRA');
	db_add.add_pilot('Fernando', 'Alonso', 'ALO', 'SPA');
	db_add.add_pilot('Luciano', 'Burti', 'BUR', 'BRA');
	db_add.add_pilot('Tomas', 'Enge', 'ENE', 'CZE');
	db_add.add_pilot('Marcus', 'Ericsson', 'ERI', 'SWE');
	db_add.add_pilot('Kamui', 'Kobayashi', 'KOB', 'JAP');
	db_add.add_pilot('Sergio', 'Perez', 'PER', 'MEX');
	db_add.add_pilot('Nico', 'Hulkenberg', 'HUL', 'GER');
	db_add.add_pilot('Roman', 'Grosjean', 'GRO', 'FRA');
	db_add.add_pilot('Pastor', 'Maldonado', 'MAL', 'VEN');
	db_add.add_pilot('Max', 'Chilton', 'CHI', 'UK');
	db_add.add_pilot('Jules', 'Bianchi', 'BIA', 'FRA');
	db_add.add_pilot('Kevin', 'Magnussen', 'MAG', 'DEN');
	db_add.add_pilot('Nico', 'Rosberg', 'ROS', 'GER');
	db_add.add_pilot('Lewis', 'Hamilton', 'HAM', 'UK');
	db_add.add_pilot('Sebastian', 'Vettel', 'VET', 'GER');
	db_add.add_pilot('Daniel', 'Ricciardo', 'RIC', 'AUS');
	db_add.add_pilot('Esteban', 'Gutierrez', 'GUT', 'MEX');
	db_add.add_pilot('Adrian', 'Sutil', 'SUT', 'GER');
	db_add.add_pilot('Jean-Eric', 'Vergne', 'VRN', 'FRA');
	db_add.add_pilot('Daniil', 'Kvyat', 'KVY', 'RUS');
	db_add.add_pilot('Felipe', 'Massa', 'MAS', 'BRA');
	db_add.add_pilot('Valtteri', 'Bottas', 'BOT', 'FIN');

	#add contracts
	db_add.add_contract(1, 'HAK','McLaren');
	db_add.add_contract(1, 'COL','McLaren');
	db_add.add_contract(1, 'MSC','Ferrari');
	db_add.add_contract(1, 'BAR','Ferrari');
	db_add.add_contract(1, 'FRE','Jordan');
	db_add.add_contract(1, 'TRU','Jordan');
	db_add.add_contract(1, 'IRV','Jaguar');
	db_add.add_contract(1, 'HRB','Jaguar');
	db_add.add_contract(1, 'RSC','Williams');
	db_add.add_contract(1, 'BUT','Williams');
	db_add.add_contract(1, 'FIS','Benetton');
	db_add.add_contract(1, 'WUR','Benetton');
	db_add.add_contract(1, 'ALE','Peugeot');
	db_add.add_contract(1, 'HID','Peugeot');
	db_add.add_contract(1, 'DIN','Sauber');
	db_add.add_contract(1, 'SAL','Sauber');
	db_add.add_contract(1, 'DLR','Arrows');
	db_add.add_contract(1, 'VER','Arrows');
	db_add.add_contract(1, 'GEN','Minardi');
	db_add.add_contract(1, 'MZC','Minardi');
	db_add.add_contract(1, 'VIL','BAR');
	db_add.add_contract(1, 'ZON','BAR');
	db_add.add_contract(2, 'HAK','McLaren');
	db_add.add_contract(2, 'COL','McLaren');
	db_add.add_contract(2, 'MSC','Ferrari');
	db_add.add_contract(2, 'BAR','Ferrari');
	db_add.add_contract(2, 'FRE','Jordan');
	db_add.add_contract(2, 'TRU','Jordan');
	db_add.add_contract(2, 'IRV','Jaguar');
	db_add.add_contract(2, 'DLR','Jaguar');
	db_add.add_contract(2, 'RSC','Williams');
	db_add.add_contract(2, 'MON','Williams');
	db_add.add_contract(2, 'FIS','Benetton');
	db_add.add_contract(2, 'BUT','Benetton');
	db_add.add_contract(2, 'HID','Sauber');
	db_add.add_contract(2, 'RAI','Sauber');
	db_add.add_contract(2, 'BER','Arrows');
	db_add.add_contract(2, 'VER','Arrows');
	db_add.add_contract(2, 'ALO','Minardi');
	db_add.add_contract(2, 'MRQ','Minardi');
	db_add.add_contract(2, 'PAN','BAR');
	db_add.add_contract(2, 'VIL','BAR');
	db_add.add_contract(2, 'ENE','ProstAcer');
	db_add.add_contract(2, 'ALE','ProstAcer');
	db_add.add_contract(3, 'ERI','Caterham');
	db_add.add_contract(3, 'KOB','Caterham');
	db_add.add_contract(3, 'RAI','Ferrari');
	db_add.add_contract(3, 'ALO','Ferrari');
	db_add.add_contract(3, 'PER','Force India');
	db_add.add_contract(3, 'HUL','Force India');
	db_add.add_contract(3, 'GRO','Lotus');
	db_add.add_contract(3, 'MAL','Lotus');
	db_add.add_contract(3, 'CHI','Marussia');
	db_add.add_contract(3, 'BIA','Marussia');
	db_add.add_contract(3, 'MAG','McLaren');
	db_add.add_contract(3, 'BUT','McLaren');
	db_add.add_contract(3, 'ROS','Mercedes');
	db_add.add_contract(3, 'HAM','Mercedes');
	db_add.add_contract(3, 'VET','Red Bull');
	db_add.add_contract(3, 'RIC','Red Bull');
	db_add.add_contract(3, 'GUT','Sauber');
	db_add.add_contract(3, 'SUT','Sauber');
	db_add.add_contract(3, 'VRN','Toro Rosso');
	db_add.add_contract(3, 'KVY','Toro Rosso');
	db_add.add_contract(3, 'MAS','Williams');
	db_add.add_contract(3, 'BOT','Williams');

	#add powerlevel
	db_add.add_powerlvl(3, 'ERI',3,4);
	db_add.add_powerlvl(3, 'KOB',3,5);
	db_add.add_powerlvl(3, 'RAI',7,9);
	db_add.add_powerlvl(3, 'ALO',7,10);
	db_add.add_powerlvl(3, 'PER',6,7);
	db_add.add_powerlvl(3, 'HUL',6,8);
	db_add.add_powerlvl(3, 'GRO',5,7);
	db_add.add_powerlvl(3, 'MAL',5,6);
	db_add.add_powerlvl(3, 'CHI',4,6);
	db_add.add_powerlvl(3, 'BIA',4,7);
	db_add.add_powerlvl(3, 'MAG',8,7);
	db_add.add_powerlvl(3, 'BUT',8,8);
	db_add.add_powerlvl(3, 'ROS',9, 9);
	db_add.add_powerlvl(3, 'HAM',9,10);
	db_add.add_powerlvl(3, 'VET',8,10);
	db_add.add_powerlvl(3, 'RIC',8,8);
	db_add.add_powerlvl(3, 'GUT',7,6);
	db_add.add_powerlvl(3, 'SUT',7,7);
	db_add.add_powerlvl(3, 'VRN',6,8);
	db_add.add_powerlvl(3, 'KVY',6,7);
	db_add.add_powerlvl(3, 'MAS',8,8);
	db_add.add_powerlvl(3, 'BOT',8,7);
