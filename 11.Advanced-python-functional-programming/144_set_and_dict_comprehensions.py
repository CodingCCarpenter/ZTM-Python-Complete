# comprehensions

# LIST

my_list = [char for char in 'hello']

# SET - works the same as LIST comprehensions = only change [] => {}
my_set = {char for char in 'hello'}

# DICTS
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key:value**2 for key, value in simple_dict.items() }
print(my_dict)

my_other_dict = {num:num*2 for num in [1,2,3]}
print(my_other_dict)