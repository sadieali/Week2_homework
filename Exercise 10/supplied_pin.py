correct_pin = 4321

login = [1, 2, 3]
# login is a list shown by square brackets, is mutable which allows pop() method

while login:
    supplied_pin = input('Enter your pin: ')
    if supplied_pin == correct_pin:
        print('Successful login')
    else:
        print('Failed login')
        print(str(login.pop()) + ' Attempts remaining')

# while, if and else are conditions
# pop() is a method which removes the last item from the list
# str convert the login integer to string to allow concatenation (using +) with string

# def pin_num():
#     attempt= 0
#     while attempt < 3:
#         num = input('Please Enter Your 4 Digit Pin: ')
#         if enter_pin(pinnum):
#             print("Pin accepted!")
#         else:
#             print("Invalid pin")
#             attempt += 1
#             print("Multiple attempts, Your card is blocked, please contact customer service")