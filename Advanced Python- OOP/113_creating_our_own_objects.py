# Creating our own objects with OOP

class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')