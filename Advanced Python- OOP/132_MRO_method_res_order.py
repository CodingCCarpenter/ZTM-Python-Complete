# MRO - Method Resolution Order
# a rule that determines which method to run when


class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num) # this prints 1 since the value of A is overwritten by the value of C


"""
visual representation of the classes relationships

A is a parent of both B and C, and D inherits from or is a child of both B and C

   A
  / \
 /   \
B     C
 \   /
  \ / 
   D

"""

# the below prints the full method resolution order for D
print(D.mro())

# dunder method version of the same thing
print(D.__mro__)

class X:
    pass
class Y:
    pass
class Z:
    pass

class E(X, Y):
    pass
class F(Y, Z):
    pass
class M(F, E, Z):
    pass

print(M.mro())

"""
prints:

[<class '__main__.M'>, <class '__main__.F'>, <class '__main__.E'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
"""