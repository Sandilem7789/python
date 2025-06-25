#strings
message = "Hello, World!"

# Print the message to the console
print(message[0:9])  # Output: Hello

#Length of the string
print(len(message))

length = len(message)
print(message[length - 8])  

# Strip whitespace from the beginning and end of a string
message2 = " Hello, World! "
print(message2.strip())  # Output: Hello, World!
print(message2.lower())  # Output: hello, world!)
print(message2.upper())  # Output: HELLO, WORLD!
print(message2.split(','))

#replace method
print(message2.replace("World", "Python"))  # Output: Hello, Python!

#Numeric Data
num = 642

print(num)
print(type(num))  # Output: <class 'int'>
print(float(num))  # Convert to float: Output: 642.0
print(str(num))  # Convert to string: Output: '642'
print(num + 10)  # Output: 652
print(num * 2)  # Output: 1284
# Convert string to integer
num_str = "123" 
num_int = int(num_str)
print(num_int)  # Output: 123


#variables
#varialbles must start with a letter or underscore
my_variable = "This is a variable"

# variables are case-sensitive

#Operators
print("""
    Operators in Python:  
      """)
# Arithmetic Operators
a = 10
b = 5
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50
print(a / b)  # Output: 2.0
print(a % b)  # Output: 0
print(a ** b)  # Output: 100000 (10 raised to the power of 5)
print(a // b)  # Output: 2 (Floor division)

#OPERATORS ON STRINGS
print("""
    Operators on Strings:  
      """)
str1 = "Hello"
str2 = "World"

print("Kuhle lokhu, " + str1 + " " + str2)  # Output: Hello World
print(str1 * 3)   # Output: HelloHelloHello

#CONTROL STATEMENTS
print("""
    CONTROL STATEMENTS: 
      """)

num1 = -1.5
if num1 > 0:
	print("Positive number")
elif num1 == 0:
	print("Zero")
else:
    print("Negative number")
    


#CONTROL STATEMENTS 2
print("""
    CONTROL STATEMENTS 2: Taking inputs
      """)

numA = float(input("Enter a number: "))
numB = float(input("Enter another number: "))

if numA > numB:
    print(f"{numA} is greater than {numB}")
elif numA < numB:
    print(f"{numA} is less than {numB}")
else:
    print(f"{numA} is equal to {numB}")

sum_result = numA + numB
print(f"The sum of {numA} and {numB} is {sum_result}")
