# Welcome to Python!

# A simple syntax to print the given string
print("Welcome to Python!")

# Doc/multiline string
"""
This is a multiline string. It may be used as a documentation string and is
ignored by the interpreter as long as it is unassigned to a variable.
"""

# Essence of indentation
if 5 > 2:
    print("Yes! 5 is always greater than 2.")
        # print("Yes, 5 is always greater than 2.") # [!] Error-prone line

# Python really doesn't care if the variable is reassigned to a different type
dyn_var = 100
dyn_var = "dumb"
print("I'm " + dyn_var)

# Explicit type conversion stuff
x = str(21)
y = int(21)
z = float(21)

print(type(x))
print(type(y))
print(type(z))

# Python does not know if  rohan  and  Rohan  could be the same variable the
# programmer did mean to use... damn
rohan = "Small Rohan"
Rohan = "Big Rohan"

print(rohan)
print(Rohan)

# I liked this... multiple assignment.
# But I'd never do that in production code
john, wick = "John", "Wick"

print(john)
print(wick)

john = wick = "John Wick"

print(john)
print(wick)

# Unpacking a tuple collection, amazing!
yaga = ['John', 'Wick']
john, wick = yaga

print(john)
print(wick)

x = "Python"
y = "is"
z = "dumb"
print(x, y, z)
print(x + y + z)

# Well, we all know that global variables are always DUMB, yet... let's use it
global_var = "Hey!"


def sayHi():
    print(global_var + " I'm a nerdy geek.")

    global sussy
    sussy = "Legendary power of Beluga!"


sayHi()
print(sussy)
