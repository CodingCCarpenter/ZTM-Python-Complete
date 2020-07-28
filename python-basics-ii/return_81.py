# RETURN IN FUNCTIONS
def sum(num1, num2):
    print('hi')
    num1 + num2

"""
Good 'clean' functions should have two characteristics:
    1. should do one thing really well
    2. should return something

The function sum() does not meet either of these requirements. 

It prints 'hi', which is unrelated to the function's purpose (give sum). 
The function also fails to return something, which means if we run
this code, 'None' will be returned. 

To correct this, we should write it as:

def sum(num1,num2):
    return num1 + num2

**remember to print it when you call the function, so you can see
the result**

print(sum(2,3))
"""

print(sum(2, 3))

# creating new function that returns properly for demonstration
def add(n1, n2):
    return n1 + n2

""" 
We can assign the returned results to a variable in order to store the value 
for later use
"""

total = add(3,4)
print(total)


# what happens if we nest a function inside of another function?
def product(number1,number2):
    def another_function(number1,number2):
        return number1 + number2
 
print(product(2,3)) #returns none

""" 
oh yeah! we need to return something! Right
now all product(2,3) does is define a function
with the same params. 

let's try again!
"""

# what happens if we return the function after we define it?
def second_product(number1,number2):
    def second_another_function(number1,number2):
        return number1 + number2
    return second_another_function

print(second_product(2,3)) # returns the function (sort of):
#<function second_product.<locals>.second_another_function at 0x00000214E4CE9670>