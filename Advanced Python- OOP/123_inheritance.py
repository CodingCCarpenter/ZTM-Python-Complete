# 4 PILLARS OF OOP

# PILLAR # 3 - INHERITANCE
# ALLOWS NEW OBJECTS TO TAKE ON THE PROPERTIES OF EXISTING OBJECTS

"""
Users:
    Wizards, Archers, Ogres
"""

class User():
    role = ''
    health = 20

    def __init__(self, name):
        self.name = name

    def sign_in(self):
        print(f'{self.name} is logged in')

# Wizard inherits the name attribute from User!
class Wizard(User):
    role = 'wizard'

    def _fireball(self, target):
        target.health = target.health - 3
        print('FIREBALL!!! You take 3 damage!')
        return target.health

    def _heal(self):
        if self.health < 15:
            self.health += 5
            print('A healing light surrounds you! Heal 5 points!')
            return self.health
        print('You did not need to heal. You wasted your turn!')

class Archer(User):
    role = 'archer'

    def _crack_shot(self, target):
        target.health = target.health - 5
        print('The archer never misses! You take 5 damage!')

wizard1 = Wizard('Dumbledore')

archer1 = Archer('Robin')

print(wizard1.sign_in())
print(archer1.sign_in())

wizard1._fireball(archer1)
print(f'archer1 health:{archer1.health} wizard1 health:{wizard1.health}')

archer1._crack_shot(wizard1)
print(f'archer1 health:{archer1.health} wizard1 health:{wizard1.health}')

wizard1._heal()
print(f'archer1 health:{archer1.health} wizard1 health:{wizard1.health}')