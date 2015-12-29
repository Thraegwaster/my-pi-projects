# Attribute Critter
# Demonstrates creating and accessing object attributes

class Critter(object):
	"""A virtual pet"""
	total = 0

	@staticmethod
	def status():
		print("\nThe total number of critters is", Critter.total)

	def __init__(self,name,age):
		print("A new critter has been born!")
		self.name = name
		self.age = age
		Critter.total += 1

	def __str__(self):
		rep = "Critter object\n"
		rep += "name: " + self.name + "\n" + "age: " + str(self.age) + "\n"
		return rep

	def talk(self):
		print("\nHi. I'm", self.name)
		print("\nI'm", self.age, "years old\n")

# main


crit1 = Critter("Ted", 8)
crit1.talk()

crit2 = Critter("Dougall", 11)
crit2.talk()

crit3 = Critter("Jack", 12)
crit3.talk()

print("The total number of critters is", Critter.total)

Critter.status

print("\nAccessing the class attribute through an object:", end= " ")
print(crit1.total)

input("\n\nPress the enter key to exit.")
