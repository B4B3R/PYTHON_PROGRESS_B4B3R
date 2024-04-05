# a tuple is not a list  but a k-uplet(s) as a collection of elements

nbs_tuple = (1,2,3,3,4,3) # you can't modify a tuple

print(nbs_tuple.count(3))

# set

nbs_set = {1, 4, 2, 9, 7, 8, 9, 3, 1} # difference with the list the set don't have any order

nbs_set.add(7)
nbs_set.remove(1)

print(nbs_set)

set_1 = {8,2,4}
set_2 = {0,1,8}

print(set_1.union(set_2))
print(set_1.intersection(set_2))

print(set_1.difference(set_2)) #unique elements to set_1
print(set_2.difference(set_1)) #unique elements to set_2