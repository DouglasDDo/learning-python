from sys import argv

# Exercise 15: Reading and Reading from File
script, filename = argv

# NOTE: w option for writes
txt_file = open(filename,'w')

# Exercise 16: Deleting and Writing to File
print "{} will be deleted now.".format(filename)
# NOTE: empties the file contents
txt_file.truncate()

print "Write some lines in:"
new_line1 = raw_input("new line 1: ")
new_line2 = raw_input("new line 2: ")
new_line3 = raw_input("new line 3: ")

lines = [new_line1, new_line2, new_line3]

for new_line in lines:
    txt_file.write(new_line)
    txt_file.write("\n")

print "Closing file"
# NOTE: close() is required to 'save'
txt_file.close()
