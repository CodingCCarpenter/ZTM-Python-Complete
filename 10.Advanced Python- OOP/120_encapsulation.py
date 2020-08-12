# 4 pillars of OOP

# Encapsulation is the binding of data and functions that manipulate that data.
# we encapsulate into one big object so that we keep everything together under
# the same object using attributes and methods

class PlayerCharacter():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def shout(self):
        print (f'my name is {self.name} and I am {self.age} years old.')
        
player1 = PlayerCharacter('Christy', 32)
print(player1.run())
print(player1.shout())