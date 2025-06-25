# LOOPS
#FOR LOOP: WHAT IS IT?
# A for loop is a control flow statement that allows code to be executed repeatedly based on
# a condition. It is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# The loop will continue until it has gone through all the items in the sequence.

print("For Loop Example:")
# This loop will iterate through each fruit in the list and print it
fruits = ["apple", "banana", "cherry", ["kiwi", "mango"]]

for fruit in fruits:
    print(fruit)
    
numbers = [1, 2, 3, 4, 5]
for number in numbers: 
    print(number)
    
#WHILE LOOP: WHAT IS IT?
# A while loop is a control flow statement that allows code to be executed repeatedly as long as
# a specified condition is true. It is useful when the number of iterations is not known beforehand.

print("\nWhile Loop Example:")
# This loop will continue until the count reaches 5
count = 0
while count < 5:
    print("Count is:", count, " - Looping...")