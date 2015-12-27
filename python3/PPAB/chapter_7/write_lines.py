# Write_lines
# Demonstrates creating a text file with the writelines() method.

print("\nCreating a text file with the writelines() method.")
text_file = open("write_lines.txt", "w")
lines = ["line 1\n",
	"This is line 2\n"
	"That makes this one line 3!\n"]

text_file.writelines(lines)
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_lines.txt", "r")
print(text_file.read())
text_file.close()

input("\n\nPress the enter key to exit.")
