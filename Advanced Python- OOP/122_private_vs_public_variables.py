class PlayerCharacter():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def shout(self):
        print (f'my name is {self.name} and I am {self.age} years old.')
        
player1 = PlayerCharacter('Christy', 32)
# when we call a specific method, we are seeing abstraction at work
# python gives us only the method, and not all of the information related to the player
print(player1.run())
print(player1.shout())

# our methods and attributes can be easily overwritten by default! Oh nooooooo!
player1.speak = 'BOOOOOOO! HISS!'
print(player1.speak)