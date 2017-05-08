def add(a, b):
    print "Adding %d and %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d from %d" % (b, a)
    return a - b

def multiply(a, b):
    print "Multiplying %d by %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d by %d" % (a, b)
    return a / b

def mod(a, b):
    print "Modding %d by %d" % (a, b)
    return a % b

print add(1,2)
print subtract(5,3)
print multiply(2,3)
print divide(10,5)
print mod(13,5)
