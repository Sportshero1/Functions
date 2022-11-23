# Conversion Calculator
# By: Scott Hadzik

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user
valid_data = True

def print_results(user_number, user_unit, conv_number, conv_unit):
    print(user_number, user_unit, 'is equal to', conv_number, conv_unit)
    result = ("{:.2f} {} is equal to {:.2f} {}")
    result.format(user_number, user_unit, conv_number, conv_unit)

def user_parser(user_input):

    global valid_data
    valid_data = True
    #TODO  address input from user without space
    # Separate the number from unit
    values = user_input.rsplit(" ")
    number = values[0]
    
    if number.isdigit():
        number = float(number)
    else:
        print("That is not a valid number") 
        valid_data = False

    unit = values[1]
   
    if unit != 'in' and unit != 'mm' and unit != 'ft':
        print("That is not a valid unit")
        valid_data = False
    
    return number, unit

while True: # Continue program until user exits
    while True: # Check for valid data
        user_input = input("number and unit to convert ")
        user_number, user_unit = user_parser(user_input)
        # Check if there are invalid messages
        if valid_data:
            break
    # Perform Calculation
    if(user_unit == 'in'):
        #perform in to mm
        conv_number = user_number * 25.4
        conv_unit = 'mm'
    elif(user_unit == 'mm'):
        #perform mm to in
        conv_number = user_number / 25.4
        conv_unit = 'in'
    elif(user_unit == 'ft'):
        conv_number = user_number * 12
        conv_unit = 'in'
    else:
        print('That is not a valid unit')
    #Create a function that prints out the answer formatted to 2 decimal points
    # Give the original number value and unit and conv_number and unit
    # 12.00 ft is equal to 144.0 in

    print_results(user_number, user_unit, conv_number, conv_unit)

