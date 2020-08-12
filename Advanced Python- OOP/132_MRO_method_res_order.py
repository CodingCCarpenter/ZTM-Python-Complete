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