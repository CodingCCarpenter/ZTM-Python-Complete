class PlayerCharacter:
    def __init__(self, name, role, attack):
        self.name = name
        self.role = role
        self.attack = attack

    # custom method that we created
    def battle_cry(self):
        print(f'I am {self.name}!!! YAAAAAAAAAAARG!!!!')
        return 'done'

    # if we recall, this is a class object attribute, which is NOT dynamic
    membership = True

    # can we do something like the class object attribute but with a method???
    # yes we can! @classmethod
    @classmethod

    # much like self above, cls represents the class that the method is on
    def add_attack_point(cls, current_attack):
        player1.attack = current_attack + 1
        return current_attack

# create an instance of PlayerCharacter
player1 = PlayerCharacter('Bacchus', 'Viking', 53)

# print the results of calling add_attack_point on player1
print(player1.add_attack_point(player1.attack))

# adding a few attack points
player1.add_attack_point(player1.attack)
print(player1.attack)

player1.add_attack_point(player1.attack)
print(player1.attack)

player1.add_attack_point(player1.attack)


# printing current attack points
print(player1.attack)

