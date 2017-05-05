from sys import argv

# Exercise 15: Reading and Reading from File
script, filename = argv

# NOTE: w option for writes
txt_file = open(filename)

print "The file named {} contains:".format(filename)
print txt_file.read()
