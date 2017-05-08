# ex. 29
people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats."

if people > cats:
    print "Not too many cats."
else:
    print "Still too many cats."

if people < dogs:
    print "Whole lotta dogs."

if people > dogs:
    print "Gonna need some more dogs."

dogs += 5

if people >= dogs:
    print "At least as many people as there are dogs."

if people <= dogs:
    print "At least as many dogs as there are people."

if people == dogs:
    print "Dog people."

# ex. 30
people = 30
cars = 40
trucks = 15

if cars > people:
    print "More cars than folks."
elif cars < people:
    print "Not enough cars."
else:
    print "Cars and people are equals in quantity."

if trucks > cars:
    print "More trucks."
elif trucks < cars:
    print "More cars."
else:
    print "Same same."

if people > trucks:
    print "Lot of people. More than trucks."
else:
    print "More or as many trucks as people."
