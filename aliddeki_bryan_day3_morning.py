"""# // return the quotient without the remainder


Comparison Operators
== equal to
!= not equal to
> greater than
>= greater than or equal to
<= less than or equal to

Logical Operators
Logical AND 'and' 
Logical OR 'or'
Logical NOT 'not'

Assignment Operators
Assign value: '='
Add value: '+'
Add and assign: '+='
Subtract and assign: '-='
Divide and assign: '/='
Modulus and assign: '%='
Exponentiate and assign: '**='

Membership Operators
In: 'in' - checks if a value exists in a sequence
Not in: 'not in' - checks if a value does not exist in a sequence


Identity Operators
Is: 'is' operator: checks if two values are not the same

"""




print(2**5)
print(3+5)
print(10%3)
print(10/3)
print(10//3)
print(10*3)
print(10-3)
print(10+3)
a = 5
print(a)

#Comparison Operators
a = 23.5
b = 15
c = 9

#Greater than
if (b > a):
    print("a is greater than b")
else:
    print("a is less than b")
    print(b > a)

#Less than
if (c < a):
    print("c is less than a")

#Greater than or equal to
if (a >= b):
    print("a is greater than or equal to b")

#Less than or equal to
if (c <= a):
    print("c is less than or equal to a")

#Equal to
if (a == b):
    print("a is equal to b")

#Not equal to
if (a != b):
    print("a is not equal to b")

#Examples with Logical Operators
a = True
b = False

#Logical AND
print(a and b)

#Logical OR
print(a or b)

#Logical NOT
print(not a)




#print(a += b)

#Identity operators
x = 10 
y = 10

print(x != y)

"""
Bitwise AND ('&'): performs bitwise AND operation between the correspoding bits of two operands
Bitwise OR ('|'): performs bitwise OR operation between the correspoding bits of two operands
Bitwise XOR ('^'): performs bitwise XOR operation between the correspoding bits of two operands
Bitwise NOT ('~'): performs bitwise NOT operation on a single operand
Bitwise left shift ('<<'): performs bitwise left shift operation on a single operand
Bitwise right shift ('>>'): performs bitwise right shift operation on a single operand
"""

#Examples on Bitwise Operators
a = 10 #in binary notation 10 is 1010
b = 20 #in binary notation 20 is 10100

#Bitwise AND
print(a & b)

#Bitwise OR
print(a | b)

#Bitwise XOR
print(a ^ b)

#Bitwise NOT
print(~a)

#Bitwise left shift
print(a << 2)

#Bitwise right shift
print(a >> 2)








