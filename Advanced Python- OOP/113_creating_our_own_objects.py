# Creating our own objects with OOP

class PlayerCharacter:
    # built in dunder method that acts as constructor - params other than 'self' will be required
    def __init__(self, name):
        self.name = name

    # custom method that we created
    def run(self):
        print('run')

player1 = PlayerCharacter('Cindy')

"""
self acts a lot like 'this' in JavaScript. It makes 
the parameters other than 'self' required, and it 
allows the function to refer to its own data. 
"""