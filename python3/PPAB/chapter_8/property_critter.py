# Property Critter
# Demonstrates Properties

class Critter(object):
	"""A virtual pet"""
	def __init__(self, name):
		print("A new critter has been born!")
		self.__name = name
	
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new_name):
		if new_name == "":
			print("A critter's name can't be the empty string.")
		else:
			self.__name = new_name
			print("Name change successful.")

	def talk(self):
		print("\nHello, I'm", self.name)

# main
crit = Critter("Jack")
crit.talk

print("\nMy critter's name is:", end= " ")
print(crit.name)

print("Attempting to change my critter's name to Dougall...")
crit.name = "Dougall"

print("My critter's name is:", end= " ")
print(crit.name)

print("\nAttempting to change the critter's name to the empty string...")
crit.name = ""

print("My critter's name is:", end= " ")
print(crit.name)

input("\nPress the enter key to exit.")
