# typecasting = converting one data type into another data type. 
# int to float, 
# float to int, 
# str to bool, 
# bool to str, 
# float to str, 
# str to int, 
# int to bool.

# Explicit typecasting = manually converting one data type into another data type using built-in functions like int(), float(), str(), bool().
# Implicit typecasting = automatically converting one data type into another data type by the Python interpreter.

name = "Riyaz"
age = 32
gpa = 3.5
smart = True

# type() function is used to check the data type of a variable.
print(f"Data type of name: {type(name)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of gpa: {type(gpa)}")
print(f"Data type of smart: {type(smart)}") 

print("\n")

# Explicit typecasting
print(f"Age as float: {float(age)}") # int to float
print(f"GPA as string: {str(gpa)}") # float to str
print(f"Age as string: {str(age)}") # int to str
print(f"GPA as integer: {int(gpa)}") # float to int
print(f"Smart as string: {str(smart)}") # bool to str
print(f"Name as boolean: {bool(name)}") # str to bool
print("str to int: will raise an error if the string is not a valid integer representation.") # str to int
print("int to bool: will return False if the integer is 0, and True for any other integer.") # int to bool

# Implicit typecasting
num1 = 10 # int
num2 = 3.14 # float
result = num1 + num2 # int is implicitly converted to float before addition
print(f"\nResult of implicit typecasting: {result}")


print(int(True)) # bool to int
print(int(False)) # bool to int