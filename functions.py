# Conversion Calculator
# By: Scott Hadzik

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user
def user_parser(user_input):
    # Do something
    # Separate the number from unit
    values = user_input.rsplit(" ")

    number = values[0]
    if number.isdigit():
        number = float(number)
    else:
        print("That is not a valid number") 

    unit = values[1]
    if unit != 'in':
        print("That is not a valid unit")
    
    return number, unit

while True:
    user_input = input("number and unit to convert ")
    user_number, user_unit = user_parser(user_input)
    print('User number', user_number)
    print('User unit', user_unit)
#     while True:
#         user_number = input("What number to convert? ")
#         if user_number.isdigit():
#             user_number = float(user_number)
#             break
#         else:
#             print('Please use a number')

#     user_unit = input("What unit is your number?")

#     if(user_unit == 'in'):
#         #perform in to mm
#         conv_number = user_number * 25.4
#         conv_unit = 'mm'
#         break
#     elif(user_unit == 'mm'):
#         #perform mm to in
#         conv_number = user_number / 25.4
#         conv_unit = 'in'
#         break
#     else:
#         print('That is not a valid unit')

# print(conv_number, conv_unit)