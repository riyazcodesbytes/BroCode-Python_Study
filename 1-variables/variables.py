# Variable = A container for a value. It can be changed and reused throughout a program.
# A variable behaves like a box that can hold different types of data, such as numbers, strings, lists, etc. 
# In Python, you can create a variable by assigning a value to it using the equals sign (=).

# String = A sequence of characters enclosed in quotes. Strings can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
first_name = "Riyaz" 
print(first_name)

# using f-strings to format the output
print(f"My name is {first_name}.")


# Integer = A whole number without a decimal point. Integers can be positive, negative, or zero.
age = 25

print(f"I am {age} years old.")


# Float = A number that has a decimal point. Floats can also be positive, negative, or zero.
height = 5.9
price = 19.99
gpa = 3.75
print(f"\nMy gpa is {gpa}.")
print(f"The price of the item is ${price}.")
print(f"My height is {height} feet.")


# Boolean = A data type that can have one of two values: True or False. 
# Booleans are often used in conditional statements and logical operations.
is_student = True
print(f"\nAm I a student? {is_student}.")

if is_student:
    print("Yes, I am a student.")
else:
    print("No, I am not a student.")