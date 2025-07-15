#Lists is a collection of items that can be of any type.
# Lists are mutable, meaning you can change their content after creation.
## You can create a list using square brackets [] and separate items with commas.
# they allow duplicate values and maintain the order of items.

# Lists can be nested, meaning you can have lists within lists.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

#you can access items in a list using their index, which starts at 0.
print("Fruits List:", fruits)

print("First fruit:", fruits[0])  # Accessing the first item
print("Second fruit:", fruits[1])  # Accessing the second item

fruits[1] = "blueberry"  # Changing the second item
print("Updated Fruits List:", fruits)