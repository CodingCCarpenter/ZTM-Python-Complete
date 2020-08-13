# List Comprehensions
# comprehensions work with lists, sets, and dictionaries
# a quick way to create lists, sets, and dictionaries rather
# than looping 

# original way
my_list = []
for char in 'hello':
    my_list.append(char)

print(my_list)

# using comprehension
the_list = [char for char in 'hello']

print(the_list)

the_second_list = [num for num in range(0,100)]

the_third_list = [num**2 for num in range(1, 100)]

the_fourth_list = [num **2 for num in range(1,100)
if num % 2 ==0]

print(the_second_list)
print(the_third_list)
print(the_fourth_list)