# var is a variable
# input is a built-in method which requires a prompt from the user
# 'Please enter a value: ' will show in the Run section for the user to add their prompt
var = input('Please enter a value: ')

# upper() is a method which is a function that belongs to an object
# upper() returns the string with all characters uppercase
# the object is the variable var
print(var.upper())

# len() is built-in function to return the character length of an object
print(len(var))

# isdecimal() is a method which check is all characters are decimal (characters between 0-9)
# Returns True or False
print(var.isdecimal())

