# Exercise 1: Obligatory Hello World
# NOTE: in Python 3 print is a fn and requires parentheses
print "Hello world"

# Exercise 2: Comments
# This is a comment...

# Exercise 3: Math & Comparison Operators
print 2 + 2
print 10 % 9
print 1 < 2
print 2 == 2
print 2 != 3

# Exercise 4: Basic Vars
foo = 4
bar = foo * 2
name = "Homer Simpson"
print foo
print name, "has", foo, "fingers on each hand."
print "He has", bar, "fingers total."

# Exercise 5: Formatted String Interpolation
zoo = "words"
zaz = 42
print "Here are some %s." % zoo
print "And %d is a number" % zaz

thing1 = "a thing"
thing2 = "another thing"
thing3 = "a third thing"

# NOTE: %r is for raw data output; use it for debugging
print "Use parentheses if you need to fprint %r, %s, %s, and beyond." % (thing1, thing2, thing3)

# Exercise 6: More of the Same
some_string = "This is a %s"
obviously = "string..."

print some_string % obviously

# Exercise 7: More Printing
print "." * 10
# NOTE: ending comma will print a space and then continue printing on same line
print "hello" + name,
print zoo + thing1

# Exercise 8 - 9: Even More Printing (new line with escape, \n)
# Skipped

# Exercise 10: Tabs
print "\tThis is tabbed."
print "\t\tThis is double tabbed."
