# SUPER()

# starting with same code from polymorphism.py
class User():
    def __init__(self, name):
        self.name = name
        self.health = 20

    def sign_in(self):
        print(f'{self.name} is logged in')

class Wizard(User):
    role = 'wizard'

    def _basic_attack(self, target):
        target.health = target.health - 3
        print('Wizard bops you on the head with their staff. You take 3 damage.')
        return target.health
    
    def _fireball(self, target):
        target.health = target.health - 7
        print('FIREBALL!!! You take 3 damage!')
        return target.health

    def _heal(self):
        if self.health < 15:
            self.health += 5
            print('A healing light surrounds you! Heal 5 points!')
            return self.health
        print( 'You did not need to heal. You wasted your turn!')

class Archer(User):
    role = 'archer'

    def _basic_attack(self, target):
        target.health = target.health - 3
        print('Archer punches you. You take 3 damage.')
        return target.health
    
    def _crack_shot(self, target):
        target.health = target.health - 7
        print('The archer never misses! You take 5 damage!')
        return target.health

    def field_medic(self):
        if self.health < 15:
            self.health += 5
            print('Thank goodness for field medics! Heal 5 points!')
            return self.health

# instantiate players
wizard1 = Wizard('Dumbledore')
archer1 = Archer('Robin')

# first two moves of game
archer1._basic_attack(wizard1)
wizard1._basic_attack(archer1)