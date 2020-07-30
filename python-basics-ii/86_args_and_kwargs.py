# *args and **kwargs

def super_func(*args, **kwargs):
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

