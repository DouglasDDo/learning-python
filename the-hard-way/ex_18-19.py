
def print_two(*args):
    arg1, arg2 = args
    print "First: %r, second: %r" % (arg1, arg2)

def print_explicit(arg1, arg2):
    print "First: %r, second: %r" % (arg1, arg2)

def no_args():
    print "Hi"

# NOTE: Unless you unpack as many args as are provided, you'll get an error
# The commented out version below will produce this error.
# print_two("words", "more words", "even more words")
print_two("words", "more words")

print_explicit("hello", "hi there")

no_args()

def passing_args(arg1, arg2):
    print "%d plus %d is equal to %d" % (arg1, arg2, (arg1 + arg2))

# harcoded
passing_args(10,20)
# math ops in args
passing_args(5+5, 10+10)
# with vars
var1, var2 = 10, 20
passing_args(var1, var2)
# mixed hardcoded and vars
passing_args(var1, 10+10)
