#sets are immutable sequences in Python, similar to tuples, but they are unordered and do not allow duplicate elements.
# Sets are created using curly braces {} or the set() constructor.
my_set = {1, 2, 3, 4, 5}
print("My Set:", my_set)

# Adding a new element to the set
my_set.add(6)
print("Set after adding 6:", my_set)

#removing an element from the set
my_set.remove(3)  # This will raise an error if 3 is not in the set
print("Set after removing 3:", my_set)

#sets operations
# Union of two sets
print("")
print("Set Operations: Union of two sets")
another_set = {4, 5, 6, 7}
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# Intersection of two sets
print("")
print("Set Operations: Intersection of two sets")
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)


# Difference of two sets
print("")
print("Set Operations: Difference of two sets")
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

# Symmetric difference of two sets
print("")
print("Set Operations: Symmetric difference of two sets")
symmetric_difference_set = my_set.symmetric_difference(another_set)
print("Symmetric difference of sets:", symmetric_difference_set)