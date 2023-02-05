# variable to identify correct pin
# constant values at top of the code for cleaner and more maintainable code
correct_pin = "4321"

# the method to track login attempts in this code is a list
# this is NOT the most efficient or simplest way to do this - code to be changed when I have time
loginAttempts = [0, 1, 2]
# login is a list shown by square brackets, is mutable which allows pop() method
# checks how many failed login attempts

# while, if and else are conditions
# while login is true (while the list contains items), an input will be requested
while loginAttempts:
    supplied_pin = input('Enter your pin: ')

    # if the supplied pin variable is equal (==) to the correct pin variable, the loop will end here
    # break is a loop control statement to trigger loop termination
    if supplied_pin == correct_pin:
        print('Successful login')
        break

    # else (if the pin is incorrect),
    # pop() is a method which removes the last item from the list after a failed login
    # str converts the login integer to string to allow concatenation (using +) with string
    else:
        print('Failed login')
        print(str(loginAttempts.pop()) + ' Attempts remaining')
