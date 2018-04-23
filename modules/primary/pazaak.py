from modules.tertiary.opponents import choose_opponent, opponent_list
from modules.tertiary.options import change_speed, rules, debug, run_amount, data_switch
from modules.secondary.checks import replay_check
from modules.primary.sections import loop
from data.data_tools import data_build, data_export



class Pazaak(object):
	def __init__(self):
		self.p = {'type':'computer', 'name':'T3M4', 'phrase': opponent_list[4]['phrase'],'record':{'win':0, 'loss':0},'gs':0,'rs':0,'deck':[],'hand':[-3,-1,1,2], 'state':'none', 'main': 'yes', 'paradigm': 'new'}
		self.c = {'type':'computer', 'name':opponent_list[4]['name'],'phrase': opponent_list[4]['phrase'],'gs':0,'rs':0,'deck':[],'hand':[-3,-1,1,2], 'state':'none', 'main': 'no', 'paradigm': 'old'}
		self.data = {'date': None, 'time': None, 'game_count':0, 'run count':0, 'win':{'p1':0, 'p2':0}, 'stay':{'p1':{}, 'p2':{}}, 'play':{'p1':{}, 'p2':{}}}
		self.options = {'speed':0, 'debug':True, 'data': True}
	#
	def game(self):
		while True:
			choice = input("\nWhat would you like to do? Enter one of the following:\n Play a game: 'game'\n Change opponent, enable multiplayer, or run a Comp v. Comp game: 'players'\n Change the speed: 'speed'\n Debug Mode: 'debug'\n Read the Rules: 'rules'\n Turn Big Data on/ off: 'data'\n Exit Game: 'exit'\n")
			if choice == 'game':
				for n in range(run_amount(self.p, self.c)):
					self.data['game_count'] += 1
					self.p, self.c, self.data = loop(self.p, self.c, self.data, self.options)
					
					if self.options['data'] == True: 
						data_export(data_build(self.p, self.c, self.data))
						print("\nGame Count: {}\n\n".format(self.data['game_count']))
					
				if self.p['type'] == 'human':
					if replay_check() == 'Y': loop(self.p, self.c, self.data, self.options) #allows player to choose to play again
					else: break
					
			elif choice == 'players':	self.p, self.c = choose_opponent(self.p, self.c)
			elif choice == 'speed':	self.options['speed'] = change_speed(self.options)
			elif choice == 'rules': rules()
			elif choice == 'debug': self.options['debug'] = debug(self.options)
			elif choice == 'data': self.options['data'] = data_switch()
			elif choice == 'exit': exit()
			else: print("Sorry, I didn't get that.")