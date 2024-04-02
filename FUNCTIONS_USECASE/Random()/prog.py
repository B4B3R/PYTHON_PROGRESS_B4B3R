# First usecase of the function random()

from random import * # or just import random but if you do that you need to call function random.random() not just random

a = random()
print(a)

list = []
# range() : 

for l in range(10):
    list.append(l)
    print(list)

for l in range(0,8):
    list.remove(l)
    print(list)
# the code below is the the same
#for l in range(start=0,stop=8):
#     list.remove(l)
#     print(list)
    

for k in range(0,10,2): # range(start = 0, stop = 10, step = 2)
    list.count(k)
    print(list)


x = range(6)

for n in x:
    print(n)

print(x)

y = range(9)

for n in y:
    print(n)

print(y)