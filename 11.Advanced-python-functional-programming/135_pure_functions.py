# what is a pure function?
# a pure function given the same input will always return the same output
# a pure function should not produce any side effects

def multiply_by2(li):
    new_list = []   
    for item in li:
        new_list.append(item*2)
    return new_list
        
print(multiply_by2([1,2,3]))

# it is important to note that the pure functions are more of a guideline
# than a rule. It's impossible to use them all the time. Try to keep as many 
# functions pure as possible
