# first usecase of the function random.choice() and len()
# first program with random value !!!!!

from random import *

my_sequence = range(100)

variable = str(choice(my_sequence)) # it's important to convert to string to be able to use len() method

print("Value :      " + str(variable))
print("Lenght :     ", len(variable)) # in this case use , not + because you don't need you have 2 string
