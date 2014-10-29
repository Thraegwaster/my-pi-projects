# Exclusive Network
# Demonstrates logical operators and compound conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!")

security = 0

username = ""
while not username:
	username = input("Username: ")

password = ""
while not password:
	password = input("Password: ")

if username == "C McHarg" and password == "grx1284thx":
	print("Hello, Chris")
	security = 5

elif username == "A McHarg" and password == "Redwine01":
	print("Hello, Amanda")
	security = 3

elif username == "S Meier" and password == "civilization":
	print("Hello Sid")
	security = 2

elif username == "guest" or password == "guest":
	print("Welcome", username, ".")
	security = 1

else:
	print("Login failed. You're not so exclusive.\n")

print("You have security level", security)
input("\n\nPress the enter key to exit")
