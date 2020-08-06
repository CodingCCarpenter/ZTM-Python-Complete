"""
starter code copied from https://repl.it/@aneagoie/OOP-Exercise-Cat#main.py
"""
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
patches = Cat('Patches', 3)
thai_chi = Cat('Thai Chi', 2)
kermit = Cat('Kermit', 6)


# 2 Create a function that finds the oldest cat
cat_ages = [patches.age, thai_chi.age, kermit.age]

def oldest_cat():
    age_of_oldest = max(cat_ages)
    return age_of_oldest

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {max(cat_ages)} years old")