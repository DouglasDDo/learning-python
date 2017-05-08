print "Door 1 or Door 2?"
first_choice = raw_input("<")

if first_choice == 1:
    print "You open the door. There's a giant bear in front of you."
    print "Do you 1. give the bear some cake or 2. punch the bear in the face?"
    print "Make your choice: 1 or 2?"

    bear = raw_input("<")

    if bear == 1:
        print "The bear ate your cake and the hand the cake was in."
    elif bear == 2:
        print "You showed that bear who's boss."
    else:
        print "The bear just ate your mom. Good job."

elif first_choice == 2:
    print "You open the door. You meet Cthulhu's cousin Robert."
    print "You can: 1. give Robert a high five, 2. eat your own head, or 3. listen to Nickelback."

    insanity = raw_input("<")

    if insanity == 1:
        print "Robert is your homie now."
    elif insanity == 2:
        print "Delicious."
    elif insanity == 3:
        print "Something is wrong with you."
    else:
        print "Robert makes you eat your own head while listening to Nickelback."

else:
    print "Nothing happened. How exciting."
