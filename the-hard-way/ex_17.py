from sys import argv
from os.path import dirname, exists, join

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

# NOTE: leaving these commented out but this is how you can navigate around dirs from
# the current dir.
# current_dir = dirname(__file__)
# source_data = open(join(current_dir, from_file)).read()
source = open(from_file)
source_data = source.read()

print "The data from the source file is %d bytes long." % len(source_data)

print "Use exists() to check whether a file exists. Result: %r" % exists(to_file)

dest = open(to_file, 'w')
dest.write(source_data)

# Close the files once writing is complete
source.close()
dest.close()
