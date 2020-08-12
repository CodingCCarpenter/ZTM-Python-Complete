class PlayerCharacter:
    # built in dunder method that acts as constructor - params other than 'self' will be required
    def __init__(self, name, role, attack):
        self.name = name
        self.role = role
        self.attack = attack

    # custom method that we created
    def battle_cry(self):
        print(f'I am {self.name}!!! YAAAAAAAAAAARG!!!!')
        return 'done'

    # this is a class object attribute, which is NOT dynamic
    membership = True


# creating a first player (instance of PlayerCharacter)
player1 = PlayerCharacter('Bacchus', 'Viking', 50)

# adding a second player (instance of PlayerCharacter)
player2 = PlayerCharacter('Krystyne', 'Elf', 43)

# initializing a 3rd player
player3 = PlayerCharacter('Tim', 'human', 7)

# attributes => pieces of data that are dynamic (name, role, attack)
# Class Object Attributes => pieces of data that are NOT dynamic



class PaidPlayer:
    membership = True

    def __init__(self, name, role, attack):
        if self.membership:
            self.name = name
            self.role = role
            self.attack = attack
        else:
            print('error: you are not authorized to create a character')
        

member1 = PaidPlayer('Jaque', 'swordsman', 43)