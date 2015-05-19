#!/usr/bin/python 
import sys
sys.path.append('redis_scripts')
import db_delete as db_del
import db_add as db_add
import db_init as db_init
import db_generate as db_gen
import db_seasonTeam as db_seas_team
import db_seasonStat as db_seas_stat
import db_seasonPlayer as db_seas_player

def print_help():
	print('{init|help|gen}')
	print('season {player|stat|team} value')
	print('{add|del} object param1 param2 ...')
	print('add season datebegin dateend count')
	print('add rule season place points')
	print('add country fullname shortname')
	print('add track name country laps')
	print('add race season track')
	print('add team name country')
	print('add pilot name surname shortname country')
	print('add contract season pilot team')
	print('add powerlvl season pilot car skill') 
	print('del season SeasonId')
	print('del rule SeasonId place')
	print('del country shortname')
	print('del track name')
	print('del race season track')
	print('del team name')
	print('del pilot shortname')
	print('del contract season pilot')
	print('del powerlvl season pilot') 


base = 3
errormsg = "unknown command format. use do help"

if len(sys.argv) == base-1:
	if sys.argv[1] == "help" :
		print_help()
	elif sys.argv[1] == "init" :
		db_init.init()
	elif sys.argv[1] == "gen" :
		db_gen.start_generate()
	else:
		print(errormsg)
elif len(sys.argv) == base + 1:
	if sys.argv[1] == "del" :
		if sys.argv[2] == "season" :
			db_del.delete_season(sys.argv[3])
		elif sys.argv[2] == "country" :
			db_del.delete_country(sys.argv[3])
		elif sys.argv[2] == "track" :
			db_del.delete_track(sys.argv[3])
		elif sys.argv[2] == "team" :
			db_del.delete_team(sys.argv[3])
		elif sys.argv[2] == "pilot" :
			db_del.delete_pilot(sys.argv[3])
		else:
			print(errormsg)
	elif sys.argv[1] == "season" :
		if sys.argv[2] == "player" :
			db_seas_player.seasonPlayer(sys.argv[3])
		elif sys.argv[2] == "stat" :
			db_seas_stat.seasonStat(sys.argv[3])
		elif sys.argv[2] == "team" :
			db_seas_team.seasonTeam(sys.argv[3])
		else:
			print(errormsg)
			
	
	else: 
		print(errormsg)
		
elif len(sys.argv) == base + 2:
	if sys.argv[1] == "del" :
		if sys.argv[2] == "rule" :
			db_del.delete_rules(sys.argv[3], sys.argv[4])
		elif sys.argv[2] == "race" :
			db_del.delete_race(sys.argv[3], sys.argv[4])
		elif sys.argv[2] == "contract" :
			db_del.delete_contract(sys.argv[3], sys.argv[4])
		elif sys.argv[2] == "powerlvl" :
			db_del.delete_powerlvl(sys.argv[3], sys.argv[4])
		else:
			print(errormsg)
		
	elif sys.argv[1] == "add" :
		if sys.argv[2] == "country" :
			db_add.add_country(sys.argv[3], sys.argv[4])
		elif sys.argv[2] == "race" :
			db_add.add_race(sys.argv[3], sys.argv[4])
		elif sys.argv[2] == "team" :
			db_add.add_team(sys.argv[3], sys.argv[4])
		else:
			print(errormsg)
	else:
		print(errormsg)
		
elif len(sys.argv) == base + 3:
	if sys.argv[1] == "add" :
		if sys.argv[2] == "season" :
			db_add.add_season(sys.argv[3], sys.argv[4], sys.argv[5])
		elif sys.argv[2] == "rule" :
			db_add.add_rules(sys.argv[3], sys.argv[4], sys.argv[5])
		elif sys.argv[2] == "track" :
			db_add.add_track(sys.argv[3], sys.argv[4], sys.argv[5])
		elif sys.argv[2] == "contract" :
			db_add.add_contract(sys.argv[3], sys.argv[4], sys.argv[5])
		else:
			print(errormsg)
	else: 
		print(errormsg)
		
elif len(sys.argv) == base + 4:
	if sys.argv[1] == "add" :
		if sys.argv[2] == "pilot" :
			db_add.add_pilot(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
		elif sys.argv[2] == "powerlvl" :
			db_add.add_powerlvl(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
		else:
			print(errormsg)
	else: 
		print(errormsg)
		
else:
	print(errormsg)