# LOOPS
#FOR LOOP: WHAT IS IT?
# A for loop is a control flow statement that allows code to be executed repeatedly based on
# a condition. It is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# The loop will continue until it has gone through all the items in the sequence.

print("For Loop Example:")
# This loop will iterate through each fruit in the list and print it

print("\nWhile Loop Example: String Iteration")   

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)

print("\nWhile Loop Example: Number Iteration")   
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
    count += 1
    # If count reaches 5, break the loop
    if count == 5:
        print("Count is equal to 5, breaking the loop.")
        break
    
#This loops counts down from 10 to the number between 10 and zero, the input will be requested from the user
print("\nWhile Loop Example: Countdown")
countdown_start = int(input("Enter a number between 0 and 10 to start the countdown: "))
while countdown_start >= 0:                                                                                 # Loop until countdown_start is less than 0
    print("Countdown:", countdown_start)
    countdown_start -= 1
    if countdown_start < 0:
        print("Countdown finished!")
        break