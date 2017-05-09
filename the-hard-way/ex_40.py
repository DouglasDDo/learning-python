class Song(object):
    """docstring for Song."""
    def __init__(self, lyrics):
        # super(Song, self).__init__()
        self.lyrics = lyrics

    def play(self):
        print self.lyrics

    def print_stuff(self, foo):
        print foo


foobar = Song('words, words, more words')
foobar.play()
foobar.print_stuff('something')

class Animal(object):
    """docstring for Animal."""
    def __init__(self, name, species):
        super(Animal, self).__init__()
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

class Dog(Animal):
    """ docstring for Dog. """
    def __init__(self, name, sound):
        Animal.__init__(self, name, "Dog")
        self.sound = sound

    def bark(self):
        return self.sound

fido = Dog('Fido', 'Woof')
print fido.getName()
print fido.getSpecies()
print isinstance(fido, Animal)
print isinstance(fido, Dog)
print fido.bark()
