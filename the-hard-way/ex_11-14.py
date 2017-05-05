# Imports: "from <package> import <module>"
from sys import argv

# Exercise 11: Using raw_input()
print "Question?"
answer = raw_input()
# NOTE: the first approach will give a quoted str whereas the second will not
print "The answer is %r" % answer
print "It could also be said as {}".format(answer)

# Exercise 12: Prompting, passing args to raw_input()
prompt = raw_input("This is prompting you to answer:\n")
print "You said", prompt

# Exercise 13: Using argv
# NOTE: By default, the first arg will be script, the script/file name
script, first, second = argv

print "The first thing you typed:", first
print "The second thing you typed:", second

# Exercise 14: More of the Same
# Skipped
