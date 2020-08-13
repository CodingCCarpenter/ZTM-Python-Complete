# Scope - what variables do I have access to?

# Python has functional scope

# global scope - accessible by all code
total = 100 

def some_func():
    # functional scope - not available outside of some_func
    counter = 100
    return counter

# we have access to total
print (total)

# but we do not have access to counter - will throw error
# uncomment line 17 and run to view error
#print(counter) 

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

# GLOBAL KEYWORD
abacus = 0

def count():
    # use the global variable to access any global variables
    global abacus 
    # after we have access to it we can use it in our function
    abacus += 1
    return abacus

print(count())

"""
note: 
    it's arguably cleaner to simply pass a global variable 
    into a function as an argument, and then create an expression
    to update the global variable as needed upon function call
"""

# NONLOCAL KEYWORD
def outer():
    x = 'local'
    def inner():
        # used to access the parent's local variable
        nonlocal x
        # here we are reassigning the parent's local variable value
        x = 'nonlocal'
        print('inner:', x)
    inner()
    print('outer:', x)

outer()