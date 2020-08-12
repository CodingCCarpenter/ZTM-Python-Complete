# MAP()

def multiply_by_2(item):
    return item * 2

print(list(map(multiply_by_2, [1,2,3])))

# my own example
users = ['Amanda', 'Joe', 'Michael', 'Laura', 'Jeremy', 'Lily']

def greet_user(user):
    return (f'Welcome to the course, {user}')

print(list(map(greet_user, users)))

# FILTER

my_list = [1,2,3]

def grab_odds(item):
    return item % 2 != 0

print(list(filter(grab_odds, my_list)))
