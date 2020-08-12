# 4 PILLARS OF OOP

# 4- Polymorphism (means many form)
""" In python, polymorphism refers to the way
 in which object classes can share the same 
 method name, but those methods can act 
 differently based on which object calls them """

# starting with same code from 123_inheritance.py
class User():
    def __init__(self, name):
        self.name = name
        self.health = 20

    def sign_in(self):
        print(f'{self.name} is logged in')

# Wizard inherits the name attribute from User!
class Wizard(User):
    role = 'wizard'

    """because of polymorphism, we can have a 
    _basic_attack method defined both here and 
    in the Archer class so that it behaves  
    differently based on which class it is called
    on"""
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

wizard1 = Wizard('Dumbledore')

archer1 = Archer('Robin')

""" The methods have different returns based 
on which class the character that calls it 
is an instance of"""
archer1._basic_attack(wizard1)
wizard1._basic_attack(archer1)