# a class to make Atl United players
class Player(object):
	# EVERY class needs to start with def __init__
	# this function gets run ONCE and only ONCE, when the object is made
	# you pass in args when you make the object
	# self is ALWAYS the first
	# everything else is optional
	def __init__(self, name, daffyDuck, age):
		self.name = name
		self.position = daffyDuck
		self.team = "Atlanta United"
		self.birthyear = 2017 - age
		perfomrance = "Awesome"
		four = 2 + 2
		self.goals_scored = 0

	def trade(self, new_team):
		self.team = new_team
	def change_pos(self, new_position):
		self.old_position = self.position
		self.position = new_position
	def score(self):
		self.goals_scored += 1
	def get_goals(self):
		return self.goals_scored

player1 = Player('Miguel Almiron', 'midfield', 25)
print player1.name
print player1.position
print player1.team

player2 = Player("Brad Guzan", "goalie", 29)
print player2.name
print player2.position
print player2.team

# player1.team = "Orlando"
# print player1.team
# print player2.team
# print player1.perfomrance

player1.trade("Orlando")
print player1.team
print player1.goals_scored
player1.score()
player1.score()
player1.score()
player1.score()
print player1.goals_scored
print player1.get_goals()
# player1.goals_scored += 1
# player1.goals_scored += 1
# player1.goals_scored += 1
# player1.goals_scored += 1
