from time import sleep
# Functions go here


# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print("Please choose a unit to convert from and a unit to convert to")
    print()
    sleep(1)
    print("This program converts measurements of time, mass, and distance")
    print()
    sleep(1)
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""


# checks input is a number more than given value
def num_check(question):
    # Check that users enter a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter a number that is more than 0"

        try:
        
            # Ask user to enter a number
            response = float(input(question))

            # Checks number is more than zero or under 200
            if response > 0:
                return response

            # outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# Checks user choice is 'weight', 'length', or 'time'
def user_choice():

    valid = False
    while not valid:

        response = input("Measurement (Weight / Distance / Time): ").lower()

        weight_ok = ["weight", "mass", "w", "wt"]
        if response in weight_ok:
            return "weight"

        distance_ok = ["length", "distance", "dist", "d"]
        if response in distance_ok:
            return "distance"

        time_ok = ["time", "t"]
        if response in time_ok:
            return "time"
        
        else:
            print("Please choose a valid measurement!")
            print()


def unit_checker(question, dictionary):

    while True:
        response = input(question).lower()
        
        if response in dictionary:
            return response
        
        else:
            print()
            print("Please enter a valid response")
            print()


# Asks user what unit they want to convert from and to
def weight_conv():

    weight_from = unit_checker("Which unit would you like to convert from (mg, g, kg, t)? ", weight_dict)
    print()
    weight_to = unit_checker("Which unit would you like to convert to? ", weight_dict)
    print()
    weight_amount = float(num_check("Please enter the amount you want to convert: "))
    print()
    
    if weight_from in weight_dict:
        divide_by = weight_dict[weight_from]

        part_1 = weight_amount / divide_by
        factor_1 = weight_dict[weight_to]

        weight_answer = part_1 * factor_1

        print("{}{} = {}{}".format(weight_amount, weight_from, weight_answer, weight_to))

def length_conv():

    length_from = unit_checker("Which unit would you like to convert from (mm, cm, m, km)? ", length_dict)
    print()
    length_to = unit_checker("Which unit would you like to convert to? ", length_dict)
    print()
    length_amount = float(num_check("Please enter the amount you want to convert: "))
    print()

    if length_from in length_dict:
        divide_by = length_dict[length_from]

        part_1 = length_amount / divide_by
        factor_1 = length_dict[length_to]

        length_answer = part_1 * factor_1

        print("{}{} = {}{}".format(length_amount, length_from, length_answer, length_to))
        
def time_conv():

    time_from = unit_checker("Which unit would you like to convert from (ms, sec, min, hour, day)? ", time_dict)
    print()
    time_to = unit_checker("Which unit would you like to convert to? ", time_dict)
    print()
    time_amount = float(num_check("Please enter the amount you want to convert: "))
    print()

    if time_from in time_dict:
        divide_by = time_dict[time_from]

        part_1 = time_amount / divide_by
        factor_1 = time_dict[time_to]

        time_answer = part_1 * factor_1

        print("{}{} = {}{}".format(time_amount, time_from, time_answer, time_to))



# Main Routine goes here


# Dictionaries
weight_dict = {
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
    "t": 0.000001
}

length_dict = {
    "cm": 100,
    "m": 1,
    "km": 0.001,
    "mm": 1000
}

time_dict = {
    "sec": 60,
    "min": 1,
    "hour": 0.6,
    "day": 0.000694444,
    "ms": 60000
}

all_units = weight_dict | length_dict | time_dict   


# Heading
statement_generator("Conversion Calculator for Weight, Distance & Time", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see instructions or any key to continue ")
print()

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print()
    print("You chose", data_type)
    print()

    # For integers, ask for integer
    # (must be an integer more than / equal to 0)
    if data_type =="weight":
        weight_conv()
    
    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type == "time":
        time_conv()
    
    # For text, ask for a string
    else:
        length_conv()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()
