""" 
problem:
create a function called highest_even that takes a list
as an argument, and returns the highest even number 

steps I think I should take to solve:
    1. isolate even numbers in separate list
    2. return highest number on evens list
 
 """

def highest_even(integer_list):
    evens = []
    
    # isolate the even numbers
    for item in integer_list:
        if item % 2 == 0:
            evens.append(item)

    # return highest number in evens list 
    return max(evens) 

print(highest_even([10,2,3,4,8,11]))