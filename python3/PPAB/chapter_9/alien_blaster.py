# Alien Blaster
# Demonstrates object interaction

class Player(object):
	"""A player in a shooter game"""
	def blast(self, enemy):
		print("The player blasts an enemy.\n")
		enemy.die()

class Alien(object):
	"""An alien in a shooter game"""
	def die(self):
		print("The alien gasps and says 'Oh, this is it.\nGood-bye, cruel universe.'")

# main

print("\t\tDeath of an alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter key to exit.")
