from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_line(line_count, f):
    print "Line number:", line_count, "; Contents:", f.readline()

current_file = open(input_file)

print "Printing all contents: \n"
print_all(current_file)

print "Rewind file: \n"
rewind(current_file)

print "Print 3 lines: \n"
line_number = 1
print_line(line_number, current_file)

line_number += 1
print_line(line_number, current_file)

line_number += 1
print_line(line_number, current_file)
