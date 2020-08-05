class PlayerCharacter:
    # built in dunder method that acts as constructor - params other than 'self' will be required
    def __init__(self, name, role, attack):
        self.name = name
        self.role = role
        self.attack = attack

    # custom method that we created
    def battle_cry(self):
        print('YAAAAAAAAAAARG!!!!')
        return 'done'


# creating a first player (instance of PlayerCharacter)
player1 = PlayerCharacter('Bacchus', 'Viking', 50)

# adding a second player (instance of PlayerCharacter)
player2 = PlayerCharacter('Krystyne', 'Elf', 43)

# initializing a 3rd player
player3 = PlayerCharacter('Tim', 'human', 7)


