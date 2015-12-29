# Attribute Critter
# Demonstrates creating and accessing object attributes

class Critter(object):
	"""A virtual pet"""
	def __init__(self,name,age):
		print("A new critter has been born!")
		self.name = name
		self.age = age

	def __str__(self):
		rep = "Critter object\n"
		rep += "name: " + self.name + "\n" + "age: " + str(self.age) + "\n"
		return rep

	def talk(self):
		print("\nHi. I'm", self.name, "\n")
		print("\nI'm", self.age, "years old\n")

# main
crit1 = Critter("Ted", 8)
crit1.talk()

crit2 = Critter("Dougall", 11)
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Printing crit2:")
print(crit2)

print("Directly accessing crit1.name and crit1.age:")
print(crit1.name, crit1.age)

print("Directly accessing crit2.name and crit2.age:")
print(crit2.name, crit2.age)

input("\n\nPress the enter key to exit.")
