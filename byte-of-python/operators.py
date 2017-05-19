foo_string = '{0} are some {1}'
these = 'these'
words = 'words'

# NOTE: Format method only works within print; you can't format before hand
#   foo_string.format(these, words); printing foo_string alone won't work
print(foo_string.format(these, words))

# Division of ints can still produce a float
print(5/2)
# NOTE: All the other operators are available as you'd expect; the one
# that sticks out is the double slash for dividing and rounding down
print(5 // 2)
