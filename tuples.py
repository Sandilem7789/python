#tuples are used to represent fixed collections of items
# Tuples are immutable, meaning you cannot change their content after creation.
#tuples are ordered collections of items, allowing duplicate values.
# You can create a tuple using parentheses () and separate items with commas.

my_tuple = (1,2,3,4,5,6,7,8,9,10)
print("My Tuple:", my_tuple)

#you can access elements in tuples using indexing, similar to lists
print("First element:", my_tuple[0])  # Accessing the first item
print("Last element:", my_tuple[-1])  # Accessing the last item

#operations on tuples
# Tuples can be concatenated using the + operator
another_tuple = (11, 12, 13)
combined_tuple = my_tuple + another_tuple
print("Combined Tuple:", combined_tuple)