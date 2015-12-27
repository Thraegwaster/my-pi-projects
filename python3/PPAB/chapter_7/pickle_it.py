# Pickle It
# Demonstrates pickling and shelving data

import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

f = open("pickles1.dat", "wb") # Pickled objects must be stored in a binary file.

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close

# Retrieving and unpickling

print("\nUnpickling lists.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close

# Using a shelf to store pickled data

print("\nShelving lists.")
s = shelve.open("pickles2.dat")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]

s.sync # make sure the data is written

# Shelves can be accessed randomly. Here's the proof...

print("\nRetrieving lists from shelved file:")
print("brand -", s["brand"])
print("variety -", s["variety"])
print("shape -", s["shape"])

s.close

input("\n\nPress the enter key to exit.")
