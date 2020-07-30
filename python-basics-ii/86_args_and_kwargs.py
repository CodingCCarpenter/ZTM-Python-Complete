# *args and **kwargs

def super_func(*args, **kwargs):
    # initialize total at 0 for kwargs for loop
    total=0
    # will print sum of all args entered:
    args_sum = sum(args)
    # will print sum of values of all kwargs entered:
    for items in kwargs.values():
        total += items

    # will return sum of all items entered
    return args_sum + total

result = super_func(1,2,3,4,5, num1=5, num2=8)
print(result)


# *args allows us to tell it to perform the action on everything given during function call
# **kwargs allows us to enter key value pairs to be stored in a dictionary.

"""
!!!!! There is a rule we must follow 
about the order of our parameters. !!!!!

The order goes:
    1. parameters
    2. *args
    3. default parameters
    4. **kwargs

def psuedo_code(parameters, *args, default_params='this', **kwargs):
    print(f"first comes {parameters}, then {*args} followed by {default_params} and finally {kwargs}")

"""