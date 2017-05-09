# ex. 33
i = 1
nums = []
while i < 9:
    if i == 5:
        i += 1
        # NOTE: continue takes the place of next
        continue
    print "Appending:", i
    nums.append(i)

    i += 1

# NOTE: range is non-inclusive
for i in range(0, len(nums)):
    print "Index:", i
    print "Element:", nums[i]

# ex. 38
plain_list = ['boo', 'baz', 'foo', 'bar']
# NOTE: While split operates the way you'd expect, join works as being a method
# on the string to be inserted
print '--INSERTION--'.join(plain_list)

# ex. 39
states = {
    'California': 'CA',
    'Washington': 'WA',
    'New York': 'NY',
    'Illinois': 'IL'
}

cities = {
    'CA': 'Sacramento',
    'WA': 'Olympia',
    'NY': 'Albany',
    'IL': 'Springfield'
}

nested = {
    'first': {
        'words': 'foo',
        'nums': 1
    },
    'second': {
        'words': 'bar',
        'nums': 2
    },
    'third': {
        'words': 'boo',
        'nums': 3
    },
    'frizzle': 'frazzle'
}

print states['California']
print nested['first']
print nested['first']['nums']

# NOTE: you can delete a dict entry with the keyword del
print nested
del nested['frizzle']
print nested

# NOTE: the items() method on dicts will return a list of tuples
for full_name, abbrev in states.items():
    print "The state of %s is abbreviated as %s." % (full_name, abbrev)

# Works with deeper dicts too. Could keep on using with more for loops
for thing1, thing2 in nested.items():
    print thing1, thing2

print "Printing state capitols:"
for full_name in states.keys():
    # NOTE: Just doing this to check out keys() method
    print cities[states[full_name]]

print "Printing state capitols again:"
for abbrev in states.values():
    # NOTE: Just doing this to check out values() method
    print cities[abbrev]

key = 'California'
print states.has_key(key)
print states.get(key, '%s is not a state in the given dict.' % key)
missing_key = 'OH'
print states.has_key(missing_key)
print states.get(missing_key, '%s is not a state in the given dict.' % missing_key)

print len(nested)
print type(states)
