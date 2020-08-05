# Creating our own objects with OOP

class PlayerCharacter:
    # built in dunder method that acts as constructor - params other than 'self' will be required
    def __init__(self, name, role):
        self.name = name
        self.role = role

    # custom method that we created
    def battle_cry(self):
        print('YAAAAAAAAAAARG!!!!')

# creating a first player
player1 = PlayerCharacter('Bacchus', 'Viking ')

"""
self acts a lot like 'this' in JavaScript. It makes 
the parameters other than 'self' required, and it 
allows the function to refer to its own data. 
"""

# adding a second player (instance of PlayerCharacter)
player2 = PlayerCharacter('Krystyne', 'Elf')

# invoke player1's battle_cry
player1.battle_cry()

# print player2's name
print(player2.name)

# invoke player2's battle_cry
player2.battle_cry()

# print player1's role
print(player1.role)

# add a new player, Tim, who has the role 'human'
player3 = PlayerCharacter('Tim', 'human')