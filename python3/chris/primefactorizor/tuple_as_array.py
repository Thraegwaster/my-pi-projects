# tuple_as_array.py
# Tests the use of a tuple as a two dimensional array

primelist = []

for i in range(0,6):
	factor = int(input("Enter your number\n"))
	index = int(input("Enter the index\n"))
	entry = (factor, index)
	primelist.append(entry)

for j in range(0,6):
	print(primelist[j][0], ",", primelist[j][1])
