# can we make a private variable???
# there are no truly private variables
# using _ before a variable, it tells us that we shouldn't change it
class PlayerCharacter():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def _shout(self):
        print (f'my name is {self._name} and I am {self._age} years old.')
        
player1 = PlayerCharacter('Christy', 32)
# when we call a specific method, we are seeing abstraction at work
# python gives us only the method, and not all of the information related to the player
print(player1.run())
print(player1._shout())

# our methods and attributes can be easily overwritten by default! Oh nooooooo!
# good thing we used the underscore! This means 'please don't alter this'

player1.shout = 'BOOOOOOO! HISS!'
print(player1.shout)
print(player1._shout())