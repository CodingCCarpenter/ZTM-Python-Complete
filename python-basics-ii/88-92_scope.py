# Scope - what variables do I have access to?

# Python has functional scope

# global scope - accessible by all code
total = 100 

def some_func():
    # functional scope - not available outside of some_func
    counter = 100

# we have access to total
print (total)

# but we do not have access to counter - will throw error
# uncomment line 17 and run to view error
# print(counter) 

"""
functional scope only applies when we define a function. 
Variables created by loops and conditionals are still 
accessible globally
"""

if True:
    x = 10

# we still have access to print x:
print(x)


# SCOPE GAME!!! 


# What variables do I have access to?
a = 1

def confusion():
    a = 5
    return a

# what will be the output of the following?
print(a) # 1 - value of global scope variable a

print(confusion()) # 5 - value functional scope variable a


""" 
Scope rules that python interpreter follows:
    1 - starts with checking local scope (same scope as expression that's looking for it)
    2 - if nothing in the local scope, checks in the parent's local scope
    3 - global scope
    4 - build in python functions
"""
