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

        error = "Please enter an integer that is more than 0 and less than 201"

        try:
        
            low_num = 1
        

            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero or under 200
            if low_num <= response:
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


# Dictionaries
weight_dict = {
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
    "t": 0.000001
}

distance_dict = {
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

# Asks user what unit they want to convert from and to
def weight_conv():

    weight_from = input("Which unit would you like to convert from (mg, g, kg, t)? ")
    print()
    weight_to = input("Which unit would you like to convert to? ")
    print()

    if weight_from in weight_dict:
        number_from = input("How many {}? ".format(weight_from))
        weight_answer = number_from * weight_dict[number_from]
        print(weight_answer)


def length_conv():

    length_from = input("Which unit would you like to convert from (mm, cm, m, km)? ")
    print()

# Main Routine goes here

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
    elif data_type == "image":
        ()
    
    # For text, ask for a string
    else:
        ()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()
