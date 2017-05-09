nums = [1,2,3,4,5]
words = ['foo', 'bar', 'zoo', 'zaz', 'stinkle', 'dinkle']
mixed = [11, 'snozberries', 13, 'oompa', 15, 'loompa']

for num in nums:
    print num

for word in words:
    print word

for item in mixed:
    print item

els = []

# NOTE: there is no push()
for i in range(0,6):
    print i
    els.append(i)

print els

# NOTE: python also allows for ranges of indices
# prints els[1 ... -1]
print els[1:]
# prints els[2 ... -2]
print els[2:-2]
# NOTE: there are no shift or unshift methods so use these instead
# makeshift shift
els = els[1:]
print els
# makeshift unshift
els = [0] + els
print els
# If you need to grab the first element from a "shift", use pop and feed i 0
first = els.pop(0)
print first, els
