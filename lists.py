#Lists is a collection of items that can be of any type.
# Lists are mutable, meaning you can change their content after creation.
## You can create a list using square brackets [] and separate items with commas.
# they allow duplicate values and maintain the order of items.

# Lists can be nested, meaning you can have lists within lists.

fruits = ["apple", "banana", "cherry", "cherry", "date", "elderberry"]

#you can access items in a list using their index, which starts at 0.
print("Fruits List:", fruits)

print("First fruit:", fruits[0])  # Accessing the first item
print("Second fruit:", fruits[1])  # Accessing the second item

fruits[1] = "blueberry"  # Changing the second item
print("Updated Fruits List:", fruits)

#Appending items to a list
fruits.append("fig")  # Adding a new item to the end of the list
print("Fruits List after appending 'fig':", fruits)

#Inserting items at a specific position
fruits.insert(2, "grape")  # Inserting 'grape' at index 2
print("Fruits List after inserting 'grape' at index 2:", fruits)

#removing items from a list
fruits.remove("cherry")  # Removing the first occurrence of 'cherry'
print("Fruits List after removing 'cherry':", fruits)

#Sorting a list
fruits.sort()  # Sorting the list in alphabetical order
print("Fruits List after sorting:", fruits)

#descending sort
fruits.sort(reverse=True)  # Sorting the list in reverse alphabetical order 
print("Fruits List after reverse sorting:", fruits)