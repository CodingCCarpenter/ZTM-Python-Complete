# DOCSTRINGS
def test(a):
    '''
    Info: this function tests and prints param "a". 
    This is called a docstring and lets us comment
    inside our function to display in the IDE.
    '''
    print(a)

test('!!!!')

# 3 WAYS TO VIEW:

#1 see the docstring when typing the function in your IDE
test('a')

#2 using help function, which returns an 'Info:' block containing the docstring
# ##note that we do not need to CALL the function!
help(test)

#3 using 'magic method' or a 'dunder method' for printing docstring tied to func
print(test.__doc__)